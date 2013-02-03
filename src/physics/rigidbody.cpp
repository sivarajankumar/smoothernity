#include "physres.h"
#include "rigidbody.hpp"
#include "world.hpp"
#include "colshape.hpp"
#include <stdlib.h>
#include <stdio.h>

struct rigidbodies_t
{
    int left;
    int left_min;
    int count;
    int allocs;
    int frees;
    rigidbody_t *pool;
    rigidbody_t *vacant;
};

static rigidbodies_t g_rigidbodies;

int rigidbody_init(int count)
{
    int i;
    rigidbody_t *rb;
    g_rigidbodies.pool = (rigidbody_t*)calloc(count, sizeof(rigidbody_t));
    if (g_rigidbodies.pool == 0)
        return PHYSRES_CANNOT_INIT;
    g_rigidbodies.vacant = g_rigidbodies.pool;
    g_rigidbodies.left = count;
    g_rigidbodies.left_min = count;
    g_rigidbodies.count = count;
    for (i = 0; i < count; ++i)
    {
        rb = g_rigidbodies.pool + i;
        if (i < count - 1)
            rb->next = g_rigidbodies.pool + i + 1;
        rb->vacant = 1;
        try {
            rb->mstate = new mstate_c();
            rb->body_data = (char*)calloc(sizeof(btRigidBody) +
                                          alignof(btRigidBody), 1);
            rb->body_align = alignof(btRigidBody) - ((rb->body_data - (char*)0)
                                                     % alignof(btRigidBody));
        } catch (...) {
            goto cleanup;
        }
    }
    return PHYSRES_OK;
cleanup:
    for (i = 0; i < count; ++i)
    {
        rb = g_rigidbodies.pool + i;
        if (rb->mstate)
            delete rb->mstate;
        if (rb->body_data)
            free(rb->body_data);
    }
    free(g_rigidbodies.pool);
    g_rigidbodies.pool = 0;
    return PHYSRES_CANNOT_INIT;
}

void rigidbody_done(void)
{
    int i;
    if (g_rigidbodies.pool == 0)
        return;
    printf("Rigid bodies usage: %i/%i, allocs/frees: %i/%i\n",
           g_rigidbodies.count - g_rigidbodies.left_min, g_rigidbodies.count,
           g_rigidbodies.allocs, g_rigidbodies.frees);
    for (i = 0; i < g_rigidbodies.count; ++i)
    {
        rigidbody_free(g_rigidbodies.pool + i);
        try {
            delete g_rigidbodies.pool[i].mstate;
            free(g_rigidbodies.pool[i].body_data);
        } catch (...) {
            fprintf(stderr, "rigidbody_done: exception\n");
        }
    }
    free(g_rigidbodies.pool);
    g_rigidbodies.pool = 0;
}

int rigidbody_left(void)
{
    return g_rigidbodies.left;
}

rigidbody_t * rigidbody_get(int rbi)
{
    if (rbi >= 0 && rbi < g_rigidbodies.count)
        return g_rigidbodies.pool + rbi;
    else
        return 0;
}

int rigidbody_free(rigidbody_t *rb)
{
    if (rb->vacant == 1)
        return PHYSRES_INVALID_RB;
    ++g_rigidbodies.left;
    ++g_rigidbodies.frees;
    rb->vacant = 1;
    rb->next = g_rigidbodies.vacant;
    g_rigidbodies.vacant = rb;
    if (rb->cs->rbs == rb)
        rb->cs->rbs = rb->cs_next;
    if (rb->cs_next)
        rb->cs_next->cs_prev = rb->cs_prev;
    if (rb->cs_prev)
        rb->cs_prev->cs_next = rb->cs_next;
    rb->cs = 0;
    rb->cs_prev = 0;
    rb->cs_next = 0;
    try
    {
        if (rb->body && rb->wld)
            rb->wld->world->removeCollisionObject(rb->body);
        if (rb->body)
            rb->body->~btRigidBody();
    }
    catch (...)
    {
        rb->body = 0;
        return PHYSRES_INTERNAL;
    }
    rb->body = 0;
    rb->wld = 0;
    return PHYSRES_OK;
}

int rigidbody_alloc(int *rbi, world_t *wld, colshape_t *cs, float *matrix,
                    float mass, float frict, float roll_frict)
{
    rigidbody_t *rb;
    if (g_rigidbodies.vacant == 0)
        return PHYSRES_OUT_OF_RB;
    if (cs->shape == 0)
        return PHYSRES_INVALID_CS;
    ++g_rigidbodies.allocs;
    --g_rigidbodies.left;
    if (g_rigidbodies.left < g_rigidbodies.left_min)
        g_rigidbodies.left_min = g_rigidbodies.left;
    rb = g_rigidbodies.vacant;
    g_rigidbodies.vacant = g_rigidbodies.vacant->next;
    rb->vacant = 0;
    rb->next = 0;

    rb->cs = cs;
    if (cs->rbs)
        cs->rbs->cs_prev = rb;
    rb->cs_next = cs->rbs;
    rb->cs_prev = 0;
    cs->rbs = rb;

    try
    {
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

        rb->body = new (rb->body_data + rb->body_align) btRigidBody(info);

        wld->world->addRigidBody(rb->body);
        rb->wld = wld;
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }

    *rbi = rb - g_rigidbodies.pool;
    return PHYSRES_OK;
}

int rigidbody_fetch_tm(rigidbody_t *rb, float *matrix)
{
    try {
        rb->mstate->m.getOpenGLMatrix(matrix);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}
