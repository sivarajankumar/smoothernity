#include "cphysics.h"
#include "vector.h"
#include "cmatrix.h"
#include "cmpool.h"
#include "cbuf.h"
#include "util.h"
#include "vlog.h"
#include "../physics/physcpp.h"
#include "../physics/physdbg.h"
#include "../physics/physres.h"

struct cphysics_t {
    struct cmpool_t *mpool;
};

static struct cphysics_t g_cphysics;

static const char * cphysics_error(int res) {
    switch (res) {
        case PHYSRES_OUT_OF_RB:
            return "out of rigid bodies";
        case PHYSRES_OUT_OF_CS:
            return "out of collision shapes";
        case PHYSRES_OUT_OF_VEH:
            return "out of vehicles";
        case PHYSRES_OUT_OF_WLD:
            return "out of worlds";
        case PHYSRES_INVALID_RB:
            return "invalid rigid body";
        case PHYSRES_INVALID_CS:
            return "invalid collision shape";
        case PHYSRES_INVALID_VEH:
            return "invalid vehicle";
        case PHYSRES_INVALID_VEH_WHEEL:
            return "invalid vehicle wheel";
        case PHYSRES_INVALID_WLD:
            return "invalid world";
        case PHYSRES_CS_HAS_REFS:
            return "collision shape has references";
        case PHYSRES_WLD_HAS_REFS:
            return "world has references";
        case PHYSRES_INTERNAL:
            return "internal error";
        default:
            return "unknown";
    }
}

static void * cphysics_malloc(size_t size) {
    return cmpool_alloc(g_cphysics.mpool, size);
}

