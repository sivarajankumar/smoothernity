#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "../util/util.h"
#include "mpool.h"
#include "timer.h"
#include "render.h"
#include "input.h"
#include "ibuf.h"
#include "vbuf.h"
#include "pbuf.h"
#include "tex.h"
#include "mesh.h"
#include "vector.h"
#include "matrix.h"
#include "physics.h"
#include "buf.h"
#include "storage.h"
#include "shprog.h"
#include "shuni.h"
#include "sync.h"
#include "query.h"

static const size_t ARRAY_ALIGN = 16;

struct main_t
{
    int *main_mpool;
    int main_mpool_len;
    int *physics_mpool;
    int physics_mpool_len;
    int screen_width;
    int screen_height;
    int mesh_count;
    int vbuf_size;
    int vbuf_count;
    int ibuf_size;
    int ibuf_count;
    int pbuf_size;
    int pbuf_count;
    int *tex;
    int tex_len;
    int vector_count;
    int vector_nesting;
    int matrix_count;
    int matrix_nesting;
    int world_count;
    int colshape_count;
    int rigidbody_count;
    int vehicle_count;
    int buf_size;
    int buf_count;
    int storage_key_size;
    int storage_data_size;
    int storage_count;
    int shprog_count;
    int shuni_count;
    int sync_count;
    int query_count;
    lua_State *lua;
    struct mpool_t *mpool;
};

static struct main_t g_main;

static int api_main_gc_step(lua_State *lua)
{
    int step;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_main_gc_step: incorrect argument");
        lua_error(lua);
        return 0;
    }
    step = lua_tointeger(lua, 1);
    lua_pop(lua, 1);
    if (step <= 0)
    {
        lua_pushstring(lua, "api_main_gc_step: negative step");
        lua_error(lua);
        return 0;
    }
    lua_gc(g_main.lua, LUA_GCSTEP, step);
    lua_gc(g_main.lua, LUA_GCSTOP, 0);
    return 0;
}

static int main_panic(lua_State *lua)
{
    fprintf(stderr, "Lua panic: %s\n", lua_tostring(lua, -1));
    return 0;
}

static void * main_lua_alloc(void *ud, void *ptr, size_t osize, size_t nsize)
{
    void *newptr;
    if (ud != 0)
        return 0;
    else if (osize == 0 && nsize == 0)
        return 0;
    else if (osize == 0 && nsize > 0)
        return mpool_alloc(g_main.mpool, nsize);
    else if (osize > 0 && nsize == 0)
    {
        mpool_free(ptr);
        return 0;
    }
    newptr = mpool_alloc(g_main.mpool, nsize);
    if (newptr == 0)
        return 0;
    else if (ptr)
    {
        if (osize <= nsize)
            memcpy(newptr, ptr, osize);
        else
            memcpy(newptr, ptr, nsize);
        mpool_free(ptr);
    }
    return newptr;
}

static int main_get_int_array(lua_State *lua, const char *field,
                              int *len, int **array)
{
    int i;
    lua_getfield(lua, -1, field);
    if (!lua_isfunction(lua, -1) || lua_pcall(lua, 0, LUA_MULTRET, 0) != 0)
    {
        fprintf(stderr, "Cannot call configure()[\"%s\"]()\n",
                field);
        return 1;
    }
    *len = lua_gettop(lua) - 1;
    if (*len <= 0)
    {
        fprintf(stderr, "Invalid configure()[\"%s\"]() return value\n",
                field);
        return 1;
    }
    *array = util_malloc(ARRAY_ALIGN, *len * sizeof(int));
    if (*array == 0)
    {
        fprintf(stderr, "Out of memory while loading configure()[\"%s\"]\n",
                field);
        return 1;
    }
    memset(*array, 0, *len * sizeof(int));
    for (i = 0; i < *len; ++i)
    {
        if (!lua_isnumber(lua, -(*len) + i))
        {
            fprintf(stderr, "The configure()[\"%s\"]()[%i] is not a number\n",
                    field, i);
            return 1;
        }
        (*array)[i] = lua_tointeger(lua, -(*len) + i);
    }
    lua_pop(lua, *len);
    return 0;
}

static int main_get_float(lua_State *lua, const char *field, float *dest)
{
    lua_getfield(lua, -1, field);
    if (!lua_isnumber(lua, -1))
    {
        fprintf(stderr, "The configure()[\"%s\"] value is not a number\n",
                field);
        return 1;
    }
    *dest = (float)lua_tonumber(lua, -1);
    lua_pop(lua, 1);
    return 0;
}

static int main_get_int(lua_State *lua, const char *field, int *dest)
{
    float f;
    if (main_get_float(lua, field, &f) != 0)
        return 1;
    *dest = (int)f;
    return 0;
}

