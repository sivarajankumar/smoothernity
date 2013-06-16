#include "cthread.h"
#include "cmpool.h"
#include "util.h"
#include "uatomic.h"
#include "uthread.h"
#include "pmem.h"
#include "lauxlib.h"
#include "lualib.h"
#include "vlog.h"
#include <setjmp.h>
#include <string.h>

/*
 * Worker threads.
 * Every worker thread has its own Lua state.
 * Main thread sends Lua chunk to run in worker thread.
 * Main and worker thread communicate with each other by exchanging strings.
 * Main thread can query current state of worker thread.
 */

#define CTHREAD_SIZE 512

enum cthread_e {
    CTHREAD_IDLE,        /* Waiting for main thread to send a new Lua chunk. */
    CTHREAD_STARTING,
    CTHREAD_RUNNING,     /* Running current Lua chunk. */
    CTHREAD_RESPONDING,  /* Waiting for main thread to receive response. */
    CTHREAD_REQUESTING,
    CTHREAD_RECEIVING,
    CTHREAD_ERROR,
    CTHREAD_DONE
};

struct cthread_t {
    struct uthread_mutex_t *mutex;
    struct uthread_cond_t *engage;
    struct uthread_t *thread;
    lua_State *lua;
    struct cmpool_t *mpool;
    const char *resp;
    size_t respsize;
    struct uatomic_int_t *state;
    jmp_buf quitjmp;
};

struct cthreads_t {
    int count;
    char *pool;
    const char *fn, *req;
    size_t fnsize, reqsize;
    struct uatomic_int_t *quit;
    jmp_buf panic;
};

_Static_assert(sizeof(struct cthread_t) <= CTHREAD_SIZE,
               "Invalid cthread_t size");

static struct cthreads_t g_cthreads;

static void cthread_loop(void *data) {
    /*
     * Wait until main thread sends Lua chunk.
     * Run received Lua chunk in local environment.
     * Repeat until quit was requested.
     */
    struct cthread_t *thread = data;
    uatomic_int_store(thread->state, CTHREAD_IDLE);
    uthread_mutex_lock(thread->mutex);
    setjmp(thread->quitjmp);
    while (!uatomic_int_load(g_cthreads.quit)) {
        uthread_cond_wait(thread->engage, thread->mutex);
        if (uatomic_int_load(thread->state) == CTHREAD_STARTING) {
            if (luaL_loadbuffer(thread->lua, g_cthreads.fn,
            g_cthreads.fnsize, "threadfn")) {
                VLOG_ERROR("load: %s", lua_tostring(thread->lua, -1));
                uatomic_int_store(thread->state, CTHREAD_ERROR);
            }
            else {
                uatomic_int_store(thread->state, CTHREAD_RUNNING);
                if (!lua_pcall(thread->lua, 0, LUA_MULTRET, 0))
                    uatomic_int_store(thread->state, CTHREAD_IDLE);
                else {
                    VLOG_ERROR("call: %s", lua_tostring(thread->lua, -1));
                    uatomic_int_store(thread->state, CTHREAD_ERROR);
                }
            }
        }
    }
    uthread_mutex_unlock(thread->mutex);
    uatomic_int_store(thread->state, CTHREAD_DONE);
}

static struct cthread_t * cthread_get(int ti) {
    if (ti >= 0 && ti < g_cthreads.count)
        return (struct cthread_t*)(g_cthreads.pool + CTHREAD_SIZE * ti);
    else
        return 0;
}

