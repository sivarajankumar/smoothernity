#include <lua.h>
#include <lauxlib.h>
#include <stdlib.h>
#include <stdio.h>
#include "mpool.h"
#include "machine.h"

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

int mypanic(lua_State *lua)
{
    fprintf(stderr, "Lua panic: %s\n", lua_tostring(lua, -1));
}

void * myalloc(void *ud, void *ptr, size_t osize, size_t nsize)
{
    return mpool_alloc(ud, ptr, osize, nsize);
}

int main(void)
{
    static const size_t POOL_SIZES[] =  {  64, 4096};
    static const size_t POOL_COUNTS[] = {1000, 1000};
    static const size_t POOL_LEN = 2;

    int status, i;
    lua_State *lua = 0;
    struct machine_t *m1 = 0, m2 = 0;
    struct mpool_t *pool = 0;

    printf("Start\n");

    status = mpool_create(&pool, POOL_SIZES, POOL_COUNTS, POOL_LEN);
    if (status)
    {
        fprintf(stderr, "Cannot create memory pool\n");
        goto cleanup;
    }

    state1.counter = 0;
    state2.counter = 0;

    lua = lua_newstate(myalloc, pool);
    if (lua == 0)
    {
        fprintf(stderr, "Cannot create Lua state\n");
        goto cleanup;
    }
    lua_atpanic(lua, mypanic);
    lua_gc(lua, LUA_GCSTOP, 0);
    machine_embrace(lua);

    luaL_openlibs(lua);

    status = luaL_dofile(lua, "script.lua");
    if (status)
    {
        fprintf(stderr, "Couldn't run file: %s\n", lua_tostring(lua, -1));
        goto cleanup;
    }

    m1 = machine_create(lua, "thread1");
    if (m1 == 0)
    {
        fprintf(stderr, "Cannot create machine1\n");
        goto cleanup;
    }
    m2 = machine_create(lua, "thread2");
    if (m2 == 0)
    {
        fprintf(stderr, "Cannot create machine2\n");
        goto cleanup;
    }

    for (i = 1; i <= 10; i++)
    {
        printf("Memory before gc: %i K\n", lua_gc(lua, LUA_GCCOUNT, 0));
        printf("GC step result: %i\n", lua_gc(lua, LUA_GCSTEP, 10));
        lua_gc(lua, LUA_GCSTOP, 0);
        printf("Memory after gc: %i K\n", lua_gc(lua, LUA_GCCOUNT, 0));
        status = machine_run(m1);
        if (status)
        {
            fprintf(stderr, "Failed to run machine1\n");
            goto cleanup;
        }
        status = machine_run(m2);
        if (status)
        {
            fprintf(stderr, "Failed to run machine2\n");
            goto cleanup;
        }
    }

cleanup:
    if (lua)
        lua_close(lua);
    if (pool)
    {
        mpool_print(pool);
        mpool_destroy(pool);
    }
    if (m1)
        machine_destroy(m1);
    if (m2)
        machine_destroy(m2);
    printf("Finish\n");
    return 0;
}
