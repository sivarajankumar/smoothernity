#include "pbuf.h"
#include "render.h"
#include "../util/util.h"
#include "../thread/thread.h"
#include <stdio.h>
#include <string.h>

static const int PBUF_DATA_ATTRS = 4;
static const size_t PBUF_DATA_SIZE = 4;
static const size_t PBUF_SIZE = 64;

struct pbufs_t
{
    int count;
    char *pool;
    struct thread_mutex_t *mutex;
};

struct pbufs_t g_pbufs;

int pbuf_thread(void)
{
    int i, count;
    struct pbuf_t *pbuf;
    count = 0;
    thread_mutex_lock(g_pbufs.mutex);
    for (i = 0; i < g_pbufs.count; ++i)
    {
        pbuf = pbuf_get(i);
        if (pbuf->state == PBUF_MAPPING)
        {
            thread_mutex_unlock(g_pbufs.mutex);
            ++count;
            glBindBuffer(GL_PIXEL_UNPACK_BUFFER, pbuf->buf_id);
            pbuf->mapped = glMapBufferRange(
                GL_PIXEL_UNPACK_BUFFER,
                (GLintptr)((struct pbuf_data_t*)0 + pbuf->mapped_ofs),
                (GLsizeiptr)((struct pbuf_data_t*)0 + pbuf->mapped_len),
                GL_MAP_WRITE_BIT | GL_MAP_UNSYNCHRONIZED_BIT |
                GL_MAP_INVALIDATE_RANGE_BIT);
            thread_mutex_lock(g_pbufs.mutex);
            if (pbuf->mapped == 0)
            {
                fprintf(stderr, "pbuf_thread: mapping error\n");
                pbuf->state = PBUF_ERROR;
            }
            else
                pbuf->state = PBUF_MAPPED;
        }
        else if (pbuf->state == PBUF_UNMAPPING)
        {
            thread_mutex_unlock(g_pbufs.mutex);
            ++count;
            glBindBuffer(GL_PIXEL_UNPACK_BUFFER, pbuf->buf_id);
            glUnmapBuffer(GL_PIXEL_UNPACK_BUFFER);
            thread_mutex_lock(g_pbufs.mutex);
            pbuf->state = PBUF_UNMAPPED;
        }
    }
    thread_mutex_unlock(g_pbufs.mutex);
    return count;
}

struct pbuf_t * pbuf_get(int pbufi)
{
    if (pbufi >= 0 && pbufi < g_pbufs.count)
        return (struct pbuf_t*)(g_pbufs.pool + PBUF_SIZE * pbufi);
    else
        return 0;
}

static int api_pbuf_map(lua_State *lua)
{
    struct pbuf_t *pbuf;
    int ofs, len;
    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_pbuf_map: incorrect argument");
        lua_error(lua);
        return 0;
    }
    pbuf = pbuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = lua_tointeger(lua, 3);
    lua_pop(lua, 3);
    if (pbuf == 0 || pbuf->state != PBUF_UNMAPPED)
    {
        lua_pushstring(lua, "api_pbuf_map: invalid pbuf");
        lua_error(lua);
        return 0;
    }
    if (len <= 0 || ofs < 0 || ofs > pbuf->size - len)
    {
        lua_pushstring(lua, "api_pbuf_map: invalid range");
        lua_error(lua);
        return 0;
    }
    thread_mutex_lock(g_pbufs.mutex);
    pbuf->mapped_ofs = ofs;
    pbuf->mapped_len = len;
    pbuf->state = PBUF_MAPPING;
    thread_mutex_unlock(g_pbufs.mutex);
    render_engage();
    return 0;
}

static int api_pbuf_unmap(lua_State *lua)
{
    struct pbuf_t *pbuf;
    if (lua_gettop(lua) != 1)
    {
        lua_pushstring(lua, "api_pbuf_unmap: incorrect argument");
        lua_error(lua);
        return 0;
    }
    pbuf = pbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (pbuf == 0 || pbuf->state != PBUF_MAPPED)
    {
        lua_pushstring(lua, "api_pbuf_unmap: invalid pbuf");
        lua_error(lua);
        return 0;
    }
    thread_mutex_lock(g_pbufs.mutex);
    pbuf->mapped = 0;
    pbuf->mapped_ofs = 0;
    pbuf->mapped_len = 0;
    pbuf->state = PBUF_UNMAPPING;
    thread_mutex_unlock(g_pbufs.mutex);
    render_engage();
    return 0;
}

static int api_pbuf_waiting(lua_State *lua)
{
    struct pbuf_t *pbuf;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_pbuf_waiting: incorrect argument");
        lua_error(lua);
        return 0;
    }
    pbuf = pbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (pbuf == 0)
    {
        lua_pushstring(lua, "api_pbuf_waiting: invalid pbuf");
        lua_error(lua);
        return 0;
    }
    lua_pushboolean(lua, pbuf->state == PBUF_MAPPING
                      || pbuf->state == PBUF_UNMAPPING);
    return 1;
}

