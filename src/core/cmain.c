#include "SDL.h"
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#include "util.h"
#include "cmpool.h"
#include "timer.h"
#include "crender.h"
#include "cinput.h"
#include "vector.h"
#include "cmatrix.h"
#include "cphysics.h"
#include "cbuf.h"
#include "cthread.h"
#include "cprog.h"
#include "crbuf.h"
#include "clog.h"
#include "vao.h"
#include "vlog.h"
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

struct cmain_t {
    int *main_mpool, main_mpool_len;
    int *physics_mpool, physics_mpool_len;
    int *thread_mpool, thread_mpool_len;
    int thread_count, screen_width, screen_height, full_screen;
    int vector_count, vector_nesting, matrix_count, matrix_nesting;
    int world_count, colshape_count, rigidbody_count, vehicle_count;
    int buf_size, prog_count, rbuf_count, vao_count;
    lua_State *lua;
    jmp_buf panic;
    struct cmpool_t *mpool;
};

static struct cmain_t g_cmain;

static int cmain_panic(lua_State *lua) {
    VLOG_ERROR("Lua panic: %s", lua_tostring(lua, -1));
    longjmp(g_cmain.panic, 1);
}

static void * cmain_lua_alloc(void *ud, void *ptr, size_t osize, size_t nsize) {
    void *newptr;
    if (ud)
        return 0;
    else if (!osize && !nsize)
        return 0;
    else if (!osize && nsize)
        return cmpool_alloc(g_cmain.mpool, nsize);
    else if (osize && !nsize) {
        cmpool_free(ptr);
        return 0;
    }
    if (!(newptr = cmpool_alloc(g_cmain.mpool, nsize)))
        return 0;
    else if (ptr) {
        if (osize <= nsize)
            memcpy(newptr, ptr, osize);
        else
            memcpy(newptr, ptr, nsize);
        cmpool_free(ptr);
    }
    return newptr;
}

static int cmain_get_int_array
(lua_State *lua, const char *field, int *len, int **array) {
    int oldtop = lua_gettop(lua);
    lua_getfield(lua, -1, field);
    if (!lua_isfunction(lua, -1) || lua_pcall(lua, 0, LUA_MULTRET, 0)) {
        VLOG_ERROR("Cannot call configure()[\"%s\"]()", field);
        return 1;
    }
    *len = lua_gettop(lua) - oldtop;
    if (*len <= 0) {
        VLOG_ERROR("Invalid configure()[\"%s\"]() return value", field);
        return 1;
    }
    *array = pmem_alloc(PMEM_ALIGNOF(int), *len * sizeof(int));
    if (!*array) {
        VLOG_ERROR("Out of memory loading configure()[\"%s\"]", field);
        return 1;
    }
    for (int i = 0; i < *len; ++i) {
        if (!util_isint(lua, -(*len) + i)) {
            VLOG_ERROR("configure()[\"%s\"]()[%i] not int", field, i);
            return 1;
        }
        (*array)[i] = lua_tointeger(lua, -(*len) + i);
    }
    lua_pop(lua, *len);
    return 0;
}

static int cmain_get_int(lua_State *lua, const char *field, int *dest) {
    lua_getfield(lua, -1, field);
    if (!util_isint(lua, -1)) {
        VLOG_ERROR("configure()[\"%s\"] value is not an integer", field);
        return 1;
    }
    *dest = lua_tointeger(lua, -1);
    lua_pop(lua, 1);
    return 0;
}

