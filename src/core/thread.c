#include "thread.h"
#include "mpool.h"
#include "shell.h"
#include "buf.h"
#include "timer.h"
#include "rbuf.h"
#include "../thread/thread.h"
#include "../platform/timer.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>
#include "lauxlib.h"
#include "lualib.h"

static const size_t THREAD_DATA_SIZE = 128;

enum thread_state_e
{
    THREAD_IDLE,
    THREAD_RUNNING,
    THREAD_RESPONDING,
    THREAD_ERROR
};

struct thread_data_t
{
    float time;
    float time_begin;
    struct thread_mutex_t *mutex;
    struct thread_cond_t *engage;
    struct thread_t *thread;
    lua_State *lua;
    struct mpool_t *mpool;
    const char *fn;
    size_t fnsize;
    const char *req;
    size_t reqsize;
    const char *resp;
    size_t respsize;
    enum thread_state_e state;
};

struct threads_t
{
    int count;
    int quit;
    char *pool;
    struct thread_mutex_t *mutex;
    struct thread_cond_t *engage;
};

static struct threads_t g_threads;

static void thread_loop(void *data)
{
    int res;
    struct thread_data_t *thread = data;
    thread_mutex_unlock(thread->mutex);
    thread_mutex_lock(thread->mutex);
    while (g_threads.quit == 0)
    {
        thread_cond_wait(thread->engage, thread->mutex);
        if (thread->state == THREAD_IDLE && thread->fn != 0)
        {
            if (luaL_loadbuffer(thread->lua, thread->fn,
                                thread->fnsize, "threadfn") != 0)
            {
                fprintf(stderr, "thread_loop load: %s\n",
                        lua_tostring(thread->lua, -1));
                thread->state = THREAD_ERROR;
            }
            else
                thread->state = THREAD_RUNNING;
            thread->fn = 0;
            thread->fnsize = 0;
            thread_mutex_lock(g_threads.mutex);
            thread_mutex_unlock(g_threads.mutex);
            thread_cond_signal(g_threads.engage);

            thread->time_begin = pfm_timer_get();
            thread_mutex_unlock(thread->mutex);
            res = lua_pcall(thread->lua, 0, LUA_MULTRET, 0);
            thread_mutex_lock(thread->mutex);
            thread->time += pfm_timer_get() - thread->time_begin;

            if (res == 0)
                thread->state = THREAD_IDLE;
            else
            {
                fprintf(stderr, "thread_loop call: %s\n",
                        lua_tostring(thread->lua, -1));
                thread->state = THREAD_ERROR;
            }
        }
    }
    thread_mutex_unlock(thread->mutex);
}

static struct thread_data_t * thread_get(int ti)
{
    if (ti >= 0 && ti < g_threads.count)
        return (struct thread_data_t*)(g_threads.pool + THREAD_DATA_SIZE * ti);
    else
        return 0;
}

