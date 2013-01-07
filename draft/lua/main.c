#include <lua.h>
#include <lauxlib.h>
#include <stdlib.h>
#include <stdio.h>

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

int main(void)
{
    printf("Start\n");

    int status, result, i;
    double sum;
    lua_State *L;
    
    L = luaL_newstate();

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

    for (i = 1; i <= 10; i++)
    {
        result = lua_resume(Lt1, 0);
        if (result && result != LUA_YIELD)
        {
            fprintf(stderr, "Failed to resume thread1: %s\n", lua_tostring(L, -1));
            exit(1);
        }
        result = lua_resume(Lt2, 0);
        if (result && result != LUA_YIELD)
        {
            fprintf(stderr, "Failed to resume thread2: %s\n", lua_tostring(L, -1));
            exit(1);
        }
    }

    lua_close(L);
    
    printf("Finish\n");
    return 0;
}
