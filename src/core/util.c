#include "util.h"

int util_isfloat(lua_State *lua, int i) {
    lua_Number n;
    return lua_isnumber(lua, i) &&
        (n = lua_tonumber(lua, i), (lua_Number)(float)n == n);
}

int util_isint(lua_State *lua, int i) {
    lua_Number n;
    return lua_isnumber(lua, i) &&
        (n = lua_tonumber(lua, i), (lua_Number)(int)n == n);
}