static void * thread_lua_alloc(void *ud, void *ptr, size_t osize, size_t nsize)
{
    struct mpool_t *mpool = ud;
    void *newptr;
    if (osize == 0 && nsize == 0)
        return 0;
    else if (osize == 0 && nsize > 0)
        return mpool_alloc(mpool, nsize);
    else if (osize > 0 && nsize == 0)
    {
        mpool_free(ptr);
        return 0;
    }
    newptr = mpool_alloc(mpool, nsize);
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

static int thread_lua_panic(lua_State *lua)
{
    fprintf(stderr, "Thread lua panic: %s\n", lua_tostring(lua, -1));
    return 0;
}

static int api_thread_run(lua_State *lua)
{
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isstring(lua, 2))
    {
        lua_pushstring(lua, "api_thread_run: incorrect argument");
        lua_error(lua);
        return 0;
    }
    thread = thread_get(lua_tointeger(lua, 1));
    if (thread == 0)
    {
        lua_pop(lua, 2);
        lua_pushstring(lua, "api_thread_run: invalid thread");
        lua_error(lua);
        return 0;
    }
    thread_mutex_lock(thread->mutex);
    if (thread->state != THREAD_IDLE)
    {
        thread_mutex_unlock(thread->mutex);
        lua_pop(lua, 2);
        lua_pushstring(lua, "api_thread_run: invalid state");
        lua_error(lua);
        return 0;
    }
    thread->fn = lua_tolstring(lua, 2, &thread->fnsize);
    thread_mutex_unlock(thread->mutex);
    thread_mutex_lock(g_threads.mutex);
    thread_cond_signal(thread->engage);
    thread_cond_wait(g_threads.engage, g_threads.mutex);
    thread_mutex_unlock(g_threads.mutex);
    lua_pop(lua, 2);
    if (thread->state == THREAD_ERROR)
    {
        lua_pushstring(lua, "api_thread_run: thread error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_thread_timings(lua_State *lua)
{
    int i;
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_thread_timings: incorrect argument");
        lua_error(lua);
        return 0;
    }
    for (i = 0; i < g_threads.count; ++i)
    {
        thread = thread_get(i);
        thread_mutex_lock(thread->mutex);
        if (thread->state == THREAD_RUNNING)
            thread->time += pfm_timer_get() - thread->time_begin;
        lua_pushnumber(lua, thread->time);
        thread->time = 0;
        thread->time_begin = pfm_timer_get();
        thread_mutex_unlock(thread->mutex);
    }
    return g_threads.count;
}

static int api_thread_request(lua_State *lua)
{
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isstring(lua, 2))
    {
        lua_pushstring(lua, "api_thread_request: incorrect argument");
        lua_error(lua);
        return 0;
    }
    thread = thread_get(lua_tointeger(lua, 1));
    if (thread == 0)
    {
        lua_pop(lua, 2);
        lua_pushstring(lua, "api_thread_request: invalid thread");
        lua_error(lua);
        return 0;
    }
    thread_mutex_lock(thread->mutex);
    if (thread->state != THREAD_RESPONDING)
    {
        thread_mutex_unlock(thread->mutex);
        lua_pop(lua, 2);
        lua_pushstring(lua, "api_thread_request: invalid state");
        lua_error(lua);
        return 0;
    }
    thread->req = lua_tolstring(lua, 2, &thread->reqsize);
    lua_pushlstring(lua, thread->resp, thread->respsize);
    thread_mutex_unlock(thread->mutex);

    thread_mutex_lock(g_threads.mutex);
    thread_cond_signal(thread->engage);
    thread_cond_wait(g_threads.engage, g_threads.mutex);
    thread_mutex_unlock(g_threads.mutex);
    return 1;
}

static int api_thread_respond(lua_State *lua)
{
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isstring(lua, 2))
    {
        lua_pushstring(lua, "api_thread_respond: incorrect argument");
        lua_error(lua);
        return 0;
    }
    thread = thread_get(lua_tointeger(lua, 1));
    if (thread == 0)
    {
        lua_pop(lua, 2);
        lua_pushstring(lua, "api_thread_respond: invalid thread");
        lua_error(lua);
        return 0;
    }
    thread_mutex_lock(thread->mutex);
    if (thread->state != THREAD_RUNNING)
    {
        thread_mutex_unlock(thread->mutex);
        lua_pop(lua, 2);
        lua_pushstring(lua, "api_thread_respond: invalid state");
        lua_error(lua);
        return 0;
    }
    thread->resp = lua_tolstring(lua, 2, &thread->respsize);
    thread->state = THREAD_RESPONDING;
    thread->time += pfm_timer_get() - thread->time_begin;
    thread_cond_wait(thread->engage, thread->mutex);
    lua_pop(lua, 2);
    thread->resp = 0;
    thread->respsize = 0;
    if (thread->req == 0)
    {
        thread_mutex_unlock(thread->mutex);
        lua_pushstring(lua, "api_thread_respond: invalid request");
        lua_error(lua);
        return 0;
    }
    lua_pushlstring(thread->lua, thread->req, thread->reqsize);
    thread->req = 0;
    thread->reqsize = 0;
    thread->state = THREAD_RUNNING;
    thread->time_begin = pfm_timer_get();
    thread_mutex_unlock(thread->mutex);

    thread_mutex_lock(g_threads.mutex);
    thread_mutex_unlock(g_threads.mutex);
    thread_cond_signal(g_threads.engage);
    return 1;
}

static int api_thread_state(lua_State *lua)
{
    struct thread_data_t *thread;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_thread_state: incorrect argument");
        lua_error(lua);
        return 0;
    }
    thread = thread_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (thread == 0)
    {
        lua_pushstring(lua, "api_thread_state: invalid thread");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, thread->state);
    return 1;
}

