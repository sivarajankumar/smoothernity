#include "colshape.hpp"
#include "rigidbody.hpp"
#include "vehicle.hpp"
#include "physres.h"
#include "ddraw.hpp"
#include <lua.h>
#include <btBulletDynamicsCommon.h>
#include <exception>

struct physcpp_t
{
    btBroadphaseInterface *broadphase;
    btCollisionDispatcher *dispatcher;
    btConstraintSolver *solver;
    btDefaultCollisionConfiguration *colcfg;
    btDiscreteDynamicsWorld *world;
    ddraw_c ddraw;
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
    int i;
    if (g_physcpp.world)
    {
        for (i = 0; i < g_physcpp.world->getNumCollisionObjects(); ++i)
        {
            g_physcpp.world->removeCollisionObject(
                g_physcpp.world->getCollisionObjectArray()[i]);
        }
    }
    rigidbody_done();
    vehicle_done();
    colshape_done();
    if (g_physcpp.world)
    {
        delete g_physcpp.world;
        g_physcpp.world = 0;
    }
    if (g_physcpp.solver)
    {
        delete g_physcpp.solver;
        g_physcpp.solver = 0;
    }
    if (g_physcpp.broadphase)
    {
        delete g_physcpp.broadphase;
        g_physcpp.broadphase = 0;
    }
    if (g_physcpp.dispatcher)
    {
        delete g_physcpp.dispatcher;
        g_physcpp.dispatcher = 0;
    }
    if (g_physcpp.colcfg)
    {
        delete g_physcpp.colcfg;
        g_physcpp.colcfg = 0;
    }
}

extern "C"
int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int cs_count, int rb_count, int veh_count)
{
    g_physcpp.memalloc = memalloc;
    btAlignedAllocSetCustom(physcpp_memalloc, memfree);
    try
    {
        g_physcpp.colcfg = new btDefaultCollisionConfiguration();
        g_physcpp.dispatcher = new btCollisionDispatcher(g_physcpp.colcfg);
        g_physcpp.broadphase = new btDbvtBroadphase();
        g_physcpp.solver = new btSequentialImpulseConstraintSolver();
        g_physcpp.world = new btDiscreteDynamicsWorld(g_physcpp.dispatcher,
                                                      g_physcpp.broadphase,
                                                      g_physcpp.solver,
                                                      g_physcpp.colcfg);
    }
    catch (std::exception)
    {
        physcpp_done();
        return PHYSRES_CANNOT_INIT;
    }
    btAlignedAllocSetCustom(memalloc, memfree);
    g_physcpp.world->setDebugDrawer(&g_physcpp.ddraw);
    if (colshape_init(cs_count) != 0
     || rigidbody_init(rb_count) != 0
     || vehicle_init(veh_count) != 0)
    {
        return PHYSRES_CANNOT_INIT;
    }
    return PHYSRES_OK;
}

extern "C"
void physcpp_update(float dt)
{
    g_physcpp.world->stepSimulation(dt);
}

extern "C"
void physcpp_ddraw(void)
{
    g_physcpp.world->debugDrawWorld();
}

extern "C"
void physcpp_ddraw_set_mode(int mode)
{
    g_physcpp.ddraw.setDebugMode(mode);
}

extern "C"
int physcpp_cs_alloc_box(int *csi, float mass, float *size)
{
    *csi = colshape_alloc();
    if (*csi == -1)
        return PHYSRES_OUT_OF_CS;
    colshape_make_box(colshape_get(*csi), mass, size);
    return PHYSRES_OK;
}

extern "C"
int physcpp_cs_alloc_hmap(int *csi, float *hmap, int width, int length,
                          float hmin, float hmax, float *scale)
{
    *csi = colshape_alloc();
    if (*csi == -1)
        return PHYSRES_OUT_OF_CS;
    colshape_make_hmap(colshape_get(*csi), hmap, width,
                       length, hmin, hmax, scale);
    return PHYSRES_OK;
}

