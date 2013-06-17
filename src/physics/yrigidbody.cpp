#include "yrigidbody.hpp"
#include "yphysres.h"
#include "ymstate.hpp"
#include "yworld.hpp"
#include "ycolshape.hpp"
#include "pmem.hpp"
#include "vlog.hpp"

static const size_t YRIGIDBODY_SIZE = 128;

struct yrigidbodies_t {
    int count;
    char *pool;
};

static_assert(sizeof(yrigidbody_t) <= YRIGIDBODY_SIZE,
              "Invalid yrigidbody_t size");

static yrigidbodies_t g_yrigidbodies;

int yrigidbody_init(int count) {
    yrigidbody_t *rb;
    g_yrigidbodies.count = count;
    g_yrigidbodies.pool = (char*)pmem_alloc(PMEM_ALIGNOF(yrigidbody_t),
                                           YRIGIDBODY_SIZE * count);
    if (!g_yrigidbodies.pool)
        return YPHYSRES_CANNOT_INIT;
    for (int i = 0; i < count; ++i) {
        rb = yrigidbody_get(i);
        rb->vacant = 1;
        rb->body = 0;
        rb->mstate = 0;
        rb->data = 0;
        rb->wld = 0;
        rb->cs = 0;
        rb->cs_prev = rb->cs_next = 0;
    }
    for (int i = 0; i < count; ++i) {
        rb = yrigidbody_get(i);
        try {
            rb->mstate = new ymstate_c();
        } catch (...) {
            return YPHYSRES_CANNOT_INIT;
        }
        rb->data = (char*)pmem_alloc(PMEM_ALIGNOF(btRigidBody),
                                     sizeof(btRigidBody));
        if (!rb->data)
            return YPHYSRES_CANNOT_INIT;
    }
    return YPHYSRES_OK;
}

void yrigidbody_done(void) {
    yrigidbody_t *rb;
    if (!g_yrigidbodies.pool)
        return;
    for (int i = 0; i < g_yrigidbodies.count; ++i) {
        rb = yrigidbody_get(i);
        yrigidbody_free(rb);
        try {
            if (rb->mstate)
                delete rb->mstate;
        } catch (...) {
            VLOG_ERROR("exception");
        }
        if (rb->data)
            pmem_free(rb->data);
    }
    pmem_free(g_yrigidbodies.pool);
    g_yrigidbodies.pool = 0;
}

yrigidbody_t * yrigidbody_get(int rbi) {
    if (rbi >= 0 && rbi < g_yrigidbodies.count)
        return (yrigidbody_t*)(g_yrigidbodies.pool + YRIGIDBODY_SIZE * rbi);
    else
        return 0;
}

int yrigidbody_free(yrigidbody_t *rb) {
    if (rb->vacant == 1)
        return YPHYSRES_INVALID_RB;
    rb->vacant = 1;
    if (rb->cs->rbs == rb)
        rb->cs->rbs = rb->cs_next;
    if (rb->cs_next)
        rb->cs_next->cs_prev = rb->cs_prev;
    if (rb->cs_prev)
        rb->cs_prev->cs_next = rb->cs_next;
    rb->cs = 0;
    rb->cs_prev = 0;
    rb->cs_next = 0;
    try {
        if (rb->body && rb->wld)
            rb->wld->world->removeCollisionObject(rb->body);
        if (rb->body)
            rb->body->~btRigidBody();
    } catch (...) {
        rb->body = 0;
        return YPHYSRES_INTERNAL;
    }
    rb->body = 0;
    rb->wld = 0;
    return YPHYSRES_OK;
}

int yrigidbody_alloc(yrigidbody_t *rb, yworld_t *wld, ycolshape_t *cs,
float *matrix, float mass, float frict, float roll_frict) {
    if (!rb->vacant)
        return YPHYSRES_INVALID_RB;
    if (!cs->shape)
        return YPHYSRES_INVALID_CS;
    rb->vacant = 0;

    rb->cs = cs;
    if (cs->rbs)
        cs->rbs->cs_prev = rb;
    rb->cs_next = cs->rbs;
    rb->cs_prev = 0;
    cs->rbs = rb;

    try {
        btVector3 inertia;
        rb->mstate->m.setFromOpenGLMatrix(matrix);

        if (mass > 0.0f)
            cs->shape->calculateLocalInertia(mass, inertia);
        else
            inertia = btVector3(0,0,0);

        btRigidBody::btRigidBodyConstructionInfo info
                (mass, rb->mstate, cs->shape, inertia);
        info.m_friction = frict;
        info.m_rollingFriction = roll_frict;

        rb->body = new (rb->data) btRigidBody(info);

        wld->world->addRigidBody(rb->body);
        rb->wld = wld;
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yrigidbody_fetch_tm(yrigidbody_t *rb, float *matrix) {
    try {
        rb->mstate->m.getOpenGLMatrix(matrix);
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

