#pragma once

#include "mstate.hpp"

struct colshape_t;

struct rigidbody_t
{
    btRigidBody *body;
    mstate_c *mstate;
    char body_data[sizeof(btRigidBody)];
    char mstate_data[sizeof(mstate_c)];
    rigidbody_t *next;
    int vacant;
};

int rigidbody_init(int count);
void rigidbody_done(void);
void rigidbody_left(int *left);
int rigidbody_alloc(void);
void rigidbody_free(int);
rigidbody_t * rigidbody_get(int);
void rigidbody_make(rigidbody_t*, colshape_t*);