static int cmain_configure(char *script) {
    lua_State *lua;
    lua = luaL_newstate();
    if (!lua)
        return 1;
    lua_atpanic(lua, cmain_panic);
    luaL_openlibs(lua);
    if (luaL_dofile(lua, script)) {
        VLOG_ERROR("Cannot run script: %s", lua_tostring(lua, -1));
        goto cleanup;
    }
    if (!lua_istable(lua, -1)) {
        VLOG_ERROR("Invalid return value of main module");
        goto cleanup;
    }
    lua_getfield(lua, -1, "configure");
    if (!lua_isfunction(lua, -1) || lua_pcall(lua, 0, LUA_MULTRET, 0)) {
        VLOG_ERROR("Cannot run configure() function: %s",
                   lua_tostring(lua, -1));
        goto cleanup;
    }
    if (!lua_istable(lua, -1)) {
        VLOG_ERROR("Invalid return value of configure() function");
        goto cleanup;
    }
    #define GETI(x) cmain_get_int(lua, #x, &g_cmain.x)
    #define GETA(x) cmain_get_int_array(lua, #x, &g_cmain.x##_len, &g_cmain.x)
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

static void cmain_done(void) {
    vao_done();
    cprog_done();
    crbuf_done();
    crender_done();

    if (g_cmain.lua)
        lua_close(g_cmain.lua);
    if (g_cmain.main_mpool) {
        pmem_free(g_cmain.main_mpool);
        g_cmain.main_mpool = 0;
    }
    if (g_cmain.physics_mpool) {
        pmem_free(g_cmain.physics_mpool);
        g_cmain.physics_mpool = 0;
    }
    if (g_cmain.thread_mpool) {
        pmem_free(g_cmain.thread_mpool);
        g_cmain.thread_mpool = 0;
    }
    cbuf_done();
    vector_done();
    cmatrix_done();
    cphysics_done();
    if (g_cmain.mpool) {
        VLOG_INFO("");
        VLOG_INFO("Main");
        cmpool_report(g_cmain.mpool);
        cmpool_destroy(g_cmain.mpool);
    }
    cthread_done();

    SDL_Quit();
}

static int cmain_init(int argc, char **argv) {
    char *script;
    if (argc < 2) {
        VLOG_INFO("Usage: %s <script.lua>", argv[0]);
        return 1;
    }
    script = argv[1];
    if (cmain_configure(script)) {
        VLOG_ERROR("Cannot configure engine");
        return 1;
    }
    if (SDL_Init(SDL_INIT_EVERYTHING)) {
        VLOG_ERROR("Cannot init SDL");
        return 1;
    }
    g_cmain.mpool = cmpool_create(g_cmain.main_mpool,
                                  g_cmain.main_mpool + g_cmain.main_mpool_len/2,
                                  g_cmain.main_mpool_len / 2);
    if (!g_cmain.mpool) {
        VLOG_ERROR("Cannot create main memory pool");
        return 1;
    }
    g_cmain.lua = lua_newstate(cmain_lua_alloc, 0);
    if (!g_cmain.lua) {
        VLOG_ERROR("Cannot create Lua state");
        return 1;
    }
    lua_atpanic(g_cmain.lua, cmain_panic);
    luaL_openlibs(g_cmain.lua);

    clog_reg_thread(g_cmain.lua);
    cinput_init(g_cmain.lua);

    if (timer_init(g_cmain.lua)) {
        VLOG_ERROR("Cannot init timer"); 
        return 1;
    }
    if (cthread_init(g_cmain.lua, g_cmain.thread_count, g_cmain.thread_mpool,
    g_cmain.thread_mpool + g_cmain.thread_mpool_len / 2,
    g_cmain.thread_mpool_len / 2)) {
        VLOG_ERROR("Cannot init threads"); 
        return 1;
    } 
    if (cphysics_init(g_cmain.lua, g_cmain.world_count, g_cmain.colshape_count,
    g_cmain.rigidbody_count, g_cmain.vehicle_count, g_cmain.physics_mpool,
    g_cmain.physics_mpool + g_cmain.physics_mpool_len / 2,
    g_cmain.physics_mpool_len / 2)) {
        VLOG_ERROR("Cannot init physics"); 
        return 1;
    } 
    if (cbuf_init(g_cmain.lua, g_cmain.buf_size)) {
        VLOG_ERROR("Cannot init buffers");
        return 1;
    }
    if (vector_init(g_cmain.lua, g_cmain.vector_count, g_cmain.vector_nesting)) {
        VLOG_ERROR("Cannot init vectors");
        return 1;
    }
    if (cmatrix_init(g_cmain.lua, g_cmain.matrix_count,
    g_cmain.matrix_nesting)) {
        VLOG_ERROR("Cannot init matrices");
        return 1;
    }
    if (crender_init(g_cmain.lua, g_cmain.screen_width,
    g_cmain.screen_height, g_cmain.full_screen)) {
        VLOG_ERROR("Cannot init render"); 
        return 1;
    } 
    if (cprog_init(g_cmain.lua, g_cmain.prog_count)) {
        VLOG_ERROR("Cannot init shader programs"); 
        return 1;
    }
    if (crbuf_init(g_cmain.lua, g_cmain.rbuf_count)) {
        VLOG_ERROR("Cannot init render buffers"); 
        return 1;
    }
    if (vao_init(g_cmain.lua, g_cmain.vao_count)) {
        VLOG_ERROR("Cannot init vertex array objects");
        return 1;
    }
    if (luaL_dofile(g_cmain.lua, script)) {
        VLOG_ERROR("Cannot run script: %s", lua_tostring(g_cmain.lua, -1));
        return 1;
    }
    return 0;
}

static void cmain_run(void) {
    VLOG_INFO("Game loop start");
    if (!lua_istable(g_cmain.lua, -1))
        VLOG_ERROR("Invalid return value of main module");
    else {
        lua_getfield(g_cmain.lua, -1, "run");
        if (!lua_isfunction(g_cmain.lua, -1))
            VLOG_ERROR("Cannot find run() function");
        else if (lua_pcall(g_cmain.lua, 0, LUA_MULTRET, 0))
            VLOG_ERROR("Error while executing run() function: %s",
                       lua_tostring(g_cmain.lua, -1));
    }
    VLOG_INFO("Game loop finish");
}

int main(int argc, char **argv) {
    if (vlog_init(stderr))
        return EXIT_FAILURE;
    VLOG_INFO("Engine start");
    if (!setjmp(g_cmain.panic))
        if (!cmain_init(argc, argv))
            cmain_run();
    cmain_done();
    VLOG_INFO("Engine finish");
    vlog_done();
    return EXIT_SUCCESS;
}