static void * cthread_lua_alloc
(void *ud, void *ptr, size_t osize, size_t nsize) {
    struct cmpool_t *mpool = ud;
    void *newptr;
    if (!osize && !nsize)
        return 0;
    else if (!osize && nsize)
        return cmpool_alloc(mpool, nsize);
    else if (osize && !nsize) {
        cmpool_free(ptr);
        return 0;
    }
    if (!(newptr = cmpool_alloc(mpool, nsize)))
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

static int cthread_lua_panic(lua_State *lua) {
    VLOG_ERROR("Lua panic: %s", lua_tostring(lua, -1));
    longjmp(g_cthreads.panic, 1);
}

static struct cthread_t * cthread_current(lua_State *lua) {
    struct cthread_t *thread;
    lua_pushlightuserdata(lua, &g_cthreads);
    lua_gettable(lua, LUA_REGISTRYINDEX);
    thread = lua_touserdata(lua, -1);
    lua_pop(lua, 1);
    return thread;
}

static int api_thread_run(lua_State *lua) {
    /* Send Lua chunk to run in blocked worker thread. */
    struct cthread_t *thread;
    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !lua_isstring(lua, 2)) {
        lua_pushstring(lua, "api_thread_run: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (!(thread = cthread_get(lua_tointeger(lua, 1)))) {
        lua_pushstring(lua, "api_thread_run: invalid thread");
        lua_error(lua);
        return 0;
    }
    if (uatomic_int_load(thread->state) != CTHREAD_IDLE) {
        lua_pushstring(lua, "api_thread_run: invalid state");
        lua_error(lua);
        return 0;
    }
    g_cthreads.fn = lua_tolstring(lua, 2, &g_cthreads.fnsize);
    uatomic_int_store(thread->state, CTHREAD_STARTING);
    while (uatomic_int_load(thread->state) == CTHREAD_STARTING)
        uthread_cond_signal(thread->engage);
    g_cthreads.fn = 0;
    g_cthreads.fnsize = 0;
    lua_pop(lua, 2);
    if (uatomic_int_load(thread->state) == CTHREAD_ERROR) {
        lua_pushstring(lua, "api_thread_run: thread error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_thread_request(lua_State *lua) {
    /* Send a string to blocked worker thread, return its response. */
    struct cthread_t *thread;
    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !lua_isstring(lua, 2)) {
        lua_pushstring(lua, "api_thread_request: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (!(thread = cthread_get(lua_tointeger(lua, 1)))) {
        lua_pushstring(lua, "api_thread_request: invalid thread");
        lua_error(lua);
        return 0;
    }
    if (uatomic_int_load(thread->state) != CTHREAD_RESPONDING) {
        lua_pushstring(lua, "api_thread_request: invalid state");
        lua_error(lua);
        return 0;
    }
    g_cthreads.req = lua_tolstring(lua, 2, &g_cthreads.reqsize);
    lua_pushlstring(lua, thread->resp, thread->respsize);
    uatomic_int_store(thread->state, CTHREAD_REQUESTING);
    while (uatomic_int_load(thread->state) == CTHREAD_REQUESTING)
        uthread_cond_signal(thread->engage);
    while (uatomic_int_load(thread->state) == CTHREAD_RECEIVING);
    g_cthreads.req = 0;
    g_cthreads.reqsize = 0;
    return 1;
}

static int api_thread_respond(lua_State *lua) {
    /* Wait for the main thread, send a string to it, return response. */
    struct cthread_t *thread = cthread_current(lua);
    if (lua_gettop(lua) != 1 || !lua_isstring(lua, 1)) {
        lua_pushstring(lua, "api_thread_respond: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (uatomic_int_load(thread->state) != CTHREAD_RUNNING) {
        lua_pushstring(lua, "api_thread_respond: invalid state");
        lua_error(lua);
        return 0;
    }
    thread->resp = lua_tolstring(lua, 1, &thread->respsize);
    uatomic_int_store(thread->state, CTHREAD_RESPONDING);
    uthread_cond_wait(thread->engage, thread->mutex);
    while (uatomic_int_load(thread->state) != CTHREAD_REQUESTING) {
        if (uatomic_int_load(g_cthreads.quit)) {
            longjmp(thread->quitjmp, 1);
        }
    }
    uatomic_int_store(thread->state, CTHREAD_RECEIVING);
    lua_pop(lua, 1);
    thread->resp = 0;
    thread->respsize = 0;
    lua_pushlstring(thread->lua, g_cthreads.req, g_cthreads.reqsize);
    uatomic_int_store(thread->state, CTHREAD_RUNNING);
    return 1;
}

static int api_thread_state(lua_State *lua) {
    /* Returns worker thread state. */
    struct cthread_t *thread;
    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_thread_state: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (!(thread = cthread_get(lua_tointeger(lua, 1)))) {
        lua_pushstring(lua, "api_thread_state: invalid thread");
        lua_error(lua);
        return 0;
    }
    lua_pop(lua, 1);
    lua_pushinteger(lua, uatomic_int_load(thread->state));
    return 1;
}

static void cthread_reg_main(lua_State *lua) {
    #define REGF(x) lua_register(lua, #x, x)
    REGF(api_thread_run);
    REGF(api_thread_request);
    REGF(api_thread_state);
    #undef REGF
    #define REGN(x) lua_pushinteger(lua, C##x); lua_setglobal(lua, "API_"#x);
    REGN(THREAD_IDLE);
    REGN(THREAD_RUNNING);
    REGN(THREAD_RESPONDING);
    REGN(THREAD_ERROR);
    #undef REGN
}

static void cthread_reg(lua_State *lua) {
    lua_register(lua, "api_thread_respond", api_thread_respond);
}

int cthread_init
(lua_State *lua, int count, const int msizes[], const int mcounts[], int mlen) {
    struct cthread_t *thread;
    lua_CFunction old_panic;

    g_cthreads.count = count;
    g_cthreads.pool = pmem_alloc(PMEM_ALIGNOF(struct cthread_t),
                                 CTHREAD_SIZE * count);
    if (!g_cthreads.pool)
        return 1;
    for (int i = 0; i < count; ++i) {
        thread = cthread_get(i);
        thread->mutex = 0;
        thread->engage = 0;
        thread->thread = 0;
        thread->lua = 0;
        thread->mpool = 0;
        thread->state = 0;
    }
    if (!(g_cthreads.quit = uatomic_int_create()))
        return 1;
    uatomic_int_store(g_cthreads.quit, 0);
    for (int i = 0; i < count; ++i) {
        thread = cthread_get(i);
        if (!(thread->mpool = cmpool_create(msizes, mcounts, mlen)) ||
        !(thread->lua = lua_newstate(cthread_lua_alloc, thread->mpool)))
            return 1;

        /* Register API, load libraries, save thread pointer to Lua registry. */
        if (setjmp(g_cthreads.panic))
            return 1;
        old_panic = lua_atpanic(thread->lua, cthread_lua_panic);
        cthread_reg(thread->lua);
        luaL_openlibs(thread->lua);
        lua_pushlightuserdata(thread->lua, &g_cthreads);
        lua_pushlightuserdata(thread->lua, thread);
        lua_settable(thread->lua, LUA_REGISTRYINDEX);
        lua_atpanic(thread->lua, old_panic);

        if (!(thread->mutex = uthread_mutex_create()) ||
        !(thread->engage = uthread_cond_create()) ||
        !(thread->state = uatomic_int_create()) ||
        !(thread->thread = uthread_create(cthread_loop, thread)))
            return 1;
    }
    cthread_reg_main(lua);
    return 0;
}

void cthread_done(void) {
    struct cthread_t *thread;

    if (g_cthreads.pool) {
        if (g_cthreads.quit)
            uatomic_int_store(g_cthreads.quit, 1);
        for (int i = 0; i < g_cthreads.count; ++i) {
            VLOG_INFO("");
            VLOG_INFO("Thread %i", i);
            thread = cthread_get(i);
            if (thread->thread) {
                if (uatomic_int_load(thread->state) != CTHREAD_IDLE)
                    VLOG_ERROR("Thread is still active");
                if (thread->engage)
                    while (uatomic_int_load(thread->state) != CTHREAD_DONE)
                        uthread_cond_signal(thread->engage);
                uthread_destroy(thread->thread);
            }
            if (thread->mutex)
                uthread_mutex_destroy(thread->mutex);
            if (thread->engage)
                uthread_cond_destroy(thread->engage);
            if (thread->lua)
                lua_close(thread->lua);
            if (thread->mpool) {
                cmpool_report(thread->mpool);
                cmpool_destroy(thread->mpool);
            }
            if (thread->state)
                uatomic_int_destroy(thread->state);
        }
        pmem_free(g_cthreads.pool);
        g_cthreads.pool = 0;
    }
    if (g_cthreads.quit)
        uatomic_int_destroy(g_cthreads.quit);
    g_cthreads.quit = 0;
}

