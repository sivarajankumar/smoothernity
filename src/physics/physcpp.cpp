#include "colshape.hpp"
#include "rigidbody.hpp"
#include "vehicle.hpp"
#include "physres.h"
#include "ddraw.hpp"
#include "world.hpp"
#include <lua.h>
#include <btBulletDynamicsCommon.h>
#include <exception>

struct physcpp_t
{
    btDbvtBroadphase *broadphase;
    btCollisionDispatcher *dispatcher;
    btSequentialImpulseConstraintSolver *solver;
    btDefaultCollisionConfiguration *colcfg;
    btDiscreteDynamicsWorld *world;
    ddraw_c *ddraw;
    char broadphase_data[sizeof(btDbvtBroadphase)];
    char dispatcher_data[sizeof(btCollisionDispatcher)];
    char solver_data[sizeof(btSequentialImpulseConstraintSolver)];
    char colcfg_data[sizeof(btDefaultCollisionConfiguration)];
    char world_data[sizeof(btDiscreteDynamicsWorld)];
    char ddraw_data[sizeof(ddraw_c)];
    void *(*memalloc)(size_t);
};

static physcpp_t g_physcpp;

static void * physcpp_memalloc(size_t size)
{
    void *res = g_physcpp.memalloc(size);
    if (res == 0)
        throw std::bad_alloc();
    return res;
}

extern "C"
void physcpp_done(void)
{
    rigidbody_done();
    vehicle_done();
    colshape_done();
    world_done();
    try
    {
        if (g_physcpp.world)
        {
            if (g_physcpp.world->getNumCollisionObjects() > 0)
                fprintf(stderr, "Physical world is not empty\n");
            g_physcpp.world->~btDiscreteDynamicsWorld();
            g_physcpp.world = 0;
        }
        if (g_physcpp.solver)
        {
            g_physcpp.solver->~btSequentialImpulseConstraintSolver();
            g_physcpp.solver = 0;
        }
        if (g_physcpp.broadphase)
        {
            g_physcpp.broadphase->~btDbvtBroadphase();
            g_physcpp.broadphase = 0;
        }
        if (g_physcpp.dispatcher)
        {
            g_physcpp.dispatcher->~btCollisionDispatcher();
            g_physcpp.dispatcher = 0;
        }
        if (g_physcpp.colcfg)
        {
            g_physcpp.colcfg->~btDefaultCollisionConfiguration();
            g_physcpp.colcfg = 0;
        }
        if (g_physcpp.ddraw)
        {
            g_physcpp.ddraw->~ddraw_c();
            g_physcpp.ddraw = 0;
        }
    }
    catch (...)
    {
        fprintf(stderr, "physcpp_done: exception\n");
    }
}

extern "C"
int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int wld_count, int cs_count, int rb_count, int veh_count)
{
    int res;
    g_physcpp.memalloc = memalloc;
    try
    {
        btAlignedAllocSetCustom(physcpp_memalloc, memfree);
        g_physcpp.colcfg = new (g_physcpp.colcfg_data)
            btDefaultCollisionConfiguration();
        g_physcpp.dispatcher = new (g_physcpp.dispatcher_data)
            btCollisionDispatcher(g_physcpp.colcfg);
        g_physcpp.broadphase = new (g_physcpp.broadphase_data)
            btDbvtBroadphase();
        g_physcpp.solver = new (g_physcpp.solver_data)
            btSequentialImpulseConstraintSolver();
        g_physcpp.world = new (g_physcpp.world_data)
            btDiscreteDynamicsWorld(g_physcpp.dispatcher,
                                    g_physcpp.broadphase,
                                    g_physcpp.solver,
                                    g_physcpp.colcfg);
        g_physcpp.ddraw = new (g_physcpp.ddraw_data) ddraw_c();
        g_physcpp.world->setDebugDrawer(g_physcpp.ddraw);
    }
    catch (...)
    {
        physcpp_done();
        return PHYSRES_CANNOT_INIT;
    }
    res = world_init(wld_count);
    if (res != PHYSRES_OK)
        return res;
    res = colshape_init(cs_count);
    if (res != PHYSRES_OK)
        return res;
    res = rigidbody_init(rb_count);
    if (res != PHYSRES_OK)
        return res;
    return vehicle_init(veh_count);
}

