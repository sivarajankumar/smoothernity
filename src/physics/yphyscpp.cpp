#include "world.hpp"
#include "ycolshape.hpp"
#include "yrigidbody.hpp"
#include "yvehicle.hpp"
#include "yphysres.h"
#include <exception>

static_assert(sizeof(float) == sizeof(btScalar),
              "float<->btScalar is not supported");

struct yphyscpp_t {
    void *(*memalloc)(size_t);
};

static yphyscpp_t g_yphyscpp;

static void * yphyscpp_memalloc(size_t size) {
    void *res = g_yphyscpp.memalloc(size);
    if (!res)
        throw std::bad_alloc();
    return res;
}

extern "C" int yphyscpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
int wld_count, int cs_count, int rb_count, int veh_count) {
    int res;
    g_yphyscpp.memalloc = memalloc;
    btAlignedAllocSetCustom(yphyscpp_memalloc, memfree);
    if ((res = world_init(wld_count)) != YPHYSRES_OK)
        return res;
    if ((res = ycolshape_init(cs_count)) != YPHYSRES_OK)
        return res;
    if ((res = yrigidbody_init(rb_count)) != YPHYSRES_OK)
        return res;
    return yvehicle_init(veh_count);
}

extern "C" void yphyscpp_done(void) {
    yrigidbody_done();
    yvehicle_done();
    ycolshape_done();
    world_done();
}

extern "C" int yphyscpp_wld_update(int wldi, float dt) {
    world_t *wld;
    if (!(wld = world_get(wldi)))
        return YPHYSRES_INVALID_WLD;
    return world_update(wld, dt);
}

extern "C" int yphyscpp_wld_ddraw(int wldi) {
    world_t *wld;
    if (!(wld = world_get(wldi)))
        return YPHYSRES_INVALID_WLD;
    return world_ddraw(wld);
}

extern "C" int yphyscpp_wld_ddraw_mode(int wldi, int mode) {
    world_t *wld;
    if (!(wld = world_get(wldi)))
        return YPHYSRES_INVALID_WLD;
    return world_ddraw_mode(wld, mode);
}

extern "C" int yphyscpp_wld_move(int wldi, float *offset) {
    world_t *wld;
    if (!(wld = world_get(wldi)))
        return YPHYSRES_INVALID_WLD;
    return world_move(wld, offset);
}

extern "C" int yphyscpp_wld_cast
(int wldi, int csi, float *mfrom, float *mto, float *vout) {
    world_t *wld;
    ycolshape_t *cs;
    if (!(wld = world_get(wldi)))
        return YPHYSRES_INVALID_WLD;
    if (!(cs = ycolshape_get(csi)))
        return YPHYSRES_INVALID_CS;
    return world_cast(wld, cs, mfrom, mto, vout);
}

extern "C" int yphyscpp_cs_alloc_box(int csi, float *size) {
    ycolshape_t *cs;
    if (!(cs = ycolshape_get(csi)))
        return YPHYSRES_INVALID_CS;
    return ycolshape_alloc_box(cs, size);
}

extern "C" int yphyscpp_cs_alloc_sphere(int csi, float r) {
    ycolshape_t *cs;
    if (!(cs = ycolshape_get(csi)))
        return YPHYSRES_INVALID_CS;
    return ycolshape_alloc_sphere(cs, r);
}

extern "C" int yphyscpp_cs_alloc_hmap(int csi, float *hmap,
int width, int length, float hmin, float hmax, float *scale) {
    ycolshape_t *cs;
    if (!(cs = ycolshape_get(csi)))
        return YPHYSRES_INVALID_CS;
    return ycolshape_alloc_hmap(cs, hmap, width, length, hmin, hmax, scale);
}

extern "C" int yphyscpp_cs_alloc_comp(int csi) {
    ycolshape_t *cs;
    if (!(cs = ycolshape_get(csi)))
        return YPHYSRES_INVALID_CS;
    return ycolshape_alloc_comp(cs);
}

extern "C" int yphyscpp_cs_comp_add(int parenti, float *matrix, int childi) {
    ycolshape_t *parent, *child;
    if (!(parent = ycolshape_get(parenti)) || !(child = ycolshape_get(childi)))
        return YPHYSRES_INVALID_CS;
    return ycolshape_comp_add(parent, matrix, child);
}

extern "C" int yphyscpp_cs_free(int csi) {
    ycolshape_t *cs;
    if (!(cs = ycolshape_get(csi)))
        return YPHYSRES_INVALID_CS;
    return ycolshape_free(cs);
}

