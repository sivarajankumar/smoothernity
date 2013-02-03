#pragma once

#include "ddraw.hpp"
#include <btBulletDynamicsCommon.h>

struct colshape_t;

struct world_t
{
    float time_scale;
    btDbvtBroadphase *broadphase;
    btCollisionDispatcher *dispatcher;
    btSequentialImpulseConstraintSolver *solver;
    btDefaultCollisionConfiguration *colcfg;
    btDiscreteDynamicsWorld *world;
    ddraw_c *ddraw;

    int vacant;
    world_t *next;
    world_t *prev;
};

int world_init(int count);
void world_done(void);
int world_left(void);
int world_update(float dt);
int world_alloc(int*);
int world_free(world_t*);
world_t * world_get(int);
int world_ddraw(world_t*);
int world_ddraw_mode(world_t*, int);
int world_move(world_t*, float*);
int world_gravity(world_t*, float*);
int world_cast(world_t*, colshape_t*, float *mfrom, float *mto, float *vout);
