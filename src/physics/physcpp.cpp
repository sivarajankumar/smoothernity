#include "world.hpp"
#include "colshape.hpp"
#include "rigidbody.hpp"
#include "vehicle.hpp"
#include "physres.h"
#include <exception>

struct physcpp_t
{
    void *(*memalloc)(size_t);
};

static physcpp_t g_physcpp;

static void * physcpp_memalloc(size_t size)
{
    void *res = g_physcpp.memalloc(size);
    if (res == 0)
        throw std::bad_alloc();
    return res;
}

extern "C"
int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int wld_count, int cs_count, int rb_count, int veh_count)
{
    int res;
    g_physcpp.memalloc = memalloc;
    btAlignedAllocSetCustom(physcpp_memalloc, memfree);
    res = world_init(wld_count);
    if (res != PHYSRES_OK)
        return res;
    res = colshape_init(cs_count);
    if (res != PHYSRES_OK)
        return res;
    res = rigidbody_init(rb_count);
    if (res != PHYSRES_OK)
        return res;
    return vehicle_init(veh_count);
}

extern "C"
void physcpp_done(void)
{
    rigidbody_done();
    vehicle_done();
    colshape_done();
    world_done();
}

extern "C"
void physcpp_left(int *cs_left, int *rb_left, int *veh_left)
{
    *cs_left = colshape_left();
    *rb_left = rigidbody_left();
    *veh_left = vehicle_left();
}

extern "C"
int physcpp_wld_update(int wldi, float dt)
{
    world_t *wld;
    wld = world_get(wldi);
    if (wld == 0)
        return PHYSRES_INVALID_WLD;
    return world_update(wld, dt);
}

extern "C"
int physcpp_wld_ddraw(int wldi)
{
    world_t *wld;
    wld = world_get(wldi);
    if (wld == 0)
        return PHYSRES_INVALID_WLD;
    return world_ddraw(wld);
}

extern "C"
int physcpp_wld_ddraw_mode(int wldi, int mode)
{
    world_t *wld;
    wld = world_get(wldi);
    if (wld == 0)
        return PHYSRES_INVALID_WLD;
    return world_ddraw_mode(wld, mode);
}

extern "C"
int physcpp_wld_move(int wldi, float *offset)
{
    world_t *wld;
    wld = world_get(wldi);
    if (wld == 0)
        return PHYSRES_INVALID_WLD;
    return world_move(wld, offset);
}

extern "C"
int physcpp_wld_cast(int wldi, int csi, float *mfrom, float *mto, float *vout)
{
    world_t *wld;
    colshape_t *cs;
    wld = world_get(wldi);
    cs = colshape_get(csi);
    if (wld == 0)
        return PHYSRES_INVALID_WLD;
    if (cs == 0)
        return PHYSRES_INVALID_CS;
    return world_cast(wld, cs, mfrom, mto, vout);
}

extern "C"
int physcpp_cs_alloc_box(int *csi, float *size)
{
    int res;
    res = colshape_alloc(csi);
    if (res != PHYSRES_OK)
        return res;
    return colshape_make_box(colshape_get(*csi), size);
}

extern "C"
int physcpp_cs_alloc_sphere(int *csi, float r)
{
    int res;
    res = colshape_alloc(csi);
    if (res != PHYSRES_OK)
        return res;
    return colshape_make_sphere(colshape_get(*csi), r);
}

extern "C"
int physcpp_cs_alloc_hmap(int *csi, float *hmap, int width, int length,
                          float hmin, float hmax, float *scale)
{
    int res;
    res = colshape_alloc(csi);
    if (res != PHYSRES_OK)
        return res;
    return colshape_make_hmap(colshape_get(*csi), hmap, width,
                              length, hmin, hmax, scale);
}

extern "C"
int physcpp_cs_alloc_comp(int *csi)
{
    int res;
    res = colshape_alloc(csi);
    if (res != PHYSRES_OK)
        return res;
    return colshape_make_comp(colshape_get(*csi));
}

