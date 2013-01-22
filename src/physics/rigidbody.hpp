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
    colshape_t *cs;
    rigidbody_t *cs_prev;
    rigidbody_t *cs_next;
};

int rigidbody_init(int count);
void rigidbody_done(void);
int rigidbody_left(void);
int rigidbody_alloc(int *rbi, btDynamicsWorld*, colshape_t*, float *matrix, 
                    float mass, float frict, float roll_frict);
int rigidbody_free(rigidbody_t*, btDynamicsWorld*);
rigidbody_t * rigidbody_get(int);
void rigidbody_fetch_tm(rigidbody_t*, float*);
