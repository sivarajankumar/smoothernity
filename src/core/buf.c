#include "buf.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>

static const size_t BUF_DATA_ALIGN = 16;

struct bufs_t g_bufs;

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
    lua_register(lua, "api_buf_set", api_buf_set);
    return 0;
}

void buf_done(void)
{
    if (g_bufs.data == 0)
        return;
    util_free(g_bufs.data);
    g_bufs.data = 0;
}
