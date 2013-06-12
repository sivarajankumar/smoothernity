#include "SDL.h"
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#include "util.h"
#include "mpool.h"
#include "timer.h"
#include "render.h"
#include "input.h"
#include "vector.h"
#include "matrix.h"
#include "physics.h"
#include "cbuf.h"
#include "cthread.h"
#include "prog.h"
#include "rbuf.h"
#include "vao.h"
#include "pmem.h"
#include <stdlib.h>
#include <stdio.h>
#include <setjmp.h>

/*
 * SDL declares main().
 * Without the following #undef, compilation on Windows fails.
 */
#undef main

#if !__STDC_IEC_559__
    #error "Implementation doesn't support IEC 60559 floating point arithmetic"
#endif

#ifndef LUA_NUMBER_DOUBLE
    #error "Lua number must have type double"
#endif

static const size_t ARRAY_ALIGN = 16;

struct main_t {
    int *main_mpool, main_mpool_len;
    int *physics_mpool, physics_mpool_len;
    int *thread_mpool, thread_mpool_len;
    int thread_count, screen_width, screen_height, full_screen;
    int vector_count, vector_nesting, matrix_count, matrix_nesting;
    int world_count, colshape_count, rigidbody_count, vehicle_count;
    int buf_size, prog_count, rbuf_count, vao_count;
    lua_State *lua;
    jmp_buf panic;
    struct mpool_t *mpool;
};

static struct main_t g_main;

static int main_panic(lua_State *lua) {
    fprintf(stderr, "Lua panic: %s\n", lua_tostring(lua, -1));
    longjmp(g_main.panic, 1);
}

static void * main_lua_alloc(void *ud, void *ptr, size_t osize, size_t nsize) {
    void *newptr;
    if (ud)
        return 0;
    else if (!osize && !nsize)
        return 0;
    else if (!osize && nsize)
        return mpool_alloc(g_main.mpool, nsize);
    else if (osize && !nsize) {
        mpool_free(ptr);
        return 0;
    }
    if (!(newptr = mpool_alloc(g_main.mpool, nsize)))
        return 0;
    else if (ptr) {
        if (osize <= nsize)
            memcpy(newptr, ptr, osize);
        else
            memcpy(newptr, ptr, nsize);
        mpool_free(ptr);
    }
    return newptr;
}

static int main_get_int_array
(lua_State *lua, const char *field, int *len, int **array) {
    int oldtop = lua_gettop(lua);
    lua_getfield(lua, -1, field);
    if (!lua_isfunction(lua, -1) || lua_pcall(lua, 0, LUA_MULTRET, 0)) {
        fprintf(stderr, "Cannot call configure()[\"%s\"]()\n", field);
        return 1;
    }
    *len = lua_gettop(lua) - oldtop;
    if (*len <= 0) {
        fprintf(stderr, "Invalid configure()[\"%s\"]() return value\n", field);
        return 1;
    }
    *array = pmem_alloc(PMEM_ALIGNOF(int), *len * sizeof(int));
    if (!*array) {
        fprintf(stderr, "Out of memory loading configure()[\"%s\"]\n", field);
        return 1;
    }
    for (int i = 0; i < *len; ++i) {
        if (!util_isint(lua, -(*len) + i)) {
            fprintf(stderr, "configure()[\"%s\"]()[%i] not num\n", field, i);
            return 1;
        }
        (*array)[i] = lua_tointeger(lua, -(*len) + i);
    }
    lua_pop(lua, *len);
    return 0;
}

static int main_get_float(lua_State *lua, const char *field, float *dest) {
    lua_getfield(lua, -1, field);
    if (!util_isfloat(lua, -1)) {
        fprintf(stderr, "configure()[\"%s\"] value is not a number\n", field);
        return 1;
    }
    *dest = (float)lua_tonumber(lua, -1);
    lua_pop(lua, 1);
    return 0;
}

static int main_get_int(lua_State *lua, const char *field, int *dest) {
    float f;
    if (main_get_float(lua, field, &f))
        return 1;
    *dest = (int)f;
    return 0;
}

static int main_configure(char *script) {
    lua_State *lua;
    lua = luaL_newstate();
    if (!lua)
        return 1;
    lua_atpanic(lua, main_panic);
    luaL_openlibs(lua);
    if (luaL_dofile(lua, script)) {
        fprintf(stderr, "Cannot run script: %s\n", lua_tostring(lua, -1));
        goto cleanup;
    }
    if (!lua_istable(lua, -1)) {
        fprintf(stderr, "Invalid return value of main module\n");
        goto cleanup;
    }
    lua_getfield(lua, -1, "configure");
    if (!lua_isfunction(lua, -1) || lua_pcall(lua, 0, LUA_MULTRET, 0)) {
        fprintf(stderr, "Cannot run configure() function: %s\n", lua_tostring(lua, -1));
        goto cleanup;
    }
    if (!lua_istable(lua, -1)) {
        fprintf(stderr, "Invalid return value of configure() function\n");
        goto cleanup;
    }
    #define GETI(x) main_get_int(lua, #x, &g_main.x)
    #define GETA(x) main_get_int_array(lua, #x, &g_main.x##_len, &g_main.x)
    if (GETI(screen_width) || GETI(screen_height) || GETI(full_screen) ||
    GETI(thread_count) || GETI(vector_count) || GETI(vector_nesting) ||
    GETI(matrix_count) || GETI(matrix_nesting) || GETI(world_count) ||
    GETI(colshape_count) || GETI(rigidbody_count) || GETI(vehicle_count) ||
    GETI(buf_size) || GETI(prog_count) || GETI(rbuf_count) || GETI(vao_count) ||
    GETA(main_mpool) || GETA(physics_mpool) || GETA(thread_mpool))
        goto cleanup;
    #undef GETI
    #undef GETA
    lua_pop(lua, 1);
    lua_close(lua);
    return 0;
cleanup:
    lua_close(lua);
    return 1;
}

