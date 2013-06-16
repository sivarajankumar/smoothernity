#include "physres.h"
#include "colshape.hpp"
#include "pmem.hpp"

static const size_t COLSHAPE_SIZE = 128;

struct colshapes_t {
    int count;
    char *pool;
};

static_assert(sizeof(colshape_t) <= COLSHAPE_SIZE, "Invalid colshape_t size");

static colshapes_t g_colshapes;

int colshape_init(int count) {
    size_t size_max, align_max;
    colshape_t *cs;

    #define FIND_SIZES(t) \
        if (sizeof(t) > size_max) size_max = sizeof(t); \
        if (PMEM_ALIGNOF(t) > align_max) align_max = PMEM_ALIGNOF(t);
    size_max = align_max = 0;
    FIND_SIZES(btBoxShape);
    FIND_SIZES(btHeightfieldTerrainShape);
    FIND_SIZES(btCompoundShape);
    FIND_SIZES(btSphereShape);
    #undef FIND_SIZES

    g_colshapes.count = count;
    g_colshapes.pool = (char*)pmem_alloc(PMEM_ALIGNOF(colshape_t),
                                         COLSHAPE_SIZE * count);
    if (!g_colshapes.pool)
        return PHYSRES_CANNOT_INIT;
    for (int i = 0; i < count; ++i ) {
        cs = colshape_get(i);
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
        if (!(colshape_get(i)->data = (char*)pmem_alloc(align_max, size_max)))
            return PHYSRES_CANNOT_INIT;
    return PHYSRES_OK;
}

void colshape_done(void) {
    colshape_t *cs;
    if (!g_colshapes.pool)
        return;
    for (int i = 0; i < g_colshapes.count; ++i) {
        cs = colshape_get(i);
        if (cs->data) {
            colshape_free(cs);
            pmem_free(cs->data);
        }
    }
    pmem_free(g_colshapes.pool);
    g_colshapes.pool = 0;
}

colshape_t * colshape_get(int colshapei) {
    if (colshapei >= 0 && colshapei < g_colshapes.count)
        return (colshape_t*)(g_colshapes.pool + COLSHAPE_SIZE * colshapei);
    else
        return 0;
}

int colshape_free(colshape_t *cs) {
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

int colshape_alloc_box(colshape_t *cs, float *size) {
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

int colshape_alloc_sphere(colshape_t *cs, float r) {
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

int colshape_alloc_hmap(colshape_t *cs, float *hmap,
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

int colshape_alloc_comp(colshape_t *cs) {
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

int colshape_comp_add(colshape_t *prt, float *matrix, colshape_t *chd) {
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
