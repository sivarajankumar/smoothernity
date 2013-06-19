#include "yworld.hpp"
#include "yddraw.hpp"
#include "ycolshape.hpp"
#include "yphysres.h"
#include "pmem.hpp"
#include "vlog.hpp"

struct yworlds_t {
    int count;
    yworld_t *pool;
};

static yworlds_t g_worlds;

int yworld_init(int count) {
    yworld_t *wld;
    g_worlds.count = count;
    g_worlds.pool = (yworld_t*)pmem_alloc(PMEM_ALIGNOF(yworld_t),
                                          sizeof(yworld_t) * count);
    if (!g_worlds.pool)
        return YPHYSRES_CANNOT_INIT;
    for (int i = 0; i < count; ++i) {
        wld = yworld_get(i);
        wld->broadphase = 0;
        wld->dispatcher = 0;
        wld->solver = 0;
        wld->colcfg = 0;
        wld->world = 0;
        wld->ddraw = 0;
    }
    for (int i = 0; i < count; ++i) {
        wld = yworld_get(i);
        try {
            wld->colcfg = new btDefaultCollisionConfiguration();
            wld->dispatcher = new btCollisionDispatcher(wld->colcfg);
            wld->broadphase = new btDbvtBroadphase();
            wld->solver = new btSequentialImpulseConstraintSolver();
            wld->world = new btDiscreteDynamicsWorld(wld->dispatcher,
                                                     wld->broadphase,
                                                     wld->solver,
                                                     wld->colcfg);
            wld->ddraw = new yddraw_c();
            wld->world->setDebugDrawer(wld->ddraw);
        } catch (...) {
            return YPHYSRES_CANNOT_INIT;
        }
    }
    return YPHYSRES_OK;
}

void yworld_done(void) {
    yworld_t *wld;
    if (!g_worlds.pool)
        return;
    for (int i = 0; i < g_worlds.count; ++i) {
        wld = yworld_get(i);
        if (wld->world && wld->world->getNumCollisionObjects() > 0)
            VLOG_ERROR("world still has refs");
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
            VLOG_ERROR("exception");
        }
    }
    pmem_free(g_worlds.pool);
    g_worlds.pool = 0;
}

int yworld_update(yworld_t *wld, float dt) {
    try {
        wld->world->stepSimulation(dt);
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

yworld_t * yworld_get(int worldi) {
    if (worldi >= 0 && worldi < g_worlds.count)
        return g_worlds.pool + worldi;
    else
        return 0;
}

int yworld_ddraw(yworld_t *wld) {
    try {
        wld->world->debugDrawWorld();
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yworld_ddraw_mode(yworld_t *wld, int mode) {
    try {
        wld->ddraw->setDebugMode(mode);
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yworld_gravity(yworld_t *wld, float *v) {
    try {
        wld->world->setGravity(btVector3(v[0], v[1], v[2]));
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yworld_move(yworld_t *wld, float *offset) {
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
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yworld_cast(yworld_t *wld, ycolshape_t *cs,
float *mfrom, float *mto, float *vout) {
    if (!cs->shape_convex)
        return YPHYSRES_INVALID_CS;
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
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}