static int main_configure(char *script)
{
    lua_State *lua;
    lua = luaL_newstate();
    if (lua == 0)
        return -1;
    lua_atpanic(lua, main_panic);
    luaL_openlibs(lua);
    if (luaL_dofile(lua, script) != 0)
    {
        fprintf(stderr, "Cannot run script: %s\n", lua_tostring(lua, -1));
        goto cleanup;
    }
    lua_getglobal(lua, "configure");
    if (!lua_isfunction(lua, -1) || lua_pcall(lua, 0, LUA_MULTRET, 0) != 0)
    {
        fprintf(stderr, "Cannot run configure() function: %s\n", lua_tostring(lua, -1));
        goto cleanup;
    }
    if (lua_gettop(lua) != 1 || !lua_istable(lua, -1))
    {
        fprintf(stderr, "Invalid return value of configure() function\n");
        goto cleanup;
    }

    if (main_get_int(lua, "screen_width", &g_main.screen_width) != 0
     || main_get_int(lua, "screen_height", &g_main.screen_height) != 0
     || main_get_int(lua, "mesh_count", &g_main.mesh_count) != 0
     || main_get_int(lua, "vbuf_size", &g_main.vbuf_size) != 0
     || main_get_int(lua, "vbuf_count", &g_main.vbuf_count) != 0
     || main_get_int(lua, "ibuf_size", &g_main.ibuf_size) != 0
     || main_get_int(lua, "ibuf_count", &g_main.ibuf_count) != 0
     || main_get_int(lua, "pbuf_size", &g_main.pbuf_size) != 0
     || main_get_int(lua, "pbuf_count", &g_main.pbuf_count) != 0
     || main_get_int(lua, "vector_count", &g_main.vector_count) != 0
     || main_get_int(lua, "vector_nesting", &g_main.vector_nesting) != 0
     || main_get_int(lua, "matrix_count", &g_main.matrix_count) != 0
     || main_get_int(lua, "matrix_nesting", &g_main.matrix_nesting) != 0
     || main_get_int(lua, "world_count", &g_main.world_count) != 0
     || main_get_int(lua, "colshape_count", &g_main.colshape_count) != 0
     || main_get_int(lua, "rigidbody_count", &g_main.rigidbody_count) != 0
     || main_get_int(lua, "vehicle_count", &g_main.vehicle_count) != 0
     || main_get_int(lua, "buf_size", &g_main.buf_size) != 0
     || main_get_int(lua, "buf_count", &g_main.buf_count) != 0
     || main_get_int(lua, "storage_key_size", &g_main.storage_key_size) != 0
     || main_get_int(lua, "storage_data_size", &g_main.storage_data_size) != 0
     || main_get_int(lua, "storage_count", &g_main.storage_count) != 0
     || main_get_int(lua, "shuni_count", &g_main.shuni_count) != 0
     || main_get_int(lua, "shprog_count", &g_main.shprog_count) != 0
     || main_get_int(lua, "sync_count", &g_main.sync_count) != 0
     || main_get_int(lua, "query_count", &g_main.query_count) != 0)
    {
        goto cleanup;
    }

    if (main_get_int_array(lua, "main_mpool", &g_main.main_mpool_len,
                           &g_main.main_mpool) != 0
     || main_get_int_array(lua, "physics_mpool", &g_main.physics_mpool_len,
                           &g_main.physics_mpool) != 0
     || main_get_int_array(lua, "tex", &g_main.tex_len, &g_main.tex) != 0)
    {
        goto cleanup;
    }

    lua_pop(lua, 1);
    lua_close(lua);
    return 0;
cleanup:
    if (g_main.main_mpool)
    {
        util_free(g_main.main_mpool);
        g_main.main_mpool = 0;
    }
    if (g_main.physics_mpool)
    {
        util_free(g_main.physics_mpool);
        g_main.physics_mpool = 0;
    }
    if (g_main.tex)
    {
        util_free(g_main.tex);
        g_main.tex = 0;
    }
    lua_close(lua);
    return 1;
}

static void main_done(void)
{
    render_thread_done();
    vbuf_done();
    ibuf_done();
    pbuf_done();
    tex_done();
    shuni_done();
    shprog_done();
    query_done();
    render_done();

    if (g_main.lua)
        lua_close(g_main.lua);
    if (g_main.mpool)
    {
        fprintf(stdout, "Main memory pool:\n");
        mpool_destroy(g_main.mpool);
    }
    if (g_main.main_mpool)
    {
        util_free(g_main.main_mpool);
        g_main.main_mpool = 0;
    }
    if (g_main.physics_mpool)
    {
        util_free(g_main.physics_mpool);
        g_main.physics_mpool = 0;
    }
    if (g_main.tex)
    {
        util_free(g_main.tex);
        g_main.tex = 0;
    }

    buf_done();
    storage_done();
    vector_done();
    matrix_done();
    sync_done();
    mesh_done();
    physics_done();
}

