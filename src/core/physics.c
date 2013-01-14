#include "physics.h"
#include "vector.h"
#include "matrix.h"
#include "mpool.h"
#include "buf.h"
#include "../physics/physcpp.h"
#include "../physics/physres.h"
#include <stdio.h>

static const char * physics_error_text(int res)
{
    static char UNKNOWN[] = "unknown";
    static char OUT_OF_RB[] = "out of rigid bodies";
    static char OUT_OF_CS[] = "out of collision shapes";
    static char INVALID_RB[] = "invalid rigid body";
    static char INVALID_CS[] = "invalid collision shape";
    if (res == (int)PHYSRES_OUT_OF_RB)
        return OUT_OF_RB;
    else if (res == (int)PHYSRES_OUT_OF_CS)
        return OUT_OF_CS;
    else if (res == (int)PHYSRES_INVALID_RB)
        return INVALID_RB;
    else if (res == (int)PHYSRES_INVALID_CS)
        return INVALID_CS;
    else
        return UNKNOWN;
}

static int api_physics_left(lua_State *lua)
{
    int cs_left, rb_left;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_physics_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    physcpp_left(&cs_left, &rb_left);
    lua_pushinteger(lua, cs_left);
    lua_pushinteger(lua, rb_left);
    return 2;
}

static int api_physics_set_gravity(lua_State *lua)
{
    struct vector_t *v;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_physics_set_gravity: incorrect argument");
        lua_error(lua);
        return 0;
    }
    v = vector_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (v == 0)
    {
        lua_pushstring(lua, "api_physics_set_gravity: invalid vector");
        lua_error(lua);
        return 0;
    }
    physcpp_set_gravity(v->value);
    return 0;
}

static int api_physics_set_ddraw(lua_State *lua)
{
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_physics_set_ddraw: incorrect argument");
        lua_error(lua);
        return 0;
    }
    physcpp_ddraw_set_mode(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    return 0;
}

static int api_physics_cs_alloc_box(lua_State *lua)
{
    struct vector_t *size;
    float mass;
    int csi;
    int res;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_cs_alloc_box: incorrect argument");
        lua_error(lua);
        return 0;
    }

    mass = lua_tonumber(lua, 1);
    size = vector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (mass < 0.0f)
    {
        lua_pushstring(lua, "api_physics_cs_alloc_box: negative mass");
        lua_error(lua);
        return 0;
    }

    if (size == 0)
    {
        lua_pushstring(lua, "api_physics_cs_alloc_box: invalid vector");
        lua_error(lua);
        return 0;
    }

    res = physcpp_cs_alloc_box(&csi, mass, size->value);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_alloc_box: error");
        lua_error(lua);
        return 0;
    }

    lua_pushinteger(lua, csi);
    return 1;
}

static int api_physics_cs_alloc_hmap(lua_State *lua)
{
    struct buf_t *hmap;
    int start, width, length, csi, res;
    float hmin, hmax;

    if (lua_gettop(lua) != 6 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6))
    {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: incorrect argument");
        lua_error(lua);
        return 0;
    }

    hmap = buf_get(lua_tointeger(lua, 1));
    start = lua_tointeger(lua, 2);
    width = lua_tointeger(lua, 3);
    length = lua_tointeger(lua, 4);
    hmin = lua_tonumber(lua, 5);
    hmax = lua_tonumber(lua, 6);
    lua_pop(lua, 6);

    if (hmap == 0)
    {
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: invalid buf");
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
    
    res = physcpp_cs_alloc_hmap(&csi, hmap->data + start, width,
                                length, hmin, hmax);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_alloc_hmap: error");
        lua_error(lua);
        return 0;
    }

    lua_pushinteger(lua, csi);
    return 1;
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
        fprintf(stderr, physics_error_text(res));
        lua_pushstring(lua, "api_physics_cs_free: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_physics_rb_alloc(lua_State *lua)
{
    struct matrix_t *matrix;
    int csi;
    int rbi;
    int res;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_physics_rb_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    csi = lua_tointeger(lua, 1);
    matrix = matrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_physics_rb_alloc: invalid matrix");
        lua_error(lua);
        return 0;
    }

    res = physcpp_rb_alloc(&rbi, csi, matrix->value);
    if (res != PHYSRES_OK)
    {
        fprintf(stderr, physics_error_text(res));
        lua_pushstring(lua, "api_physics_rb_alloc: error");
        lua_error(lua);
        return 0;
    }

    lua_pushinteger(lua, rbi);
    return 1;
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
        fprintf(stderr, physics_error_text(res));
        lua_pushstring(lua, "api_physics_rb_free: error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

int physics_init(lua_State *lua, int cs_count, int rb_count)
{
    if (physcpp_init(mpool_alloc, mpool_free, cs_count, rb_count)
     != PHYSRES_OK)
    {
        return 1;
    }
    lua_register(lua, "api_physics_left", api_physics_left);
    lua_register(lua, "api_physics_set_gravity", api_physics_set_gravity);
    lua_register(lua, "api_physics_set_ddraw", api_physics_set_ddraw);
    lua_register(lua, "api_physics_cs_alloc_box", api_physics_cs_alloc_box);
    lua_register(lua, "api_physics_cs_alloc_hmap", api_physics_cs_alloc_hmap);
    lua_register(lua, "api_physics_cs_free", api_physics_cs_free);
    lua_register(lua, "api_physics_rb_alloc", api_physics_rb_alloc);
    lua_register(lua, "api_physics_rb_free", api_physics_rb_free);
    return 0;
}

void physics_done(void)
{
    physcpp_done();
}

void physics_update(float dt)
{
    physcpp_update(dt);
}

void physics_ddraw(void)
{
    physcpp_ddraw();
}

int physics_rb_get_new_matrix(int rbi, float *matrix)
{
    return physcpp_rb_get_new_matrix(rbi, matrix);
}
