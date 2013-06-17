#include "physres.h"
#include "ycolshape.hpp"
#include "pmem.hpp"

static const size_t YCOLSHAPE_SIZE = 128;

struct ycolshapes_t {
    int count;
    char *pool;
};

static_assert(sizeof(ycolshape_t) <= YCOLSHAPE_SIZE,
              "Invalid ycolshape_t size");

static ycolshapes_t g_ycolshapes;

int ycolshape_init(int count) {
    size_t size_max, align_max;
    ycolshape_t *cs;

    #define FIND_SIZES(t) \
        if (sizeof(t) > size_max) size_max = sizeof(t); \
        if (PMEM_ALIGNOF(t) > align_max) align_max = PMEM_ALIGNOF(t);
    size_max = align_max = 0;
    FIND_SIZES(btBoxShape);
    FIND_SIZES(btHeightfieldTerrainShape);
    FIND_SIZES(btCompoundShape);
    FIND_SIZES(btSphereShape);
    #undef FIND_SIZES

    g_ycolshapes.count = count;
    g_ycolshapes.pool = (char*)pmem_alloc(PMEM_ALIGNOF(ycolshape_t),
                                          YCOLSHAPE_SIZE * count);
    if (!g_ycolshapes.pool)
        return PHYSRES_CANNOT_INIT;
    for (int i = 0; i < count; ++i ) {
        cs = ycolshape_get(i);
        cs->vacant = 1;
        cs->shape_box = 0;
        cs->shape_sphere = 0;
        cs->shape_hmap = 0;
        cs->shape_comp = 0;
        cs->shape_convex = 0;
        cs->shape = 0;
        cs->data = 0;
        cs->comp = cs->comp_children = cs->comp_next = cs->comp_prev = 0;
        cs->vehs = 0;
        cs->rbs = 0;
    }
    for (int i = 0; i < count; ++i)
        if (!(ycolshape_get(i)->data = (char*)pmem_alloc(align_max, size_max)))
            return PHYSRES_CANNOT_INIT;
    return PHYSRES_OK;
}

void ycolshape_done(void) {
    ycolshape_t *cs;
    if (!g_ycolshapes.pool)
        return;
    for (int i = 0; i < g_ycolshapes.count; ++i) {
        cs = ycolshape_get(i);
        if (cs->data) {
            ycolshape_free(cs);
            pmem_free(cs->data);
        }
    }
    pmem_free(g_ycolshapes.pool);
    g_ycolshapes.pool = 0;
}

ycolshape_t * ycolshape_get(int colshapei) {
    if (colshapei >= 0 && colshapei < g_ycolshapes.count)
        return (ycolshape_t*)(g_ycolshapes.pool + YCOLSHAPE_SIZE * colshapei);
    else
        return 0;
}

int ycolshape_free(ycolshape_t *cs) {
    if (cs->vacant == 1)
        return PHYSRES_INVALID_CS;
    if (cs->comp_children || cs->vehs || cs->rbs)
        return PHYSRES_CS_HAS_REFS;
    cs->vacant = 1;
    if (cs->comp) {
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
    if (cs->shape) {
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

int ycolshape_alloc_box(ycolshape_t *cs, float *size) {
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

int ycolshape_alloc_sphere(ycolshape_t *cs, float r) {
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

int ycolshape_alloc_hmap(ycolshape_t *cs, float *hmap,
int width, int length, float hmin, float hmax, float *scale) {
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

int ycolshape_alloc_comp(ycolshape_t *cs) {
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

int ycolshape_comp_add(ycolshape_t *prt, float *matrix, ycolshape_t *chd) {
    if (!prt->shape_comp || !chd->shape || chd->shape_comp || chd->comp)
        return PHYSRES_INVALID_CS;
    chd->comp = prt;
    chd->comp_next = prt->comp_children;
    if (prt->comp_children)
        prt->comp_children->comp_prev = chd;
    prt->comp_children = chd;

    try {
        btTransform tm;
        tm.setFromOpenGLMatrix(matrix);
        prt->shape_comp->addChildShape(tm, chd->shape);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}
