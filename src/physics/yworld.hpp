#ifndef YWORLD_HPP
#define YWORLD_HPP

#include "btBulletDynamicsCommon.h"

class yddraw_c;
struct ycolshape_t;

struct yworld_t {
    btDbvtBroadphase *broadphase;
    btCollisionDispatcher *dispatcher;
    btSequentialImpulseConstraintSolver *solver;
    btDefaultCollisionConfiguration *colcfg;
    btDiscreteDynamicsWorld *world;
    yddraw_c *ddraw;
};

int yworld_init(int count);
void yworld_done(void);
int yworld_update(yworld_t*, float dt);
yworld_t * yworld_get(int);
int yworld_ddraw(yworld_t*);
int yworld_ddraw_mode(yworld_t*, int);
int yworld_move(yworld_t*, float*);
int yworld_gravity(yworld_t*, float*);
int yworld_cast(yworld_t*, ycolshape_t*, float *mfrom, float *mto, float *vout);

#endif /* YWORLD_HPP */

