#include "cutil.h"
#include <float.h>

int cutil_isfloat(lua_State *lua, int i) {
    lua_Number n;
    return lua_isnumber(lua, i) &&
        (n = lua_tonumber(lua, i), n > -FLT_MAX && n < FLT_MAX);
}

int cutil_isint(lua_State *lua, int i) {
    lua_Number n;
    return lua_isnumber(lua, i) &&
        (n = lua_tonumber(lua, i), (lua_Number)(int)n == n);
}

