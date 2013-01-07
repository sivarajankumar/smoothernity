#include <lua.h>
#include <lauxlib.h>
#include <stdlib.h>
#include <stdio.h>
#include "mpool.h"

/*
TODO:

Main loop:
    - Run scene graph
    - Run control Lua thread
    - Run background Lua thread
    - Run Lua garbage collector

Control Lua thread:
    - Polls user input and game events
    - Yields explicitly every frame

Background Lua thread:
    - Used for background computations
    - Periodically calls API function which will yield
      if too much time is consumed in the current frame

Every API function can yield if too much time is consumed.
*/

size_t POOL_SIZES[] =  {  64, 4096};
size_t POOL_COUNTS[] = {1000, 1000};
size_t POOL_LEN = 2;

struct mpool_t *g_pool;

struct mystate
{
    int counter;
};

int myyield(lua_State *L)
{
    struct mystate *state;
    state = lua_touserdata(L, -1);
    lua_pop(L, 1);
    if (++state->counter % 2)
        return lua_yield(L, 0);
    else
        return 0;
}

void * myalloc(void *ud, void *ptr, size_t osize, size_t nsize)
{
    return mpool_alloc(ud, ptr, osize, nsize);
}

int main(void)
{
    int status, i;
    double sum;
    lua_State *L;
    struct mystate state1, state2;

    printf("Start\n");

    status = mpool_create(&g_pool, POOL_SIZES, POOL_COUNTS, POOL_LEN);
    if (status)
    {
        fprintf(stderr, "Couldn't create memory pool\n");
        exit(1);
    }

    state1.counter = 0;
    state2.counter = 0;

    L = lua_newstate(myalloc, g_pool);
    lua_gc(L, LUA_GCSTOP, 0);
    lua_register(L, "myyield", myyield);

    luaL_openlibs(L);

    status = luaL_dofile(L, "script.lua");
    if (status)
    {
        fprintf(stderr, "Couldn't run file: %s\n", lua_tostring(L, -1));
        exit(1);
    }

    lua_State *Lt1, *Lt2;
    Lt1 = lua_newthread(L);
    Lt2 = lua_newthread(L);
    lua_getglobal(Lt1, "thread1");
    lua_getglobal(Lt2, "thread2");
    lua_pushlightuserdata(Lt1, &state1);
    lua_pushlightuserdata(Lt2, &state2);

    for (i = 1; i <= 10; i++)
    {
        printf("Memory before gc: %i K\n", lua_gc(L, LUA_GCCOUNT, 0));
        printf("GC step result: %i\n", lua_gc(L, LUA_GCSTEP, 10));
        lua_gc(L, LUA_GCSTOP, 0);
        printf("Memory after gc: %i K\n", lua_gc(L, LUA_GCCOUNT, 0));
        status = lua_resume(Lt1, 1);
        if (status && status != LUA_YIELD)
        {
            fprintf(stderr, "Failed to resume thread1: %s\n", lua_tostring(Lt1, -1));
            exit(1);
        }
        status = lua_resume(Lt2, 1);
        if (status && status != LUA_YIELD)
        {
            fprintf(stderr, "Failed to resume thread2: %s\n", lua_tostring(Lt2, -1));
            exit(1);
        }
        printf("Counter1 is %i, counter2 is %i\n", state1.counter, state2.counter);
    }

    lua_close(L);
    mpool_print(g_pool);
    mpool_destroy(g_pool);
    
    printf("Finish\n");
    return 0;
}
