#include "vbuf.h"

static int api_vbuf_alloc(lua_State *lua)
{
    if (lua_gettop(lua) == 0)
    {
        lua_pushinteger(lua, vbuf_alloc());
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_vbuf_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_vbuf_free(lua_State *lua)
{
    if (lua_gettop(lua) == 1 && lua_isnumber(lua, -1))
    {
        vbuf_free(lua_tointeger(lua, -1));
        lua_pop(lua, 1);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_vbuf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_vbuf_bake(lua_State *lua)
{
    if (lua_gettop(lua) == 1 && lua_isnumber(lua, -1))
    {
        vbuf_bake(lua_tointeger(lua, -1));
        lua_pop(lua, 1);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_vbuf_bake: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_vbuf_write(lua_State *lua)
{
    if (lua_gettop(lua) == 11
     && lua_isnumber(lua, -11) && lua_isnumber(lua, -10) && lua_isnumber(lua, -9)
     && lua_isnumber(lua, -8) && lua_isnumber(lua, -7) && lua_isnumber(lua, -6)
     && lua_isnumber(lua, -5) && lua_isnumber(lua, -4) && lua_isnumber(lua, -3)
     && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        vbuf_write(lua_tointeger(lua, -11),
                   lua_tointeger(lua, -10),
                   (float)lua_tonumber(lua, -9),
                   (float)lua_tonumber(lua, -8),
                   (float)lua_tonumber(lua, -7),
                   (float)lua_tonumber(lua, -6),
                   (float)lua_tonumber(lua, -5),
                   (float)lua_tonumber(lua, -4),
                   (float)lua_tonumber(lua, -3),
                   (float)lua_tonumber(lua, -2),
                   (float)lua_tonumber(lua, -1));
        lua_pop(lua, 11);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_vbuf_write: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_vbuf_query(lua_State *lua)
{
    int size, left;
    if (lua_gettop(lua) == 0)
    {
        vbuf_query(&size, &left);
        lua_pushinteger(lua, size);
        lua_pushinteger(lua, left);
        return 2;
    }
    else
    {
        lua_pushstring(lua, "api_vbuf_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

