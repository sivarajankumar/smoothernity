#pragma once

#include <btBulletDynamicsCommon.h>

#define COLSHAPE_SIZE sizeof(btBoxShape)

struct colshape_t
{
    btBoxShape *shape_box;
    btCollisionShape *shape;
    btVector3 inertia;
    float mass;
    char data[COLSHAPE_SIZE];
    colshape_t *next;
    int vacant;
};

int colshape_init(int count);
void colshape_done(void);
void colshape_query(int *left);
int colshape_alloc(void);
void colshape_free(int);
colshape_t * colshape_get(int);
void colshape_make_box(colshape_t *col, float mass, float *size);
