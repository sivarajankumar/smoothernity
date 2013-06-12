#include "world.hpp"
#include "colshape.hpp"
#include "physres.h"
#include "../platform/mem.hpp"
#include <stdio.h>

static const size_t WORLD_SIZE = 128;

struct worlds_t {
    int count;
    char *pool;
};

static_assert(sizeof(world_t) <= WORLD_SIZE, "Invalid world_t size");

static worlds_t g_worlds;

int world_init(int count) {
    world_t *wld;
    g_worlds.count = count;
    g_worlds.pool = (char*)mem_alloc(MEM_ALIGNOF(world_t), WORLD_SIZE * count);
    if (!g_worlds.pool)
        return PHYSRES_CANNOT_INIT;
    for (int i = 0; i < count; ++i) {
        wld = world_get(i);
        wld->broadphase = 0;
        wld->dispatcher = 0;
        wld->solver = 0;
        wld->colcfg = 0;
        wld->world = 0;
        wld->ddraw = 0;
    }
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
            return PHYSRES_CANNOT_INIT;
        }
    }
    return PHYSRES_OK;
}

void world_done(void) {
    world_t *wld;
    if (!g_worlds.pool)
        return;
    for (int i = 0; i < g_worlds.count; ++i) {
        wld = world_get(i);
        if (wld->world && wld->world->getNumCollisionObjects() > 0)
            fprintf(stderr, "world_done: world still has refs\n");
        try {
            if (wld->world)
                delete wld->world;
            if (wld->solver)
                delete wld->solver;
            if (wld->broadphase)
                delete wld->broadphase;
            if (wld->dispatcher)
                delete wld->dispatcher;
            if (wld->colcfg)
                delete wld->colcfg;
            if (wld->ddraw)
                delete wld->ddraw;
        } catch (...) {
            fprintf(stderr, "world_done: exception\n");
        }
    }
    mem_free(g_worlds.pool);
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
