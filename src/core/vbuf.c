#include "vbuf.h"
#include "render.h"
#include "../util/util.h"
#include "../thread/thread.h"
#include <stdio.h>
#include <string.h>

static const int VBUF_DATA_ATTRS = 9;
static const size_t VBUF_DATA_SIZE = 32;
static const size_t VBUF_SIZE = 64;

struct vbuf_data_t
{
    GLfloat pos[3];
    GLfloat tex[2];
    GLubyte color[4];
    char padding[8];
};

struct vbufs_t g_vbufs;

int vbuf_thread(void)
{
    return 0;
}

static int api_vbuf_map(lua_State *lua)
{
    struct vbuf_t *vbuf;
    int ofs, len;
    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_vbuf_map: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vbuf = vbuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = lua_tointeger(lua, 3);
    lua_pop(lua, 3);
    if (vbuf == 0 || vbuf->state != VBUF_IDLE)
    {
        lua_pushstring(lua, "api_vbuf_map: invalid vbuf");
        lua_error(lua);
        return 0;
    }
    if (len <= 0 || ofs < 0 || ofs > vbuf->size - len)
    {
        lua_pushstring(lua, "api_vbuf_map: invalid range");
        lua_error(lua);
        return 0;
    }
    thread_mutex_lock(g_vbufs.mutex);
    vbuf->mapped_ofs = ofs;
    vbuf->mapped_len = len;
    glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
    vbuf->mapped = glMapBufferRange(
        GL_ARRAY_BUFFER,
        (GLintptr)((int)VBUF_DATA_SIZE * vbuf->mapped_ofs),
        (GLsizeiptr)((int)VBUF_DATA_SIZE * vbuf->mapped_len),
        GL_MAP_WRITE_BIT | GL_MAP_UNSYNCHRONIZED_BIT |
        GL_MAP_INVALIDATE_RANGE_BIT);
    vbuf->state = VBUF_MAPPED;
    thread_mutex_unlock(g_vbufs.mutex);
    if (vbuf->mapped == 0)
    {
        lua_pushstring(lua, "api_vbuf_map: mapping error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vbuf_unmap(lua_State *lua)
{
    struct vbuf_t *vbuf;
    if (lua_gettop(lua) != 1)
    {
        lua_pushstring(lua, "api_vbuf_unmap: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vbuf = vbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (vbuf == 0 || vbuf->state != VBUF_MAPPED)
    {
        lua_pushstring(lua, "api_vbuf_unmap: invalid vbuf");
        lua_error(lua);
        return 0;
    }
    thread_mutex_lock(g_vbufs.mutex);
    vbuf->mapped = 0;
    vbuf->mapped_ofs = 0;
    vbuf->mapped_len = 0;
    vbuf->state = VBUF_IDLE;
    glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
    glUnmapBuffer(GL_ARRAY_BUFFER);
    thread_mutex_unlock(g_vbufs.mutex);
    return 0;
}

static int api_vbuf_copy(lua_State *lua)
{
    struct vbuf_t *vbuf_from, *vbuf_to;
    int ofs_from, ofs_to, len;
    if (lua_gettop(lua) != 5 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5))
    {
        lua_pushstring(lua, "api_vbuf_copy: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vbuf_from = vbuf_get(lua_tointeger(lua, 1));
    vbuf_to = vbuf_get(lua_tointeger(lua, 2));
    ofs_from = lua_tointeger(lua, 3);
    ofs_to = lua_tointeger(lua, 4);
    len = lua_tointeger(lua, 5);
    lua_pop(lua, 5);
    if (vbuf_from == 0 || vbuf_from->state != VBUF_IDLE
    ||  vbuf_to == 0 || vbuf_to->state != VBUF_IDLE)
    {
        lua_pushstring(lua, "api_vbuf_copy: invalid vbuf");
        lua_error(lua);
        return 0;
    }
    if (len <= 0 || ofs_from < 0 || ofs_from > vbuf_from->size - len
    || ofs_to < 0 || ofs_to > vbuf_to->size - len)
    {
        lua_pushstring(lua, "api_vbuf_copy: invalid range");
        lua_error(lua);
        return 0;
    }
    glBindBuffer(GL_COPY_READ_BUFFER, vbuf_from->buf_id);
    glBindBuffer(GL_COPY_WRITE_BUFFER, vbuf_to->buf_id);
    glCopyBufferSubData(GL_COPY_READ_BUFFER, GL_COPY_WRITE_BUFFER,
        (GLintptr)((int)VBUF_DATA_SIZE * ofs_from),
        (GLintptr)((int)VBUF_DATA_SIZE * ofs_to),
        (GLsizeiptr)((int)VBUF_DATA_SIZE * len));
    return 0;
}

static int api_vbuf_waiting(lua_State *lua)
{
    struct vbuf_t *vbuf;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_vbuf_waiting: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vbuf = vbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (vbuf == 0)
    {
        lua_pushstring(lua, "api_vbuf_waiting: invalid vbuf");
        lua_error(lua);
        return 0;
    }
    lua_pushboolean(lua, vbuf->state == VBUF_MAPPING
                      || vbuf->state == VBUF_UNMAPPING);
    return 1;
}

static int api_vbuf_set(lua_State *lua)
{
    int ofs, len, i, j, iofs;
    float x, y, z, r, g, b, a, u, v;
    struct vbuf_t *vbuf;
    struct vbuf_data_t *data;

    if (lua_gettop(lua) < (2 + VBUF_DATA_ATTRS) || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_vbuf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vbuf = vbuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = (lua_gettop(lua) - 2) / VBUF_DATA_ATTRS;

    thread_mutex_lock(g_vbufs.mutex);
    if (vbuf == 0 || vbuf->state != VBUF_MAPPED)
    {
        thread_mutex_unlock(g_vbufs.mutex);
        lua_pushstring(lua, "api_vbuf_set: invalid vbuf");
        lua_error(lua);
        return 0;
    }

    if (ofs < vbuf->mapped_ofs || ofs > vbuf->mapped_ofs + vbuf->mapped_len - len)
    {
        thread_mutex_unlock(g_vbufs.mutex);
        lua_pushstring(lua, "api_vbuf_set: data out of range");
        lua_error(lua);
        return 0;
    }

    if ((lua_gettop(lua) - 2) % VBUF_DATA_ATTRS != 0)
    {
        thread_mutex_unlock(g_vbufs.mutex);
        lua_pushstring(lua, "api_vbuf_set: incorrect data count");
        lua_error(lua);
        return 0;
    }

    for (i = 0; i < len; ++i)
    {
        iofs = 3 + (i * VBUF_DATA_ATTRS);
        for (j = 0; j < VBUF_DATA_ATTRS; ++j)
        {
            if (!lua_isnumber(lua, iofs + j))
            {
                thread_mutex_unlock(g_vbufs.mutex);
                lua_pushstring(lua, "api_vbuf_set: incorrect data type");
                lua_error(lua);
                return 0;
            }
        }
        x = (float)lua_tonumber(lua, iofs);
        y = (float)lua_tonumber(lua, iofs + 1);
        z = (float)lua_tonumber(lua, iofs + 2);
        r = (float)lua_tonumber(lua, iofs + 3);
        g = (float)lua_tonumber(lua, iofs + 4);
        b = (float)lua_tonumber(lua, iofs + 5);
        a = (float)lua_tonumber(lua, iofs + 6);
        u = (float)lua_tonumber(lua, iofs + 7);
        v = (float)lua_tonumber(lua, iofs + 8);

        if (r < 0.0f || r > 1.0f || g < 0.0f || g > 1.0f 
         || b < 0.0f || b > 1.0f || a < 0.0f || a > 1.0f)
        {
            thread_mutex_unlock(g_vbufs.mutex);
            lua_pushstring(lua, "api_vbuf_set: color out of range");
            lua_error(lua);
            return 0;
        }

        data = vbuf->mapped;
        data += ofs - vbuf->mapped_ofs + i;

        data->pos[0] = x;
        data->pos[1] = y;
        data->pos[2] = z;

        data->tex[0] = u;
        data->tex[1] = v;

        data->color[0] = (GLubyte) (r * 255.0f);
        data->color[1] = (GLubyte) (g * 255.0f);
        data->color[2] = (GLubyte) (b * 255.0f);
        data->color[3] = (GLubyte) (a * 255.0f);
    }

    thread_mutex_unlock(g_vbufs.mutex);
    lua_pop(lua, 3 + (len * VBUF_DATA_ATTRS));
    return 0;
}

void vbuf_reg_thread(lua_State *lua)
{
    lua_register(lua, "api_vbuf_set", api_vbuf_set);
}

int vbuf_init(lua_State *lua, int *sizes, int count)
{
    struct vbuf_data_t data;
    struct vbuf_t *vbuf;
    int i;
    if (sizeof(struct vbuf_t) > VBUF_SIZE
    ||  sizeof(struct vbuf_data_t) != VBUF_DATA_SIZE)
    {
        fprintf(stderr, "Invalid sizes:\n"
                        "sizeof(struct vbuf_t) == %i\n"
                        "sizeof(struct vbuf_data_t) == %i\n",
                (int)sizeof(struct vbuf_t),
                (int)sizeof(struct vbuf_data_t));
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
    g_vbufs.pool = util_malloc(VBUF_SIZE, VBUF_SIZE * count);
    if (g_vbufs.pool == 0)
        return 1;
    memset(g_vbufs.pool, 0, VBUF_SIZE * count);
    g_vbufs.count = count;
    g_vbufs.offset_pos = (char*)0 + ((char*)&data.pos - (char*)&data);
    g_vbufs.offset_tex = (char*)0 + ((char*)&data.tex - (char*)&data);
    g_vbufs.offset_color = (char*)0 + ((char*)&data.color - (char*)&data);
    for (i = 0; i < count; ++i)
    {
        vbuf = vbuf_get(i);
        vbuf->size = sizes[i];
        vbuf->state = VBUF_IDLE;
        glGenBuffers(1, &vbuf->buf_id);
        glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
        glBufferData(GL_ARRAY_BUFFER, VBUF_DATA_SIZE * vbuf->size,
                     0, GL_DYNAMIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    g_vbufs.mutex = thread_mutex_create();
    if (g_vbufs.mutex == 0)
        goto cleanup;

    lua_register(lua, "api_vbuf_set", api_vbuf_set);
    lua_register(lua, "api_vbuf_copy", api_vbuf_copy);
    lua_register(lua, "api_vbuf_map", api_vbuf_map);
    lua_register(lua, "api_vbuf_unmap", api_vbuf_unmap);
    lua_register(lua, "api_vbuf_waiting", api_vbuf_waiting);

    return 0;
cleanup:
    util_free(g_vbufs.pool);
    g_vbufs.pool = 0;
    return 1;
}

void vbuf_done(void)
{
    int i;
    if (g_vbufs.pool == 0)
        return;
    for (i = 0; i < g_vbufs.count; ++i)
        glDeleteBuffers(1, &vbuf_get(i)->buf_id);
    util_free(g_vbufs.pool);
    g_vbufs.pool = 0;
    if (g_vbufs.mutex)
        thread_mutex_destroy(g_vbufs.mutex);
}

struct vbuf_t * vbuf_get(int vbufi)
{
    if (vbufi >= 0 && vbufi < g_vbufs.count)
        return (struct vbuf_t*)(g_vbufs.pool + VBUF_SIZE * vbufi);
    else
        return 0;
}

void vbuf_select(struct vbuf_t * vbuf)
{
    glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, VBUF_DATA_SIZE, g_vbufs.offset_pos);
    glEnableClientState(GL_TEXTURE_COORD_ARRAY);
    glTexCoordPointer(2, GL_FLOAT, VBUF_DATA_SIZE, g_vbufs.offset_tex);
    glEnableClientState(GL_COLOR_ARRAY);
    glColorPointer(4, GL_UNSIGNED_BYTE, VBUF_DATA_SIZE, g_vbufs.offset_color);
}
