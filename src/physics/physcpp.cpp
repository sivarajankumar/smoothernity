#include "colshape.hpp"
#include "rigidbody.hpp"
#include <lua.h>
#include <btBulletDynamicsCommon.h>
#include <exception>

struct physics_t
{
    btBroadphaseInterface *broadphase;
    btCollisionDispatcher *dispatcher;
    btConstraintSolver *solver;
    btDefaultCollisionConfiguration *colcfg;
    btDiscreteDynamicsWorld *world;
};

static physics_t g_physics;

extern "C"
void physcpp_done(void)
{
    int i;
    if (g_physics.world)
    {
        for (i = 0; i < g_physics.world->getNumCollisionObjects(); --i)
        {
            g_physics.world->removeCollisionObject(
                g_physics.world->getCollisionObjectArray()[i]);
        }
    }
    rigidbody_done();
    colshape_done();
    if (g_physics.world)
    {
        delete g_physics.world;
        g_physics.world = 0;
    }
    if (g_physics.solver)
    {
        delete g_physics.solver;
        g_physics.solver = 0;
    }
    if (g_physics.broadphase)
    {
        delete g_physics.broadphase;
        g_physics.broadphase = 0;
    }
    if (g_physics.dispatcher)
    {
        delete g_physics.dispatcher;
        g_physics.dispatcher = 0;
    }
    if (g_physics.colcfg)
    {
        delete g_physics.colcfg;
        g_physics.colcfg = 0;
    }
}

extern "C"
int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int cs_count, int rb_count)
{
    btAlignedAllocSetCustom(memalloc, memfree);
    try
    {
        g_physics.colcfg = new btDefaultCollisionConfiguration();
        g_physics.dispatcher = new btCollisionDispatcher(g_physics.colcfg);
        g_physics.broadphase = new btDbvtBroadphase();
        g_physics.solver = new btSequentialImpulseConstraintSolver();
        g_physics.world = new btDiscreteDynamicsWorld(g_physics.dispatcher,
                                                      g_physics.broadphase,
                                                      g_physics.solver,
                                                      g_physics.colcfg);
    }
    catch (std::exception)
    {
        physcpp_done();
        return 1;
    }
    if (colshape_init(cs_count) != 0
     || rigidbody_init(rb_count) != 0)
    {
        return 1;
    }
    return 0;
}
