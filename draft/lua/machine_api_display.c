#include "display.h"

static int api_display_set_clear_color(lua_State *lua)
{
    if (lua_gettop(lua) == 3
     && lua_isnumber(lua, -3) && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        display_set_clear_color
            ((float)lua_tonumber(lua, -3),
             (float)lua_tonumber(lua, -2),
             (float)lua_tonumber(lua, -1));
        lua_pop(lua, 3);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_display_set_clear_color: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_display_tween_clear_color(lua_State *lua)
{
    if (lua_gettop(lua) == 3
     && lua_isnumber(lua, -3) && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        display_tween_clear_color
            (lua_tonumber(lua, -3),
             lua_tonumber(lua, -2),
             lua_tonumber(lua, -1));
        lua_pop(lua, 3);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_display_tween_clear_color: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

