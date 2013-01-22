#include "physres.h"
#include "colshape.hpp"
#include <stdlib.h>
#include <stdio.h>

struct colshapes_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    colshape_t *pool;
    colshape_t *vacant;
};

static colshapes_t g_colshapes;

int colshape_init(int count)
{
    int i;
    size_t size;
    struct colshape_t *cs;

    size = sizeof(btBoxShape);
    if (size < sizeof(btHeightfieldTerrainShape))
        size = sizeof(btHeightfieldTerrainShape);
    if (size < sizeof(btCompoundShape))
        size = sizeof(btCompoundShape);

    g_colshapes.pool = (colshape_t*)calloc(count, sizeof(colshape_t));
    if (g_colshapes.pool == 0)
        return PHYSRES_CANNOT_INIT;
    g_colshapes.count = count;
    g_colshapes.left = count;
    g_colshapes.left_min = count;
    g_colshapes.vacant = g_colshapes.pool;
    for (i = 0; i < count; ++i)
    {
        cs = g_colshapes.pool + i;
        if (i < count - 1)
            cs->next = g_colshapes.pool + i + 1;
        cs->vacant = 1;
        cs->data = calloc(size, 1);
        if (cs->data == 0)
            goto cleanup;
    }
    return PHYSRES_OK;
cleanup:
    for (i = 0; i < count; ++i)
    {
        cs = g_colshapes.pool + i;
        if (cs->data)
            free(cs->data);
    }
    free(g_colshapes.pool);
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
        cs = g_colshapes.pool + i;
        colshape_free(cs, 0);
        free(cs->data);
    }
    free(g_colshapes.pool);
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
    *csi = colshape - g_colshapes.pool;
    return PHYSRES_OK;
}

colshape_t * colshape_get(int colshapei)
{
    if (colshapei >= 0 && colshapei < g_colshapes.count)
        return g_colshapes.pool + colshapei;
    else
        return 0;
}

int colshape_free(colshape_t *cs, btDynamicsWorld *world)
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
        cs->comp->shape_comp->removeChildShape(cs->shape);
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
        cs->shape->~btCollisionShape();
    cs->shape = 0;
    cs->shape_box = 0;
    cs->shape_hmap = 0;
    cs->shape_comp = 0;
    cs->next = g_colshapes.vacant;
    g_colshapes.vacant = cs;
    return PHYSRES_OK;
}

void colshape_make_box(colshape_t *colshape, float *size)
{
    colshape->shape_box = new (colshape->data)
        btBoxShape(btVector3(size[0], size[1], size[2]));
    colshape->shape = colshape->shape_box;
}

void colshape_make_hmap(colshape_t *cs, float *hmap, int width, int length,
                        float hmin, float hmax, float *scale)
{
    cs->shape_hmap = new (cs->data)
        btHeightfieldTerrainShape(width, length, hmap, 1,
                                  hmin, hmax, 1, PHY_FLOAT, false);
    cs->shape_hmap->setLocalScaling(btVector3(scale[0], scale[1], scale[2]));
    cs->shape = cs->shape_hmap;
}

void colshape_make_comp(colshape_t *colshape)
{
    colshape->shape_comp = new (colshape->data) btCompoundShape();
    colshape->shape = colshape->shape_comp;
}

int colshape_comp_add(colshape_t *parent, float *matrix, colshape_t *child)
{
    btTransform tm;
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

    tm.setFromOpenGLMatrix(matrix);
    parent->shape_comp->addChildShape(tm, child->shape);

    return PHYSRES_OK;
}