extern "C" int yphyscpp_rb_alloc(int rbi, int wldi, int csi,
float *matrix, float mass, float frict, float roll_frict) {
    world_t *wld;
    ycolshape_t *cs;
    yrigidbody_t *rb;
    if (!(wld = world_get(wldi)))
        return YPHYSRES_INVALID_WLD;
    if (!(cs = ycolshape_get(csi)))
        return YPHYSRES_INVALID_CS;
    if (!(rb = yrigidbody_get(rbi)))
        return YPHYSRES_INVALID_RB;
    return yrigidbody_alloc(rb, wld, cs, matrix,
                           mass, frict, roll_frict);
}

extern "C" int yphyscpp_rb_free(int rbi) {
    yrigidbody_t *rb;
    if (!(rb = yrigidbody_get(rbi)))
        return YPHYSRES_INVALID_RB;
    return yrigidbody_free(rb);
}

extern "C" int yphyscpp_rb_fetch_tm(int rbi, float *matrix) {
    yrigidbody_t *rb;
    if (!(rb = yrigidbody_get(rbi)))
        return YPHYSRES_INVALID_RB;
    return yrigidbody_fetch_tm(rb, matrix);
}

extern "C" int yphyscpp_wld_gravity(int wldi, float *v) {
    world_t *wld;
    if (!(wld = world_get(wldi)))
        return YPHYSRES_INVALID_WLD;
    return world_gravity(wld, v);
}

extern "C" int yphyscpp_veh_alloc(int vehi, int wldi, int shapei,
int inerti, float *tm, float mass, float ch_frict, float ch_roll_frict,
float sus_stif, float sus_comp, float sus_damp, float sus_trav,
float sus_force, float slip_frict) {
    world_t *wld;
    ycolshape_t *shape, *inert;
    yvehicle_t *veh;
    if (!(wld = world_get(wldi)))
        return YPHYSRES_INVALID_WLD;
    if (!(shape = ycolshape_get(shapei)) || !(inert = ycolshape_get(inerti)))
        return YPHYSRES_INVALID_CS;
    if (!(veh = yvehicle_get(vehi)))
        return YPHYSRES_INVALID_VEH;
    return yvehicle_alloc(veh, wld, shape, inert, tm, mass,
                         ch_frict, ch_roll_frict, sus_stif, sus_comp,
                         sus_damp, sus_trav, sus_force, slip_frict);
}

extern "C" int yphyscpp_veh_free(int vehi) {
    yvehicle_t *veh;
    if (!(veh = yvehicle_get(vehi)))
        return YPHYSRES_INVALID_VEH;
    return yvehicle_free(veh);
}

extern "C" int yphyscpp_veh_add_wheel(int *wheel, int vehi, float *pos,
float *dir, float *axl, float sus_rest, float roll, float radius, int front) {
    yvehicle_t *veh;
    if (!(veh = yvehicle_get(vehi)))
        return YPHYSRES_INVALID_VEH;
    return yvehicle_add_wheel(veh, wheel, pos, dir, axl, sus_rest,
                             roll, radius, front);
}

extern "C" int yphyscpp_veh_set_wheel
(int vehi, int wheel, float engine, float brake, float steer) {
    yvehicle_t *veh;
    if (!(veh = yvehicle_get(vehi)))
        return YPHYSRES_INVALID_VEH;
    return yvehicle_set_wheel(veh, wheel, engine, brake, steer);
}

extern "C" int yphyscpp_veh_fetch_chassis_tm(int vehi, float *matrix) {
    yvehicle_t *veh;
    if (!(veh = yvehicle_get(vehi)))
        return YPHYSRES_INVALID_VEH;
    return yvehicle_fetch_chassis_tm(veh, matrix);
}

extern "C" int yphyscpp_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix) {
    yvehicle_t *veh;
    if (!(veh = yvehicle_get(vehi)))
        return YPHYSRES_INVALID_VEH;
    return yvehicle_fetch_wheel_tm(veh, wheel, matrix);
}

extern "C" int yphyscpp_veh_transform(int vehi, float *matrix) {
    yvehicle_t *veh;
    if (!(veh = yvehicle_get(vehi)))
        return YPHYSRES_INVALID_VEH;
    return yvehicle_transform(veh, matrix);
}

extern "C" int yphyscpp_veh_wheel_contact(int vehi, int wheel, int *in_contact) {
    yvehicle_t *veh;
    if (!(veh = yvehicle_get(vehi)))
        return YPHYSRES_INVALID_VEH;
    return yvehicle_wheel_contact(veh, wheel, in_contact);
}
