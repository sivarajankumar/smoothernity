#include "text.h"

static int api_text_alloc(lua_State *lua)
{
    if (lua_gettop(lua) == 4 && lua_isstring(lua, -4)
     && lua_isnumber(lua, -3) && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        lua_pushinteger(lua, text_alloc(lua_tostring(lua, -4),
                                        lua_tointeger(lua, -3),
                                        lua_tointeger(lua, -2),
                                        lua_tointeger(lua, -1)));
        lua_pop(lua, 4);
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_text_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_text_free(lua_State *lua)
{
    if (lua_gettop(lua) == 1 && lua_isnumber(lua, -1))
    {
        text_free(lua_tointeger(lua, -1));
        lua_pop(lua, 1);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_text_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_text_query(lua_State *lua)
{
    int size, left;
    if (lua_gettop(lua) == 0)
    {
        text_query(&size, &left);
        lua_pushinteger(lua, size);
        lua_pushinteger(lua, left);
        return 2;
    }
    else
    {
        lua_pushstring(lua, "api_text_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
}



