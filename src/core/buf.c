#include "buf.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static const size_t BUF_SIZE = 32;
static const size_t BUF_DATA_ALIGN = 16;

struct bufs_t g_bufs;

static int api_buf_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_buf_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_bufs.left);
    return 1;
}

static int api_buf_set(lua_State *lua)
{
    struct buf_t *buf;
    int start, len, i;

    if (lua_gettop(lua) < 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_buf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }

    buf = buf_get(lua_tointeger(lua, 1));
    start = lua_tointeger(lua, 2);
    len = lua_gettop(lua) - 2;

    if (buf == 0)
    {
        lua_pushstring(lua, "api_buf_set: invalid buf");
        lua_error(lua);
        return 0;
    }

    if (start < 0 || start >= g_bufs.size - len)
    {
        lua_pushstring(lua, "api_buf_set: start index out of range");
        lua_error(lua);
        return 0;
    }

    for (i = 0; i < len; ++i)
    {
        if (!lua_isnumber(lua, i + 3))
        {
            lua_pushstring(lua, "api_buf_set: incorrect data type");
            lua_error(lua);
            return 0;
        }
        buf->data[start + i] = lua_tonumber(lua, i + 3);
    }

    lua_pop(lua, len + 2);

    return 0;
}

static int api_buf_alloc(lua_State *lua)
{
    struct buf_t *buf;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_buf_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    if (g_bufs.vacant == 0)
    {
        lua_pushstring(lua, "api_buf_alloc: out of bufs");
        lua_error(lua);
        return 0;
    }
    
    ++g_bufs.frees;
    --g_bufs.left;
    if (g_bufs.left < g_bufs.left_min)
        g_bufs.left_min = g_bufs.left;
    buf = g_bufs.vacant;
    g_bufs.vacant = g_bufs.vacant->next;
    buf->next = 0;
    buf->vacant = 0;

    lua_pushinteger(lua, ((char*)buf - g_bufs.pool) / BUF_SIZE);
    return 1;
}

static int api_buf_free(lua_State *lua)
{
    struct buf_t *buf;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_buf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    buf = buf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (buf == 0 || buf->vacant == 1)
    {
        lua_pushstring(lua, "api_buf_free: invalid buf");
        lua_error(lua);
        return 0;
    }
    
    ++g_bufs.allocs;
    ++g_bufs.left;
    buf->vacant = 1;
    buf->next = g_bufs.vacant;
    g_bufs.vacant = buf;
    return 0;
}

int buf_init(lua_State *lua, int size, int count)
{
    int i;
    struct buf_t *buf;
    if (sizeof(struct buf_t) > BUF_SIZE
    ||  (size & (size - 1)) != 0)
    {
        fprintf(stderr, "Invalid size:\n"
                        "sizeof(struct buf_t) == %i\n"
                        "size == %i\n",
                (int)sizeof(struct buf_t), size);
        return 1;
    }
    g_bufs.pool = aligned_alloc(BUF_SIZE, BUF_SIZE * count);
    if (g_bufs.pool == 0)
        return 1;
    memset(g_bufs.pool, 0, BUF_SIZE * count);
    g_bufs.vacant = (struct buf_t*)g_bufs.pool;
    g_bufs.count = count;
    g_bufs.left = count;
    g_bufs.size = size;
    g_bufs.left_min = count;
    for (i = 0; i < count; ++i)
    {
        buf = buf_get(i);
        if (i < count - 1)
            buf->next = buf_get(i + 1);
        buf->vacant = 1;
        buf->data = aligned_alloc(BUF_DATA_ALIGN, sizeof(float) * size);
        if (buf->data == 0)
            goto cleanup;
        memset(buf->data, 0, sizeof(float) * size);
    }
    lua_register(lua, "api_buf_alloc", api_buf_alloc);
    lua_register(lua, "api_buf_free", api_buf_free);
    lua_register(lua, "api_buf_left", api_buf_left);
    lua_register(lua, "api_buf_set", api_buf_set);
    return 0;
cleanup:
    buf_done();
    return 1;
}

void buf_done(void)
{
    int i;
    struct buf_t *buf;
    if (g_bufs.pool == 0)
        return;
    printf("Buffers usage: %i/%i, allocs/frees: %i/%i\n",
           g_bufs.count - g_bufs.left_min, g_bufs.count,
           g_bufs.allocs, g_bufs.frees);
    for (i = 0; i < g_bufs.count; ++i)
    {
        buf = buf_get(i);
        if (buf->data)
            free(buf->data);
    }
    free(g_bufs.pool);
    g_bufs.pool = 0;
}

struct buf_t * buf_get(int bufi)
{
    if (bufi >= 0 && bufi < g_bufs.count)
        return (struct buf_t*)(g_bufs.pool + BUF_SIZE * bufi);
    else
        return 0;
}