static int api_pbuf_set(lua_State *lua)
{
    int ofs, len, i, j, iofs;
    float r, g, b, a;
    struct pbuf_t *pbuf;
    struct pbuf_data_t *data;

    if (lua_gettop(lua) < (2 + PBUF_DATA_ATTRS) || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_pbuf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }

    pbuf = pbuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = (lua_gettop(lua) - 2) / PBUF_DATA_ATTRS;

    thread_mutex_lock(g_pbufs.mutex);
    if (pbuf == 0 || pbuf->state != PBUF_MAPPED)
    {
        thread_mutex_unlock(g_pbufs.mutex);
        lua_pushstring(lua, "api_pbuf_set: invalid pbuf");
        lua_error(lua);
        return 0;
    }

    if (ofs < pbuf->mapped_ofs || ofs > pbuf->mapped_ofs + pbuf->mapped_len - len)
    {
        thread_mutex_unlock(g_pbufs.mutex);
        lua_pushstring(lua, "api_pbuf_set: data out of range");
        lua_error(lua);
        return 0;
    }

    if ((lua_gettop(lua) - 2) % PBUF_DATA_ATTRS != 0)
    {
        thread_mutex_unlock(g_pbufs.mutex);
        lua_pushstring(lua, "api_pbuf_set: incorrect data count");
        lua_error(lua);
        return 0;
    }

    for (i = 0; i < len; ++i)
    {
        iofs = 3 + (i * PBUF_DATA_ATTRS);
        for (j = 0; j < PBUF_DATA_ATTRS; ++j)
        {
            if (!lua_isnumber(lua, iofs + j))
            {
                thread_mutex_unlock(g_pbufs.mutex);
                lua_pushstring(lua, "api_pbuf_set: incorrect data type");
                lua_error(lua);
                return 0;
            }
        }
        r = (float)lua_tonumber(lua, iofs);
        g = (float)lua_tonumber(lua, iofs + 1);
        b = (float)lua_tonumber(lua, iofs + 2);
        a = (float)lua_tonumber(lua, iofs + 3);

        if (r < 0.0f || r > 1.0f || g < 0.0f || g > 1.0f 
         || b < 0.0f || b > 1.0f || a < 0.0f || a > 1.0f)
        {
            thread_mutex_unlock(g_pbufs.mutex);
            lua_pushstring(lua, "api_pbuf_set: color out of range");
            lua_error(lua);
            return 0;
        }

        data = pbuf->mapped;
        data += ofs - pbuf->mapped_ofs + i;

        data->color[0] = (GLubyte) (r * 255.0f);
        data->color[1] = (GLubyte) (g * 255.0f);
        data->color[2] = (GLubyte) (b * 255.0f);
        data->color[3] = (GLubyte) (a * 255.0f);
    }

    thread_mutex_unlock(g_pbufs.mutex);
    lua_pop(lua, 3 + (len * PBUF_DATA_ATTRS));
    return 0;
}

void pbuf_reg_thread(lua_State *lua)
{
    lua_register(lua, "api_pbuf_set", api_pbuf_set);
}

int pbuf_init(lua_State *lua, int *sizes, int count)
{
    struct pbuf_t *pbuf;
    int i;
    if (sizeof(struct pbuf_t) > PBUF_SIZE
    ||  sizeof(struct pbuf_data_t) != PBUF_DATA_SIZE)
    {
        fprintf(stderr, "Invalid sizes:\n"
                        "sizeof(struct pbuf_t) == %i\n"
                        "sizeof(struct pbuf_data_t) == %i\n",
                (int)sizeof(struct pbuf_t),
                (int)sizeof(struct pbuf_data_t));
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
    g_pbufs.pool = util_malloc(PBUF_SIZE, PBUF_SIZE * count);
    if (g_pbufs.pool == 0)
        return 1;
    memset(g_pbufs.pool, 0, PBUF_SIZE * count);
    g_pbufs.count = count;
    for (i = 0; i < count; ++i)
    {
        pbuf = pbuf_get(i);
        pbuf->state = PBUF_UNMAPPED;
        pbuf->size = sizes[i];
        glGenBuffers(1, &pbuf->buf_id);
        glBindBuffer(GL_PIXEL_UNPACK_BUFFER, pbuf->buf_id);
        glBufferData(GL_PIXEL_UNPACK_BUFFER, PBUF_DATA_SIZE * pbuf->size,
                     0, GL_DYNAMIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    g_pbufs.mutex = thread_mutex_create();
    if (g_pbufs.mutex == 0)
        goto cleanup;

    lua_register(lua, "api_pbuf_set", api_pbuf_set);
    lua_register(lua, "api_pbuf_map", api_pbuf_map);
    lua_register(lua, "api_pbuf_unmap", api_pbuf_unmap);
    lua_register(lua, "api_pbuf_waiting", api_pbuf_waiting);

    return 0;
cleanup:
    util_free(g_pbufs.pool);
    g_pbufs.pool = 0;
    return 1;
}

void pbuf_done(void)
{
    int i;
    if (g_pbufs.pool == 0)
        return;
    for (i = 0; i < g_pbufs.count; ++i)
        glDeleteBuffers(1, &pbuf_get(i)->buf_id);
    util_free(g_pbufs.pool);
    g_pbufs.pool = 0;
    if (g_pbufs.mutex)
        thread_mutex_destroy(g_pbufs.mutex);
}