static void main_done(void) {
    vao_done();
    prog_done();
    rbuf_done();
    render_done();

    if (g_main.lua)
        lua_close(g_main.lua);
    if (g_main.main_mpool) {
        pmem_free(g_main.main_mpool);
        g_main.main_mpool = 0;
    }
    if (g_main.physics_mpool) {
        pmem_free(g_main.physics_mpool);
        g_main.physics_mpool = 0;
    }
    if (g_main.thread_mpool) {
        pmem_free(g_main.thread_mpool);
        g_main.thread_mpool = 0;
    }
    cbuf_done();
    vector_done();
    matrix_done();
    physics_done();
    if (g_main.mpool) {
        fprintf(stderr, "\nMain memory pool:\n");
        mpool_destroy(g_main.mpool);
    }
    cthread_done();

    SDL_Quit();
}

static int main_init(int argc, char **argv) {
    char *script;
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <script.lua>\n", argv[0]);
        return 1;
    }
    script = argv[1];
    if (main_configure(script)) {
        fprintf(stderr, "Cannot configure engine\n");
        return 1;
    }
    if (SDL_Init(SDL_INIT_EVERYTHING)) {
        fprintf(stderr, "Cannot init SDL\n");
        return 1;
    }
    g_main.mpool = mpool_create(g_main.main_mpool,
                                g_main.main_mpool + g_main.main_mpool_len / 2,
                                g_main.main_mpool_len / 2);
    if (!g_main.mpool) {
        fprintf(stderr, "Cannot create main memory pool\n");
        return 1;
    }
    g_main.lua = lua_newstate(main_lua_alloc, 0);
    if (!g_main.lua) {
        fprintf(stderr, "Cannot create Lua state\n");
        return 1;
    }
    lua_atpanic(g_main.lua, main_panic);
    luaL_openlibs(g_main.lua);

    input_init(g_main.lua);

    if (timer_init(g_main.lua)) {
        fprintf(stderr, "Cannot init timer\n"); 
        return 1;
    }
    if (cthread_init(g_main.lua, g_main.thread_count, g_main.thread_mpool,
    g_main.thread_mpool + g_main.thread_mpool_len / 2,
    g_main.thread_mpool_len / 2)) {
        fprintf(stderr, "Cannot init threads\n"); 
        return 1;
    } 
    if (physics_init(g_main.lua, g_main.world_count, g_main.colshape_count,
    g_main.rigidbody_count, g_main.vehicle_count, g_main.physics_mpool,
    g_main.physics_mpool + g_main.physics_mpool_len / 2,
    g_main.physics_mpool_len / 2)) {
        fprintf(stderr, "Cannot init physics\n"); 
        return 1;
    } 
    if (cbuf_init(g_main.lua, g_main.buf_size)) {
        fprintf(stderr, "Cannot init buffers\n");
        return 1;
    }
    if (vector_init(g_main.lua, g_main.vector_count, g_main.vector_nesting)) {
        fprintf(stderr, "Cannot init vectors\n");
        return 1;
    }
    if (matrix_init(g_main.lua, g_main.matrix_count, g_main.matrix_nesting)) {
        fprintf(stderr, "Cannot init matrices\n");
        return 1;
    }
    if (render_init(g_main.lua, g_main.screen_width,
    g_main.screen_height, g_main.full_screen)) {
        fprintf(stderr, "Cannot init render\n"); 
        return 1;
    } 
    if (prog_init(g_main.lua, g_main.prog_count)) {
        fprintf(stderr, "Cannot init shader programs\n"); 
        return 1;
    }
    if (rbuf_init(g_main.lua, g_main.rbuf_count)) {
        fprintf(stderr, "Cannot init render buffers\n"); 
        return 1;
    }
    if (vao_init(g_main.lua, g_main.vao_count)) {
        fprintf(stderr, "Cannot init vertex array objects\n");
        return 1;
    }
    if (luaL_dofile(g_main.lua, script)) {
        fprintf(stderr, "Cannot run script: %s\n", lua_tostring(g_main.lua, -1));
        return 1;
    }
    return 0;
}

static void main_loop(void) {
    fprintf(stderr, "Game loop start\n");
    if (!lua_istable(g_main.lua, -1))
        fprintf(stderr, "Invalid return value of main module\n");
    else {
        lua_getfield(g_main.lua, -1, "run");
        if (!lua_isfunction(g_main.lua, -1))
            fprintf(stderr, "Cannot find run() function\n");
        else if (lua_pcall(g_main.lua, 0, LUA_MULTRET, 0))
            fprintf(stderr, "Error while executing run() function: %s\n",
                    lua_tostring(g_main.lua, -1));
    }
    fprintf(stderr, "Game loop finish\n");
}

int main(int argc, char **argv) {
    fprintf(stderr, "Engine start\n");
    if (!setjmp(g_main.panic))
        if (!main_init(argc, argv))
            main_loop();
    main_done();
    fprintf(stderr, "Engine finish\n");
    return EXIT_SUCCESS;
}

