#pragma once

#include "mstate.hpp"

struct world_t;
struct colshape_t;

struct rigidbody_t
{
    btRigidBody *body;
    mstate_c *mstate;
    char *data;
    rigidbody_t *next;
    int vacant;
    world_t *wld;
    colshape_t *cs;
    rigidbody_t *cs_prev;
    rigidbody_t *cs_next;
};

int rigidbody_init(int count);
void rigidbody_done(void);
int rigidbody_left(void);
int rigidbody_alloc(int *rbi, world_t*, colshape_t*, float *matrix, 
                    float mass, float frict, float roll_frict);
int rigidbody_free(rigidbody_t*);
rigidbody_t * rigidbody_get(int);
int rigidbody_fetch_tm(rigidbody_t*, float*);
