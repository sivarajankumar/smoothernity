#ifndef YCOLSHAPE_HPP
#define YCOLSHAPE_HPP

#include "btBulletDynamicsCommon.h"
#include "BulletCollision/CollisionShapes/btHeightfieldTerrainShape.h"

struct yrigidbody_t;
struct yvehicle_t;

struct ycolshape_t {
    btBoxShape *shape_box;
    btSphereShape *shape_sphere;
    btHeightfieldTerrainShape *shape_hmap;
    btCompoundShape *shape_comp;
    btConvexShape *shape_convex;
    btCollisionShape *shape;
    char *data;
    ycolshape_t *comp, *comp_children, *comp_next, *comp_prev;
    int vacant;
    yvehicle_t *vehs;
    yrigidbody_t *rbs;
};

int ycolshape_init(int count);
void ycolshape_done(void);
int ycolshape_free(ycolshape_t*);
ycolshape_t * ycolshape_get(int);
int ycolshape_alloc_box(ycolshape_t *col, float *size);
int ycolshape_alloc_sphere(ycolshape_t *col, float r);
int ycolshape_alloc_hmap(ycolshape_t *col, float *hmap, int width, int length,
                         float hmin, float hmax, float *scale);
int ycolshape_alloc_comp(ycolshape_t *col);
int ycolshape_comp_add(ycolshape_t*, float *matrix, ycolshape_t *child);

#endif /* YCOLSHAPE_HPP */

