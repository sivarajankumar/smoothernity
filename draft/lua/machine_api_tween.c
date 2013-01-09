#include "tween.h"

static int api_tween_alloc(lua_State *lua)
{
    if (lua_gettop(lua) == 0)
    {
        lua_pushinteger(lua, tween_alloc());
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_tween_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_tween_free(lua_State *lua)
{
    int tween;
    if (lua_gettop(lua) == 1 && lua_isnumber(lua, -1))
    {
        tween = lua_tointeger(lua, -1);
        lua_pop(lua, 1);
        tween_free(tween);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_tween_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_tween_play_sine(lua_State *lua)
{
    if (lua_gettop(lua) == 4
     && lua_isnumber(lua, -4) && lua_isnumber(lua, -3)
     && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        tween_play_sine(lua_tointeger(lua, -4),
                        lua_tonumber(lua, -3),
                        lua_tonumber(lua, -2),
                        lua_tonumber(lua, -1));
        lua_pop(lua, 4);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_tween_play_sine: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

