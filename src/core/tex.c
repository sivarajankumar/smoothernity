#include "tex.h"
#include "pbuf.h"
#include "../util/util.h"
#include <GL/glew.h>
#include <stdio.h>
#include <string.h>

static const size_t TEX_SIZE = 16;

struct tex_init_t
{
    int size;
    int layers;
};

struct tex_t
{
    GLuint tex_id;
    int size; /* log2 */
    int layers;
};

struct texs_t
{
    int count;
    char *pool;
};

static struct texs_t g_texs;

static struct tex_t * tex_get(int texi)
{
    if (texi >= 0 && texi < g_texs.count)
        return (struct tex_t*)(g_texs.pool + TEX_SIZE * texi);
    else
        return 0;
}

static int api_tex_set(lua_State *lua)
{
    struct tex_t *tex;
    struct pbuf_t *pbuf;
    int texi, ofs, layer, mip, xofs, yofs, xsize, ysize;
    if (lua_gettop(lua) != 9 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6) || !lua_isnumber(lua, 7)
    || !lua_isnumber(lua, 8) || !lua_isnumber(lua, 9))
    {
        lua_pushstring(lua, "api_tex_set: incorrect argument");
        lua_error(lua);
        return 0;
    }
    texi = lua_tointeger(lua, 1);
    pbuf = pbuf_get(lua_tointeger(lua, 2));
    ofs = lua_tointeger(lua, 3);
    layer = lua_tointeger(lua, 4);
    mip = lua_tointeger(lua, 5);
    xofs = lua_tointeger(lua, 6);
    yofs = lua_tointeger(lua, 7);
    xsize = lua_tointeger(lua, 8);
    ysize = lua_tointeger(lua, 9);
    lua_pop(lua, 9);
    tex = tex_get(texi);
    if (tex == 0 || pbuf == 0 || pbuf->state != PBUF_UNMAPPED)
    {
        lua_pushstring(lua, "api_tex_set: invalid object");
        lua_error(lua);
        return 0;
    }
    if (mip < 0 || mip > tex->size)
    {
        lua_pushstring(lua, "api_tex_set: invalid mip");
        lua_error(lua);
        return 0;
    }
    if (layer < 0 || layer >= tex->layers)
    {
        lua_pushstring(lua, "api_tex_set: invalid layer");
        lua_error(lua);
        return 0;
    }
    if (xsize <= 0 || xofs < 0 || xofs > (1 << tex->size) - xsize
    ||  ysize <= 0 || yofs < 0 || yofs > (1 << tex->size) - ysize)
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
    glActiveTexture(GL_TEXTURE0 + texi);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER, pbuf->buf_id);
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glTexSubImage3D(GL_TEXTURE_2D_ARRAY, mip, xofs, yofs, layer,
                    xsize, ysize, 1, GL_RGBA, GL_UNSIGNED_BYTE,
                    (struct pbuf_data_t*)0 + ofs);
    return 0;
}

static int api_tex_wrap(lua_State *lua)
{
    struct tex_t *tex;
    int texi, wrap;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_tex_wrap: incorrect argument");
        lua_error(lua);
        return 0;
    }
    texi = lua_tointeger(lua, 1);
    wrap = lua_tointeger(lua, 2);
    lua_pop(lua, 2);
    tex = tex_get(texi);
    if (tex == 0)
    {
        lua_pushstring(lua, "api_tex_wrap: invalid texture");
        lua_error(lua);
        return 0;
    }
    glActiveTexture(GL_TEXTURE0 + texi);
    glBindTexture(GL_TEXTURE_2D_ARRAY, tex->tex_id);
    glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_WRAP_S, wrap);
    glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_WRAP_T, wrap);
    glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_WRAP_R, wrap);
    if (glGetError() != GL_NO_ERROR)
    {
        lua_pushstring(lua, "api_tex_wrap: gl error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

int tex_init(lua_State *lua, int *sizes, int len)
{
    int i;
    struct tex_t *tex;
    struct tex_init_t *tinit;
    GLint max_units;
    if (sizeof(struct tex_t) > TEX_SIZE || len % 2 != 0)
    {
        fprintf(stderr, "Invalid sizes:\nsizeof(struct tex_t) == %i\nlen = %i\n",
                (int)sizeof(struct tex_t), len);
        return 1;
    }
    g_texs.count = len / 2;
    g_texs.pool = util_malloc(TEX_SIZE, TEX_SIZE * g_texs.count);
    if (g_texs.pool == 0)
        return 1;
    memset(g_texs.pool, 0, TEX_SIZE * g_texs.count);
    for (i = 0; i < g_texs.count; ++i)
    {
        tinit = (struct tex_init_t*)sizes + i;
        tex = tex_get(i);
        tex->size = tinit->size;
        tex->layers = tinit->layers;
        glGenTextures(1, &tex->tex_id);
        glActiveTexture(GL_TEXTURE0 + i);
        glBindTexture(GL_TEXTURE_2D_ARRAY, tex->tex_id);
        glTexStorage3D(GL_TEXTURE_2D_ARRAY, tex->size + 1, GL_RGBA8,
                       1 << tex->size, 1 << tex->size, tex->layers);
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MIN_FILTER,
                        GL_LINEAR_MIPMAP_LINEAR);
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    lua_register(lua, "api_tex_set", api_tex_set);
    lua_register(lua, "api_tex_wrap", api_tex_wrap);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, y);

    glGetIntegerv(GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS, &max_units);
    LUA_PUBLISH(max_units, "API_TEX_MAX_UNITS");
    LUA_PUBLISH(GL_CLAMP_TO_EDGE, "API_TEX_WRAP_EDGE");
    LUA_PUBLISH(GL_REPEAT, "API_TEX_WRAP_REPEAT");
    LUA_PUBLISH(GL_MIRRORED_REPEAT, "API_TEX_MIRRORED_REPEAT");
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
    for (i = 0; i < g_texs.count; ++i)
        glDeleteTextures(1, &tex_get(i)->tex_id);
    util_free(g_texs.pool);
    g_texs.pool = 0;
}