extern "C"
int physcpp_cs_comp_add(int parenti, float *matrix, int childi)
{
    colshape_t *parent, *child;
    parent = colshape_get(parenti);
    child = colshape_get(childi);
    if (parent == 0 || child == 0)
        return PHYSRES_INVALID_CS;
    return colshape_comp_add(parent, matrix, child);
}

extern "C"
int physcpp_cs_free(int csi)
{
    colshape_t *cs;
    cs = colshape_get(csi);
    if (cs == 0)
        return PHYSRES_INVALID_CS;
    return colshape_free(cs);
}

extern "C"
int physcpp_rb_alloc(int *rbi, int wldi, int csi, float *matrix,
                     float mass, float frict, float roll_frict)
{
    world_t *wld;
    colshape_t *cs;
    wld = world_get(wldi);
    cs = colshape_get(csi);
    if (wld == 0)
        return PHYSRES_INVALID_WLD;
    if (cs == 0)
        return PHYSRES_INVALID_CS;
    return rigidbody_alloc(rbi, wld, cs, matrix,
                           mass, frict, roll_frict);
}

extern "C"
int physcpp_rb_free(int rbi)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0)
        return PHYSRES_INVALID_RB;
    return rigidbody_free(rb);
}

extern "C"
int physcpp_rb_fetch_tm(int rbi, float *matrix)
{
    rigidbody_t *rb;
    rb = rigidbody_get(rbi);
    if (rb == 0)
        return PHYSRES_INVALID_RB;
    return rigidbody_fetch_tm(rb, matrix);
}

extern "C"
int physcpp_wld_gravity(int wldi, float *v)
{
    world_t *wld;
    wld = world_get(wldi);
    if (wld == 0)
        return PHYSRES_INVALID_WLD;
    return world_gravity(wld, v);
}

extern "C"
int physcpp_veh_alloc(int *vehi, int wldi, int shapei, int inerti, float *tm,
                      float mass, float ch_frict, float ch_roll_frict,
                      float sus_stif, float sus_comp, float sus_damp,
                      float sus_trav, float sus_force, float slip_frict)
{
    world_t *wld;
    colshape_t *shape, *inert;
    wld = world_get(wldi);
    shape = colshape_get(shapei);
    inert = colshape_get(inerti);
    if (wld == 0)
        return PHYSRES_INVALID_WLD;
    if (shape == 0 || inert == 0)
        return PHYSRES_INVALID_CS;
    return vehicle_alloc(vehi, wld, shape, inert, tm, mass,
                         ch_frict, ch_roll_frict, sus_stif, sus_comp,
                         sus_damp, sus_trav, sus_force, slip_frict);
}

extern "C"
int physcpp_veh_free(int vehi)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_free(veh);
}

extern "C"
int physcpp_veh_add_wheel(int *wheel, int vehi, float *pos, float *dir,
                          float *axl, float sus_rest, float roll,
                          float radius, int front)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_add_wheel(veh, wheel, pos, dir, axl, sus_rest,
                             roll, radius, front);
}

extern "C"
int physcpp_veh_set_wheel(int vehi, int wheel, float engine,
                          float brake, float steer)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_set_wheel(veh, wheel, engine, brake, steer);
}

extern "C"
int physcpp_veh_fetch_chassis_tm(int vehi, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_fetch_chassis_tm(veh, matrix);
}

extern "C"
int physcpp_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_fetch_wheel_tm(veh, wheel, matrix);
}

extern "C"
int physcpp_veh_transform(int vehi, float *matrix)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_transform(veh, matrix);
}

extern "C"
int physcpp_veh_wheel_contact(int vehi, int wheel, int *in_contact)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0)
        return PHYSRES_INVALID_VEH;
    return vehicle_wheel_contact(veh, wheel, in_contact);
}
