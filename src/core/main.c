#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <SDL.h>
#include "mpool.h"
#include "machine.h"
#include "timer.h"
#include "display.h"
#include "input.h"
#include "ibuf.h"
#include "vbuf.h"
#include "mesh.h"
#include "text.h"
#include "vector.h"
#include "matrix.h"
#include "physics.h"
#include "buf.h"

struct main_t
{
    int *mpool_sizes;
    int *mpool_counts;
    int mpool_len;
    float frame_time;
    float logic_time;
    int gc_step;
    int display_width;
    int display_height;
    int mesh_count;
    int vbuf_size;
    int vbuf_count;
    int ibuf_size;
    int ibuf_count;
    int text_size;
    int text_count;
    int vector_count;
    int vector_nesting;
    int matrix_count;
    int matrix_nesting;
    int colshape_count;
    int rigidbody_count;
    int vehicle_count;
    int buf_size;
    int buf_count;
    lua_State *lua;
    struct machine_t *controller;
    struct machine_t *worker;
    struct timer_t *logic_timer;
    struct timer_t *gc_timer;
    float last_gc_time;
};

static struct main_t g_main;

static int api_main_timing(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_main_timing: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushnumber(lua, g_main.last_gc_time);
    return 1;
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
        return mpool_alloc(nsize);
    else if (osize > 0 && nsize == 0)
    {
        mpool_free(ptr);
        return 0;
    }
    newptr = mpool_alloc(nsize);
    if (newptr == 0)
        return 0;
    else if (osize <= nsize)
        memcpy(newptr, ptr, osize);
    else
        memcpy(newptr, ptr, nsize);
    mpool_free(ptr);
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
    *array = calloc(*len, sizeof(int));
    if (*array == 0)
    {
        fprintf(stderr, "Out of memory while loading configure()[\"%s\"]\n",
                field);
        return 1;
    }
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
    *dest = lua_tonumber(lua, -1);
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

    if (main_get_float(lua, "frame_time", &g_main.frame_time) != 0
     || main_get_float(lua, "logic_time", &g_main.logic_time) != 0
     || main_get_int(lua, "gc_step", &g_main.gc_step) != 0
     || main_get_int(lua, "display_width", &g_main.display_width) != 0
     || main_get_int(lua, "display_height", &g_main.display_height) != 0
     || main_get_int(lua, "mesh_count", &g_main.mesh_count) != 0
     || main_get_int(lua, "vbuf_size", &g_main.vbuf_size) != 0
     || main_get_int(lua, "vbuf_count", &g_main.vbuf_count) != 0
     || main_get_int(lua, "ibuf_size", &g_main.ibuf_size) != 0
     || main_get_int(lua, "ibuf_count", &g_main.ibuf_count) != 0
     || main_get_int(lua, "text_size", &g_main.text_size) != 0
     || main_get_int(lua, "text_count", &g_main.text_count) != 0
     || main_get_int(lua, "vector_count", &g_main.vector_count) != 0
     || main_get_int(lua, "vector_nesting", &g_main.vector_nesting) != 0
     || main_get_int(lua, "matrix_count", &g_main.matrix_count) != 0
     || main_get_int(lua, "matrix_nesting", &g_main.matrix_nesting) != 0
     || main_get_int(lua, "colshape_count", &g_main.colshape_count) != 0
     || main_get_int(lua, "rigidbody_count", &g_main.rigidbody_count) != 0
     || main_get_int(lua, "vehicle_count", &g_main.vehicle_count) != 0
     || main_get_int(lua, "buf_size", &g_main.buf_size) != 0
     || main_get_int(lua, "buf_count", &g_main.buf_count) != 0)
    {
        goto cleanup;
    }

    if (main_get_int_array(lua, "mpool_sizes", &g_main.mpool_len,
                           &g_main.mpool_sizes) != 0
     || main_get_int_array(lua, "mpool_counts", &g_main.mpool_len,
                           &g_main.mpool_counts) != 0)
    {
        goto cleanup;
    }

    lua_pop(lua, 1);
    lua_close(lua);
    return 0;
cleanup:
    if (g_main.mpool_sizes)
    {
        free(g_main.mpool_sizes);
        g_main.mpool_sizes = 0;
    }
    if (g_main.mpool_counts)
    {
        free(g_main.mpool_counts);
        g_main.mpool_counts = 0;
    }
    lua_close(lua);
    return 1;
}

