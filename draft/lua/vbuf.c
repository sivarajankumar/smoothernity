#include "vbuf.h"
#include "scene.h"
#include <stdlib.h>

struct vbufs_t g_vbufs;

static void vbuf_free(struct vbuf_t *vbuf)
{
    vbuf->vacant = 1;
    ++g_vbufs.left;

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
    --g_vbufs.left;

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
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_vbuf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vbuf = vbuf_get(lua_tointeger(lua, -1));
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
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_vbuf_bake: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vbuf = vbuf_get(lua_tointeger(lua, -1));
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

static int api_vbuf_write(lua_State *lua)
{
    int datai;
    float x, y, z, r, g, b, a, u, v;
    struct vbuf_t *vbuf;
    struct vbuf_data_t *data;

    if (lua_gettop(lua) != 11 || !lua_isnumber(lua, -11)
    || !lua_isnumber(lua, -10) || !lua_isnumber(lua, -9)
    || !lua_isnumber(lua, -8) || !lua_isnumber(lua, -7)
    || !lua_isnumber(lua, -6) || !lua_isnumber(lua, -5)
    || !lua_isnumber(lua, -4) || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_vbuf_write: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vbuf = vbuf_get(lua_tointeger(lua, -11));
    datai = lua_tointeger(lua, -10);
    x = (float)lua_tonumber(lua, -9);
    y = (float)lua_tonumber(lua, -8);
    z = (float)lua_tonumber(lua, -7);
    r = (float)lua_tonumber(lua, -6);
    g = (float)lua_tonumber(lua, -5);
    b = (float)lua_tonumber(lua, -4);
    a = (float)lua_tonumber(lua, -3);
    u = (float)lua_tonumber(lua, -2);
    v = (float)lua_tonumber(lua, -1);
    lua_pop(lua, 11);

    if (datai < 0 || datai >= g_vbufs.size)
    {
        lua_pushstring(lua, "api_vbuf_write: data out of range");
        lua_error(lua);
        return 0;
    }

    if (vbuf == 0 || vbuf->mapped == 0)
    {
        lua_pushstring(lua, "api_vbuf_write: invalid vbuf");
        lua_error(lua);
        return 0;
    }

    if (r < 0.0f || r > 1.0f || g < 0.0f || g > 1.0f 
     || b < 0.0f || b > 1.0f || a < 0.0f || a > 1.0f)
    {
        lua_pushstring(lua, "api_vbuf_write: color out of range");
        lua_error(lua);
        return 0;
    }

    data = vbuf->mapped;
    data += datai;

    data->pos[0] = x;
    data->pos[1] = y;
    data->pos[2] = z;

    data->tex[0] = u;
    data->tex[1] = v;

    data->color[0] = (GLubyte) (r * 255.0f);
    data->color[1] = (GLubyte) (g * 255.0f);
    data->color[2] = (GLubyte) (b * 255.0f);
    data->color[3] = (GLubyte) (a * 255.0f);

    return 0;
}

static int api_vbuf_query(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_vbuf_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_vbufs.size);
    lua_pushinteger(lua, g_vbufs.left);
    return 2;
}

int vbuf_init(lua_State *lua, int size, int count)
{
    struct vbuf_data_t data;
    int i;
    g_vbufs.pool = calloc(count, sizeof(struct vbuf_t));
    if (g_vbufs.pool == 0)
        return 1;
    for (i = 0; i < count; ++i)
    {
        g_vbufs.pool[i].vacant = 1;
        if (i > 0)
            g_vbufs.pool[i].prev = g_vbufs.pool + i - 1;
        if (i < count - 1)
            g_vbufs.pool[i].next = g_vbufs.pool + i + 1;
        glGenBuffers(1, &g_vbufs.pool[i].buf_id);
        glBindBuffer(GL_ARRAY_BUFFER, g_vbufs.pool[i].buf_id);
        glBufferData(GL_ARRAY_BUFFER, sizeof(struct vbuf_data_t) * size,
                     0, GL_STATIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    g_vbufs.vacant = g_vbufs.pool;
    g_vbufs.size = size;
    g_vbufs.count = count;
    g_vbufs.left = count;
    g_vbufs.offset_pos = (char*)0 + ((char*)&data.pos - (char*)&data);
    g_vbufs.offset_tex = (char*)0 + ((char*)&data.tex - (char*)&data);
    g_vbufs.offset_color = (char*)0 + ((char*)&data.color - (char*)&data);

    lua_register(lua, "api_vbuf_alloc", api_vbuf_alloc);
    lua_register(lua, "api_vbuf_free", api_vbuf_free);
    lua_register(lua, "api_vbuf_write", api_vbuf_write);
    lua_register(lua, "api_vbuf_bake", api_vbuf_bake);
    lua_register(lua, "api_vbuf_query", api_vbuf_query);

    return 0;
cleanup:
    free(g_vbufs.pool);
    g_vbufs.pool = 0;
    return 1;
}

void vbuf_done(void)
{
    if (g_vbufs.pool)
    {
        while (g_vbufs.mapped)
            vbuf_free(g_vbufs.mapped);
        while (g_vbufs.baked)
            vbuf_free(g_vbufs.baked);
        free(g_vbufs.pool);
        g_vbufs.pool = 0;
    }
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
    glVertexPointer(3, GL_FLOAT, sizeof(struct vbuf_data_t), g_vbufs.offset_pos);
    glEnableClientState(GL_TEXTURE_COORD_ARRAY);
    glTexCoordPointer(2, GL_FLOAT, sizeof(struct vbuf_data_t), g_vbufs.offset_tex);
    glEnableClientState(GL_COLOR_ARRAY);
    glColorPointer(4, GL_UNSIGNED_BYTE, sizeof(struct vbuf_data_t), g_vbufs.offset_color);
}
