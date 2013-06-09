#include "thread.h"
#include "mpool.h"
#include "../mp/atomic.h"
#include "../mp/thread.h"
#include "../platform/timer.h"
#include "../util/util.h"
#include "lauxlib.h"
#include "lualib.h"
#include <stdio.h>
#include <string.h>
#include <setjmp.h>

/*
 * Worker threads.
 * Every worker thread has its own Lua state.
 * Main thread sends Lua chunk to run in worker thread.
 * Main and worker thread communicate with each other by exchanging strings.
 * Main thread can query current state of worker thread.
 */

static const size_t THREAD_DATA_SIZE = 512;

enum thread_state_e {
    THREAD_IDLE,        /* Waiting for main thread to send a new Lua chunk. */
    THREAD_STARTING,
    THREAD_RUNNING,     /* Running current Lua chunk. */
    THREAD_RESPONDING,  /* Waiting for main thread to receive response. */
    THREAD_REQUESTING,
    THREAD_RECEIVING,
    THREAD_ERROR,
    THREAD_DONE
};

struct thread_data_t {
    struct thread_mutex_t *mutex;
    struct thread_cond_t *engage;
    struct thread_t *thread;
    lua_State *lua;
    struct mpool_t *mpool;
    const char *resp;
    size_t respsize;
    struct atomic_int_t *state;
    jmp_buf quitjmp;
};

struct threads_t {
    int count;
    char *pool;
    const char *fn, *req;
    size_t fnsize, reqsize;
    struct atomic_int_t *quit;
    jmp_buf panic;
};

static struct threads_t g_threads;

static void thread_loop(void *data) {
    /*
     * Wait until main thread sends Lua chunk.
     * Run received Lua chunk in local environment.
     * Repeat until quit was requested.
     */
    struct thread_data_t *thread = data;
    atomic_int_store(thread->state, THREAD_IDLE);
    thread_mutex_lock(thread->mutex);
    setjmp(thread->quitjmp);
    while (!atomic_int_load(g_threads.quit)) {
        thread_cond_wait(thread->engage, thread->mutex);
        if (atomic_int_load(thread->state) == THREAD_STARTING) {
            if (luaL_loadbuffer(thread->lua, g_threads.fn,
            g_threads.fnsize, "threadfn")) {
                fprintf(stderr, "thread_loop load: %s\n",
                        lua_tostring(thread->lua, -1));
                atomic_int_store(thread->state, THREAD_ERROR);
            }
            else {
                atomic_int_store(thread->state, THREAD_RUNNING);
                if (!lua_pcall(thread->lua, 0, LUA_MULTRET, 0))
                    atomic_int_store(thread->state, THREAD_IDLE);
                else {
                    fprintf(stderr, "thread_loop call: %s\n",
                            lua_tostring(thread->lua, -1));
                    atomic_int_store(thread->state, THREAD_ERROR);
                }
            }
        }
    }
    thread_mutex_unlock(thread->mutex);
    atomic_int_store(thread->state, THREAD_DONE);
}

static struct thread_data_t * thread_get(int ti) {
    if (ti >= 0 && ti < g_threads.count)
        return (struct thread_data_t*)(g_threads.pool + THREAD_DATA_SIZE * ti);
    else
        return 0;
}

