#include "physres.h"
#include "rigidbody.hpp"
#include "world.hpp"
#include "colshape.hpp"
#include "../util/util.hpp"
#include "../platform/memory.h"
#include <stdio.h>

static const size_t RIGIDBODY_SIZE = 128;

struct rigidbodies_t {
    int count;
    char *pool;
};

static rigidbodies_t g_rigidbodies;

int rigidbody_init(int count) {
    rigidbody_t *rb;
    if (sizeof(rigidbody_t) > RIGIDBODY_SIZE) {
        fprintf(stderr, "Invalid size:\nsizeof(rigidbody_t) == %i\n",
                (int)sizeof(rigidbody_t));
        return PHYSRES_CANNOT_INIT;
    }
    g_rigidbodies.count = count;
    g_rigidbodies.pool = (char*)util_malloc(RIGIDBODY_SIZE, RIGIDBODY_SIZE * count);
    if (!g_rigidbodies.pool)
        return PHYSRES_CANNOT_INIT;
    for (int i = 0; i < count; ++i) {
        rb = rigidbody_get(i);
        rb->vacant = 1;
        rb->body = 0;
        rb->mstate = 0;
        rb->data = 0;
        rb->wld = 0;
        rb->cs = 0;
        rb->cs_prev = rb->cs_next = 0;
    }
    for (int i = 0; i < count; ++i) {
        rb = rigidbody_get(i);
        try {
            rb->mstate = new mstate_c();
        } catch (...) {
            return PHYSRES_CANNOT_INIT;
        }
        rb->data = (char*)util_malloc(ALIGNOF(btRigidBody), sizeof(btRigidBody));
        if (!rb->data)
            return PHYSRES_CANNOT_INIT;
    }
    return PHYSRES_OK;
}

void rigidbody_done(void) {
    rigidbody_t *rb;
    if (!g_rigidbodies.pool)
        return;
    for (int i = 0; i < g_rigidbodies.count; ++i) {
        rb = rigidbody_get(i);
        rigidbody_free(rb);
        try {
            if (rb->mstate)
                delete rb->mstate;
        } catch (...) {
            fprintf(stderr, "rigidbody_done: exception\n");
        }
        if (rb->data)
            util_free(rb->data);
    }
    util_free(g_rigidbodies.pool);
    g_rigidbodies.pool = 0;
}

rigidbody_t * rigidbody_get(int rbi) {
    if (rbi >= 0 && rbi < g_rigidbodies.count)
        return (rigidbody_t*)(g_rigidbodies.pool + RIGIDBODY_SIZE * rbi);
    else
        return 0;
}

int rigidbody_free(rigidbody_t *rb) {
    if (rb->vacant == 1)
        return PHYSRES_INVALID_RB;
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
        return PHYSRES_INTERNAL;
    }
    rb->body = 0;
    rb->wld = 0;
    return PHYSRES_OK;
}

int rigidbody_alloc(rigidbody_t *rb, world_t *wld, colshape_t *cs,
float *matrix, float mass, float frict, float roll_frict) {
    if (!rb->vacant)
        return PHYSRES_INVALID_RB;
    if (!cs->shape)
        return PHYSRES_INVALID_CS;
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
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int rigidbody_fetch_tm(rigidbody_t *rb, float *matrix) {
    try {
        rb->mstate->m.getOpenGLMatrix(matrix);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}
