#include "ibuf.h"
#include "vbuf.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>

static const size_t IBUF_SIZE = 64;

struct ibufs_t g_ibufs;

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
    ++g_ibufs.allocs;
    --g_ibufs.left;
    if (g_ibufs.left < g_ibufs.left_min)
        g_ibufs.left_min = g_ibufs.left;

    ibuf->state = IBUF_UNMAPPED;
    ibuf->next = 0;

    lua_pushinteger(lua, ((char*)ibuf - g_ibufs.pool) / IBUF_SIZE);
    return 1;
}

static int api_ibuf_map(lua_State *lua)
{
    struct ibuf_t *ibuf;
    int ofs, len;
    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_ibuf_map: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ibuf = ibuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = lua_tointeger(lua, 3);
    lua_pop(lua, 3);
    if (ibuf == 0 || ibuf->state != IBUF_UNMAPPED)
    {
        lua_pushstring(lua, "api_ibuf_map: invalid ibuf");
        lua_error(lua);
        return 0;
    }
    if (len <= 0 || ofs < 0 || ofs > g_ibufs.size - len)
    {
        lua_pushstring(lua, "api_ibuf_map: invalid range");
        lua_error(lua);
        return 0;
    }
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
    ibuf->mapped = glMapBufferRange(GL_ELEMENT_ARRAY_BUFFER,
                                    (GLintptr)(ofs * (int)sizeof(ibuf_data_t)),
                                    (GLsizeiptr)(len * (int)sizeof(ibuf_data_t)),
                                    GL_MAP_WRITE_BIT | GL_MAP_UNSYNCHRONIZED_BIT);
    if (ibuf->mapped == 0)
    {
        lua_pushstring(lua, "api_ibuf_map: mapping error");
        lua_error(lua);
        return 0;
    }
    ibuf->mapped_ofs = ofs;
    ibuf->mapped_len = len;
    ibuf->state = IBUF_MAPPED;
    return 0;
}

static int api_ibuf_unmap(lua_State *lua)
{
    struct ibuf_t *ibuf;
    if (lua_gettop(lua) != 1)
    {
        lua_pushstring(lua, "api_ibuf_unmap: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ibuf = ibuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (ibuf == 0 || ibuf->state != IBUF_MAPPED)
    {
        lua_pushstring(lua, "api_ibuf_unmap: invalid ibuf");
        lua_error(lua);
        return 0;
    }
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
    glUnmapBuffer(GL_ELEMENT_ARRAY_BUFFER);
    ibuf->mapped = 0;
    ibuf->mapped_ofs = 0;
    ibuf->mapped_len = 0;
    ibuf->state = IBUF_UNMAPPED;
    return 0;
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

    if (ibuf == 0 || ibuf->state != IBUF_UNMAPPED)
    {
        lua_pushstring(lua, "api_ibuf_free: invalid ibuf");
        lua_error(lua);
        return 0;
    }

    ++g_ibufs.left;
    ++g_ibufs.frees;

    ibuf->state = IBUF_VACANT;
    ibuf->next = g_ibufs.vacant;
    g_ibufs.vacant = ibuf;
    return 0;
}

static int api_ibuf_set(lua_State *lua)
{
    struct ibuf_t *ibuf;
    ibuf_data_t *data;
    int ofs, len, index, i;

    if (lua_gettop(lua) < 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_ibuf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ibuf = ibuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = lua_gettop(lua) - 2;

    if (ibuf == 0 || ibuf->state != IBUF_MAPPED)
    {
        lua_pushstring(lua, "api_ibuf_set: invalid ibuf");
        lua_error(lua);
        return 0;
    }

    if (ofs < ibuf->mapped_ofs || ofs > ibuf->mapped_ofs + ibuf->mapped_len - len)
    {
        lua_pushstring(lua, "api_ibuf_set: data out of range");
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
        data[ofs - ibuf->mapped_ofs + i] = index;
    }

    lua_pop(lua, lua_gettop(lua));
    return 0;
}

static int api_ibuf_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_ibuf_left: incorrect argument");
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
        ibuf->state = IBUF_VACANT;
        ibuf->next = ibuf_get(i + 1);
        glGenBuffers(1, &ibuf->buf_id);
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(ibuf_data_t) * size,
                     0, GL_STREAM_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }

    lua_register(lua, "api_ibuf_alloc", api_ibuf_alloc);
    lua_register(lua, "api_ibuf_free", api_ibuf_free);
    lua_register(lua, "api_ibuf_set", api_ibuf_set);
    lua_register(lua, "api_ibuf_map", api_ibuf_map);
    lua_register(lua, "api_ibuf_unmap", api_ibuf_unmap);
    lua_register(lua, "api_ibuf_left", api_ibuf_left);

    return 0;
cleanup:
    util_free(g_ibufs.pool);
    g_ibufs.pool = 0;
    return 1;
}

void ibuf_done(void)
{
    int i;
    if (g_ibufs.pool == 0)
        return;
    printf("Index buffers usage: %i/%i, allocs/frees: %i/%i\n",
           g_ibufs.count - g_ibufs.left_min, g_ibufs.count,
           g_ibufs.allocs, g_ibufs.frees);
    for (i = 0; i < g_ibufs.count; ++i)
        glDeleteBuffers(1, &ibuf_get(i)->buf_id);
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
