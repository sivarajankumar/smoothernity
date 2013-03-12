#include "physics.h"
#include "vector.h"
#include "matrix.h"
#include "mpool.h"
#include "buf.h"
#include "../physics/physcpp.h"
#include "../physics/physres.h"
#include <stdio.h>

struct physics_t
{
    struct mpool_t *mpool;
};

static struct physics_t g_physics;

static const char * physics_error_text(int res)
{
    static char UNKNOWN[] = "unknown";
    static char OUT_OF_RB[] = "out of rigid bodies";
    static char OUT_OF_CS[] = "out of collision shapes";
    static char OUT_OF_VEH[] = "out of vehicles";
    static char OUT_OF_WLD[] = "out of worlds";
    static char INVALID_RB[] = "invalid rigid body";
    static char INVALID_CS[] = "invalid collision shape";
    static char INVALID_VEH[] = "invalid vehicle";
    static char INVALID_VEH_WHEEL[] = "invalid vehicle wheel";
    static char INVALID_WLD[] = "invalid world";
    static char CS_HAS_REFS[] = "collision shape has references";
    static char WLD_HAS_REFS[] = "world has references";
    static char INTERNAL[] = "internal error";
    if (res == (int)PHYSRES_OUT_OF_RB)
        return OUT_OF_RB;
    else if (res == (int)PHYSRES_OUT_OF_CS)
        return OUT_OF_CS;
    else if (res == (int)PHYSRES_OUT_OF_VEH)
        return OUT_OF_VEH;
    else if (res == (int)PHYSRES_OUT_OF_WLD)
        return OUT_OF_WLD;
    else if (res == (int)PHYSRES_INVALID_RB)
        return INVALID_RB;
    else if (res == (int)PHYSRES_INVALID_CS)
        return INVALID_CS;
    else if (res == (int)PHYSRES_INVALID_VEH)
        return INVALID_VEH;
    else if (res == (int)PHYSRES_INVALID_VEH_WHEEL)
        return INVALID_VEH_WHEEL;
    else if (res == (int)PHYSRES_INVALID_WLD)
        return INVALID_WLD;
    else if (res == (int)PHYSRES_CS_HAS_REFS)
        return CS_HAS_REFS;
    else if (res == (int)PHYSRES_WLD_HAS_REFS)
        return WLD_HAS_REFS;
    else if (res == (int)PHYSRES_INTERNAL)
        return INTERNAL;
    else
        return UNKNOWN;
}

static void * physics_malloc(size_t size)
{
    return mpool_alloc(g_physics.mpool, size);
}

