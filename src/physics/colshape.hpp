#pragma once

#include <btBulletDynamicsCommon.h>
#include <BulletCollision/CollisionShapes/btHeightfieldTerrainShape.h>

struct colshape_t
{
    btBoxShape *shape_box;
    btHeightfieldTerrainShape *shape_hmap;
    btCollisionShape *shape;
    btVector3 inertia;
    float mass;
    void *data;
    colshape_t *next;
    int vacant;
};

int colshape_init(int count);
void colshape_done(void);
void colshape_left(int *left);
int colshape_alloc(void);
void colshape_free(int);
colshape_t * colshape_get(int);
void colshape_make_box(colshape_t *col, float mass, float *size);
void colshape_make_hmap(colshape_t *col, float *hmap, int width, int length,
                        float hmin, float hmax, float *scale);
