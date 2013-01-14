#include "rigidbody.hpp"
#include "colshape.hpp"
#include <stdlib.h>

struct rigidbodies_t
{
    int left;
    int count;
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
        return 1;
    g_rigidbodies.vacant = g_rigidbodies.pool;
    g_rigidbodies.left = count;
    g_rigidbodies.count = count;
    for (i = 0; i < count; ++i)
    {
        rb = g_rigidbodies.pool + i;
        if (i < count - 1)
            rb->next = g_rigidbodies.pool + i + 1;
        rb->vacant = 1;
        rb->mstate = new (rb->mstate_data) mstate_c();
    }
    return 0;
}

void rigidbody_done(void)
{
    int i;
    if (g_rigidbodies.pool)
    {
        for (i = 0; i < g_rigidbodies.count; ++i)
        {
            rigidbody_free(i, 0);
            g_rigidbodies.pool[i].mstate->~mstate_c();
        }
        free(g_rigidbodies.pool);
        g_rigidbodies.pool = 0;
    }
}

void rigidbody_left(int *left)
{
    *left = g_rigidbodies.left;
}

rigidbody_t * rigidbody_get(int rbi)
{
    if (rbi >= 0 && rbi < g_rigidbodies.count)
        return g_rigidbodies.pool + rbi;
    else
        return 0;
}

void rigidbody_free(int rbi, btDynamicsWorld *world)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0 || rb->vacant == 1)
        return;
    ++g_rigidbodies.left;
    rb->vacant = 1;
    rb->next = g_rigidbodies.vacant;
    g_rigidbodies.vacant = rb;
    if (rb->body && world)
        world->removeCollisionObject(rb->body);
    if (rb->body)
        rb->body->~btRigidBody();
    rb->body = 0;
}

int rigidbody_alloc(btDynamicsWorld *world, colshape_t *cs,
                    float *matrix, float frict, float roll_frict)
{
    rigidbody_t *rb;
    if (g_rigidbodies.vacant == 0)
        return -1;
    --g_rigidbodies.left;
    rb = g_rigidbodies.vacant;
    g_rigidbodies.vacant = g_rigidbodies.vacant->next;
    rb->vacant = 0;
    rb->next = 0;

    rb->mstate->get.setFromOpenGLMatrix(matrix);
    rb->mstate->set = rb->mstate->get;
    rb->mstate->was_set = 1;

    btRigidBody::btRigidBodyConstructionInfo info
            (cs->mass, rb->mstate, cs->shape, cs->inertia);
    info.m_friction = frict;
    info.m_rollingFriction = roll_frict;

    rb->body = new (rb->body_data) btRigidBody(info);
    world->addRigidBody(rb->body);
    return rb - g_rigidbodies.pool;
}