extern "C"
int physcpp_update(float dt)
{
    try {
        g_physcpp.world->stepSimulation(dt);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

extern "C"
int physcpp_ddraw(void)
{
    try {
        g_physcpp.world->debugDrawWorld();
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

extern "C"
int physcpp_ddraw_set_mode(int mode)
{
    try {
        g_physcpp.ddraw->setDebugMode(mode);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

extern "C"
int physcpp_move(float *offset)
{
    try
    {
        int i;
        btCollisionObject *obj;
        btRigidBody *rb;
        btTransform tm;
        btVector3 ofs(offset[0], offset[1], offset[2]);
        for (i = 0; i < g_physcpp.world->getNumCollisionObjects(); ++i)
        {
            obj = g_physcpp.world->getCollisionObjectArray()[i];

            tm = obj->getWorldTransform();
            tm.setOrigin(tm.getOrigin() + ofs);
            obj->setWorldTransform(tm);

            tm = obj->getInterpolationWorldTransform();
            tm.setOrigin(tm.getOrigin() + ofs);
            obj->setInterpolationWorldTransform(tm);

            rb = btRigidBody::upcast(obj);
            if (rb && rb->getMotionState())
            {
                rb->getMotionState()->getWorldTransform(tm);
                tm.setOrigin(tm.getOrigin() + ofs);
                rb->getMotionState()->setWorldTransform(tm);
            }
        }
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

extern "C"
int physcpp_cs_alloc_box(int *csi, float *size)
{
    int res;
    res = colshape_alloc(csi);
    if (res != PHYSRES_OK)
        return res;
    return colshape_make_box(colshape_get(*csi), size);
}

extern "C"
int physcpp_cs_alloc_hmap(int *csi, float *hmap, int width, int length,
                          float hmin, float hmax, float *scale)
{
    int res;
    res = colshape_alloc(csi);
    if (res != PHYSRES_OK)
        return res;
    return colshape_make_hmap(colshape_get(*csi), hmap, width,
                              length, hmin, hmax, scale);
}

extern "C"
int physcpp_cs_alloc_comp(int *csi)
{
    int res;
    res = colshape_alloc(csi);
    if (res != PHYSRES_OK)
        return res;
    return colshape_make_comp(colshape_get(*csi));
}

extern "C"
int physcpp_cs_comp_add(int parenti, float *matrix, int childi)
{
    colshape_t *parent, *child;
    parent = colshape_get(parenti);
    child = colshape_get(childi);
    if (parent == 0 || child == 0)
        return PHYSRES_INVALID_CS;
    return colshape_comp_add(parent, matrix, child);
}

extern "C"
int physcpp_cs_free(int csi)
{
    colshape_t *cs;
    cs = colshape_get(csi);
    if (cs == 0)
        return PHYSRES_INVALID_CS;
    return colshape_free(cs);
}

extern "C"
int physcpp_rb_alloc(int *rbi, int csi, float *matrix,
                     float mass, float frict, float roll_frict)
{
    colshape_t *cs;
    cs = colshape_get(csi);
    if (cs == 0)
        return PHYSRES_INVALID_CS;
    return rigidbody_alloc(rbi, g_physcpp.world, cs, matrix,
                           mass, frict, roll_frict);
}

extern "C"
int physcpp_rb_free(int rbi)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0)
        return PHYSRES_INVALID_RB;
    return rigidbody_free(rb, g_physcpp.world);
}

extern "C"
int physcpp_rb_fetch_tm(int rbi, float *matrix)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0)
        return PHYSRES_INVALID_RB;
    return rigidbody_fetch_tm(rb, matrix);
}

extern "C"
int physcpp_set_gravity(float *v)
{
    try {
        g_physcpp.world->setGravity(btVector3(v[0], v[1], v[2]));
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

extern "C"
void physcpp_left(int *cs_left, int *rb_left, int *veh_left)
{
    *cs_left = colshape_left();
    *rb_left = rigidbody_left();
    *veh_left = vehicle_left();
}

extern "C"
int physcpp_veh_alloc(int *vehi, int shapei, int inerti, float *matrix,
                      float mass, float ch_frict, float ch_roll_frict,
                      float sus_stif, float sus_comp, float sus_damp,
                      float sus_trav, float sus_force, float slip_frict)
{
    colshape_t *shape, *inert;
    shape = colshape_get(shapei);
    inert = colshape_get(inerti);
    if (shape == 0 || inert == 0)
        return PHYSRES_INVALID_CS;
    return vehicle_alloc(vehi, g_physcpp.world, shape, inert, matrix, mass,
                         ch_frict, ch_roll_frict, sus_stif, sus_comp,
                         sus_damp, sus_trav, sus_force, slip_frict);
}

extern "C"
int physcpp_veh_free(int vehi)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_free(veh, g_physcpp.world);
}

extern "C"
int physcpp_veh_add_wheel(int *wheel, int vehi, float *pos, float *dir,
                          float *axl, float sus_rest, float roll,
                          float radius, int front)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_add_wheel(veh, wheel, pos, dir, axl, sus_rest,
                             roll, radius, front);
}

extern "C"
int physcpp_veh_set_wheel(int vehi, int wheel, float engine,
                          float brake, float steer)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_set_wheel(veh, wheel, engine, brake, steer);
}

extern "C"
int physcpp_veh_fetch_chassis_tm(int vehi, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_fetch_chassis_tm(veh, matrix);
}

extern "C"
int physcpp_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_fetch_wheel_tm(veh, wheel, matrix);
}

extern "C"
int physcpp_veh_transform(int vehi, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_transform(veh, matrix);
}

extern "C"
int physcpp_veh_wheel_contact(int vehi, int wheel, int *in_contact)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_wheel_contact(veh, wheel, in_contact);
}
