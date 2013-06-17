#ifndef YRIGIDBODY_HPP
#define YRIGIDBODY_HPP

#include "btBulletDynamicsCommon.h"

class ymstate_c;
struct yworld_t;
struct ycolshape_t;

struct yrigidbody_t {
    btRigidBody *body;
    ymstate_c *mstate;
    char *data;
    int vacant;
    yworld_t *wld;
    ycolshape_t *cs;
    yrigidbody_t *cs_prev, *cs_next;
};

int yrigidbody_init(int count);
void yrigidbody_done(void);
int yrigidbody_alloc(yrigidbody_t *rb, yworld_t*, ycolshape_t*, float *matrix, 
                    float mass, float frict, float roll_frict);
int yrigidbody_free(yrigidbody_t*);
yrigidbody_t * yrigidbody_get(int);
int yrigidbody_fetch_tm(yrigidbody_t*, float*);

#endif /* YRIGIDBODY_HPP */