static int main_init(int argc, char **argv)
{
    if (main_configure(argv[argc-1]) != 0)
    {
        fprintf(stderr, "Cannot init main\n");
        return 1;
    }

    g_main.mpool = mpool_create(g_main.main_mpool,
                                g_main.main_mpool + g_main.main_mpool_len / 2,
                                g_main.main_mpool_len / 2);
    if (g_main.mpool == 0)
    {
        fprintf(stderr, "Cannot create main memory pool\n");
        return 1;
    }

    g_main.lua = lua_newstate(main_lua_alloc, 0);
    if (g_main.lua == 0)
    {
        fprintf(stderr, "Cannot create Lua state\n");
        return 1;
    }
    lua_atpanic(g_main.lua, main_panic);
    lua_gc(g_main.lua, LUA_GCSTOP, 0);

    luaL_openlibs(g_main.lua);

    if (luaL_dofile(g_main.lua, argv[argc-1]) != 0)
    {
        fprintf(stderr, "Cannot run script: %s\n", lua_tostring(g_main.lua, -1));
        return 1;
    }

    input_init(g_main.lua);

    if (timer_init(g_main.lua) != 0)
    {
        fprintf(stderr, "Cannot init timer\n"); 
        return 1;
    }

    if (physics_init(g_main.lua, g_main.world_count, g_main.colshape_count,
                     g_main.rigidbody_count, g_main.vehicle_count,
                     g_main.physics_mpool,
                     g_main.physics_mpool + g_main.physics_mpool_len / 2,
                     g_main.physics_mpool_len / 2) != 0)
    {
        fprintf(stderr, "Cannot init physics\n"); 
        return 1;
    } 

    if (storage_init(g_main.lua, g_main.storage_key_size,
                     g_main.storage_data_size, g_main.storage_count) != 0)
    {
        fprintf(stderr, "Cannot init storages\n");
        return 1;
    }

    if (buf_init(g_main.lua, g_main.buf_size, g_main.buf_count) != 0)
    {
        fprintf(stderr, "Cannot init buffers\n");
        return 1;
    }

    if (vector_init(g_main.lua, g_main.vector_count, g_main.vector_nesting) != 0)
    {
        fprintf(stderr, "Cannot init vectors\n");
        return 1;
    }

    if (matrix_init(g_main.lua, g_main.matrix_count, g_main.matrix_nesting) != 0)
    {
        fprintf(stderr, "Cannot init matrices\n");
        return 1;
    }

    if (mesh_init(g_main.lua, g_main.mesh_count) != 0)
    {
        fprintf(stderr, "Cannot init meshes\n");
        return 1;
    }

    if (sync_init(g_main.lua, g_main.sync_count) != 0)
    {
        fprintf(stderr, "Cannot init syncs\n");
        return 1;
    }

    if (render_init(g_main.lua, g_main.screen_width, g_main.screen_height) != 0)
    {
        fprintf(stderr, "Cannot init render\n"); 
        return 1;
    } 

    if (query_init(g_main.lua, g_main.query_count) != 0)
    {
        fprintf(stderr, "Cannot init queries\n");
        return 1;
    }

    if (vbuf_init(g_main.lua, g_main.vbuf_size, g_main.vbuf_count) != 0)
    {
        fprintf(stderr, "Cannot init vertex buffers\n");
        return 1;
    }

    if (ibuf_init(g_main.lua, g_main.ibuf_size, g_main.ibuf_count) != 0)
    {
        fprintf(stderr, "Cannot init index buffers\n");
        return 1;
    }

    if (pbuf_init(g_main.lua, g_main.pbuf_size, g_main.pbuf_count) != 0)
    {
        fprintf(stderr, "Cannot init pixel buffers\n");
        return 1;
    }

    if (tex_init(g_main.lua, g_main.tex, g_main.tex_len) != 0)
    {
        fprintf(stderr, "Cannot init textures\n");
        return 1;
    }

    if (shprog_init(g_main.lua, g_main.shprog_count) != 0)
    {
        fprintf(stderr, "Cannot init shader programs\n");
        return 1;
    }

    if (shuni_init(g_main.lua, g_main.shuni_count) != 0)
    {
        fprintf(stderr, "Cannot init shader uniforms\n");
        return 1;
    }

    lua_register(g_main.lua, "api_main_gc_step", api_main_gc_step);
    return 0;
}

static void main_loop(void)
{
    printf("Game loop start\n");
    lua_getglobal(g_main.lua, "run");
    if (!lua_isfunction(g_main.lua, -1))
        fprintf(stderr, "Cannot find run() function\n");
    else if (lua_pcall(g_main.lua, 0, LUA_MULTRET, 0) != 0)
        fprintf(stderr, "Error while executing run() function: %s\n", lua_tostring(g_main.lua, -1));
    printf("Game loop finish\n");
}

int main(int argc, char **argv)
{
    printf("Engine start\n");
    if (main_init(argc, argv) == 0)
        main_loop();
    main_done();
    printf("Engine finish\n");
    return 0;
}
