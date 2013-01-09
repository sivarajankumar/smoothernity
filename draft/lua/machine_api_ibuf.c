#include "ibuf.h"

static int api_ibuf_alloc(lua_State *lua)
{
    if (lua_gettop(lua) == 0)
    {
        lua_pushinteger(lua, ibuf_alloc());
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_ibuf_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_ibuf_free(lua_State *lua)
{
    if (lua_gettop(lua) == 1 && lua_isnumber(lua, -1))
    {
        ibuf_free(lua_tointeger(lua, -1));
        lua_pop(lua, 1);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_ibuf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_ibuf_bake(lua_State *lua)
{
    if (lua_gettop(lua) == 1 && lua_isnumber(lua, -1))
    {
        ibuf_bake(lua_tointeger(lua, -1));
        lua_pop(lua, 1);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_ibuf_bake: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_ibuf_write(lua_State *lua)
{
    if (lua_gettop(lua) == 3
     && lua_isnumber(lua, -3) && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        ibuf_write(lua_tointeger(lua, -3),
                   lua_tointeger(lua, -2),
                   lua_tointeger(lua, -1));
        lua_pop(lua, 3);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_ibuf_write: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_ibuf_query(lua_State *lua)
{
    int size, left;
    if (lua_gettop(lua) == 0)
    {
        ibuf_query(&size, &left);
        lua_pushinteger(lua, size);
        lua_pushinteger(lua, left);
        return 2;
    }
    else
    {
        lua_pushstring(lua, "api_ibuf_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

