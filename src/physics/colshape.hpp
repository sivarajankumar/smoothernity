#ifndef PHYSICS_COLSHAPE_HPP
#define PHYSICS_COLSHAPE_HPP

#include "btBulletDynamicsCommon.h"
#include "BulletCollision/CollisionShapes/btHeightfieldTerrainShape.h"

struct rigidbody_t;
struct vehicle_t;

struct colshape_t {
    btBoxShape *shape_box;
    btSphereShape *shape_sphere;
    btHeightfieldTerrainShape *shape_hmap;
    btCompoundShape *shape_comp;
    btConvexShape *shape_convex;
    btCollisionShape *shape;
    char *data;
    colshape_t *comp;
    colshape_t *comp_children;
    colshape_t *comp_next;
    colshape_t *comp_prev;
    int vacant;
    vehicle_t *vehs;
    rigidbody_t *rbs;
};

int colshape_init(int count);
void colshape_done(void);
int colshape_free(colshape_t*);
colshape_t * colshape_get(int);
int colshape_alloc_box(colshape_t *col, float *size);
int colshape_alloc_sphere(colshape_t *col, float r);
int colshape_alloc_hmap(colshape_t *col, float *hmap, int width, int length,
                        float hmin, float hmax, float *scale);
int colshape_alloc_comp(colshape_t *col);
int colshape_comp_add(colshape_t*, float *matrix, colshape_t *child);

#endif /* PHYSICS_COLSHAPE_HPP */

