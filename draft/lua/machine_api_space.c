#include "space.h"

static int api_space_alloc(lua_State *lua)
{
    if (lua_gettop(lua) == 0)
    {
        lua_pushinteger(lua, space_alloc());
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_space_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_space_free(lua_State *lua)
{
    if (lua_gettop(lua) == 1 && lua_isnumber(lua, -1))
    {
        space_free(lua_tointeger(lua, -1));
        lua_pop(lua, 1);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_space_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_space_query(lua_State *lua)
{
    int left;
    if (lua_gettop(lua) == 0)
    {
        space_query(&left);
        lua_pushinteger(lua, left);
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_space_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_space_offset(lua_State *lua)
{
    if (lua_gettop(lua) == 4
     && lua_isnumber(lua, -4) && lua_isnumber(lua, -3)
     && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        space_offset(lua_tointeger(lua, -4),
                     (float)lua_tonumber(lua, -3),
                     (float)lua_tonumber(lua, -2),
                     (float)lua_tonumber(lua, -1));
        lua_pop(lua, 4);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_space_offset: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_space_offset_tween(lua_State *lua)
{
    if (lua_gettop(lua) == 4
     && lua_isnumber(lua, -4) && lua_isnumber(lua, -3)
     && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        space_offset_tween(lua_tointeger(lua, -4),
                           lua_tointeger(lua, -3),
                           lua_tointeger(lua, -2),
                           lua_tointeger(lua, -1));
        lua_pop(lua, 4);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_space_offset_tween: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_space_scale(lua_State *lua)
{
    if (lua_gettop(lua) == 4
     && lua_isnumber(lua, -4) && lua_isnumber(lua, -3)
     && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        space_scale(lua_tointeger(lua, -4),
                    (float)lua_tonumber(lua, -3),
                    (float)lua_tonumber(lua, -2),
                    (float)lua_tonumber(lua, -1));
        lua_pop(lua, 4);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_space_scale: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_space_scale_tween(lua_State *lua)
{
    if (lua_gettop(lua) == 4
     && lua_isnumber(lua, -4) && lua_isnumber(lua, -3)
     && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        space_scale_tween(lua_tointeger(lua, -4),
                          lua_tointeger(lua, -3),
                          lua_tointeger(lua, -2),
                          lua_tointeger(lua, -1));
        lua_pop(lua, 4);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_space_scale_tween: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_space_rotation(lua_State *lua)
{
    if (lua_gettop(lua) == 3
     && lua_isnumber(lua, -3) && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        space_rotation(lua_tointeger(lua, -3),
                       lua_tointeger(lua, -2),
                       (float)lua_tonumber(lua, -1));
        lua_pop(lua, 3);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_space_rotation: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_space_rotation_tween(lua_State *lua)
{
    if (lua_gettop(lua) == 3
     && lua_isnumber(lua, -3) && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        space_rotation_tween(lua_tointeger(lua, -3),
                             lua_tointeger(lua, -2),
                             lua_tointeger(lua, -1));
        lua_pop(lua, 3);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_space_rotation_tween: incorrect argument");
        lua_error(lua);
        return 0;
    }
}
