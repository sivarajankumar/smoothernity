#include "world.hpp"
#include "physres.hpp"
#include "ddraw.hpp"
#include <btBulletDynamicsCommon.h>
#include <stdlib.h>
#include <stdio.h>

struct world_t
{
    float time_scale;
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

    int vacant;
    world_t *next;
    world_t *prev;
};

struct worlds_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    world_t *pool;
    world_t *vacant;
    world_t *active;
};

static worlds_t g_worlds;

int world_init(int count)
{
    int i;
    world_t *wld;
    g_worlds.pool = (world_t*)calloc(count, sizeof(world_t));
    if (g_worlds.pool == 0)
        return PHYSRES_CANNOT_INIT;
    g_worlds.vacant = g_worlds.pool;
    g_worlds.count = count;
    g_worlds.left = count;
    g_worlds.left_min = count;
    for (i = 0; i < count; ++i)
    {
        wld = g_worlds.pool + i;
        wld->vacant = 1;
        if (i < count - 1)
            wld->next = g_worlds.pool + i + 1;
        if (i > 0)
            wld->prev = g_worlds.pool + i - 1;
        try
        {
            wld->colcfg = new (wld->colcfg_data)
                btDefaultCollisionConfiguration();
            wld->dispatcher = new (wld->dispatcher_data)
                btCollisionDispatcher(wld->colcfg);
            wld->broadphase = new (wld->broadphase_data)
                btDbvtBroadphase();
            wld->solver = new (wld->solver_data)
                btSequentialImpulseConstraintSolver();
            wld->world = new (wld->world_data)
                btDiscreteDynamicsWorld(wld->dispatcher,
                                        wld->broadphase,
                                        wld->solver,
                                        wld->colcfg);
            wld->ddraw = new (wld->ddraw_data) ddraw_c();
            wld->world->setDebugDrawer(wld->ddraw);
        }
        catch (...)
        {
            goto cleanup;
        }
    }
    return PHYSRES_OK;
cleanup:
    free(g_worlds.pool);
    g_worlds.pool = 0;
    return PHYSRES_CANNOT_INIT;
}

void world_done(void)
{
    int i;
    world_t *wld;
    if (g_worlds.pool == 0)
        return;
    printf("Worlds usage: %i/%i, allocs/frees: %i/%i\n",
           g_worlds.count - g_worlds.left_min, g_worlds.count,
           g_worlds.allocs, g_worlds.frees);
    if (g_worlds.active)
        fprintf(stderr, "Some worlds are still active\n");
    for (i = 0; i < g_worlds.count; ++i)
    {
        wld = g_worlds.pool + i;
        try
        {
            wld->world->~btDiscreteDynamicsWorld();
            wld->solver->~btSequentialImpulseConstraintSolver();
            wld->broadphase->~btDbvtBroadphase();
            wld->dispatcher->~btCollisionDispatcher();
            wld->colcfg->~btDefaultCollisionConfiguration();
            wld->ddraw->~ddraw_c();
        }
        catch (...)
        {
            fprintf(stderr, "world_done: exception\n");
        }
    }
    free(g_worlds.pool);
    g_worlds.pool = 0;
}

int world_update(float dt)
{
    world_t *wld;
    for (wld = g_worlds.active; wld; wld = wld->next)
    {
        if (wld->time_scale == 0.0f)
            continue;
        try {
            wld->world->stepSimulation(dt * wld->time_scale);
        } catch (...) {
            return PHYSRES_INTERNAL;
        }
    }
    return PHYSRES_OK;
}

int world_alloc(int *worldi)
{
    world_t *wld;
    if (g_worlds.vacant == 0)
        return PHYSRES_OUT_OF_WLD;

    ++g_worlds.allocs;
    --g_worlds.left;
    if (g_worlds.left < g_worlds.left_min)
        g_worlds.left_min = g_worlds.left;

    wld = g_worlds.vacant;
    g_worlds.vacant = g_worlds.vacant->next;

    wld->prev = 0;
    wld->next = g_worlds.active;
    if (g_worlds.active)
        g_worlds.active->prev = wld;
    g_worlds.active = wld;

    wld->time_scale = 1;
    wld->vacant = 0;

    *worldi = wld - g_worlds.pool;

    return PHYSRES_OK;
}

int world_free(world_t *wld)
{
    if (wld->vacant == 1)
        return PHYSRES_INVALID_WLD;
    try {
        if (wld->world->getNumCollisionObjects() > 0)
            return PHYSRES_INVALID_WLD;
    } catch (...) {
        return PHYSRES_INTERNAL;
    }

    ++g_worlds.frees;
    ++g_worlds.left;

    if (wld->prev)
        wld->prev->next = wld->next;
    if (wld->next)
        wld->next->prev = wld->prev;
    if (wld == g_worlds.active)
        g_worlds.active = wld->next;

    wld->prev = 0;
    wld->next = g_worlds.vacant;
    if (g_worlds.vacant)
        g_worlds.vacant->prev = wld;
    g_worlds.vacant = wld;

    wld->vacant = 1;

    return PHYSRES_OK;
}

world_t * world_get(int worldi)
{
    if (worldi >= 0 && worldi < g_worlds.count)
        return g_worlds.pool + worldi;
    else
        return 0;
}

int world_ddraw(world_t *wld)
{
    try {
        wld->world->debugDrawWorld();
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}
