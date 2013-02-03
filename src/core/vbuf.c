#include "vbuf.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

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

static void vbuf_free(struct vbuf_t *vbuf)
{
    vbuf->vacant = 1;
    ++g_vbufs.left;
    ++g_vbufs.frees;

    if (vbuf->mapped)
    {
        glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
        glUnmapBuffer(GL_ARRAY_BUFFER);
        vbuf->mapped = 0;
        if (vbuf == g_vbufs.mapped)
            g_vbufs.mapped = vbuf->next;
    }
    else if (vbuf == g_vbufs.baked)
        g_vbufs.baked = vbuf->next;

    if (vbuf->prev)
        vbuf->prev->next = vbuf->next;
    if (vbuf->next)
        vbuf->next->prev = vbuf->prev;

    if (g_vbufs.vacant)
        g_vbufs.vacant->prev = vbuf;
    vbuf->prev = 0;
    vbuf->next = g_vbufs.vacant;
    g_vbufs.vacant = vbuf;
}

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
    vbuf->vacant = 0;
    g_vbufs.vacant = vbuf->next;
    ++g_vbufs.allocs;
    --g_vbufs.left;
    if (g_vbufs.left < g_vbufs.left_min)
        g_vbufs.left_min = g_vbufs.left;

    glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
    vbuf->mapped = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY);

    if (vbuf->prev)
        vbuf->prev->next = vbuf->next;
    if (vbuf->next)
        vbuf->next->prev = vbuf->prev;

    if (g_vbufs.mapped)
        g_vbufs.mapped->prev = vbuf;
    vbuf->prev = 0;
    vbuf->next = g_vbufs.mapped;
    g_vbufs.mapped = vbuf;

    lua_pushinteger(lua, vbuf - g_vbufs.pool);
    return 1;
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

    if (vbuf == 0 || vbuf->vacant == 1)
    {
        lua_pushstring(lua, "api_vbuf_free: invalid vbuf");
        lua_error(lua);
        return 0;
    }

    vbuf_free(vbuf);
    return 0;
}

static int api_vbuf_bake(lua_State *lua)
{
    struct vbuf_t *vbuf;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_vbuf_bake: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vbuf = vbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (vbuf == 0 || vbuf->mapped == 0)
    {
        lua_pushstring(lua, "api_vbuf_bake: invalid vbuf");
        lua_error(lua);
        return 0;
    }

    glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
    glUnmapBuffer(GL_ARRAY_BUFFER);
    vbuf->mapped = 0;

    if (g_vbufs.mapped == vbuf)
        g_vbufs.mapped = vbuf->next;

    if (vbuf->prev)
        vbuf->prev->next = vbuf->next;
    if (vbuf->next)
        vbuf->next->prev = vbuf->prev;

    if (g_vbufs.baked)
        g_vbufs.baked->prev = vbuf;
    vbuf->prev = 0;
    vbuf->next = g_vbufs.baked;
    g_vbufs.baked = vbuf;
    return 0;
}