extern "C"
int physcpp_cs_free(int csi)
{
    colshape_t *cs;
    cs = colshape_get(csi);
    if (cs == 0)
        return PHYSRES_INVALID_CS;
    colshape_free(cs, g_physcpp.world);
    return PHYSRES_OK;
}

extern "C"
int physcpp_rb_alloc(int *rbi, int csi, float *matrix,
                     float frict, float roll_frict)
{
    colshape_t *cs;
    cs = colshape_get(csi);
    if (cs == 0 || cs->shape == 0)
        return PHYSRES_INVALID_CS;
    *rbi = rigidbody_alloc(g_physcpp.world, cs, matrix, frict, roll_frict);
    if (rigidbody_get(*rbi) == 0)
        return PHYSRES_OUT_OF_RB;
    return PHYSRES_OK;
}

extern "C"
int physcpp_rb_free(int rbi)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0)
        return PHYSRES_INVALID_RB;
    rigidbody_free(rb, g_physcpp.world);
    return PHYSRES_OK;
}

extern "C"
int physcpp_rb_fetch_tm(int rbi, float *matrix)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0)
        return PHYSRES_INVALID_RB;
    rigidbody_fetch_tm(rb, matrix);
    return PHYSRES_OK;
}

extern "C"
void physcpp_set_gravity(float *v)
{
    g_physcpp.world->setGravity(btVector3(v[0], v[1], v[2]));
}

extern "C"
void physcpp_left(int *cs_left, int *rb_left, int *veh_left)
{
    colshape_left(cs_left);
    rigidbody_left(rb_left);
    vehicle_left(veh_left);
}

extern "C"
int physcpp_veh_alloc(int *vehi, int csi, float *matrix,
                      float ch_frict, float ch_roll_frict,
                      float sus_stif, float sus_comp, float sus_damp,
                      float sus_trav, float sus_force, float slip_frict)
{
    colshape_t *cs;
    cs = colshape_get(csi);
    if (cs == 0 || cs->shape == 0)
        return PHYSRES_INVALID_CS;
    *vehi = vehicle_alloc(g_physcpp.world, cs, matrix, ch_frict, ch_roll_frict,
                          sus_stif, sus_comp, sus_damp, sus_trav, sus_force,
                          slip_frict);
    if (vehicle_get(*vehi) == 0)
        return PHYSRES_OUT_OF_VEH;
    return PHYSRES_OK;
}

extern "C"
int physcpp_veh_free(int vehi)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    vehicle_free(veh, g_physcpp.world);
    return PHYSRES_OK;
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
    *wheel = vehicle_add_wheel(veh, pos, dir, axl, sus_rest,
                               roll, radius, front);
    return PHYSRES_OK;
}

extern "C"
int physcpp_veh_set_wheel(int vehi, int wheel, float engine,
                          float brake, float steer)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    if (0 != vehicle_set_wheel(veh, wheel, engine, brake, steer))
        return PHYSRES_INVALID_VEH_WHEEL;
    return PHYSRES_OK;
}

extern "C"
int physcpp_veh_fetch_chassis_tm(int vehi, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    vehicle_fetch_chassis_tm(veh, matrix);
    return PHYSRES_OK;
}

extern "C"
int physcpp_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    if (0 != vehicle_fetch_wheel_tm(veh, wheel, matrix))
        return PHYSRES_INVALID_VEH_WHEEL;
    return PHYSRES_OK;
}

extern "C"
int physcpp_veh_transform(int vehi, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    vehicle_transform(veh, matrix);
    return PHYSRES_OK;
}

extern "C"
int physcpp_veh_wheel_contact(int vehi, int wheel, int *in_contact)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    if (0 != vehicle_wheel_contact(veh, wheel, in_contact))
        return PHYSRES_INVALID_VEH_WHEEL;
    return PHYSRES_OK;
}