static int api_physics_wld_update(lua_State *lua) {
    float dt;
    int wldi, res;
    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isfloat(lua, 2)) {
        lua_pushstring(lua, "api_physics_wld_update: incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    dt = (float)lua_tonumber(lua, 2);
    lua_pop(lua, 2);
    if (dt < 0.0f) {
        lua_pushstring(lua, "api_physics_wld_update: negative dt");
        lua_error(lua);
        return 0;
    }
    if ((res = physcpp_wld_update(wldi, dt)) != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_wld_update: physics error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_ddraw(lua_State *lua) {
    int wldi, res;
    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_physics_wld_ddraw: incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    lua_pop(lua, 1);
    if ((res = physcpp_wld_ddraw(wldi)) != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_wld_ddraw: draw error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_gravity(lua_State *lua) {
    int res, wldi;
    struct vector_t *v;
    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_physics_wld_gravity: incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    v = vector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (!v) {
        lua_pushstring(lua, "api_physics_wld_gravity: invalid vector");
        lua_error(lua);
        return 0;
    }
    if ((res = physcpp_wld_gravity(wldi, v->value)) != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_wld_gravity: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_move(lua_State *lua) {
    int res, wldi;
    struct vector_t *v;
    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_physics_wld_move: incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    v = vector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (!v) {
        lua_pushstring(lua, "api_physics_wld_move: invalid vector");
        lua_error(lua);
        return 0;
    }
    if ((res = physcpp_wld_move(wldi, v->value)) != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_wld_move: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_ddraw_mode(lua_State *lua) {
    int res;
    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_physics_wld_ddraw_mode: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_wld_ddraw_mode(lua_tointeger(lua, 1), lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_wld_ddraw_mode: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_box(lua_State *lua) {
    struct vector_t *size;
    int csi, res;

    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_physics_cs_alloc_box: incorrect argument");
        lua_error(lua);
        return 0;
    }
    csi = lua_tointeger(lua, 1);
    size = vector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (!size) {
        lua_pushstring(lua, "api_physics_cs_alloc_box: invalid vector");
        lua_error(lua);
        return 0;
    }
    if ((res = physcpp_cs_alloc_box(csi, size->value)) != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_cs_alloc_box: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_sphere(lua_State *lua) {
    float r;
    int csi, res;

    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isfloat(lua, 2)) {
        lua_pushstring(lua, "api_physics_cs_alloc_sphere: incorrect argument");
        lua_error(lua);
        return 0;
    }
    csi = lua_tointeger(lua, 1);
    r = (float)lua_tonumber(lua, 2);
    lua_pop(lua, 2);

    if (r <= 0) {
        lua_pushstring(lua, "api_physics_cs_alloc_sphere: radius <= 0");
        lua_error(lua);
        return 0;
    }
    if ((res = physcpp_cs_alloc_sphere(csi, r)) != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_cs_alloc_sphere: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_hmap(lua_State *lua) {
    struct vector_t *scale;
    int start, width, length, csi, res;
    float hmin, hmax;

    if (lua_gettop(lua) != 7 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isfloat(lua, 5) ||
    !util_isfloat(lua, 6) || !util_isint(lua, 7)) {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: incorrect argument");
        lua_error(lua);
        return 0;
    }
    csi = lua_tointeger(lua, 1);
    start = lua_tointeger(lua, 2);
    width = lua_tointeger(lua, 3);
    length = lua_tointeger(lua, 4);
    hmin = (float)lua_tonumber(lua, 5);
    hmax = (float)lua_tonumber(lua, 6);
    scale = vector_get(lua_tointeger(lua, 7));
    lua_pop(lua, 7);

    if (!scale) {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: invalid vector");
        lua_error(lua);
        return 0;
    }
    if (start < 0 || start >= g_cbufs.size - (width * length)) {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: start out of range");
        lua_error(lua);
        return 0;
    }
    if (width <= 0 || length <= 0) {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: dims out of range");
        lua_error(lua);
        return 0;
    }
    if (hmin >= hmax) {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: hmin >= hmax");
        lua_error(lua);
        return 0;
    }
    res = physcpp_cs_alloc_hmap(csi, g_cbufs.data + start, width,
                                length, hmin, hmax, scale->value);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_comp(lua_State *lua) {
    int res;

    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_physics_cs_alloc_comp: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_cs_alloc_comp(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_cs_alloc_comp: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_comp_add(lua_State *lua) {
    int parenti, childi, res;
    struct cmatrix_t *m;

    if (lua_gettop(lua) != 3 || !util_isint(lua, 1) ||
    !util_isint(lua, 2) || !util_isint(lua, 3)) {
        lua_pushstring(lua, "api_physics_cs_comp_add: incorrect argument");
        lua_error(lua);
        return 0;
    }
    parenti = lua_tointeger(lua, 1);
    m = cmatrix_get(lua_tointeger(lua, 2));
    childi = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (!m) {
        lua_pushstring(lua, "api_physics_cs_comp_add: invalid matrix");
        lua_error(lua);
        return 0;
    }
    if ((res = physcpp_cs_comp_add(parenti, m->value, childi)) != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_cs_comp_add: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_free(lua_State *lua) {
    int res;
    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_physics_cs_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_cs_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_cs_free: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_rb_alloc(lua_State *lua) {
    struct cmatrix_t *matrix;
    int rbi, wldi, csi, res;
    float mass, fr, roll_fr;

    if (lua_gettop(lua) != 7 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isfloat(lua, 5) ||
    !util_isfloat(lua, 6) || !util_isfloat(lua, 7)) {
        lua_pushstring(lua, "api_physics_rb_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbi = lua_tointeger(lua, 1);
    wldi = lua_tointeger(lua, 2);
    csi = lua_tointeger(lua, 3);
    matrix = cmatrix_get(lua_tointeger(lua, 4));
    mass = (float)lua_tonumber(lua, 5);
    fr = (float)lua_tonumber(lua, 6);
    roll_fr = (float)lua_tonumber(lua, 7);
    lua_pop(lua, 7);

    if (!matrix) {
        lua_pushstring(lua, "api_physics_rb_alloc: invalid matrix");
        lua_error(lua);
        return 0;
    }
    if (mass < 0.0f) {
        lua_pushstring(lua, "api_physics_rb_alloc: negative mass");
        lua_error(lua);
        return 0;
    }
    if (fr < 0.0f || roll_fr < 0.0f) {
        lua_pushstring(lua, "api_physics_rb_alloc: negative friction");
        lua_error(lua);
        return 0;
    }
    res = physcpp_rb_alloc(rbi, wldi, csi, matrix->value, mass, fr, roll_fr);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_rb_alloc: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_rb_free(lua_State *lua) {
    int res;
    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_physics_rb_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_rb_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_rb_free: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_alloc(lua_State *lua) {
    struct cmatrix_t *matrix;
    int wldi, shapei, inerti, vehi, res;
    float mass, ch_frict, ch_roll_frict, sus_stif, sus_comp;
    float sus_damp, sus_trav, sus_force, slip_frict;

    if (lua_gettop(lua) != 14 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isint(lua, 5) ||
    !util_isfloat(lua, 6) || !util_isfloat(lua, 7) || !util_isfloat(lua, 8) ||
    !util_isfloat(lua, 9) || !util_isfloat(lua, 10) || !util_isfloat(lua, 11) ||
    !util_isfloat(lua, 12) || !util_isfloat(lua, 13) || !util_isfloat(lua, 14)){
        lua_pushstring(lua, "api_physics_veh_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vehi = lua_tointeger(lua, 1);
    wldi = lua_tointeger(lua, 2);
    shapei = lua_tointeger(lua, 3);
    inerti = lua_tointeger(lua, 4);
    matrix = cmatrix_get(lua_tointeger(lua, 5));
    mass = (float)lua_tonumber(lua, 6);
    ch_frict = (float)lua_tonumber(lua, 7);
    ch_roll_frict = (float)lua_tonumber(lua, 8);
    sus_stif = (float)lua_tonumber(lua, 9);
    sus_comp = (float)lua_tonumber(lua, 10);
    sus_damp = (float)lua_tonumber(lua, 11);
    sus_trav = (float)lua_tonumber(lua, 12);
    sus_force = (float)lua_tonumber(lua, 13);
    slip_frict = (float)lua_tonumber(lua, 14);
    lua_pop(lua, 14);

    if (!matrix) {
        lua_pushstring(lua, "api_physics_veh_alloc: invalid matrix");
        lua_error(lua);
        return 0;
    }
    if (mass < 0.0f) {
        lua_pushstring(lua, "api_physics_veh_alloc: negative mass");
        lua_error(lua);
        return 0;
    }
    if (ch_frict < 0.0f || ch_roll_frict < 0.0f || slip_frict < 0.0f) {
        lua_pushstring(lua, "api_physics_veh_alloc: negative friction");
        lua_error(lua);
        return 0;
    }
    res = physcpp_veh_alloc(vehi, wldi, shapei, inerti, matrix->value, mass,
                            ch_frict, ch_roll_frict, sus_stif, sus_comp,
                            sus_damp, sus_trav, sus_force, slip_frict);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_veh_alloc: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_free(lua_State *lua) {
    int res;
    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_physics_veh_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_veh_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_veh_free: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_add_wheel(lua_State *lua) {
    struct vector_t *pos, *dir, *axl;
    float sus_rest, roll, radius;
    int vehi, front, wheel, res;
    if (lua_gettop(lua) != 8 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isfloat(lua, 5) ||
    !util_isfloat(lua, 6) || !util_isfloat(lua, 7) || !util_isint(lua, 8)) {
        lua_pushstring(lua, "api_physics_veh_add_wheel: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vehi = lua_tointeger(lua, 1);
    pos = vector_get(lua_tointeger(lua, 2));
    dir = vector_get(lua_tointeger(lua, 3));
    axl = vector_get(lua_tointeger(lua, 4));
    sus_rest = (float)lua_tonumber(lua, 5);
    roll = (float)lua_tonumber(lua, 6);
    radius = (float)lua_tonumber(lua, 7);
    front = !!lua_tointeger(lua, 8);
    lua_pop(lua, 8);

    if (!pos || !dir || !axl) {
        lua_pushstring(lua, "api_physics_veh_add_wheel: invalid vector");
        lua_error(lua);
        return 0;
    }
    if (radius <= 0.0f) {
        lua_pushstring(lua, "api_physics_veh_add_wheel: radius not positive");
        lua_error(lua);
        return 0;
    }
    res = physcpp_veh_add_wheel(&wheel, vehi, pos->value, dir->value,
                                axl->value, sus_rest, roll, radius,
                                front);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_veh_add_wheel: error");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, wheel);
    return 1;
}

static int api_physics_veh_set_wheel(lua_State *lua) {
    int vehi, wheel, res;
    float engine, brake, steer;
    if (lua_gettop(lua) != 5 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isfloat(lua, 3) || !util_isfloat(lua, 4) || !util_isfloat(lua, 5)) {
        lua_pushstring(lua, "api_physics_veh_set_wheel: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vehi = lua_tointeger(lua, 1);
    wheel = lua_tointeger(lua, 2);
    engine = (float)lua_tonumber(lua, 3);
    brake = (float)lua_tonumber(lua, 4);
    steer = (float)lua_tonumber(lua, 5);
    lua_pop(lua, 5);

    res = physcpp_veh_set_wheel(vehi, wheel, engine, brake, steer);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_veh_set_wheel: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_transform(lua_State *lua) {
    int vehi, res;
    struct cmatrix_t *matrix;
    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_physics_veh_transform: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vehi = lua_tointeger(lua, 1);
    matrix = cmatrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (!matrix) {
        lua_pushstring(lua, "api_physics_veh_transform: invalid matrix");
        lua_error(lua);
        return 0;
    }
    if ((res = physcpp_veh_transform(vehi, matrix->value)) != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_veh_transform: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_wheel_contact(lua_State *lua)
{
    int in_contact, res;
    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_physics_veh_wheel_contact: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_veh_wheel_contact(lua_tointeger(lua, 1),
                                    lua_tointeger(lua, 2), &in_contact);
    lua_pop(lua, 2);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        lua_pushstring(lua, "api_physics_veh_wheel_contact: error");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, in_contact);
    return 1;
}

int cphysics_init(lua_State *lua, int wld_count, int cs_count, int rb_count,
int veh_count, const int msizes[], const int mcounts[], int mlen) {
    g_cphysics.mpool = cmpool_create(msizes, mcounts, mlen);
    if (!g_cphysics.mpool)
        return 1;
    if (physcpp_init(cphysics_malloc, cmpool_free, wld_count,
    cs_count, rb_count, veh_count) != PHYSRES_OK)
        return 1;
    #define REGF(x) lua_register(lua, #x, x)
    REGF(api_physics_wld_ddraw);
    REGF(api_physics_wld_ddraw_mode);
    REGF(api_physics_wld_gravity);
    REGF(api_physics_wld_move);
    REGF(api_physics_wld_update);
    REGF(api_physics_cs_alloc_box);
    REGF(api_physics_cs_alloc_sphere);
    REGF(api_physics_cs_alloc_hmap);
    REGF(api_physics_cs_alloc_comp);
    REGF(api_physics_cs_comp_add);
    REGF(api_physics_cs_free);
    REGF(api_physics_rb_alloc);
    REGF(api_physics_rb_free);
    REGF(api_physics_veh_alloc);
    REGF(api_physics_veh_free);
    REGF(api_physics_veh_add_wheel);
    REGF(api_physics_veh_set_wheel);
    REGF(api_physics_veh_transform);
    REGF(api_physics_veh_wheel_contact);
    #undef REGF
    #define REGN(x) lua_pushinteger(lua, PHYSDBG_##x); \
                    lua_setglobal(lua, "API_PHYSICS_"#x);
    PHYSDBG(REGN)
    #undef REGN
    return 0;
}

void cphysics_done(void) {
    physcpp_done();
    if (g_cphysics.mpool) {
        VLOG_INFO("");
        VLOG_INFO("Physics");
        cmpool_report(g_cphysics.mpool);
        cmpool_destroy(g_cphysics.mpool);
    }
}

int cphysics_wld_cast(int wldi, int csi, float *mfrom, float *mto, float *vout) {
    int res = physcpp_wld_cast(wldi, csi, mfrom, mto, vout);
    if (res != PHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        return 1;
    }
    return 0;
}

int cphysics_rb_fetch_tm(int rbi, float *matrix) {
    return physcpp_rb_fetch_tm(rbi, matrix);
}

int cphysics_veh_fetch_chassis_tm(int vehi, float *matrix) {
    return physcpp_veh_fetch_chassis_tm(vehi, matrix);
}

int cphysics_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix) {
    return physcpp_veh_fetch_wheel_tm(vehi, wheel, matrix);
}

