#include "ibuf.h"
#include "vbuf.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>

static const size_t IBUF_SIZE = 64;

struct ibufs_t g_ibufs;

static void ibuf_free(struct ibuf_t *ibuf)
{
    ibuf->vacant = 1;
    ++g_ibufs.left;
    ++g_ibufs.frees;

    if (ibuf->mapped)
    {
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
        glUnmapBuffer(GL_ELEMENT_ARRAY_BUFFER);
        ibuf->mapped = 0;
        if (g_ibufs.mapped == ibuf)
            g_ibufs.mapped = ibuf->next;
    }
    else if (g_ibufs.baked == ibuf)
        g_ibufs.baked = ibuf->next;

    if (ibuf->prev)
        ibuf->prev->next = ibuf->next;
    if (ibuf->next)
        ibuf->next->prev = ibuf->prev;

    if (g_ibufs.vacant)
        g_ibufs.vacant->prev = ibuf;
    ibuf->prev = 0;
    ibuf->next = g_ibufs.vacant;
    g_ibufs.vacant = ibuf;
}

static int api_ibuf_alloc(lua_State *lua)
{
    struct ibuf_t *ibuf;

    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_ibuf_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    if (g_ibufs.vacant == 0)
    {
        lua_pushstring(lua, "api_ibuf_alloc: out of ibufs");
        lua_error(lua);
        return 0;
    }

    ibuf = g_ibufs.vacant;
    g_ibufs.vacant = g_ibufs.vacant->next;
    ibuf->vacant = 0;
    ++g_ibufs.allocs;
    --g_ibufs.left;
    if (g_ibufs.left < g_ibufs.left_min)
        g_ibufs.left_min = g_ibufs.left;

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
    ibuf->mapped = glMapBuffer(GL_ELEMENT_ARRAY_BUFFER, GL_WRITE_ONLY);

    if (ibuf->prev)
        ibuf->prev->next = ibuf->next;
    if (ibuf->next)
        ibuf->next->prev = ibuf->prev;

    if (g_ibufs.mapped)
        g_ibufs.mapped->prev = ibuf;
    ibuf->prev = 0;
    ibuf->next = g_ibufs.mapped;
    g_ibufs.mapped = ibuf;

    lua_pushinteger(lua, ((char*)ibuf - g_ibufs.pool) / IBUF_SIZE);
    return 1;
}

static int api_ibuf_free(lua_State *lua)
{
    struct ibuf_t *ibuf;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_ibuf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    ibuf = ibuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (ibuf == 0 || ibuf->vacant == 1)
    {
        lua_pushstring(lua, "api_ibuf_free: invalid ibuf");
        lua_error(lua);
        return 0;
    }

    ibuf_free(ibuf);
    return 0;
}

static int api_ibuf_bake(lua_State *lua)
{
    struct ibuf_t *ibuf;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_ibuf_bake: incorrect argument");
        lua_error(lua);
        return 0;
    }

    ibuf = ibuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (ibuf == 0 || ibuf->mapped == 0)
    {
        lua_pushstring(lua, "api_ibuf_bake: invalid ibuf");
        lua_error(lua);
        return 0;
    }

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
    glUnmapBuffer(GL_ELEMENT_ARRAY_BUFFER);
    ibuf->mapped = 0;

    if (g_ibufs.mapped == ibuf)
        g_ibufs.mapped = ibuf->next;

    if (ibuf->prev)
        ibuf->prev->next = ibuf->next;
    if (ibuf->next)
        ibuf->next->prev = ibuf->prev;

    if (g_ibufs.baked)
        g_ibufs.baked->prev = ibuf;
    ibuf->prev = 0;
    ibuf->next = g_ibufs.baked;
    g_ibufs.baked = ibuf;
    return 0;
}