static void * thread_lua_alloc
(void *ud, void *ptr, size_t osize, size_t nsize) {
    struct mpool_t *mpool = ud;
    void *newptr;
    if (!osize && !nsize)
        return 0;
    else if (!osize && nsize)
        return mpool_alloc(mpool, nsize);
    else if (osize && !nsize) {
        mpool_free(ptr);
        return 0;
    }
    if (!(newptr = mpool_alloc(mpool, nsize)))
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

static int thread_lua_panic(lua_State *lua) {
    fprintf(stderr, "Thread lua panic: %s\n", lua_tostring(lua, -1));
    longjmp(g_threads.panic, 1);
}

static struct thread_data_t * thread_current(lua_State *lua) {
    struct thread_data_t *thread;
    lua_pushlightuserdata(lua, &g_threads);
    lua_gettable(lua, LUA_REGISTRYINDEX);
    thread = lua_touserdata(lua, -1);
    lua_pop(lua, 1);
    return thread;
}

static int api_thread_run(lua_State *lua) {
    /* Send Lua chunk to run in blocked worker thread. */
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 2 ||
    !lua_isnumber(lua, 1) || !lua_isstring(lua, 2)) {
        lua_pushstring(lua, "api_thread_run: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (!(thread = thread_get(lua_tointeger(lua, 1)))) {
        lua_pushstring(lua, "api_thread_run: invalid thread");
        lua_error(lua);
        return 0;
    }
    if (atomic_int_load(thread->state) != THREAD_IDLE) {
        lua_pushstring(lua, "api_thread_run: invalid state");
        lua_error(lua);
        return 0;
    }
    g_threads.fn = lua_tolstring(lua, 2, &g_threads.fnsize);
    atomic_int_store(thread->state, THREAD_STARTING);
    while (atomic_int_load(thread->state) == THREAD_STARTING)
        thread_cond_signal(thread->engage);
    g_threads.fn = 0;
    g_threads.fnsize = 0;
    lua_pop(lua, 2);
    if (atomic_int_load(thread->state) == THREAD_ERROR) {
        lua_pushstring(lua, "api_thread_run: thread error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_thread_request(lua_State *lua) {
    /* Send a string to blocked worker thread, return its response. */
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 2 ||
    !lua_isnumber(lua, 1) || !lua_isstring(lua, 2)) {
        lua_pushstring(lua, "api_thread_request: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (!(thread = thread_get(lua_tointeger(lua, 1)))) {
        lua_pushstring(lua, "api_thread_request: invalid thread");
        lua_error(lua);
        return 0;
    }
    if (atomic_int_load(thread->state) != THREAD_RESPONDING) {
        lua_pushstring(lua, "api_thread_request: invalid state");
        lua_error(lua);
        return 0;
    }
    g_threads.req = lua_tolstring(lua, 2, &g_threads.reqsize);
    lua_pushlstring(lua, thread->resp, thread->respsize);
    atomic_int_store(thread->state, THREAD_REQUESTING);
    while (atomic_int_load(thread->state) == THREAD_REQUESTING)
        thread_cond_signal(thread->engage);
    while (atomic_int_load(thread->state) == THREAD_RECEIVING);
    g_threads.req = 0;
    g_threads.reqsize = 0;
    return 1;
}

static int api_thread_respond(lua_State *lua) {
    /* Wait for the main thread, send a string to it, return response. */
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 1 || !lua_isstring(lua, 1)) {
        lua_pushstring(lua, "api_thread_respond: incorrect argument");
        lua_error(lua);
        return 0;
    }
    thread = thread_current(lua);
    if (atomic_int_load(thread->state) != THREAD_RUNNING) {
        lua_pushstring(lua, "api_thread_respond: invalid state");
        lua_error(lua);
        return 0;
    }
    thread->resp = lua_tolstring(lua, 1, &thread->respsize);
    atomic_int_store(thread->state, THREAD_RESPONDING);
    thread_cond_wait(thread->engage, thread->mutex);
    while (atomic_int_load(thread->state) != THREAD_REQUESTING) {
        if (atomic_int_load(g_threads.quit)) {
            longjmp(thread->quitjmp, 1);
        }
    }
    atomic_int_store(thread->state, THREAD_RECEIVING);
    lua_pop(lua, 1);
    thread->resp = 0;
    thread->respsize = 0;
    lua_pushlstring(thread->lua, g_threads.req, g_threads.reqsize);
    atomic_int_store(thread->state, THREAD_RUNNING);
    return 1;
}

static int api_thread_state(lua_State *lua) {
    /* Returns worker thread state. */
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1)) {
        lua_pushstring(lua, "api_thread_state: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (!(thread = thread_get(lua_tointeger(lua, 1)))) {
        lua_pushstring(lua, "api_thread_state: invalid thread");
        lua_error(lua);
        return 0;
    }
    lua_pop(lua, 1);
    lua_pushinteger(lua, atomic_int_load(thread->state));
    return 1;
}

static void thread_reg_main(lua_State *lua) {
    #define REGF(x) lua_register(lua, #x, x)
    REGF(api_thread_run);
    REGF(api_thread_request);
    REGF(api_thread_state);
    #undef REGF
    #define REGN(x) lua_pushinteger(lua, x); lua_setglobal(lua, "API_"#x);
    REGN(THREAD_IDLE);
    REGN(THREAD_RUNNING);
    REGN(THREAD_RESPONDING);
    REGN(THREAD_ERROR);
    #undef REGN
}

static void thread_reg(lua_State *lua) {
    lua_register(lua, "api_thread_respond", api_thread_respond);
}

int thread_init
(lua_State *lua, int count, const int msizes[], const int mcounts[], int mlen) {
    struct thread_data_t *thread;
    lua_CFunction old_panic;

    if (sizeof(struct thread_data_t) > THREAD_DATA_SIZE) {
        fprintf(stderr, "Invalid sizes:\nsizeof(struct thread_data_t) == %i\n",
                (int)sizeof(struct thread_data_t));
        return 1;
    }
    g_threads.count = count;
    g_threads.pool = util_malloc(THREAD_DATA_SIZE, THREAD_DATA_SIZE * count);
    if (!g_threads.pool)
        return 1;
    memset(g_threads.pool, 0, THREAD_DATA_SIZE * count);
    if (!(g_threads.quit = atomic_int_create()))
        return 1;
    atomic_int_store(g_threads.quit, 0);
    for (int i = 0; i < count; ++i) {
        thread = thread_get(i);
        if (!(thread->mpool = mpool_create(msizes, mcounts, mlen)) ||
        !(thread->lua = lua_newstate(thread_lua_alloc, thread->mpool)))
            return 1;

        /* Load libraries, save current thread pointer to Lua registry. */
        if (setjmp(g_threads.panic))
            return 1;
        old_panic = lua_atpanic(thread->lua, thread_lua_panic);
        luaL_openlibs(thread->lua);
        lua_pushlightuserdata(thread->lua, &g_threads);
        lua_pushlightuserdata(thread->lua, thread);
        lua_settable(thread->lua, LUA_REGISTRYINDEX);
        lua_atpanic(thread->lua, old_panic);

        if (!(thread->mutex = thread_mutex_create()) ||
        !(thread->engage = thread_cond_create()) ||
        !(thread->state = atomic_int_create()) ||
        !(thread->thread = thread_create(thread_loop, thread)))
            return 1;
        thread_reg(thread->lua);
    }
    thread_reg_main(lua);
    return 0;
}

void thread_done(void) {
    struct thread_data_t *thread;

    if (g_threads.pool) {
        if (g_threads.quit)
            atomic_int_store(g_threads.quit, 1);
        for (int i = 0; i < g_threads.count; ++i) {
            thread = thread_get(i);
            if (thread->thread) {
                if (atomic_int_load(thread->state) != THREAD_IDLE)
                    fprintf(stderr, "\nThread %i is still active\n", i);
                if (thread->engage)
                    while (atomic_int_load(thread->state) != THREAD_DONE)
                        thread_cond_signal(thread->engage);
                thread_destroy(thread->thread);
            }
            if (thread->mutex)
                thread_mutex_destroy(thread->mutex);
            if (thread->engage)
                thread_cond_destroy(thread->engage);
            if (thread->lua)
                lua_close(thread->lua);
            if (thread->mpool) {
                fprintf(stderr, "\nThread %i memory pool:\n", i);
                mpool_destroy(thread->mpool);
            }
            if (thread->state)
                atomic_int_destroy(thread->state);
        }
        util_free(g_threads.pool);
        g_threads.pool = 0;
    }
    if (g_threads.quit)
        atomic_int_destroy(g_threads.quit);
    g_threads.quit = 0;
}

