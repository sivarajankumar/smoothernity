#include "colshape.hpp"
#include "rigidbody.hpp"
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
};

static physcpp_t g_physcpp;

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
                 int cs_count, int rb_count)
{
    btAlignedAllocSetCustom(memalloc, memfree);
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
    g_physcpp.world->setDebugDrawer(&g_physcpp.ddraw);
    if (colshape_init(cs_count) != 0
     || rigidbody_init(rb_count) != 0)
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
    if (colshape_get(csi) == 0)
        return PHYSRES_INVALID_CS;
    colshape_free(csi);
    return PHYSRES_OK;
}

extern "C"
int physcpp_rb_alloc(int *rbi, int csi, float *matrix)
{
    rigidbody_t *rb;
    colshape_t *cs;
    *rbi = rigidbody_alloc();
    rb = rigidbody_get(*rbi);
    cs = colshape_get(csi);
    if (rb == 0)
        return PHYSRES_OUT_OF_RB;
    if (cs == 0 || cs->shape == 0)
        return PHYSRES_INVALID_CS;
    rb->mstate->get.setFromOpenGLMatrix(matrix);
    rb->mstate->set = rb->mstate->get;
    rb->mstate->was_set = 1;
    rigidbody_make(rb, cs);
    g_physcpp.world->addRigidBody(rb->body);
    return PHYSRES_OK;
}

extern "C"
int physcpp_rb_free(int rbi)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0)
        return PHYSRES_INVALID_RB;
    if (rb->body)
        g_physcpp.world->removeCollisionObject(rb->body);
    rigidbody_free(rbi);
    return PHYSRES_OK;
}

extern "C"
int physcpp_rb_get_new_matrix(int rbi, float *matrix)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0)
        return PHYSRES_INVALID_RB;
    if (rb->mstate->was_set)
    {
        rb->mstate->set.getOpenGLMatrix(matrix);
        rb->mstate->was_set = 0;
    }
    return PHYSRES_OK;
}

extern "C"
void physcpp_set_gravity(float *v)
{
    g_physcpp.world->setGravity(btVector3(v[0], v[1], v[2]));
}

extern "C"
void physcpp_left(int *cs_left, int *rb_left)
{
    colshape_left(cs_left);
    rigidbody_left(rb_left);
}