static int api_vbuf_set(lua_State *lua)
{
    int start, len, i, j, ofs;
    float x, y, z, r, g, b, a, u, v;
    struct vbuf_t *vbuf;
    struct vbuf_data_t *data;

    if (lua_gettop(lua) < 11 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_vbuf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vbuf = vbuf_get(lua_tointeger(lua, 1));
    start = lua_tointeger(lua, 2);
    len = (lua_gettop(lua) - 2) / 9;

    if (vbuf == 0 || vbuf->mapped == 0)
    {
        lua_pushstring(lua, "api_vbuf_set: invalid vbuf");
        lua_error(lua);
        return 0;
    }

    if (start < 0 || start >= g_vbufs.size - len)
    {
        lua_pushstring(lua, "api_vbuf_set: data out of range");
        lua_error(lua);
        return 0;
    }

    if ((lua_gettop(lua) - 2) % 9 != 0)
    {
        lua_pushstring(lua, "api_vbuf_set: incorrect data count");
        lua_error(lua);
        return 0;
    }

    for (i = 0; i < len; ++i)
    {
        ofs = 3 + (i * 9);
        for (j = 0; j < 9; ++j)
        {
            if (!lua_isnumber(lua, ofs + j))
            {
                lua_pushstring(lua, "api_vbuf_set: incorrect data type");
                lua_error(lua);
                return 0;
            }
        }
        x = (float)lua_tonumber(lua, ofs);
        y = (float)lua_tonumber(lua, ofs + 1);
        z = (float)lua_tonumber(lua, ofs + 2);
        r = (float)lua_tonumber(lua, ofs + 3);
        g = (float)lua_tonumber(lua, ofs + 4);
        b = (float)lua_tonumber(lua, ofs + 5);
        a = (float)lua_tonumber(lua, ofs + 6);
        u = (float)lua_tonumber(lua, ofs + 7);
        v = (float)lua_tonumber(lua, ofs + 8);

        if (r < 0.0f || r > 1.0f || g < 0.0f || g > 1.0f 
         || b < 0.0f || b > 1.0f || a < 0.0f || a > 1.0f)
        {
            lua_pushstring(lua, "api_vbuf_set: color out of range");
            lua_error(lua);
            return 0;
        }

        data = vbuf->mapped;
        data += start + i;

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

    lua_pop(lua, 3 + (len * 9));
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
    int i;
    if (sizeof(struct vbuf_t) != VBUF_SIZE
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
    g_vbufs.pool = aligned_alloc(VBUF_SIZE, VBUF_SIZE * count);
    if (g_vbufs.pool == 0)
        return 1;
    memset(g_vbufs.pool, 0, VBUF_SIZE * count);
    for (i = 0; i < count; ++i)
    {
        g_vbufs.pool[i].vacant = 1;
        if (i > 0)
            g_vbufs.pool[i].prev = g_vbufs.pool + i - 1;
        if (i < count - 1)
            g_vbufs.pool[i].next = g_vbufs.pool + i + 1;
        glGenBuffers(1, &g_vbufs.pool[i].buf_id);
        glBindBuffer(GL_ARRAY_BUFFER, g_vbufs.pool[i].buf_id);
        glBufferData(GL_ARRAY_BUFFER, VBUF_DATA_SIZE * size,
                     0, GL_STATIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    g_vbufs.vacant = g_vbufs.pool;
    g_vbufs.size = size;
    g_vbufs.count = count;
    g_vbufs.left = count;
    g_vbufs.left_min = count;
    g_vbufs.offset_pos = (char*)0 + ((char*)&data.pos - (char*)&data);
    g_vbufs.offset_tex = (char*)0 + ((char*)&data.tex - (char*)&data);
    g_vbufs.offset_color = (char*)0 + ((char*)&data.color - (char*)&data);

    lua_register(lua, "api_vbuf_alloc", api_vbuf_alloc);
    lua_register(lua, "api_vbuf_free", api_vbuf_free);
    lua_register(lua, "api_vbuf_set", api_vbuf_set);
    lua_register(lua, "api_vbuf_bake", api_vbuf_bake);
    lua_register(lua, "api_vbuf_left", api_vbuf_left);

    return 0;
cleanup:
    free(g_vbufs.pool);
    g_vbufs.pool = 0;
    return 1;
}

void vbuf_done(void)
{
    if (g_vbufs.pool == 0)
        return;
    printf("Vertex buffers usage: %i/%i, allocs/frees: %i/%i\n",
           g_vbufs.count - g_vbufs.left_min, g_vbufs.count,
           g_vbufs.allocs, g_vbufs.frees);
    while (g_vbufs.mapped)
        vbuf_free(g_vbufs.mapped);
    while (g_vbufs.baked)
        vbuf_free(g_vbufs.baked);
    free(g_vbufs.pool);
    g_vbufs.pool = 0;
}

struct vbuf_t * vbuf_get(int vbufi)
{
    if (vbufi >= 0 && vbufi < g_vbufs.count)
        return g_vbufs.pool + vbufi;
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
