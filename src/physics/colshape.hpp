#pragma once

#include <btBulletDynamicsCommon.h>
#include <BulletCollision/CollisionShapes/btHeightfieldTerrainShape.h>

struct rigidbody_t;
struct vehicle_t;

struct colshape_t
{
    btBoxShape *shape_box;
    btHeightfieldTerrainShape *shape_hmap;
    btCompoundShape *shape_comp;
    btCollisionShape *shape;
    void *data;
    colshape_t *comp;
    colshape_t *comp_children;
    colshape_t *comp_next;
    colshape_t *comp_prev;
    colshape_t *next;
    int vacant;
    vehicle_t *vehs;
    rigidbody_t *rbs;
};

int colshape_init(int count);
void colshape_done(void);
int colshape_left(void);
int colshape_alloc(int*);
int colshape_free(colshape_t*, btDynamicsWorld*);
colshape_t * colshape_get(int);
void colshape_make_box(colshape_t *col, float *size);
void colshape_make_hmap(colshape_t *col, float *hmap, int width, int length,
                        float hmin, float hmax, float *scale);
void colshape_make_comp(colshape_t *col);
int colshape_comp_add(colshape_t*, float *matrix, colshape_t *child);