static void main_done(void)
{
    vbuf_done();
    ibuf_done();
    display_done();

    if (g_main.lua)
        lua_close(g_main.lua);
    if (g_main.controller)
        machine_destroy(g_main.controller);
    if (g_main.worker)
        machine_destroy(g_main.worker);
    if (g_main.logic_timer)
        timer_destroy(g_main.logic_timer);
    if (g_main.gc_timer)
        timer_destroy(g_main.gc_timer);
    if (g_main.mpool_sizes)
    {
        free(g_main.mpool_sizes);
        g_main.mpool_sizes = 0;
    }
    if (g_main.mpool_counts)
    {
        free(g_main.mpool_counts);
        g_main.mpool_counts = 0;
    }

    input_done();
    buf_done();
    vector_done();
    matrix_done();
    mesh_done();
    text_done();
    physics_done();
    mpool_done();
}

static int main_init(int argc, char **argv)
{
    if (main_configure(argv[argc-1]) != 0)
    {
        fprintf(stderr, "Cannot init main\n");
        return 1;
    }

    if (mpool_init(g_main.mpool_sizes,
                   g_main.mpool_counts,
                   g_main.mpool_len) == 0)
    {
        fprintf(stderr, "Cannot create memory pool\n");
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

    machine_init(g_main.lua);

    g_main.logic_timer = timer_create();
    g_main.gc_timer = timer_create();
    if (g_main.logic_timer == 0 || g_main.gc_timer == 0)
    {
        fprintf(stderr, "Cannot create timers\n");
        return 1;
    }

    if (input_init(g_main.lua) != 0)
    {
        fprintf(stderr, "Cannot init input\n");
        return 1;
    }

    if (physics_init(g_main.lua, g_main.colshape_count,
                     g_main.rigidbody_count, g_main.vehicle_count) != 0)
    {
        fprintf(stderr, "Cannot init physics\n"); 
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

    if (text_init(g_main.lua, g_main.text_size, g_main.text_count) != 0)
    {
        fprintf(stderr, "Cannot init texts\n");
        return 1;
    }

    g_main.controller = machine_create(g_main.lua, "control");
    if (g_main.controller == 0)
    {
        fprintf(stderr, "Cannot create controller\n");
        return 1;
    }

    g_main.worker = machine_create(g_main.lua, "work");
    if (g_main.worker == 0)
    {
        fprintf(stderr, "Cannot create worker\n");
        return 1;
    }

    if (display_init(g_main.lua, &argc, argv, g_main.display_width,
                                       g_main.display_height) != 0)
    {
        fprintf(stderr, "Cannot set video mode\n"); 
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
    lua_register(g_main.lua, "api_main_timing", api_main_timing);
    return 0;
}

static void main_loop(void)
{
    printf("Game loop start\n");
    while (machine_running(g_main.controller) || machine_running(g_main.worker))
    {
        timer_reset(g_main.logic_timer);
        physics_update(g_main.frame_time);
        input_update();

        timer_reset(g_main.gc_timer);
        lua_gc(g_main.lua, LUA_GCSTEP, g_main.gc_step);
        lua_gc(g_main.lua, LUA_GCSTOP, 0);
        g_main.last_gc_time = timer_passed(g_main.gc_timer);

        if (machine_step(g_main.controller, 0) != 0)
        {
            fprintf(stderr, "Failed to run controller\n");
            return;
        }
        if (machine_step(g_main.worker, g_main.logic_time -
                         timer_passed(g_main.logic_timer)) != 0)
        {
            fprintf(stderr, "Failed to run worker\n");
            return;
        }
        display_update(g_main.frame_time);
    }
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
