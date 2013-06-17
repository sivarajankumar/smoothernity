#include "cphysics.h"
#include "cvector.h"
#include "cmatrix.h"
#include "cmpool.h"
#include "cbuf.h"
#include "cutil.h"
#include "vlog.h"
#include "yphyscpp.h"
#include "yphysdbg.h"
#include "yphysres.h"

struct cphysics_t {
    struct cmpool_t *mpool;
};

static struct cphysics_t g_cphysics;

static const char * cphysics_error(int res) {
    switch (res) {
        case YPHYSRES_OUT_OF_RB:
            return "out of rigid bodies";
        case YPHYSRES_OUT_OF_CS:
            return "out of collision shapes";
        case YPHYSRES_OUT_OF_VEH:
            return "out of vehicles";
        case YPHYSRES_OUT_OF_WLD:
            return "out of worlds";
        case YPHYSRES_INVALID_RB:
            return "invalid rigid body";
        case YPHYSRES_INVALID_CS:
            return "invalid collision shape";
        case YPHYSRES_INVALID_VEH:
            return "invalid vehicle";
        case YPHYSRES_INVALID_VEH_WHEEL:
            return "invalid vehicle wheel";
        case YPHYSRES_INVALID_WLD:
            return "invalid world";
        case YPHYSRES_CS_HAS_REFS:
            return "collision shape has references";
        case YPHYSRES_WLD_HAS_REFS:
            return "world has references";
        case YPHYSRES_INTERNAL:
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
    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isfloat(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    dt = (float)lua_tonumber(lua, 2);
    lua_pop(lua, 2);
    if (dt < 0.0f) {
        lua_pushstring(lua, "negative dt");
        lua_error(lua);
        return 0;
    }
    if ((res = yphyscpp_wld_update(wldi, dt)) != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_ddraw(lua_State *lua) {
    int wldi, res;
    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    lua_pop(lua, 1);
    if ((res = yphyscpp_wld_ddraw(wldi)) != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_gravity(lua_State *lua) {
    int res, wldi;
    struct cvector_t *v;
    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    v = cvector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (!v) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    if ((res = yphyscpp_wld_gravity(wldi, v->value)) != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_move(lua_State *lua) {
    int res, wldi;
    struct cvector_t *v;
    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    v = cvector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (!v) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    if ((res = yphyscpp_wld_move(wldi, v->value)) != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_ddraw_mode(lua_State *lua) {
    int res;
    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_wld_ddraw_mode(lua_tointeger(lua, 1), lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_box(lua_State *lua) {
    struct cvector_t *size;
    int csi, res;

    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    csi = lua_tointeger(lua, 1);
    size = cvector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (!size) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    if ((res = yphyscpp_cs_alloc_box(csi, size->value)) != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_sphere(lua_State *lua) {
    float r;
    int csi, res;

    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isfloat(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    csi = lua_tointeger(lua, 1);
    r = (float)lua_tonumber(lua, 2);
    lua_pop(lua, 2);

    if (r <= 0) {
        lua_pushstring(lua, "radius <= 0");
        lua_error(lua);
        return 0;
    }
    if ((res = yphyscpp_cs_alloc_sphere(csi, r)) != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_hmap(lua_State *lua) {
    struct cvector_t *scale;
    int start, width, length, csi, res;
    float hmin, hmax;

    if (lua_gettop(lua) != 7 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isint(lua, 3) || !cutil_isint(lua, 4) || !cutil_isfloat(lua, 5) ||
    !cutil_isfloat(lua, 6) || !cutil_isint(lua, 7)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    csi = lua_tointeger(lua, 1);
    start = lua_tointeger(lua, 2);
    width = lua_tointeger(lua, 3);
    length = lua_tointeger(lua, 4);
    hmin = (float)lua_tonumber(lua, 5);
    hmax = (float)lua_tonumber(lua, 6);
    scale = cvector_get(lua_tointeger(lua, 7));
    lua_pop(lua, 7);

    if (!scale) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    if (start < 0 || start >= g_cbufs.size - (width * length)) {
        lua_pushstring(lua, "start out of range");
        lua_error(lua);
        return 0;
    }
    if (width <= 0 || length <= 0) {
        lua_pushstring(lua, "dims out of range");
        lua_error(lua);
        return 0;
    }
    if (hmin >= hmax) {
        lua_pushstring(lua, "hmin >= hmax");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_cs_alloc_hmap(csi, g_cbufs.data + start, width,
                                length, hmin, hmax, scale->value);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_comp(lua_State *lua) {
    int res;

    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_cs_alloc_comp(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_comp_add(lua_State *lua) {
    int parenti, childi, res;
    struct cmatrix_t *m;

    if (lua_gettop(lua) != 3 || !cutil_isint(lua, 1) ||
    !cutil_isint(lua, 2) || !cutil_isint(lua, 3)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    parenti = lua_tointeger(lua, 1);
    m = cmatrix_get(lua_tointeger(lua, 2));
    childi = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (!m) {
        lua_pushstring(lua, "invalid matrix");
        lua_error(lua);
        return 0;
    }
    if ((res = yphyscpp_cs_comp_add(parenti, m->value, childi)) != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_free(lua_State *lua) {
    int res;
    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_cs_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_rb_alloc(lua_State *lua) {
    struct cmatrix_t *matrix;
    int rbi, wldi, csi, res;
    float mass, fr, roll_fr;

    if (lua_gettop(lua) != 7 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isint(lua, 3) || !cutil_isint(lua, 4) || !cutil_isfloat(lua, 5) ||
    !cutil_isfloat(lua, 6) || !cutil_isfloat(lua, 7)) {
        lua_pushstring(lua, "incorrect argument");
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
        lua_pushstring(lua, "invalid matrix");
        lua_error(lua);
        return 0;
    }
    if (mass < 0.0f) {
        lua_pushstring(lua, "negative mass");
        lua_error(lua);
        return 0;
    }
    if (fr < 0.0f || roll_fr < 0.0f) {
        lua_pushstring(lua, "negative friction");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_rb_alloc(rbi, wldi, csi, matrix->value, mass, fr, roll_fr);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_rb_free(lua_State *lua) {
    int res;
    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_rb_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
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

    if (lua_gettop(lua) != 14 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isint(lua, 3) || !cutil_isint(lua, 4) || !cutil_isint(lua, 5) ||
    !cutil_isfloat(lua, 6) || !cutil_isfloat(lua, 7) || !cutil_isfloat(lua, 8) ||
    !cutil_isfloat(lua, 9) || !cutil_isfloat(lua, 10) || !cutil_isfloat(lua, 11) ||
    !cutil_isfloat(lua, 12) || !cutil_isfloat(lua, 13) || !cutil_isfloat(lua, 14)){
        lua_pushstring(lua, "incorrect argument");
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
        lua_pushstring(lua, "invalid matrix");
        lua_error(lua);
        return 0;
    }
    if (mass < 0.0f) {
        lua_pushstring(lua, "negative mass");
        lua_error(lua);
        return 0;
    }
    if (ch_frict < 0.0f || ch_roll_frict < 0.0f || slip_frict < 0.0f) {
        lua_pushstring(lua, "negative friction");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_veh_alloc(vehi, wldi, shapei, inerti, matrix->value, mass,
                            ch_frict, ch_roll_frict, sus_stif, sus_comp,
                            sus_damp, sus_trav, sus_force, slip_frict);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_free(lua_State *lua) {
    int res;
    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_veh_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_add_wheel(lua_State *lua) {
    struct cvector_t *pos, *dir, *axl;
    float sus_rest, roll, radius;
    int vehi, front, wheel, res;
    if (lua_gettop(lua) != 8 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isint(lua, 3) || !cutil_isint(lua, 4) || !cutil_isfloat(lua, 5) ||
    !cutil_isfloat(lua, 6) || !cutil_isfloat(lua, 7) || !cutil_isint(lua, 8)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vehi = lua_tointeger(lua, 1);
    pos = cvector_get(lua_tointeger(lua, 2));
    dir = cvector_get(lua_tointeger(lua, 3));
    axl = cvector_get(lua_tointeger(lua, 4));
    sus_rest = (float)lua_tonumber(lua, 5);
    roll = (float)lua_tonumber(lua, 6);
    radius = (float)lua_tonumber(lua, 7);
    front = !!lua_tointeger(lua, 8);
    lua_pop(lua, 8);

    if (!pos || !dir || !axl) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    if (radius <= 0.0f) {
        lua_pushstring(lua, "radius not positive");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_veh_add_wheel(&wheel, vehi, pos->value, dir->value,
                                axl->value, sus_rest, roll, radius,
                                front);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, wheel);
    return 1;
}

static int api_physics_veh_set_wheel(lua_State *lua) {
    int vehi, wheel, res;
    float engine, brake, steer;
    if (lua_gettop(lua) != 5 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isfloat(lua, 3) || !cutil_isfloat(lua, 4) || !cutil_isfloat(lua, 5)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vehi = lua_tointeger(lua, 1);
    wheel = lua_tointeger(lua, 2);
    engine = (float)lua_tonumber(lua, 3);
    brake = (float)lua_tonumber(lua, 4);
    steer = (float)lua_tonumber(lua, 5);
    lua_pop(lua, 5);

    res = yphyscpp_veh_set_wheel(vehi, wheel, engine, brake, steer);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_transform(lua_State *lua) {
    int vehi, res;
    struct cmatrix_t *matrix;
    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vehi = lua_tointeger(lua, 1);
    matrix = cmatrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (!matrix) {
        lua_pushstring(lua, "invalid matrix");
        lua_error(lua);
        return 0;
    }
    if ((res = yphyscpp_veh_transform(vehi, matrix->value)) != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_wheel_contact(lua_State *lua)
{
    int in_contact, res;
    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = yphyscpp_veh_wheel_contact(lua_tointeger(lua, 1),
                                    lua_tointeger(lua, 2), &in_contact);
    lua_pop(lua, 2);
    if (res != YPHYSRES_OK) {
        lua_pushstring(lua, cphysics_error(res));
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
    if (yphyscpp_init(cphysics_malloc, cmpool_free, wld_count,
    cs_count, rb_count, veh_count) != YPHYSRES_OK)
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
    #define REGN(x) lua_pushinteger(lua, YPHYSDBG_##x); \
                    lua_setglobal(lua, "API_PHYSICS_"#x);
    YPHYSDBG(REGN)
    #undef REGN
    return 0;
}

void cphysics_done(void) {
    yphyscpp_done();
    if (g_cphysics.mpool) {
        VLOG_INFO("Physics:");
        cmpool_report(g_cphysics.mpool);
        cmpool_destroy(g_cphysics.mpool);
    }
}

int cphysics_wld_cast(int wldi, int csi, float *mfrom, float *mto, float *vout) {
    int res = yphyscpp_wld_cast(wldi, csi, mfrom, mto, vout);
    if (res != YPHYSRES_OK) {
        VLOG_ERROR(cphysics_error(res));
        return 1;
    }
    return 0;
}

int cphysics_rb_fetch_tm(int rbi, float *matrix) {
    return yphyscpp_rb_fetch_tm(rbi, matrix);
}

int cphysics_veh_fetch_chassis_tm(int vehi, float *matrix) {
    return yphyscpp_veh_fetch_chassis_tm(vehi, matrix);
}

int cphysics_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix) {
    return yphyscpp_veh_fetch_wheel_tm(vehi, wheel, matrix);
}

