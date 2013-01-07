#include <lua.h>
#include <lauxlib.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "mpool.h"
#include "machine.h"
#include "timer.h"

/*
TODO:

Main loop:
    - Run scene graph
    - Run controller Lua thread
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
    static const int FRAME_TIME = 10000;
    static const int GC_STEP = 10;
    static const int MIN_DELAY = 1000;

    int status, i, time_left, max_deviation;
    lua_State *lua = 0;
    struct machine_t *controller = 0, *worker = 0;
    struct mpool_t *pool = 0;
    struct timer_t *frame_timer = 0;

    printf("Start\n");

    frame_timer = timer_create();
    if (frame_timer == 0)
    {
        fprintf(stderr, "Cannot create timer\n");
        goto cleanup;
    }

    pool = mpool_create(POOL_SIZES, POOL_COUNTS, POOL_LEN);
    if (pool == 0)
    {
        fprintf(stderr, "Cannot create memory pool\n");
        goto cleanup;
    }

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
        timer_reset(frame_timer);
        lua_gc(lua, LUA_GCSTEP, GC_STEP);
        lua_gc(lua, LUA_GCSTOP, 0);
        status = machine_step(controller, 0);
        if (status)
        {
            fprintf(stderr, "Failed to run controller\n");
            goto cleanup;
        }
        status = machine_step(worker, FRAME_TIME - timer_passed(frame_timer));
        if (status)
        {
            fprintf(stderr, "Failed to run worker\n");
            goto cleanup;
        }
        time_left = timer_passed(frame_timer);
        if (FRAME_TIME - time_left > MIN_DELAY)
            usleep(FRAME_TIME - time_left);
        if (timer_passed(frame_timer) - FRAME_TIME > max_deviation)
            max_deviation = timer_passed(frame_timer) - FRAME_TIME;
    }
    printf("Maximum deviation: %i us\n", max_deviation);

cleanup:
    if (lua)
        lua_close(lua);
    if (pool)
    {
        mpool_print(pool);
        mpool_destroy(pool);
    }
    if (controller)
        machine_destroy(controller);
    if (worker)
        machine_destroy(worker);
    if (frame_timer)
        timer_destroy(frame_timer);
    printf("Finish\n");
    return 0;
}
