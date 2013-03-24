#include "buf.h"
#include "interp.h"
#include "../util/util.h"
#include <math.h>
#include <stdio.h>
#include <string.h>

static const size_t BUF_DATA_ALIGN = 16;

enum buf_interp_e
{
    BUF_IPL_NEAREST = 0,
    BUF_IPL_LINEAR,
    BUF_IPL_SPLINE,
    BUF_IPL_TOTAL
};

struct bufs_t g_bufs;

static float buf_get_nearest(int start, int width, int length, int x, int y)
{
    x = x % width;
    y = y % length;
    if (x < 0)
        x += width;
    if (y < 0)
        y += length;
    return g_bufs.data[start + x + (y * width)];
}

static float buf_get_linear(int start, int width, int length, float x, float y)
{
    float fx, fy, cx, cy;
    float v00, v01, v10, v11, v0y, v1y;
    fx = floorf(x);
    fy = floorf(y);
    cx = ceilf(x);
    cy = ceilf(y);
    v00 = buf_get_nearest(start, width, length, (int)fx, (int)fy);
    v01 = buf_get_nearest(start, width, length, (int)fx, (int)cy);
    v10 = buf_get_nearest(start, width, length, (int)cx, (int)fy);
    v11 = buf_get_nearest(start, width, length, (int)cx, (int)cy);
    v0y = interp_linear(y - fy, v00, v01);
    v1y = interp_linear(y - fy, v10, v11);
    return interp_linear(x - fx, v0y, v1y);
}

static float buf_get_spline(int start, int width, int length, float x, float y)
{
    float fx, fy;
    float v00, v01, v02, v03;
    float v10, v11, v12, v13;
    float v20, v21, v22, v23;
    float v30, v31, v32, v33;
    float v0y, v1y, v2y, v3y;
    fx = floorf(x);
    fy = floorf(y);
    v00 = buf_get_nearest(start, width, length, (int)(fx - 1.0f), (int)(fy - 1.0f));
    v01 = buf_get_nearest(start, width, length, (int)(fx - 1.0f), (int)fy);
    v02 = buf_get_nearest(start, width, length, (int)(fx - 1.0f), (int)(fy + 1.0f));
    v03 = buf_get_nearest(start, width, length, (int)(fx - 1.0f), (int)(fy + 2.0f));
    v10 = buf_get_nearest(start, width, length, (int)fx, (int)(fy - 1.0f));
    v11 = buf_get_nearest(start, width, length, (int)fx, (int)fy);
    v12 = buf_get_nearest(start, width, length, (int)fx, (int)(fy + 1.0f));
    v13 = buf_get_nearest(start, width, length, (int)fx, (int)(fy + 2.0f));
    v20 = buf_get_nearest(start, width, length, (int)(fx + 1.0f), (int)(fy - 1.0f));
    v21 = buf_get_nearest(start, width, length, (int)(fx + 1.0f), (int)fy);
    v22 = buf_get_nearest(start, width, length, (int)(fx + 1.0f), (int)(fy + 1.0f));
    v23 = buf_get_nearest(start, width, length, (int)(fx + 1.0f), (int)(fy + 2.0f));
    v30 = buf_get_nearest(start, width, length, (int)(fx + 2.0f), (int)(fy - 1.0f));
    v31 = buf_get_nearest(start, width, length, (int)(fx + 2.0f), (int)fy);
    v32 = buf_get_nearest(start, width, length, (int)(fx + 2.0f), (int)(fy + 1.0f));
    v33 = buf_get_nearest(start, width, length, (int)(fx + 2.0f), (int)(fy + 2.0f));
    v0y = interp_spline(y - fy, v00, v01, v02, v03);
    v1y = interp_spline(y - fy, v10, v11, v12, v13);
    v2y = interp_spline(y - fy, v20, v21, v22, v23);
    v3y = interp_spline(y - fy, v30, v31, v32, v33);
    return interp_spline(x - fx, v0y, v1y, v2y, v3y);
}

static float buf_get_interp(int start, enum buf_interp_e interp, int width,
                            int length, float x, float y)
{
    if (interp == BUF_IPL_NEAREST)
        return buf_get_nearest(start, width, length, (int)x, (int)y);
    else if (interp == BUF_IPL_LINEAR)
        return buf_get_linear(start, width, length, x, y);
    else if (interp == BUF_IPL_SPLINE)
        return buf_get_spline(start, width, length, x, y);
    return 0;
}

static int api_buf_set(lua_State *lua)
{
    int start, len, i;

    if (lua_gettop(lua) < 2 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_buf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }

    start = lua_tointeger(lua, 1);
    len = lua_gettop(lua) - 1;

    if (start < 0 || start >= g_bufs.size - len)
    {
        lua_pushstring(lua, "api_buf_set: start index out of range");
        lua_error(lua);
        return 0;
    }

    for (i = 0; i < len; ++i)
    {
        if (!lua_isnumber(lua, i + 2))
        {
            lua_pushstring(lua, "api_buf_set: incorrect data type");
            lua_error(lua);
            return 0;
        }
        g_bufs.data[start + i] = (float)lua_tonumber(lua, i + 2);
    }

    lua_pop(lua, len + 1);

    return 0;
}

static int api_buf_get(lua_State *lua)
{
    int start, interp, width, length;
    float x, y;

    if (lua_gettop(lua) < 6 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6))
    {
        lua_pushstring(lua, "api_buf_get: incorrect argument");
        lua_error(lua);
        return 0;
    }

    start = lua_tointeger(lua, 1);
    interp = lua_tointeger(lua, 2);
    width = lua_tointeger(lua, 3);
    length = lua_tointeger(lua, 4);
    x = (float)lua_tonumber(lua, 5);
    y = (float)lua_tonumber(lua, 6);
    lua_pop(lua, 6);

    if (start < 0 || start >= g_bufs.size - (width * length))
    {
        lua_pushstring(lua, "api_buf_get: invalid range");
        lua_error(lua);
        return 0;
    }

    if (interp < 0 || interp >= BUF_IPL_TOTAL)
    {
        lua_pushstring(lua, "api_buf_get: invalid interp");
        lua_error(lua);
        return 0;
    }

    lua_pushnumber(lua, buf_get_interp(start, interp, width, length, x, y));
    return 1;
}

void buf_reg_thread(lua_State *lua)
{
    lua_register(lua, "api_buf_set", api_buf_set);
    lua_register(lua, "api_buf_get", api_buf_get);

    #define LUA_PUBLISH(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);

    LUA_PUBLISH(BUF_IPL_NEAREST);
    LUA_PUBLISH(BUF_IPL_LINEAR);
    LUA_PUBLISH(BUF_IPL_SPLINE);
}

int buf_init(lua_State *lua, int size)
{
    if ((size & (size - 1)) != 0)
    {
        fprintf(stderr, "Invalid size:\nsize == %i\n", size);
        return 1;
    }
    g_bufs.size = size;
    g_bufs.data = util_malloc(BUF_DATA_ALIGN, sizeof(float) * size);
    if (g_bufs.data == 0)
        return 1;
    memset(g_bufs.data, 0, sizeof(float) * size);
    buf_reg_thread(lua);
    return 0;
}

void buf_done(void)
{
    if (g_bufs.data == 0)
        return;
    util_free(g_bufs.data);
    g_bufs.data = 0;
}
