#ifndef PHYSICS_RIGIDBODY_HPP
#define PHYSICS_RIGIDBODY_HPP

#include "mstate.hpp"

struct world_t;
struct ycolshape_t;

struct rigidbody_t {
    btRigidBody *body;
    mstate_c *mstate;
    char *data;
    int vacant;
    world_t *wld;
    ycolshape_t *cs;
    rigidbody_t *cs_prev, *cs_next;
};

int rigidbody_init(int count);
void rigidbody_done(void);
int rigidbody_alloc(rigidbody_t *rb, world_t*, ycolshape_t*, float *matrix, 
                    float mass, float frict, float roll_frict);
int rigidbody_free(rigidbody_t*);
rigidbody_t * rigidbody_get(int);
int rigidbody_fetch_tm(rigidbody_t*, float*);

#endif /* PHYSICS_RIGIDBODY_HPP */

