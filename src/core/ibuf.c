#include "ibuf.h"
#include "render.h"
#include "../util/util.h"
#include "../thread/thread.h"
#include <stdio.h>
#include <string.h>

static const size_t IBUF_SIZE = 64;

struct ibufs_t g_ibufs;

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
    if (len <= 0 || ofs < 0 || ofs > ibuf->size - len)
    {
        lua_pushstring(lua, "api_ibuf_map: invalid range");
        lua_error(lua);
        return 0;
    }
    thread_mutex_lock(g_ibufs.mutex);
    ibuf->mapped_ofs = ofs;
    ibuf->mapped_len = len;
    ibuf->state = IBUF_MAPPED;
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
    ibuf->mapped = glMapBufferRange(
        GL_ELEMENT_ARRAY_BUFFER,
        (GLintptr)((int)sizeof(ibuf_data_t) * ibuf->mapped_ofs),
        (GLsizeiptr)((int)sizeof(ibuf_data_t) * ibuf->mapped_len),
        GL_MAP_WRITE_BIT | GL_MAP_UNSYNCHRONIZED_BIT |
        GL_MAP_INVALIDATE_RANGE_BIT);
    thread_mutex_unlock(g_ibufs.mutex);
    if (ibuf->mapped == 0)
    {
        lua_pushstring(lua, "api_ibuf_map: mapping error");
        lua_error(lua);
        return 0;
    }
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
    thread_mutex_lock(g_ibufs.mutex);
    ibuf->mapped = 0;
    ibuf->mapped_ofs = 0;
    ibuf->mapped_len = 0;
    ibuf->state = IBUF_UNMAPPED;
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
    glUnmapBuffer(GL_ELEMENT_ARRAY_BUFFER);
    thread_mutex_unlock(g_ibufs.mutex);
    return 0;
}

static int api_ibuf_copy(lua_State *lua)
{
    struct ibuf_t *ibuf_from, *ibuf_to;
    int ofs_from, ofs_to, len;
    if (lua_gettop(lua) != 5 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5))
    {
        lua_pushstring(lua, "api_ibuf_copy: incorrect argument");
        lua_error(lua);
        return 0;
    }
    ibuf_from = ibuf_get(lua_tointeger(lua, 1));
    ibuf_to = ibuf_get(lua_tointeger(lua, 2));
    ofs_from = lua_tointeger(lua, 3);
    ofs_to = lua_tointeger(lua, 4);
    len = lua_tointeger(lua, 5);
    lua_pop(lua, 5);
    if (ibuf_from == 0 || ibuf_from->state != IBUF_UNMAPPED
    ||  ibuf_to == 0 || ibuf_to->state != IBUF_UNMAPPED)
    {
        lua_pushstring(lua, "api_ibuf_copy: invalid ibuf");
        lua_error(lua);
        return 0;
    }
    if (len <= 0 || ofs_from < 0 || ofs_from > ibuf_from->size - len
    || ofs_to < 0 || ofs_to > ibuf_to->size - len)
    {
        lua_pushstring(lua, "api_ibuf_copy: invalid range");
        lua_error(lua);
        return 0;
    }
    glBindBuffer(GL_COPY_READ_BUFFER, ibuf_from->buf_id);
    glBindBuffer(GL_COPY_WRITE_BUFFER, ibuf_to->buf_id);
    glCopyBufferSubData(GL_COPY_READ_BUFFER, GL_COPY_WRITE_BUFFER,
        (GLintptr)((int)sizeof(ibuf_data_t) * ofs_from),
        (GLintptr)((int)sizeof(ibuf_data_t) * ofs_to),
        (GLsizeiptr)((int)sizeof(ibuf_data_t) * len));
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

    thread_mutex_lock(g_ibufs.mutex);
    if (ibuf == 0 || ibuf->state != IBUF_MAPPED)
    {
        thread_mutex_unlock(g_ibufs.mutex);
        lua_pushstring(lua, "api_ibuf_set: invalid ibuf");
        lua_error(lua);
        return 0;
    }

    if (ofs < ibuf->mapped_ofs || ofs > ibuf->mapped_ofs + ibuf->mapped_len - len)
    {
        thread_mutex_unlock(g_ibufs.mutex);
        lua_pushstring(lua, "api_ibuf_set: data out of range");
        lua_error(lua);
        return 0;
    }

    data = ibuf->mapped;
    for (i = 0; i < len; ++i)
    {
        if (!lua_isnumber(lua, 3 + i))
        {
            thread_mutex_unlock(g_ibufs.mutex);
            lua_pushstring(lua, "api_ibuf_set: incorrect data type");
            lua_error(lua);
            return 0;
        }
        index = lua_tointeger(lua, 3 + i);
        data[ofs - ibuf->mapped_ofs + i] = index;
    }

    thread_mutex_unlock(g_ibufs.mutex);
    lua_pop(lua, lua_gettop(lua));
    return 0;
}

void ibuf_reg_thread(lua_State *lua)
{
    lua_register(lua, "api_ibuf_set", api_ibuf_set);
}

int ibuf_init(lua_State *lua, int *sizes, int count)
{
    int i;
    struct ibuf_t *ibuf;
    if (sizeof(struct ibuf_t) > IBUF_SIZE)
    {
        fprintf(stderr, "Invalid sizes:\nsizeof(struct ibuf_t) == %i\n",
                (int)sizeof(struct ibuf_t));
        return 1;
    }
    for (i = 0; i < count; ++i)
    {
        if ((sizes[i] & (sizes[i] - 1)) != 0)
        {
            fprintf(stderr, "Invalid sizes:\nsize == %i\n", sizes[i]);
            return 1;
        }
    }
    g_ibufs.pool = util_malloc(IBUF_SIZE, IBUF_SIZE * count);
    if (g_ibufs.pool == 0)
        return 1;
    memset(g_ibufs.pool, 0, IBUF_SIZE * count);
    g_ibufs.count = count;
    for (i = 0; i < count; ++i)
    {
        ibuf = ibuf_get(i);
        ibuf->state = IBUF_UNMAPPED;
        ibuf->size = sizes[i];
        glGenBuffers(1, &ibuf->buf_id);
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(ibuf_data_t) * ibuf->size,
                     0, GL_DYNAMIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    g_ibufs.mutex = thread_mutex_create();
    if (g_ibufs.mutex == 0)
        goto cleanup;

    lua_register(lua, "api_ibuf_set", api_ibuf_set);
    lua_register(lua, "api_ibuf_copy", api_ibuf_copy);
    lua_register(lua, "api_ibuf_map", api_ibuf_map);
    lua_register(lua, "api_ibuf_unmap", api_ibuf_unmap);

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
    for (i = 0; i < g_ibufs.count; ++i)
        glDeleteBuffers(1, &ibuf_get(i)->buf_id);
    util_free(g_ibufs.pool);
    g_ibufs.pool = 0;
    if (g_ibufs.mutex)
        thread_mutex_destroy(g_ibufs.mutex);
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
