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

struct main_t
{
    int *mpool_sizes;
    int *mpool_counts;
    int mpool_len;
    int logic_time;
    int gc_step;
    int min_delay;
    int display_width;
    int display_height;
    int fps;
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
};

static struct main_t g_main;

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

static int main_get_int(lua_State *lua, const char *field, int *dest)
{
    lua_getfield(lua, -1, field);
    if (!lua_isnumber(lua, -1))
    {
        fprintf(stderr, "The configure()[\"%s\"] value is not a number\n",
                field);
        return 1;
    }
    *dest = lua_tointeger(lua, -1);
    lua_pop(lua, 1);
    return 0;
}

static int main_init(char *script)
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

    if (main_get_int(lua, "logic_time", &g_main.logic_time) != 0
     || main_get_int(lua, "gc_step", &g_main.gc_step) != 0
     || main_get_int(lua, "min_delay", &g_main.min_delay) != 0
     || main_get_int(lua, "display_width", &g_main.display_width) != 0
     || main_get_int(lua, "display_height", &g_main.display_height) != 0
     || main_get_int(lua, "fps", &g_main.fps) != 0
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
     || main_get_int(lua, "rigidbody_count", &g_main.rigidbody_count) != 0)
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

void main_done(void)
{
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
}

int main(int argc, char **argv)
{
    int time_left, max_deviation;
    lua_State *lua = 0;
    struct machine_t *controller = 0, *worker = 0;
    struct timer_t *logic_timer = 0;

    printf("Start\n");

    if (main_init(argv[argc-1]) != 0)
    {
        fprintf(stderr, "Cannot init main\n");
        goto cleanup;
    }

    if (mpool_init(g_main.mpool_sizes,
                   g_main.mpool_counts,
                   g_main.mpool_len) == 0)
    {
        fprintf(stderr, "Cannot create memory pool\n");
        goto cleanup;
    }

    lua = lua_newstate(main_lua_alloc, 0);
    if (lua == 0)
    {
        fprintf(stderr, "Cannot create Lua state\n");
        goto cleanup;
    }
    lua_atpanic(lua, main_panic);
    lua_gc(lua, LUA_GCSTOP, 0);

    luaL_openlibs(lua);

    if (luaL_dofile(lua, argv[argc-1]) != 0)
    {
        fprintf(stderr, "Cannot run script: %s\n", lua_tostring(lua, -1));
        goto cleanup;
    }

    machine_init(lua);
    input_init(lua);

    if (physics_init(lua, g_main.colshape_count, g_main.rigidbody_count) != 0)
    {
        fprintf(stderr, "Cannot init physics\n"); 
        goto cleanup;
    } 

    if (display_init(lua, &argc, argv, g_main.display_width,
                                       g_main.display_height) != 0)
    {
        fprintf(stderr, "Cannot set video mode\n"); 
        goto cleanup;
    } 

    if (vbuf_init(lua, g_main.vbuf_size, g_main.vbuf_count) != 0)
    {
        fprintf(stderr, "Cannot init vertex buffers\n");
        goto cleanup;
    }

    if (ibuf_init(lua, g_main.ibuf_size, g_main.ibuf_count) != 0)
    {
        fprintf(stderr, "Cannot init index buffers\n");
        goto cleanup;
    }

    if (vector_init(lua, g_main.vector_count, g_main.vector_nesting) != 0)
    {
        fprintf(stderr, "Cannot init vectors\n");
        goto cleanup;
    }

    if (matrix_init(lua, g_main.matrix_count, g_main.matrix_nesting) != 0)
    {
        fprintf(stderr, "Cannot init matrices\n");
        goto cleanup;
    }

    if (mesh_init(lua, g_main.mesh_count) != 0)
    {
        fprintf(stderr, "Cannot init meshes\n");
        goto cleanup;
    }

    if (text_init(lua, g_main.text_size, g_main.text_count) != 0)
    {
        fprintf(stderr, "Cannot init texts\n");
        goto cleanup;
    }

    logic_timer = timer_create();
    if (logic_timer == 0)
    {
        fprintf(stderr, "Cannot create timer\n");
        goto cleanup;
    }

    controller = machine_create(lua, "control");
    if (controller == 0)
    {
        fprintf(stderr, "Cannot create controller\n");
        goto cleanup;
    }

    worker = machine_create(lua, "work");
    if (worker == 0)
    {
        fprintf(stderr, "Cannot create worker\n");
        goto cleanup;
    }

    max_deviation = 0;
    while (machine_running(controller) || machine_running(worker))
    {
        timer_reset(logic_timer);
        lua_gc(lua, LUA_GCSTEP, g_main.gc_step);
        lua_gc(lua, LUA_GCSTOP, 0);
        input_update();
        display_update(1.0f / (float)g_main.fps);
        if (machine_step(controller, 0) != 0)
        {
            fprintf(stderr, "Failed to run controller\n");
            goto cleanup;
        }
        if (machine_step(worker, g_main.logic_time - timer_passed(logic_timer)) != 0)
        {
            fprintf(stderr, "Failed to run worker\n");
            goto cleanup;
        }
        time_left = timer_passed(logic_timer);
        if (g_main.logic_time - time_left > g_main.min_delay)
            SDL_Delay((g_main.logic_time - time_left) / 1000);
        if (timer_passed(logic_timer) - g_main.logic_time > max_deviation)
            max_deviation = timer_passed(logic_timer) - g_main.logic_time;
        display_show();
    }
    printf("Maximum deviation: %i us\n", max_deviation);

cleanup:
    vbuf_done();
    ibuf_done();
    display_done();
    vector_done();
    matrix_done();
    mesh_done();
    text_done();
    main_done();
    physics_done();
    if (lua)
        lua_close(lua);
    if (controller)
        machine_destroy(controller);
    if (worker)
        machine_destroy(worker);
    if (logic_timer)
        timer_destroy(logic_timer);
    mpool_done();
    printf("Finish\n");
    return 0;
}
