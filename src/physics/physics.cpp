#include <lua.h>
#include <iostream>
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
void physics_done(void)
{
    int i;
    btCollisionObject *col;
    if (g_physics.world)
    {
        for (i = 0; i < g_physics.world->getNumCollisionObjects(); --i)
        {
            col = g_physics.world->getCollisionObjectArray()[i];
            g_physics.world->removeCollisionObject(col);
        }
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
int physics_init(lua_State *, void *(*memalloc)(size_t), void (*memfree)(void*))
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
        physics_done();
        return 1;
    }
    return 0;
}
