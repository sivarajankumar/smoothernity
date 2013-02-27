#include "timer.h"
#include "../platform/timer.h"

static int api_timer(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_timer: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushnumber(lua, pfm_timer_get());
    return 1;
}

int timer_init(lua_State *lua)
{
    lua_register(lua, "api_timer", api_timer);
    return pfm_timer_init();
}
