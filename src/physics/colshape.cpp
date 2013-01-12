#include "colshape.hpp"
#include <stdlib.h>

struct colshapes_t
{
    int count;
    int left;
    colshape_t *pool;
    colshape_t *vacant;
};

static colshapes_t g_colshapes;

int colshape_init(int count)
{
    int i;
    g_colshapes.pool = (colshape_t*)calloc(count, sizeof(colshape_t));
    if (g_colshapes.pool == 0)
        return 1;
    g_colshapes.count = count;
    g_colshapes.left = count;
    g_colshapes.vacant = g_colshapes.pool;
    for (i = 0; i < count; ++i)
    {
        if (i < count - 1)
            g_colshapes.pool[i].next = g_colshapes.pool + i + 1;
        g_colshapes.pool[i].vacant = 1;
    }
    return 0;
}

void colshape_done(void)
{
    int i;
    if (g_colshapes.pool)
    {
        for (i = 0; i < g_colshapes.count; ++i)
            colshape_free(i);
        free(g_colshapes.pool);
        g_colshapes.pool = 0;
    }
}

void colshape_query(int *left)
{
    *left = g_colshapes.left;
}

int colshape_alloc(void)
{
    colshape_t *colshape;
    if (g_colshapes.vacant == 0)
        return -1;
    --g_colshapes.left;
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

void colshape_free(int colshapei)
{
    colshape_t *colshape;
    colshape = colshape_get(colshapei);
    if (colshape == 0 || colshape->vacant == 1)
        return;
    ++g_colshapes.left;
    colshape->vacant = 1;
    if (colshape->shape)
        colshape->shape->~btCollisionShape();
    colshape->shape = 0;
    colshape->shape_box = 0;
    colshape->next = g_colshapes.vacant;
    g_colshapes.vacant = colshape;
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
