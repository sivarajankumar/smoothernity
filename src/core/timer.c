#include "timer.h"
#include "../platform/timer.h"
#include "SDL.h"

static int api_timer(lua_State *lua)
{
    if (lua_gettop(lua))
    {
        lua_pushstring(lua, "api_timer: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushnumber(lua, pfm_timer_get());
    return 1;
}

static int api_timer_delay(lua_State *lua)
{
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_timer_delay: incorrect argument");
        lua_error(lua);
        return 0;
    }
    SDL_Delay((int)(lua_tonumber(lua, 1) * 1000.0));
    lua_pop(lua, 1);
    return 0;
}

void timer_reg_thread(lua_State *lua)
{
    lua_register(lua, "api_timer", api_timer);
    lua_register(lua, "api_timer_delay", api_timer_delay);
}

int timer_init(lua_State *lua)
{
    timer_reg_thread(lua);
    return pfm_timer_init();
}

