#include "colshape.hpp"
#include "rigidbody.hpp"
#include "vehicle.hpp"
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

    g_colshapes.pool = (colshape_t*)calloc(count, sizeof(colshape_t));
    if (g_colshapes.pool == 0)
        return 1;
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
    return 0;
cleanup:
    for (i = 0; i < count; ++i)
    {
        cs = g_colshapes.pool + i;
        if (cs->data)
            free(cs->data);
    }
    free(g_colshapes.pool);
    return 1;
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

void colshape_left(int *left)
{
    *left = g_colshapes.left;
}

int colshape_alloc(void)
{
    colshape_t *colshape;
    if (g_colshapes.vacant == 0)
        return -1;
    ++g_colshapes.allocs;
    --g_colshapes.left;
    if (g_colshapes.left < g_colshapes.left_min)
        g_colshapes.left_min = g_colshapes.left;
    colshape = g_colshapes.vacant;
    g_colshapes.vacant = g_colshapes.vacant->next;
    colshape->vacant = 0;
    colshape->next = 0;
    return colshape - g_colshapes.pool;
}

colshape_t * colshape_get(int colshapei)
{
    if (colshapei >= 0 && colshapei < g_colshapes.count)
        return g_colshapes.pool + colshapei;
    else
        return 0;
}

void colshape_free(colshape_t *cs, btDynamicsWorld *world)
{
    if (cs == 0 || cs->vacant == 1)
        return;
    ++g_colshapes.left;
    ++g_colshapes.frees;
    cs->vacant = 1;
    if (cs->shape)
        cs->shape->~btCollisionShape();
    cs->shape = 0;
    cs->shape_box = 0;
    cs->next = g_colshapes.vacant;
    g_colshapes.vacant = cs;
    while (cs->vehs)
        vehicle_free(cs->vehs, world);
    while (cs->rbs)
        rigidbody_free(cs->rbs, world);
}

void colshape_make_box(colshape_t *colshape, float mass, float *size)
{
    if (colshape->shape)
        return;
    colshape->shape_box = new (colshape->data)
        btBoxShape(btVector3(size[0], size[1], size[2]));
    colshape->shape = colshape->shape_box;
    colshape->mass = mass;
    if (mass > 0.0f)
        colshape->shape_box->calculateLocalInertia(mass, colshape->inertia);
    else
        colshape->inertia = btVector3(0,0,0);
}

void colshape_make_hmap(colshape_t *cs, float *hmap, int width, int length,
                        float hmin, float hmax, float *scale)
{
    if (cs->shape)
        return;
    cs->shape_hmap = new (cs->data)
        btHeightfieldTerrainShape(width, length, hmap, 1,
                                  hmin, hmax, 1, PHY_FLOAT, false);
    cs->shape_hmap->setLocalScaling(btVector3(scale[0], scale[1], scale[2]));
    cs->shape = cs->shape_hmap;
    cs->mass = 0;
    cs->inertia = btVector3(0,0,0);
}
