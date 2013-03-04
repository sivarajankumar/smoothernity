#include "thread.h"
#include "mpool.h"
#include "../thread/thread.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>
#include <lualib.h>

static const size_t THREAD_DATA_SIZE = 32;

enum thread_state_e
{
    THREAD_IDLE,
    THREAD_RUNNING,
    THREAD_WAITING
};

struct thread_data_t
{
    struct thread_mutex_t *mutex;
    struct thread_cond_t *engage;
    struct thread_t *thread;
    lua_State *lua;
    struct mpool_t *mpool;
    enum thread_state_e state;
};

struct threads_t
{
    int count;
    int quit;
    char *pool;
};

static struct threads_t g_threads;

static void thread_loop(void *data)
{
    struct thread_data_t *thread = data;
    while (g_threads.quit == 0)
    {
        thread_mutex_lock(thread->mutex);
        thread_cond_wait(thread->engage, thread->mutex);
        thread_mutex_unlock(thread->mutex);
    }
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
        thread->thread = thread_create(thread_loop, thread);
        if (thread == 0)
            goto cleanup;
    }
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
        fprintf(stdout, "\nThread %i memory pool:\n", i);
        mpool_destroy(thread->mpool);
    }
    util_free(g_threads.pool);
    g_threads.pool = 0;
}
