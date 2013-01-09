#include "ibuf.h"
#include "scene.h"
#include <stdlib.h>

struct ibufs_t g_ibufs;

static void ibuf_free(struct ibuf_t *ibuf)
{
    ibuf->vacant = 1;
    ++g_ibufs.left;

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
    ibuf->vacant = 0;
    --g_ibufs.left;

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
    ibuf->mapped = glMapBuffer(GL_ELEMENT_ARRAY_BUFFER, GL_WRITE_ONLY);

    if (g_ibufs.vacant == ibuf)
        g_ibufs.vacant = ibuf->next;

    if (ibuf->prev)
        ibuf->prev->next = ibuf->next;
    if (ibuf->next)
        ibuf->next->prev = ibuf->prev;

    if (g_ibufs.mapped)
        g_ibufs.mapped->prev = ibuf;
    ibuf->prev = 0;
    ibuf->next = g_ibufs.mapped;
    g_ibufs.mapped = ibuf;

    lua_pushinteger(lua, ibuf - g_ibufs.pool);
    return 1;
}

static int api_ibuf_free(lua_State *lua)
{
    struct ibuf_t *ibuf;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_ibuf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    ibuf = ibuf_get(lua_tointeger(lua, -1));
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

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_ibuf_bake: incorrect argument");
        lua_error(lua);
        return 0;
    }

    ibuf = ibuf_get(lua_tointeger(lua, -1));
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

static int api_ibuf_write(lua_State *lua)
{
    struct ibuf_t *ibuf;
    struct ibuf_data_t *data;
    int datai, index;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_ibuf_write: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ibuf = ibuf_get(lua_tointeger(lua, -3));
    datai = lua_tointeger(lua, -2);
    index = lua_tointeger(lua, -1);
    lua_pop(lua, 3);

    if (datai < 0 || datai >= g_ibufs.size)
    {
        lua_pushstring(lua, "api_ibuf_write: data out of range");
        lua_error(lua);
        return 0;
    }

    if (index < 0 || index >= g_vbufs.size)
    {
        lua_pushstring(lua, "api_ibuf_write: index out of range");
        lua_error(lua);
        return 0;
    }

    if (ibuf == 0 || ibuf->mapped == 0)
    {
        lua_pushstring(lua, "api_ibuf_write: invalid ibuf");
        lua_error(lua);
        return 0;
    }

    data = ibuf->mapped;
    data += datai;

    data->index = index;
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
    lua_pushinteger(lua, g_ibufs.size);
    lua_pushinteger(lua, g_ibufs.left);
    return 2;
}

int ibuf_init(lua_State *lua, int size, int count)
{
    int i;
    g_ibufs.pool = calloc(count, sizeof(struct ibuf_t));
    if (g_ibufs.pool == 0)
        return 1;
    for (i = 0; i < count; ++i)
    {
        g_ibufs.pool[i].vacant = 1;
        if (i > 0)
            g_ibufs.pool[i].prev = g_ibufs.pool + i - 1;
        if (i < count - 1)
            g_ibufs.pool[i].next = g_ibufs.pool + i + 1;
        glGenBuffers(1, &g_ibufs.pool[i].buf_id);
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, g_ibufs.pool[i].buf_id);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(struct ibuf_data_t) * size,
                     0, GL_STATIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    g_ibufs.vacant = g_ibufs.pool;
    g_ibufs.size = size;
    g_ibufs.count = count;
    g_ibufs.left = count;

    lua_register(lua, "api_ibuf_alloc", api_ibuf_alloc);
    lua_register(lua, "api_ibuf_free", api_ibuf_free);
    lua_register(lua, "api_ibuf_write", api_ibuf_write);
    lua_register(lua, "api_ibuf_bake", api_ibuf_bake);
    lua_register(lua, "api_ibuf_query", api_ibuf_query);

    return 0;
cleanup:
    free(g_ibufs.pool);
    g_ibufs.pool = 0;
    return 1;
}

void ibuf_done(void)
{
    if (g_ibufs.pool)
    {
        while (g_ibufs.mapped)
            ibuf_free(g_ibufs.mapped);
        while (g_ibufs.baked)
            ibuf_free(g_ibufs.baked);
        free(g_ibufs.pool);
        g_ibufs.pool = 0;
    }
}

struct ibuf_t * ibuf_get(int ibufi)
{
    if (ibufi >= 0 && ibufi < g_ibufs.count)
        return g_ibufs.pool + ibufi;
    else
        return 0;
}

void ibuf_select(struct ibuf_t * ibuf)
{
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
}