static int api_physics_wld_update(lua_State *lua)
{
    float dt;
    int wldi, res;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_wld_update: incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    dt = (float)lua_tonumber(lua, 2);
    lua_pop(lua, 2);
    if (dt < 0.0f)
    {
        lua_pushstring(lua, "api_physics_wld_update: negative dt");
        lua_error(lua);
        return 0;
    }
    res = physcpp_wld_update(wldi, dt);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_wld_update: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_wld_update: physics error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_ddraw(lua_State *lua)
{
    int wldi, res;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_physics_wld_ddraw: incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    lua_pop(lua, 1);
    res = physcpp_wld_ddraw(wldi);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "physics_wld_ddraw: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_wld_ddraw: draw error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_gravity(lua_State *lua)
{
    int res, wldi;
    struct vector_t *v;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_wld_gravity: incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    v = vector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (v == 0)
    {
        lua_pushstring(lua, "api_physics_wld_gravity: invalid vector");
        lua_error(lua);
        return 0;
    }
    res = physcpp_wld_gravity(wldi, v->value);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_wld_gravity: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_wld_gravity: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_move(lua_State *lua)
{
    int res, wldi;
    struct vector_t *v;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_wld_move: incorrect argument");
        lua_error(lua);
        return 0;
    }
    wldi = lua_tointeger(lua, 1);
    v = vector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (v == 0)
    {
        lua_pushstring(lua, "api_physics_wld_move: invalid vector");
        lua_error(lua);
        return 0;
    }
    res = physcpp_wld_move(wldi, v->value);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_wld_move: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_wld_move: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_wld_ddraw_mode(lua_State *lua)
{
    int res;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_wld_ddraw_mode: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_wld_ddraw_mode(lua_tointeger(lua, 1), lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_wld_ddraw_mode: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_wld_ddraw_mode: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_box(lua_State *lua)
{
    struct vector_t *size;
    int csi, res;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_cs_alloc_box: incorrect argument");
        lua_error(lua);
        return 0;
    }

    csi = lua_tointeger(lua, 1);
    size = vector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (size == 0)
    {
        lua_pushstring(lua, "api_physics_cs_alloc_box: invalid vector");
        lua_error(lua);
        return 0;
    }

    res = physcpp_cs_alloc_box(csi, size->value);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_cs_alloc_box: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_alloc_box: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_sphere(lua_State *lua)
{
    float r;
    int csi, res;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_cs_alloc_sphere: incorrect argument");
        lua_error(lua);
        return 0;
    }

    csi = lua_tointeger(lua, 1);
    r = (float)lua_tonumber(lua, 2);
    lua_pop(lua, 2);

    if (r <= 0)
    {
        lua_pushstring(lua, "api_physics_cs_alloc_sphere: radius <= 0");
        lua_error(lua);
        return 0;
    }

    res = physcpp_cs_alloc_sphere(csi, r);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_cs_alloc_sphere: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_alloc_sphere: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_hmap(lua_State *lua)
{
    struct vector_t *scale;
    int start, width, length, csi, res;
    float hmin, hmax;

    if (lua_gettop(lua) != 7 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6) || !lua_isnumber(lua, 7))
    {
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

    if (scale == 0)
    {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: invalid vector");
        lua_error(lua);
        return 0;
    }

    if (start < 0 || start >= g_bufs.size - (width * length))
    {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: "
                            "start index out of range");
        lua_error(lua);
        return 0;
    }

    if (width <= 0 || length <= 0)
    {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: "
                            "dimensions out of range");
        lua_error(lua);
        return 0;
    }

    if (hmin >= hmax)
    {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: hmin >= hmax");
        lua_error(lua);
        return 0;
    }
    
    res = physcpp_cs_alloc_hmap(csi, g_bufs.data + start, width,
                                length, hmin, hmax, scale->value);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_cs_alloc_hmap: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_alloc_comp(lua_State *lua)
{
    int res;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_physics_cs_alloc_comp: incorrect argument");
        lua_error(lua);
        return 0;
    }

    res = physcpp_cs_alloc_comp(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_cs_alloc_comp: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_alloc_comp: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_cs_comp_add(lua_State *lua)
{
    int parenti, childi, res;
    struct matrix_t *matrix;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_physics_cs_comp_add: incorrect argument");
        lua_error(lua);
        return 0;
    }

    parenti = lua_tointeger(lua, 1);
    matrix = matrix_get(lua_tointeger(lua, 2));
    childi = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_physics_cs_comp_add: invalid matrix");
        lua_error(lua);
        return 0;
    }

    res = physcpp_cs_comp_add(parenti, matrix->value, childi);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_cs_comp_add: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_comp_add: error");
        lua_error(lua);
        return 0;
    }

    return 0;
}

static int api_physics_cs_free(lua_State *lua)
{
    int res;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_physics_cs_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_cs_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_cs_free: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_free: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_rb_alloc(lua_State *lua)
{
    struct matrix_t *matrix;
    int rbi, wldi, csi, res;
    float mass, frict, roll_frict;

    if (lua_gettop(lua) != 7 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6) || !lua_isnumber(lua, 7))
    {
        lua_pushstring(lua, "api_physics_rb_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    rbi = lua_tointeger(lua, 1);
    wldi = lua_tointeger(lua, 2);
    csi = lua_tointeger(lua, 3);
    matrix = matrix_get(lua_tointeger(lua, 4));
    mass = (float)lua_tonumber(lua, 5);
    frict = (float)lua_tonumber(lua, 6);
    roll_frict = (float)lua_tonumber(lua, 7);
    lua_pop(lua, 7);

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_physics_rb_alloc: invalid matrix");
        lua_error(lua);
        return 0;
    }

    if (mass < 0.0f)
    {
        lua_pushstring(lua, "api_physics_rb_alloc: negative mass");
        lua_error(lua);
        return 0;
    }

    if (frict < 0.0f || roll_frict < 0.0f)
    {
        lua_pushstring(lua, "api_physics_rb_alloc: negative friction");
        lua_error(lua);
        return 0;
    }

    res = physcpp_rb_alloc(rbi, wldi, csi, matrix->value, mass, frict, roll_frict);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_rb_alloc: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_rb_alloc: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_rb_free(lua_State *lua)
{
    int res;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_physics_rb_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_rb_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_rb_free: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_rb_free: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_alloc(lua_State *lua)
{
    struct matrix_t *matrix;
    int wldi, shapei, inerti, vehi, res, i;
    float mass, ch_frict, ch_roll_frict, sus_stif, sus_comp;
    float sus_damp, sus_trav, sus_force, slip_frict;

    if (lua_gettop(lua) != 14)
    {
        lua_pushstring(lua, "api_physics_veh_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    for (i = 1; i <= lua_gettop(lua); ++i)
    {
        if (!lua_isnumber(lua, i))
        {
            lua_pushstring(lua, "api_physics_veh_alloc: incorrect argument");
            lua_error(lua);
            return 0;
        }
    }

    vehi = lua_tointeger(lua, 1);
    wldi = lua_tointeger(lua, 2);
    shapei = lua_tointeger(lua, 3);
    inerti = lua_tointeger(lua, 4);
    matrix = matrix_get(lua_tointeger(lua, 5));
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

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_physics_veh_alloc: invalid matrix");
        lua_error(lua);
        return 0;
    }

    if (mass < 0.0f)
    {
        lua_pushstring(lua, "api_physics_veh_alloc: negative mass");
        lua_error(lua);
        return 0;
    }

    if (ch_frict < 0.0f || ch_roll_frict < 0.0f || slip_frict < 0.0f)
    {
        lua_pushstring(lua, "api_physics_veh_alloc: negative friction");
        lua_error(lua);
        return 0;
    }

    res = physcpp_veh_alloc(vehi, wldi, shapei, inerti, matrix->value, mass,
                            ch_frict, ch_roll_frict, sus_stif, sus_comp,
                            sus_damp, sus_trav, sus_force, slip_frict);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_veh_alloc: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_veh_alloc: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_free(lua_State *lua)
{
    int res;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_physics_veh_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_veh_free(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_veh_free: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_veh_free: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_add_wheel(lua_State *lua)
{
    struct vector_t *pos, *dir, *axl;
    float sus_rest, roll, radius;
    int vehi, front, wheel, res, i;
    if (lua_gettop(lua) != 8)
    {
        lua_pushstring(lua, "api_physics_veh_add_wheel: incorrect argument");
        lua_error(lua);
        return 0;
    }
    for (i = 1; i <= lua_gettop(lua); ++i)
    {
        if (!lua_isnumber(lua, i))
        {
            lua_pushstring(lua, "api_physics_veh_add_wheel: incorrect argument");
            lua_error(lua);
            return 0;
        }
    }
    vehi = lua_tointeger(lua, 1);
    pos = vector_get(lua_tointeger(lua, 2));
    dir = vector_get(lua_tointeger(lua, 3));
    axl = vector_get(lua_tointeger(lua, 4));
    sus_rest = (float)lua_tonumber(lua, 5);
    roll = (float)lua_tonumber(lua, 6);
    radius = (float)lua_tonumber(lua, 7);
    front = lua_tointeger(lua, 8);
    lua_pop(lua, 8);

    if (pos == 0 || dir == 0 || axl == 0)
    {
        lua_pushstring(lua, "api_physics_veh_add_wheel: invalid vector");
        lua_error(lua);
        return 0;
    }

    if (radius <= 0.0f)
    {
        lua_pushstring(lua, "api_physics_veh_add_wheel: radius not positive");
        lua_error(lua);
        return 0;
    }
    
    if (front != 0 && front != 1)
    {
        lua_pushstring(lua, "api_physics_veh_add_wheel: front out of range");
        lua_error(lua);
        return 0;
    }

    res = physcpp_veh_add_wheel(&wheel, vehi, pos->value, dir->value,
                                axl->value, sus_rest, roll, radius,
                                front);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_veh_add_wheel: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_veh_add_wheel: error");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, wheel);
    return 1;
}

static int api_physics_veh_set_wheel(lua_State *lua)
{
    int vehi, wheel, res, i;
    float engine, brake, steer;
    if (lua_gettop(lua) != 5)
    {
        lua_pushstring(lua, "api_physics_veh_set_wheel: incorrect argument");
        lua_error(lua);
        return 0;
    }
    for (i = 1; i <= lua_gettop(lua); ++i)
    {
        if (!lua_isnumber(lua, i))
        {
            lua_pushstring(lua, "api_physics_veh_set_wheel: incorrect argument");
            lua_error(lua);
            return 0;
        }
    }
    vehi = lua_tointeger(lua, 1);
    wheel = lua_tointeger(lua, 2);
    engine = (float)lua_tonumber(lua, 3);
    brake = (float)lua_tonumber(lua, 4);
    steer = (float)lua_tonumber(lua, 5);
    lua_pop(lua, 5);

    res = physcpp_veh_set_wheel(vehi, wheel, engine, brake, steer);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_veh_set_wheel: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_veh_set_wheel: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_transform(lua_State *lua)
{
    int vehi, res;
    struct matrix_t *matrix;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_veh_transform: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vehi = lua_tointeger(lua, 1);
    matrix = matrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);
    if (matrix == 0)
    {
        lua_pushstring(lua, "api_physics_veh_transform: invalid matrix");
        lua_error(lua);
        return 0;
    }
    res = physcpp_veh_transform(vehi, matrix->value);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_veh_transform: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_veh_transform: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_veh_wheel_contact(lua_State *lua)
{
    int in_contact, res;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_veh_wheel_contact: incorrect argument");
        lua_error(lua);
        return 0;
    }
    res = physcpp_veh_wheel_contact(lua_tointeger(lua, 1),
                                    lua_tointeger(lua, 2), &in_contact);
    lua_pop(lua, 2);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "api_physics_veh_wheel_contact: %s\n", physics_error_text(res));
        lua_pushstring(lua, "api_physics_veh_wheel_contact: error");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, in_contact);
    return 1;
}

int physics_init(lua_State *lua, int wld_count, int cs_count,
                 int rb_count, int veh_count,
                 const int msizes[], const int mcounts[], int mlen)
{
    g_physics.mpool = mpool_create(msizes, mcounts, mlen);
    if (g_physics.mpool == 0)
        return 1;
    if (physcpp_init(physics_malloc, mpool_free, wld_count,
                     cs_count, rb_count, veh_count) != PHYSRES_OK)
    {
        return 1;
    }
    lua_register(lua, "api_physics_wld_ddraw", api_physics_wld_ddraw);
    lua_register(lua, "api_physics_wld_ddraw_mode", api_physics_wld_ddraw_mode);
    lua_register(lua, "api_physics_wld_gravity", api_physics_wld_gravity);
    lua_register(lua, "api_physics_wld_move", api_physics_wld_move);
    lua_register(lua, "api_physics_wld_update", api_physics_wld_update);
    lua_register(lua, "api_physics_cs_alloc_box", api_physics_cs_alloc_box);
    lua_register(lua, "api_physics_cs_alloc_sphere", api_physics_cs_alloc_sphere);
    lua_register(lua, "api_physics_cs_alloc_hmap", api_physics_cs_alloc_hmap);
    lua_register(lua, "api_physics_cs_alloc_comp", api_physics_cs_alloc_comp);
    lua_register(lua, "api_physics_cs_comp_add", api_physics_cs_comp_add);
    lua_register(lua, "api_physics_cs_free", api_physics_cs_free);
    lua_register(lua, "api_physics_rb_alloc", api_physics_rb_alloc);
    lua_register(lua, "api_physics_rb_free", api_physics_rb_free);
    lua_register(lua, "api_physics_veh_alloc", api_physics_veh_alloc);
    lua_register(lua, "api_physics_veh_free", api_physics_veh_free);
    lua_register(lua, "api_physics_veh_add_wheel", api_physics_veh_add_wheel);
    lua_register(lua, "api_physics_veh_set_wheel", api_physics_veh_set_wheel);
    lua_register(lua, "api_physics_veh_transform", api_physics_veh_transform);
    lua_register(lua, "api_physics_veh_wheel_contact",
                       api_physics_veh_wheel_contact);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, y); \
        lua_setglobal(lua, x);

    LUA_PUBLISH("API_PHYSICS_NO_DEBUG", 0);
    LUA_PUBLISH("API_PHYSICS_DRAW_WIREFRAME", 1 << 0);
    LUA_PUBLISH("API_PHYSICS_DRAW_AABB", 1 << 1);
    LUA_PUBLISH("API_PHYSICS_DRAW_FEATURES_TEXT", 1 << 2);
    LUA_PUBLISH("API_PHYSICS_DRAW_CONTACT_POINTS", 1 << 3);
    LUA_PUBLISH("API_PHYSICS_NO_DEACTIVATION", 1 << 4);
    LUA_PUBLISH("API_PHYSICS_NO_HELP_TEXT", 1 << 5);
    LUA_PUBLISH("API_PHYSICS_DRAW_TEXT", 1 << 6);
    LUA_PUBLISH("API_PHYSICS_PROFILE_TIMINGS", 1 << 7);
    LUA_PUBLISH("API_PHYSICS_ENABLE_SAT_COMPARISON", 1 << 8);
    LUA_PUBLISH("API_PHYSICS_DISABLE_BULLET_LCP", 1 << 9);
    LUA_PUBLISH("API_PHYSICS_ENABLE_CCD", 1 << 10);
    LUA_PUBLISH("API_PHYSICS_DRAW_CONSTRAINTS", 1 << 11);
    LUA_PUBLISH("API_PHYSICS_DRAW_CONSTRAINT_LIMITS", 1 << 12);
    LUA_PUBLISH("API_PHYSICS_FAST_WIREFRAME", 1 << 13);
    LUA_PUBLISH("API_PHYSICS_DRAW_NORMALS", 1 << 14);
    return 0;
}

void physics_done(void)
{
    physcpp_done();
    fprintf(stdout, "\nPhysics memory pool:\n");
    if (g_physics.mpool)
        mpool_destroy(g_physics.mpool);
}

int physics_wld_cast(int wldi, int csi, float *mfrom, float *mto, float *vout)
{
    int res;
    res = physcpp_wld_cast(wldi, csi, mfrom, mto, vout);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, "physics_wld_cast: %s\n", physics_error_text(res));
        return 1;
    }
    return 0;
}

int physics_rb_fetch_tm(int rbi, float *matrix)
{
    return physcpp_rb_fetch_tm(rbi, matrix);
}

int physics_veh_fetch_chassis_tm(int vehi, float *matrix)
{
    return physcpp_veh_fetch_chassis_tm(vehi, matrix);
}

int physics_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix)
{
    return physcpp_veh_fetch_wheel_tm(vehi, wheel, matrix);
}