static void thread_reg_main(lua_State *lua)
{
    lua_register(lua, "api_thread_run", api_thread_run);
    lua_register(lua, "api_thread_request", api_thread_request);
    lua_register(lua, "api_thread_timings", api_thread_timings);
    lua_register(lua, "api_thread_state", api_thread_state);

    #define LUA_PUBLISH(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);

    LUA_PUBLISH(THREAD_IDLE);
    LUA_PUBLISH(THREAD_RUNNING);
    LUA_PUBLISH(THREAD_RESPONDING);
    LUA_PUBLISH(THREAD_ERROR);
}

static void thread_reg(lua_State *lua)
{
    lua_register(lua, "api_thread_respond", api_thread_respond);
    shell_reg_thread(lua);
    buf_reg_thread(lua);
    timer_reg_thread(lua);
    rbuf_reg_thread(lua);
}

int thread_init(lua_State *lua, int count, const int msizes[],
                const int mcounts[], int mlen)
{
    struct thread_data_t *thread;
    int i;
    if (sizeof(struct thread_data_t) > THREAD_DATA_SIZE)
    {
        fprintf(stderr, "Invalid sizes:\nsizeof(struct thread_data_t) == %i\n",
                (int)sizeof(struct thread_data_t));
        return 1;
    }
    g_threads.pool = util_malloc(THREAD_DATA_SIZE, THREAD_DATA_SIZE * count);
    if (g_threads.pool == 0)
        return 1;
    memset(g_threads.pool, 0, THREAD_DATA_SIZE * count);
    g_threads.count = count;
    for (i = 0; i < count; ++i)
    {
        thread = thread_get(i);
        thread->mpool = mpool_create(msizes, mcounts, mlen);
        if (thread->mpool == 0)
            goto cleanup;
        thread->lua = lua_newstate(thread_lua_alloc, thread->mpool);
        if (thread->lua == 0)
            goto cleanup;
        lua_atpanic(thread->lua, thread_lua_panic);
        luaL_openlibs(thread->lua);
        thread->state = THREAD_IDLE;
        thread->mutex = thread_mutex_create();
        if (thread->mutex == 0)
            goto cleanup;
        thread->engage = thread_cond_create();
        if (thread->engage == 0)
            goto cleanup;
        thread_mutex_lock(thread->mutex);
        thread->thread = thread_create(thread_loop, thread);
        if (thread == 0)
            goto cleanup;
        thread_reg(thread->lua);
    }
    g_threads.mutex = thread_mutex_create();
    if (g_threads.mutex == 0)
        goto cleanup;
    g_threads.engage = thread_cond_create();
    if (g_threads.engage == 0)
        goto cleanup;
    thread_reg_main(lua);
    return 0;
cleanup:
    g_threads.quit = 1;
    for (i = 0; i < count; ++i)
    {
        thread = thread_get(i);
        if (thread->engage)
            thread_cond_signal(thread->engage);
        if (thread->thread)
            thread_destroy(thread->thread);
        if (thread->mutex)
            thread_mutex_destroy(thread->mutex);
        if (thread->engage)
            thread_cond_destroy(thread->engage);
        if (thread->lua)
            lua_close(thread->lua);
        if (thread->mpool)
            mpool_destroy(thread->mpool);
    }
    util_free(g_threads.pool);
    g_threads.pool = 0;
    if (g_threads.mutex)
        thread_mutex_destroy(g_threads.mutex);
    if (g_threads.engage)
        thread_cond_destroy(g_threads.engage);
    return 1;
}

void thread_done(void)
{
    int i;
    struct thread_data_t *thread;
    if (g_threads.pool == 0)
        return;
    g_threads.quit = 1;
    for (i = 0; i < g_threads.count; ++i)
    {
        thread = thread_get(i);
        thread_cond_signal(thread->engage);
        thread_destroy(thread->thread);
        thread_mutex_destroy(thread->mutex);
        thread_cond_destroy(thread->engage);
        lua_close(thread->lua);
        fprintf(stderr, "\nThread %i memory pool:\n", i);
        mpool_destroy(thread->mpool);
    }
    util_free(g_threads.pool);
    g_threads.pool = 0;
    thread_mutex_destroy(g_threads.mutex);
    thread_cond_destroy(g_threads.engage);
}

