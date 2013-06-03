#ifndef PHYSICS_WORLD_HPP
#define PHYSICS_WORLD_HPP

#include "ddraw.hpp"
#include "btBulletDynamicsCommon.h"

struct colshape_t;

struct world_t {
    btDbvtBroadphase *broadphase;
    btCollisionDispatcher *dispatcher;
    btSequentialImpulseConstraintSolver *solver;
    btDefaultCollisionConfiguration *colcfg;
    btDiscreteDynamicsWorld *world;
    ddraw_c *ddraw;
};

int world_init(int count);
void world_done(void);
int world_update(world_t*, float dt);
world_t * world_get(int);
int world_ddraw(world_t*);
int world_ddraw_mode(world_t*, int);
int world_move(world_t*, float*);
int world_gravity(world_t*, float*);
int world_cast(world_t*, colshape_t*, float *mfrom, float *mto, float *vout);

#endif /* PHYSICS_WORLD_HPP */

