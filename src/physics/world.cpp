#include "world.hpp"
#include "colshape.hpp"
#include "physres.h"
#include <stdlib.h>
#include <stdio.h>

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

int world_left(void)
{
    return g_worlds.left;
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
            return PHYSRES_WLD_HAS_REFS;
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

int world_ddraw_mode(world_t *wld, int mode)
{
    try {
        wld->ddraw->setDebugMode(mode);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int world_gravity(world_t *wld, float *v)
{
    try {
        wld->world->setGravity(btVector3(v[0], v[1], v[2]));
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int world_move(world_t *wld, float *offset)
{
    try
    {
        int i;
        btCollisionObject *obj;
        btRigidBody *rb;
        btTransform tm;
        btVector3 ofs(offset[0], offset[1], offset[2]);
        for (i = 0; i < wld->world->getNumCollisionObjects(); ++i)
        {
            obj = wld->world->getCollisionObjectArray()[i];

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

int world_cast(world_t *wld, colshape_t *cs, float *mfrom,
               float *mto, float *vout)
{
    if (cs->shape_convex == 0)
        return PHYSRES_INVALID_CS;
    try
    {
        btTransform tmfrom, tmto;
        tmfrom.setFromOpenGLMatrix(mfrom);
        tmto.setFromOpenGLMatrix(mto);
        btCollisionWorld::ClosestConvexResultCallback res(tmfrom.getOrigin(),
                                                          tmto.getOrigin());
        wld->world->convexSweepTest(cs->shape_convex, tmfrom, tmto, res);
        btVector3 out(lerp(res.m_convexFromWorld, res.m_convexToWorld,
                           res.m_closestHitFraction));
        vout[0] = out.m_floats[0];
        vout[1] = out.m_floats[1];
        vout[2] = out.m_floats[2];
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}