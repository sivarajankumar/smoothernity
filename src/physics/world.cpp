#include "world.hpp"
#include "colshape.hpp"
#include "physres.h"
#include "../util/util.hpp"
#include <stdio.h>
#include <string.h>

static const size_t WORLD_SIZE = 128;

struct worlds_t {
    int count;
    char *pool;
};

static worlds_t g_worlds;

int world_init(int count) {
    world_t *wld;
    if (sizeof(world_t) > WORLD_SIZE) {
        fprintf(stderr, "Invalid size:\nsizeof(world_t) == %i\n",
                (int)sizeof(world_t));
        return PHYSRES_CANNOT_INIT;
    }
    g_worlds.pool = (char*)util_malloc(WORLD_SIZE, WORLD_SIZE * count);
    if (!g_worlds.pool)
        return PHYSRES_CANNOT_INIT;
    memset(g_worlds.pool, 0, WORLD_SIZE * count);
    g_worlds.count = count;
    for (int i = 0; i < count; ++i) {
        wld = world_get(i);
        try {
            wld->colcfg = new btDefaultCollisionConfiguration();
            wld->dispatcher = new btCollisionDispatcher(wld->colcfg);
            wld->broadphase = new btDbvtBroadphase();
            wld->solver = new btSequentialImpulseConstraintSolver();
            wld->world = new btDiscreteDynamicsWorld(wld->dispatcher,
                                                     wld->broadphase,
                                                     wld->solver,
                                                     wld->colcfg);
            wld->ddraw = new ddraw_c();
            wld->world->setDebugDrawer(wld->ddraw);
        } catch (...) {
            goto cleanup;
        }
    }
    return PHYSRES_OK;
cleanup:
    for (int i = 0; i < count; ++i) {
        wld = world_get(i);
        if (wld->colcfg)
            delete wld->colcfg;
        if (wld->dispatcher)
            delete wld->dispatcher;
        if (wld->broadphase)
            delete wld->broadphase;
        if (wld->solver)
            delete wld->solver;
        if (wld->world)
            delete wld->world;
        if (wld->ddraw)
            delete wld->ddraw;
    }
    util_free(g_worlds.pool);
    g_worlds.pool = 0;
    return PHYSRES_CANNOT_INIT;
}

void world_done(void) {
    world_t *wld;
    if (!g_worlds.pool)
        return;
    for (int i = 0; i < g_worlds.count; ++i) {
        wld = world_get(i);
        if (wld->world->getNumCollisionObjects() > 0)
            fprintf(stderr, "world_done: world still has refs\n");
        try {
            delete wld->world;
            delete wld->solver;
            delete wld->broadphase;
            delete wld->dispatcher;
            delete wld->colcfg;
            delete wld->ddraw;
        } catch (...) {
            fprintf(stderr, "world_done: exception\n");
        }
    }
    util_free(g_worlds.pool);
    g_worlds.pool = 0;
}

int world_update(world_t *wld, float dt) {
    try {
        wld->world->stepSimulation(dt);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

world_t * world_get(int worldi) {
    if (worldi >= 0 && worldi < g_worlds.count)
        return (world_t*)(g_worlds.pool + WORLD_SIZE * worldi);
    else
        return 0;
}

int world_ddraw(world_t *wld) {
    try {
        wld->world->debugDrawWorld();
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int world_ddraw_mode(world_t *wld, int mode) {
    try {
        wld->ddraw->setDebugMode(mode);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int world_gravity(world_t *wld, float *v) {
    try {
        wld->world->setGravity(btVector3(v[0], v[1], v[2]));
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int world_move(world_t *wld, float *offset) {
    try {
        btCollisionObject *obj;
        btRigidBody *rb;
        btTransform tm;
        btVector3 ofs(offset[0], offset[1], offset[2]);
        for (int i = 0; i < wld->world->getNumCollisionObjects(); ++i) {
            obj = wld->world->getCollisionObjectArray()[i];

            tm = obj->getWorldTransform();
            tm.setOrigin(tm.getOrigin() + ofs);
            obj->setWorldTransform(tm);

            tm = obj->getInterpolationWorldTransform();
            tm.setOrigin(tm.getOrigin() + ofs);
            obj->setInterpolationWorldTransform(tm);

            rb = btRigidBody::upcast(obj);
            if (rb && rb->getMotionState()) {
                rb->getMotionState()->getWorldTransform(tm);
                tm.setOrigin(tm.getOrigin() + ofs);
                rb->getMotionState()->setWorldTransform(tm);
            }
        }
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int world_cast(world_t *wld, colshape_t *cs,
float *mfrom, float *mto, float *vout) {
    if (!cs->shape_convex)
        return PHYSRES_INVALID_CS;
    try {
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
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}
