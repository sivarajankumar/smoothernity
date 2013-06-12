#include "cbuf.h"
#include "interp.h"
#include "util.h"
#include "pmem.h"
#include <math.h>
#include <stdio.h>

enum cbuf_interp_e {
    CBUF_IPL_NEAREST,
    CBUF_IPL_LINEAR,
    CBUF_IPL_SPLINE,
    CBUF_IPL_TOTAL
};

struct cbufs_t g_cbufs;

static float cbuf_get_nearest(int ofs, int sx, int sy, int x, int y) {
    while ((x = x % sx) < 0)
        x += sx;
    while ((y = y % sy) < 0)
        y += sy;
    return g_cbufs.data[ofs + x + (y * sx)];
}

static float cbuf_get_linear(int ofs, int sx, int sy, float x, float y) {
    float fx, fy, cx, cy, v00, v01, v10, v11, v0y, v1y;
    fx = floorf(x);
    fy = floorf(y);
    cx = ceilf(x);
    cy = ceilf(y);
    v00 = cbuf_get_nearest(ofs, sx, sy, (int)fx, (int)fy);
    v01 = cbuf_get_nearest(ofs, sx, sy, (int)fx, (int)cy);
    v10 = cbuf_get_nearest(ofs, sx, sy, (int)cx, (int)fy);
    v11 = cbuf_get_nearest(ofs, sx, sy, (int)cx, (int)cy);
    v0y = interp_linear(y - fy, v00, v01);
    v1y = interp_linear(y - fy, v10, v11);
    return interp_linear(x - fx, v0y, v1y);
}

static float cbuf_get_spline(int ofs, int sx, int sy, float x, float y) {
    int ix, iy;
    float v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23;
    float v30, v31, v32, v33, v0y, v1y, v2y, v3y, fx, fy;
    fx = floorf(x);
    fy = floorf(y);
    ix = (int)fx;
    iy = (int)fy;
    #define GET(dx,dy) cbuf_get_nearest(ofs, sx, sy, ix + dx, iy + dy)
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

static float cbuf_get_interp
(int ofs, enum cbuf_interp_e interp, int sx, int sy, float x, float y) {
    if (interp == CBUF_IPL_NEAREST)
        return cbuf_get_nearest(ofs, sx, sy, (int)x, (int)y);
    else if (interp == CBUF_IPL_LINEAR)
        return cbuf_get_linear(ofs, sx, sy, x, y);
    else if (interp == CBUF_IPL_SPLINE)
        return cbuf_get_spline(ofs, sx, sy, x, y);
    return 0;
}

static int api_buf_set(lua_State *lua) {
    int ofs, len;

    if (lua_gettop(lua) < 2 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_buf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ofs = lua_tointeger(lua, 1);
    len = lua_gettop(lua) - 1;

    if (ofs < 0 || ofs >= g_cbufs.size - len) {
        lua_pushstring(lua, "api_buf_set: ofs index out of range");
        lua_error(lua);
        return 0;
    }
    for (int i = 0; i < len; ++i) {
        if (!util_isfloat(lua, i + 2)) {
            lua_pushstring(lua, "api_buf_set: incorrect data type");
            lua_error(lua);
            return 0;
        }
        g_cbufs.data[ofs + i] = (float)lua_tonumber(lua, i + 2);
    }
    lua_pop(lua, len + 1);

    return 0;
}

static int api_buf_get(lua_State *lua) {
    int ofs, interp, sx, sy;
    float x, y;

    if (lua_gettop(lua) < 6 ||
    !util_isint(lua, 1) || !util_isint(lua, 2) || !util_isint(lua, 3) ||
    !util_isint(lua, 4) || !util_isfloat(lua, 5) || !util_isfloat(lua, 6)) {
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

    if (ofs < 0 || ofs >= g_cbufs.size - (sx * sy)) {
        lua_pushstring(lua, "api_buf_get: invalid range");
        lua_error(lua);
        return 0;
    }
    if (interp < 0 || interp >= CBUF_IPL_TOTAL) {
        lua_pushstring(lua, "api_buf_get: invalid interp");
        lua_error(lua);
        return 0;
    }
    lua_pushnumber(lua, cbuf_get_interp(ofs, interp, sx, sy, x, y));
    return 1;
}

void cbuf_reg_thread(lua_State *lua) {
    lua_register(lua, "api_buf_set", api_buf_set);
    lua_register(lua, "api_buf_get", api_buf_get);
    #define REG(x) lua_pushinteger(lua, C##x); lua_setglobal(lua, "API_"#x);
    REG(BUF_IPL_NEAREST);
    REG(BUF_IPL_LINEAR);
    REG(BUF_IPL_SPLINE);
    #undef REG
}

int cbuf_init(lua_State *lua, int size) {
    if (size & (size - 1)) {
        fprintf(stderr, "Invalid size:\nsize == %i\n", size);
        return 1;
    }
    g_cbufs.size = size;
    g_cbufs.data = pmem_alloc(PMEM_ALIGNOF(float), sizeof(float) * size);
    if (!g_cbufs.data)
        return 1;
    for (int i = 0; i < size; ++i)
        g_cbufs.data[i] = 0;
    cbuf_reg_thread(lua);
    return 0;
}

void cbuf_done(void) {
    if (!g_cbufs.data)
        return;
    pmem_free(g_cbufs.data);
    g_cbufs.data = 0;
}

