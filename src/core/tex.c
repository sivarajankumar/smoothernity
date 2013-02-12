#include "tex.h"
#include "pbuf.h"
#include "../util/util.h"
#include <GL/gl.h>
#include <stdio.h>
#include <string.h>

static const size_t TEX_SIZE = 16;

struct tex_t
{
    GLuint tex_id;
    int vacant;
    struct tex_t *next;
};

struct texs_t
{
    int size; /* log2 */
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct tex_t *vacant;
};

static struct texs_t g_texs;

static struct tex_t * tex_get(int texi)
{
    if (texi >= 0 && texi < g_texs.count)
        return (struct tex_t*)(g_texs.pool + TEX_SIZE * texi);
    else
        return 0;
}

static int api_tex_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_tex_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_texs.left);
    return 1;
}

static int api_tex_alloc(lua_State *lua)
{
    struct tex_t *tex;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_tex_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (g_texs.vacant == 0)
    {
        lua_pushstring(lua, "api_tex_alloc: out of textures");
        lua_error(lua);
        return 0;
    }

    ++g_texs.allocs;
    --g_texs.left;
    if (g_texs.left < g_texs.left_min)
        g_texs.left_min = g_texs.left;

    tex = g_texs.vacant;
    g_texs.vacant = g_texs.vacant->next;
    tex->next = 0;
    tex->vacant = 0;

    lua_pushinteger(lua, ((char*)tex - g_texs.pool) / TEX_SIZE);    
    return 1;
}

static int api_tex_free(lua_State *lua)
{
    struct tex_t *tex;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_tex_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    tex = tex_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (tex == 0 || tex->vacant == 1)
    {
        lua_pushstring(lua, "api_tex_free: invalid texture");
        lua_error(lua);
        return 0;
    }
    
    ++g_texs.frees;
    ++g_texs.left;

    tex->vacant = 1;
    tex->next = g_texs.vacant;
    g_texs.vacant = tex;
    return 0;
}

static int api_tex_set(lua_State *lua)
{
    struct tex_t *tex;
    struct pbuf_t *pbuf;
    int ofs, mip, xofs, yofs, xsize, ysize;
    if (lua_gettop(lua) != 8 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6) || !lua_isnumber(lua, 7)
    || !lua_isnumber(lua, 8))
    {
        lua_pushstring(lua, "api_tex_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    tex = tex_get(lua_tointeger(lua, 1));
    pbuf = pbuf_get(lua_tointeger(lua, 2));
    ofs = lua_tointeger(lua, 3);
    mip = lua_tointeger(lua, 4);
    xofs = lua_tointeger(lua, 5);
    yofs = lua_tointeger(lua, 6);
    xsize = lua_tointeger(lua, 7);
    ysize = lua_tointeger(lua, 8);
    lua_pop(lua, 8);
    if (tex == 0 || pbuf == 0 || pbuf->state != PBUF_UNMAPPED)
    {
        lua_pushstring(lua, "api_tex_set: invalid object");
        lua_error(lua);
        return 0;
    }
    if (mip < 0 || mip > g_texs.size)
    {
        lua_pushstring(lua, "api_tex_set: invalid mip");
        lua_error(lua);
        return 0;
    }
    if (xsize <= 0 || xofs < 0 || xofs > (1 << g_texs.size) - xsize
    ||  ysize <= 0 || yofs < 0 || yofs > (1 << g_texs.size) - ysize)
    {
        lua_pushstring(lua, "api_tex_set: invalid xy range");
        lua_error(lua);
        return 0;
    }
    if (ofs < 0 || ofs > g_pbufs.size - xsize*ysize)
    {
        lua_pushstring(lua, "api_tex_set: invalid pbuf offset");
        lua_error(lua);
        return 0;
    }
    glBindTexture(GL_TEXTURE_2D, tex->tex_id);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER, pbuf->buf_id);
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glTexSubImage2D(GL_TEXTURE_2D, mip, xofs, yofs, xsize, ysize,
                    GL_RGBA, GL_UNSIGNED_BYTE,
                    (struct pbuf_data_t*)0 + ofs);
    return 0;
}

int tex_init(lua_State *lua, int size, int count)
{
    int i;
    struct tex_t *tex;
    if (sizeof(struct tex_t) > TEX_SIZE)
    {
        fprintf(stderr, "Invalid sizes:\nsizeof(struct tex_t) == %i\n",
                (int)sizeof(struct tex_t));
        return 1;
    }
    g_texs.pool = util_malloc(TEX_SIZE, TEX_SIZE * count);
    if (g_texs.pool == 0)
        return 1;
    memset(g_texs.pool, 0, TEX_SIZE * count);
    g_texs.size = size;
    g_texs.count = count;
    g_texs.left = count;
    g_texs.left_min = count;
    g_texs.vacant = tex_get(0);
    for (i = 0; i < count; ++i)
    {
        tex = tex_get(i);
        tex->next = tex_get(i + 1);
        tex->vacant = 1;
        glGenTextures(1, &tex->tex_id);
        glBindTexture(GL_TEXTURE_2D, tex->tex_id);
        glTexStorage2D(GL_TEXTURE_2D, size + 1, GL_RGBA8,
                       1 << size, 1 << size);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    lua_register(lua, "api_tex_left", api_tex_left);
    lua_register(lua, "api_tex_alloc", api_tex_alloc);
    lua_register(lua, "api_tex_free", api_tex_free);
    lua_register(lua, "api_tex_set", api_tex_set);
    return 0;
cleanup:
    util_free(g_texs.pool);
    g_texs.pool = 0;
    return 1;
}

void tex_done(void)
{
    int i;
    if (g_texs.pool == 0)
        return;
    printf("Textures usage: %i/%i, allocs/frees: %i/%i\n",
           g_texs.count - g_texs.left_min, g_texs.count,
           g_texs.allocs, g_texs.frees);
    for (i = 0; i < g_texs.count; ++i)
        glDeleteTextures(1, &tex_get(i)->tex_id);
    util_free(g_texs.pool);
    g_texs.pool = 0;
}
