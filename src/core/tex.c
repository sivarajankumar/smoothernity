#include "tex.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>

static const size_t TEX_SIZE = 8;

struct tex_t
{
    int vacant;
    struct tex_t *next;
};

struct texs_t
{
    int size;
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

int tex_init(lua_State *lua, int size, int count)
{
    struct tex_t *tex;
    int i;
    if (sizeof(struct tex_t) > TEX_SIZE
    ||  (size & (size - 1)) != 0)
    {
        fprintf(stderr, "Invalid sizes:\n"
                        "sizeof(struct tex_t) == %i\n"
                        "size == %i\n",
                (int)sizeof(struct tex_t),
                size);
        return 1;
    }
    g_tex.pool = util_malloc(TEX_SIZE, TEX_SIZE * count);
    if (g_tex.pool == 0)
        return 1;
    memset(g_tex.pool, 0, TEX_SIZE * count);
    g_texs.size = size;
    g_texs.count = count;
    g_texs.left = count;
    g_texs.left_min = count;
    g_texs.vacant = tex_get(0);
    for (i = 0; i < count; ++i)
    {
        tex = tex_get(i);
        tex->vacant = 1;
        tex->next = tex_get(i + 1);
    }
    lua_register(lua, "api_tex_left", api_tex_left);
    lua_register(lua, "api_tex_alloc", api_tex_alloc);
    lua_register(lua, "api_tex_free", api_tex_free);
    lua_register(lua, "api_tex_set", api_tex_set);
}

void tex_done(void)
{
}
