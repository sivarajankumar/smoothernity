#include "vbuf.h"
#include "../util/util.h"
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

static int api_vbuf_alloc(lua_State *lua)
{
    struct vbuf_t *vbuf;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_vbuf_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    if (g_vbufs.vacant == 0)
    {
        lua_pushstring(lua, "api_vbuf_alloc: out of vbufs");
        lua_error(lua);
        return 0;
    }

    vbuf = g_vbufs.vacant;
    g_vbufs.vacant = g_vbufs.vacant->next;

    ++g_vbufs.allocs;
    --g_vbufs.left;
    if (g_vbufs.left < g_vbufs.left_min)
        g_vbufs.left_min = g_vbufs.left;

    vbuf->state = VBUF_UNMAPPED;
    vbuf->next = 0;

    lua_pushinteger(lua, ((char*)vbuf - g_vbufs.pool) / VBUF_SIZE);
    return 1;
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
    if (vbuf == 0 || vbuf->state != VBUF_UNMAPPED)
    {
        lua_pushstring(lua, "api_vbuf_map: invalid vbuf");
        lua_error(lua);
        return 0;
    }
    if (len <= 0 || ofs < 0 || ofs > g_vbufs.size - len)
    {
        lua_pushstring(lua, "api_vbuf_map: invalid range");
        lua_error(lua);
        return 0;
    }
    glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
    vbuf->mapped = glMapBufferRange(GL_ARRAY_BUFFER,
                                    (GLintptr)(ofs * (int)VBUF_DATA_SIZE),
                                    (GLsizeiptr)(len * (int)VBUF_DATA_SIZE),
                                    GL_MAP_WRITE_BIT | GL_MAP_UNSYNCHRONIZED_BIT |
                                    GL_MAP_INVALIDATE_RANGE_BIT);
    if (vbuf->mapped == 0)
    {
        lua_pushstring(lua, "api_vbuf_map: mapping error");
        lua_error(lua);
        return 0;
    }
    vbuf->mapped_ofs = ofs;
    vbuf->mapped_len = len;
    vbuf->state = VBUF_MAPPED;
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
    glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
    glUnmapBuffer(GL_ARRAY_BUFFER);
    vbuf->mapped = 0;
    vbuf->mapped_ofs = 0;
    vbuf->mapped_len = 0;
    vbuf->state = VBUF_UNMAPPED;
    return 0;
}

static int api_vbuf_free(lua_State *lua)
{
    struct vbuf_t *vbuf;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_vbuf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vbuf = vbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (vbuf == 0 || vbuf->state != VBUF_UNMAPPED)
    {
        lua_pushstring(lua, "api_vbuf_free: invalid vbuf");
        lua_error(lua);
        return 0;
    }

    ++g_vbufs.left;
    ++g_vbufs.frees;

    vbuf->next = g_vbufs.vacant;
    g_vbufs.vacant = vbuf;
    vbuf->state = VBUF_VACANT;
    return 0;
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

    if (vbuf == 0 || vbuf->state != VBUF_MAPPED)
    {
        lua_pushstring(lua, "api_vbuf_set: invalid vbuf");
        lua_error(lua);
        return 0;
    }

    if (ofs < vbuf->mapped_ofs || ofs > vbuf->mapped_ofs + vbuf->mapped_len - len)
    {
        lua_pushstring(lua, "api_vbuf_set: data out of range");
        lua_error(lua);
        return 0;
    }

    if ((lua_gettop(lua) - 2) % VBUF_DATA_ATTRS != 0)
    {
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

    lua_pop(lua, 3 + (len * VBUF_DATA_ATTRS));
    return 0;
}

static int api_vbuf_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_vbuf_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_vbufs.left);
    return 1;
}

int vbuf_init(lua_State *lua, int size, int count)
{
    struct vbuf_data_t data;
    struct vbuf_t *vbuf;
    int i;
    if (sizeof(struct vbuf_t) > VBUF_SIZE
    ||  sizeof(struct vbuf_data_t) != VBUF_DATA_SIZE
    ||  (size & (size - 1)) != 0)
    {
        fprintf(stderr, "Invalid sizes:\n"
                        "sizeof(struct vbuf_t) == %i\n"
                        "sizeof(struct vbuf_data_t) == %i\n"
                        "size == %i\n",
                (int)sizeof(struct vbuf_t),
                (int)sizeof(struct vbuf_data_t),
                size);
        return 1;
    }
    g_vbufs.pool = util_malloc(VBUF_SIZE, VBUF_SIZE * count);
    if (g_vbufs.pool == 0)
        return 1;
    memset(g_vbufs.pool, 0, VBUF_SIZE * count);
    g_vbufs.size = size;
    g_vbufs.count = count;
    g_vbufs.left = count;
    g_vbufs.left_min = count;
    g_vbufs.offset_pos = (char*)0 + ((char*)&data.pos - (char*)&data);
    g_vbufs.offset_tex = (char*)0 + ((char*)&data.tex - (char*)&data);
    g_vbufs.offset_color = (char*)0 + ((char*)&data.color - (char*)&data);
    g_vbufs.vacant = vbuf_get(0);
    for (i = 0; i < count; ++i)
    {
        vbuf = vbuf_get(i);
        vbuf->state = VBUF_VACANT;
        vbuf->next = vbuf_get(i + 1);
        glGenBuffers(1, &vbuf->buf_id);
        glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
        glBufferData(GL_ARRAY_BUFFER, VBUF_DATA_SIZE * size,
                     0, GL_DYNAMIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }

    lua_register(lua, "api_vbuf_alloc", api_vbuf_alloc);
    lua_register(lua, "api_vbuf_free", api_vbuf_free);
    lua_register(lua, "api_vbuf_set", api_vbuf_set);
    lua_register(lua, "api_vbuf_map", api_vbuf_map);
    lua_register(lua, "api_vbuf_unmap", api_vbuf_unmap);
    lua_register(lua, "api_vbuf_left", api_vbuf_left);

    return 0;
cleanup:
    util_free(g_vbufs.pool);
    g_vbufs.pool = 0;
    return 1;
}

void vbuf_done(void)
{
    int i;
    struct vbuf_t *vbuf;
    if (g_vbufs.pool == 0)
        return;
    printf("Vertex buffers usage: %i/%i, allocs/frees: %i/%i\n",
           g_vbufs.count - g_vbufs.left_min, g_vbufs.count,
           g_vbufs.allocs, g_vbufs.frees);
    for (i = 0; i < g_vbufs.count; ++i)
    {
        vbuf = vbuf_get(i);
        glDeleteBuffers(1, &vbuf->buf_id);
    }
    util_free(g_vbufs.pool);
    g_vbufs.pool = 0;
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