static int api_ibuf_set(lua_State *lua)
{
    struct ibuf_t *ibuf;
    ibuf_data_t *data;
    int start, len, index, i;

    if (lua_gettop(lua) < 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_ibuf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ibuf = ibuf_get(lua_tointeger(lua, 1));
    start = lua_tointeger(lua, 2);
    len = lua_gettop(lua) - 2;

    if (ibuf == 0 || ibuf->mapped == 0)
    {
        lua_pushstring(lua, "api_ibuf_set: invalid ibuf");
        lua_error(lua);
        return 0;
    }

    if (start < 0 || start >= g_ibufs.size - len)
    {
        lua_pushstring(lua, "api_ibuf_set: start index out of range");
        lua_error(lua);
        return 0;
    }

    data = ibuf->mapped;
    for (i = 0; i < len; ++i)
    {
        if (!lua_isnumber(lua, 3 + i))
        {
            lua_pushstring(lua, "api_ibuf_set: incorrect data type");
            lua_error(lua);
            return 0;
        }
        index = lua_tointeger(lua, 3 + i);
        if (index < 0 || index >= g_vbufs.size)
        {
            lua_pushstring(lua, "api_ibuf_set: index out of range");
            lua_error(lua);
            return 0;
        }
        data[start + i] = index;
    }

    lua_pop(lua, lua_gettop(lua));
    return 0;
}

static int api_ibuf_query(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_ibuf_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_ibufs.left);
    return 1;
}

int ibuf_init(lua_State *lua, int size, int count)
{
    int i;
    struct ibuf_t *ibuf;
    if (sizeof(struct ibuf_t) > IBUF_SIZE
    ||  (size & (size - 1)) != 0)
    {
        fprintf(stderr, "Invalid sizes:\n"
                        "sizeof(struct ibuf_t) == %i\n"
                        "size == %i\n",
                (int)sizeof(struct ibuf_t),
                size);
        return 1;
    }
    g_ibufs.pool = util_malloc(IBUF_SIZE, IBUF_SIZE * count);
    if (g_ibufs.pool == 0)
        return 1;
    memset(g_ibufs.pool, 0, IBUF_SIZE * count);
    g_ibufs.size = size;
    g_ibufs.count = count;
    g_ibufs.left = count;
    g_ibufs.left_min = count;
    g_ibufs.vacant = ibuf_get(0);
    for (i = 0; i < count; ++i)
    {
        ibuf = ibuf_get(i);
        ibuf->vacant = 1;
        if (i > 0)
            ibuf->prev = ibuf_get(i - 1);
        if (i < count - 1)
            ibuf->next = ibuf_get(i + 1);
        glGenBuffers(1, &ibuf->buf_id);
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(ibuf_data_t) * size,
                     0, GL_STATIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }

    lua_register(lua, "api_ibuf_alloc", api_ibuf_alloc);
    lua_register(lua, "api_ibuf_free", api_ibuf_free);
    lua_register(lua, "api_ibuf_set", api_ibuf_set);
    lua_register(lua, "api_ibuf_bake", api_ibuf_bake);
    lua_register(lua, "api_ibuf_query", api_ibuf_query);

    return 0;
cleanup:
    util_free(g_ibufs.pool);
    g_ibufs.pool = 0;
    return 1;
}

void ibuf_done(void)
{
    if (g_ibufs.pool == 0)
        return;
    printf("Index buffers usage: %i/%i, allocs/frees: %i/%i\n",
           g_ibufs.count - g_ibufs.left_min, g_ibufs.count,
           g_ibufs.allocs, g_ibufs.frees);
    while (g_ibufs.mapped)
        ibuf_free(g_ibufs.mapped);
    while (g_ibufs.baked)
        ibuf_free(g_ibufs.baked);
    util_free(g_ibufs.pool);
    g_ibufs.pool = 0;
}

struct ibuf_t * ibuf_get(int ibufi)
{
    if (ibufi >= 0 && ibufi < g_ibufs.count)
        return (struct ibuf_t*)(g_ibufs.pool + IBUF_SIZE * ibufi);
    else
        return 0;
}

void ibuf_select(struct ibuf_t * ibuf)
{
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
}
