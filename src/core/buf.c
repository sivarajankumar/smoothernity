#include "buf.h"
#include "interp.h"
#include "../util/util.h"
#include <math.h>
#include <stdio.h>
#include <string.h>

static const size_t BUF_DATA_ALIGN = 16;

enum buf_interp_e {
    BUF_IPL_NEAREST,
    BUF_IPL_LINEAR,
    BUF_IPL_SPLINE,
    BUF_IPL_TOTAL
};

struct bufs_t g_bufs;

static float buf_get_nearest(int ofs, int sx, int sy, int x, int y) {
    while ((x = x % sx) < 0)
        x += sx;
    while ((y = y % sy) < 0)
        y += sy;
    return g_bufs.data[ofs + x + (y * sx)];
}

static float buf_get_linear(int ofs, int sx, int sy, float x, float y) {
    float fx, fy, cx, cy, v00, v01, v10, v11, v0y, v1y;
    fx = floorf(x);
    fy = floorf(y);
    cx = ceilf(x);
    cy = ceilf(y);
    v00 = buf_get_nearest(ofs, sx, sy, (int)fx, (int)fy);
    v01 = buf_get_nearest(ofs, sx, sy, (int)fx, (int)cy);
    v10 = buf_get_nearest(ofs, sx, sy, (int)cx, (int)fy);
    v11 = buf_get_nearest(ofs, sx, sy, (int)cx, (int)cy);
    v0y = interp_linear(y - fy, v00, v01);
    v1y = interp_linear(y - fy, v10, v11);
    return interp_linear(x - fx, v0y, v1y);
}

static float buf_get_spline(int ofs, int sx, int sy, float x, float y) {
    int ix, iy;
    float v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23;
    float v30, v31, v32, v33, v0y, v1y, v2y, v3y, fx, fy;
    fx = floorf(x);
    fy = floorf(y);
    ix = (int)fx;
    iy = (int)fy;
    #define GET(dx,dy) buf_get_nearest(ofs, sx, sy, ix + dx, iy + dy)
    v00 = GET(-1, -1); v01 = GET(-1, 0); v02 = GET(-1, 1); v03 = GET(-1, 2);
    v10 = GET( 0, -1); v11 = GET( 0, 0); v12 = GET( 0, 1); v13 = GET( 0, 2);
    v20 = GET( 1, -1); v21 = GET( 1, 0); v22 = GET( 1, 1); v23 = GET( 1, 2);
    v30 = GET( 2, -1); v31 = GET( 2, 0); v32 = GET( 2, 1); v33 = GET( 2, 2);
    #undef GET
    v0y = interp_spline(y - fy, v00, v01, v02, v03);
    v1y = interp_spline(y - fy, v10, v11, v12, v13);
    v2y = interp_spline(y - fy, v20, v21, v22, v23);
    v3y = interp_spline(y - fy, v30, v31, v32, v33);
    return interp_spline(x - fx, v0y, v1y, v2y, v3y);
}

static float buf_get_interp
(int ofs, enum buf_interp_e interp, int sx, int sy, float x, float y) {
    if (interp == BUF_IPL_NEAREST)
        return buf_get_nearest(ofs, sx, sy, (int)x, (int)y);
    else if (interp == BUF_IPL_LINEAR)
        return buf_get_linear(ofs, sx, sy, x, y);
    else if (interp == BUF_IPL_SPLINE)
        return buf_get_spline(ofs, sx, sy, x, y);
    return 0;
}

static int api_buf_set(lua_State *lua) {
    int ofs, len;

    if (lua_gettop(lua) < 2 || !lua_isnumber(lua, 1)) {
        lua_pushstring(lua, "api_buf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ofs = lua_tointeger(lua, 1);
    len = lua_gettop(lua) - 1;

    if (ofs < 0 || ofs >= g_bufs.size - len) {
        lua_pushstring(lua, "api_buf_set: ofs index out of range");
        lua_error(lua);
        return 0;
    }
    for (int i = 0; i < len; ++i) {
        if (!lua_isnumber(lua, i + 2)) {
            lua_pushstring(lua, "api_buf_set: incorrect data type");
            lua_error(lua);
            return 0;
        }
        g_bufs.data[ofs + i] = (float)lua_tonumber(lua, i + 2);
    }
    lua_pop(lua, len + 1);

    return 0;
}

static int api_buf_get(lua_State *lua) {
    int ofs, interp, sx, sy;
    float x, y;

    if (lua_gettop(lua) < 6 ||
    !lua_isnumber(lua, 1) || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3) ||
    !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5) || !lua_isnumber(lua, 6)) {
        lua_pushstring(lua, "api_buf_get: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ofs = lua_tointeger(lua, 1);
    interp = lua_tointeger(lua, 2);
    sx = lua_tointeger(lua, 3);
    sy = lua_tointeger(lua, 4);
    x = (float)lua_tonumber(lua, 5);
    y = (float)lua_tonumber(lua, 6);
    lua_pop(lua, 6);

    if (ofs < 0 || ofs >= g_bufs.size - (sx * sy)) {
        lua_pushstring(lua, "api_buf_get: invalid range");
        lua_error(lua);
        return 0;
    }
    if (interp < 0 || interp >= BUF_IPL_TOTAL) {
        lua_pushstring(lua, "api_buf_get: invalid interp");
        lua_error(lua);
        return 0;
    }
    lua_pushnumber(lua, buf_get_interp(ofs, interp, sx, sy, x, y));
    return 1;
}

void buf_reg_thread(lua_State *lua) {
    lua_register(lua, "api_buf_set", api_buf_set);
    lua_register(lua, "api_buf_get", api_buf_get);
    #define REG(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);
    REG(BUF_IPL_NEAREST);
    REG(BUF_IPL_LINEAR);
    REG(BUF_IPL_SPLINE);
    #undef REG
}

int buf_init(lua_State *lua, int size) {
    if (size & (size - 1)) {
        fprintf(stderr, "Invalid size:\nsize == %i\n", size);
        return 1;
    }
    g_bufs.size = size;
    g_bufs.data = util_malloc(BUF_DATA_ALIGN, sizeof(float) * size);
    if (!g_bufs.data)
        return 1;
    memset(g_bufs.data, 0, sizeof(float) * size);
    buf_reg_thread(lua);
    return 0;
}

void buf_done(void) {
    if (!g_bufs.data)
        return;
    util_free(g_bufs.data);
    g_bufs.data = 0;
}

