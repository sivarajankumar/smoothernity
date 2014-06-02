#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
    lua_State *lua;
    lua = luaL_newstate();
    if (lua) {
        luaL_openlibs(lua);
        if (luaL_dofile(lua, "sandbox.lua")) {
            fprintf(stderr, "Cannot run script: %s", lua_tostring(lua, -1));
        }
        lua_close(lua);
    }
    return 0;
}
