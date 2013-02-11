#include "physres.h"
#include "colshape.hpp"
#include "../util/util.hpp"
#include <stdio.h>

static const size_t COLSHAPE_SIZE = 128;

struct colshapes_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    colshape_t *vacant;
};

union colshape_u
{
    btBoxShape box;
    btHeightfieldTerrainShape hf;
    btCompoundShape comp;
    btSphereShape sph;
};

static colshapes_t g_colshapes;

int colshape_init(int count)
{
    int i;
    colshape_t *cs;
    if (sizeof(colshape_t) > COLSHAPE_SIZE)
    {
        fprintf(stderr, "Invalid size:\nsizeof(colshape_t) == %i\n",
                (int)sizeof(colshape_t));
        return PHYSRES_CANNOT_INIT;
    }
    g_colshapes.pool = (char*)util_malloc(COLSHAPE_SIZE, COLSHAPE_SIZE * count);
    if (g_colshapes.pool == 0)
        return PHYSRES_CANNOT_INIT;
    memset(g_colshapes.pool, 0, COLSHAPE_SIZE * count);
    g_colshapes.count = count;
    g_colshapes.left = count;
    g_colshapes.left_min = count;
    g_colshapes.vacant = colshape_get(0);
    for (i = 0; i < count; ++i)
    {
        cs = colshape_get(i);
        cs->next = colshape_get(i + 1);
        cs->vacant = 1;
        cs->data = (char*)util_malloc(alignof(colshape_u), sizeof(colshape_u));
        if (cs->data == 0)
            goto cleanup;
    }
    return PHYSRES_OK;
cleanup:
    for (i = 0; i < count; ++i)
    {
        cs = colshape_get(i);
        if (cs->data)
            util_free(cs->data);
    }
    util_free(g_colshapes.pool);
    return PHYSRES_CANNOT_INIT;
}

void colshape_done(void)
{
    int i;
    colshape_t *cs;
    if (g_colshapes.pool == 0)
        return;
    printf("Collision shapes usage: %i/%i, allocs/frees: %i/%i\n",
           g_colshapes.count - g_colshapes.left_min, g_colshapes.count,
           g_colshapes.allocs, g_colshapes.frees);
    for (i = 0; i < g_colshapes.count; ++i)
    {
        cs = colshape_get(i);
        colshape_free(cs);
        util_free(cs->data);
    }
    util_free(g_colshapes.pool);
    g_colshapes.pool = 0;
}

int colshape_left(void)
{
    return g_colshapes.left;
}

int colshape_alloc(int *csi)
{
    colshape_t *colshape;
    if (g_colshapes.vacant == 0)
        return PHYSRES_OUT_OF_CS;
    ++g_colshapes.allocs;
    --g_colshapes.left;
    if (g_colshapes.left < g_colshapes.left_min)
        g_colshapes.left_min = g_colshapes.left;
    colshape = g_colshapes.vacant;
    g_colshapes.vacant = g_colshapes.vacant->next;
    colshape->vacant = 0;
    colshape->next = 0;
    *csi = ((char*)colshape - g_colshapes.pool) / COLSHAPE_SIZE;
    return PHYSRES_OK;
}

colshape_t * colshape_get(int colshapei)
{
    if (colshapei >= 0 && colshapei < g_colshapes.count)
        return (colshape_t*)(g_colshapes.pool + COLSHAPE_SIZE * colshapei);
    else
        return 0;
}

int colshape_free(colshape_t *cs)
{
    if (cs->vacant == 1)
        return PHYSRES_INVALID_CS;
    if (cs->comp_children || cs->vehs || cs->rbs)
        return PHYSRES_CS_HAS_REFS;
    ++g_colshapes.left;
    ++g_colshapes.frees;
    cs->vacant = 1;
    if (cs->comp)
    {
        try {
            cs->comp->shape_comp->removeChildShape(cs->shape);
        } catch (...) {
            return PHYSRES_INTERNAL;
        }
        if (cs->comp->comp_children == cs)
            cs->comp->comp_children = cs->comp_next;
        if (cs->comp_prev)
            cs->comp_prev->comp_next = cs->comp_next;
        if (cs->comp_next)
            cs->comp_next->comp_prev = cs->comp_prev;
        cs->comp = 0;
        cs->comp_prev = 0;
        cs->comp_next = 0;
    }
    if (cs->shape)
    {
        try {
            cs->shape->~btCollisionShape();
        } catch (...) {
            return PHYSRES_INTERNAL;
        }
    }
    cs->shape = 0;
    cs->shape_convex = 0;
    cs->shape_box = 0;
    cs->shape_hmap = 0;
    cs->shape_comp = 0;
    cs->next = g_colshapes.vacant;
    g_colshapes.vacant = cs;
    return PHYSRES_OK;
}

int colshape_make_box(colshape_t *colshape, float *size)
{
    try {
        colshape->shape_box = new (colshape->data)
            btBoxShape(btVector3(size[0], size[1], size[2]));
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    colshape->shape = colshape->shape_box;
    colshape->shape_convex = colshape->shape_box;
    return PHYSRES_OK;
}

int colshape_make_sphere(colshape_t *colshape, float r)
{
    try {
        colshape->shape_sphere = new (colshape->data) btSphereShape(r);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    colshape->shape = colshape->shape_sphere;
    colshape->shape_convex = colshape->shape_sphere;
    return PHYSRES_OK;
}

int colshape_make_hmap(colshape_t *cs, float *hmap, int width, int length,
                       float hmin, float hmax, float *scale)
{
    try {
        cs->shape_hmap = new (cs->data)
            btHeightfieldTerrainShape(width, length, hmap, 1,
                                      hmin, hmax, 1, PHY_FLOAT, false);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    cs->shape_hmap->setLocalScaling(btVector3(scale[0], scale[1], scale[2]));
    cs->shape = cs->shape_hmap;
    return PHYSRES_OK;
}

int colshape_make_comp(colshape_t *colshape)
{
    try {
        colshape->shape_comp = new (colshape->data) btCompoundShape();
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    colshape->shape = colshape->shape_comp;
    return PHYSRES_OK;
}

int colshape_comp_add(colshape_t *parent, float *matrix, colshape_t *child)
{
    if (parent->shape_comp == 0 || child->shape == 0
     || child->shape_comp != 0 || child->comp != 0)
    {
        return PHYSRES_INVALID_CS;
    }

    child->comp = parent;
    child->comp_next = parent->comp_children;
    if (parent->comp_children)
        parent->comp_children->comp_prev = child;
    parent->comp_children = child;

    try {
        btTransform tm;
        tm.setFromOpenGLMatrix(matrix);
        parent->shape_comp->addChildShape(tm, child->shape);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }

    return PHYSRES_OK;
}
