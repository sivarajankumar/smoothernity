#include "physres.h"
#include "colshape.hpp"
#include "../util/util.hpp"
#include "../platform/memory.h"
#include <stdio.h>

static const size_t COLSHAPE_SIZE = 128;

struct colshapes_t
{
    int count;
    char *pool;
};

static colshapes_t g_colshapes;

int colshape_init(int count)
{
    size_t size_max, align_max;
    int i;
    colshape_t *cs;

    #define FIND_SIZES(t) \
        if (sizeof(t) > size_max) size_max = sizeof(t); \
        if (ALIGNOF(t) > align_max) align_max = ALIGNOF(t);
    size_max = align_max = 0;
    FIND_SIZES(btBoxShape);
    FIND_SIZES(btHeightfieldTerrainShape);
    FIND_SIZES(btCompoundShape);
    FIND_SIZES(btSphereShape);

    if (sizeof(colshape_t) > COLSHAPE_SIZE)
    {
        fprintf(stderr, "Invalid size:\nsizeof(colshape_t) == %i\n",
                (int)sizeof(colshape_t));
        return PHYSRES_CANNOT_INIT;
    }
    g_colshapes.pool = (char*)util_malloc(COLSHAPE_SIZE, COLSHAPE_SIZE * count);
    if (!g_colshapes.pool)
        return PHYSRES_CANNOT_INIT;
    memset(g_colshapes.pool, 0, COLSHAPE_SIZE * count);
    g_colshapes.count = count;
    for (i = 0; i < count; ++i)
    {
        cs = colshape_get(i);
        cs->vacant = 1;
        cs->data = (char*)util_malloc(align_max, size_max);
        if (!cs->data)
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
    if (!g_colshapes.pool)
        return;
    for (i = 0; i < g_colshapes.count; ++i)
    {
        cs = colshape_get(i);
        colshape_free(cs);
        util_free(cs->data);
    }
    util_free(g_colshapes.pool);
    g_colshapes.pool = 0;
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
    return PHYSRES_OK;
}

int colshape_alloc_box(colshape_t *cs, float *size)
{
    if (!cs->vacant)
        return PHYSRES_INVALID_CS;
    cs->vacant = 0;
    try {
        cs->shape_box = new (cs->data)
            btBoxShape(btVector3(size[0], size[1], size[2]));
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    cs->shape = cs->shape_box;
    cs->shape_convex = cs->shape_box;
    return PHYSRES_OK;
}

int colshape_alloc_sphere(colshape_t *cs, float r)
{
    if (!cs->vacant)
        return PHYSRES_INVALID_CS;
    cs->vacant = 0;
    try {
        cs->shape_sphere = new (cs->data) btSphereShape(r);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    cs->shape = cs->shape_sphere;
    cs->shape_convex = cs->shape_sphere;
    return PHYSRES_OK;
}

int colshape_alloc_hmap(colshape_t *cs, float *hmap, int width, int length,
                       float hmin, float hmax, float *scale)
{
    if (!cs->vacant)
        return PHYSRES_INVALID_CS;
    cs->vacant = 0;
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

int colshape_alloc_comp(colshape_t *cs)
{
    if (!cs->vacant)
        return PHYSRES_INVALID_CS;
    cs->vacant = 0;
    try {
        cs->shape_comp = new (cs->data) btCompoundShape();
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    cs->shape = cs->shape_comp;
    return PHYSRES_OK;
}

int colshape_comp_add(colshape_t *parent, float *matrix, colshape_t *child)
{
    if (!parent->shape_comp || !child->shape
    || child->shape_comp || child->comp)
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
