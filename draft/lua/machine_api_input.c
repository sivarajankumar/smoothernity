#include "input.h"

static int api_input_key_escape(lua_State *lua)
{
    if (lua_gettop(lua) == 0)
    {
        lua_pushinteger(lua, input_key_escape());
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_input_key_escape: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

