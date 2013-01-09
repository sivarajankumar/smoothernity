#include "mesh.h"

static int api_mesh_alloc(lua_State *lua)
{
    if (lua_gettop(lua) == 7 && lua_isnumber(lua, -7)
     && lua_isnumber(lua, -6) && lua_isnumber(lua, -5) && lua_isnumber(lua, -4)
     && lua_isnumber(lua, -3) && lua_isnumber(lua, -2) && lua_isnumber(lua, -1))
    {
        lua_pushinteger(lua, mesh_alloc(lua_tointeger(lua, -7),
                                        lua_tointeger(lua, -6),
                                        lua_tointeger(lua, -5),
                                        lua_tointeger(lua, -4),
                                        lua_tointeger(lua, -3),
                                        lua_tointeger(lua, -2),
                                        lua_tointeger(lua, -1)));
        lua_pop(lua, 7);
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_mesh_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_mesh_free(lua_State *lua)
{
    if (lua_gettop(lua) == 1 && lua_isnumber(lua, -1))
    {
        mesh_free(lua_tointeger(lua, -1));
        lua_pop(lua, 1);
        return 0;
    }
    else
    {
        lua_pushstring(lua, "api_mesh_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_mesh_query(lua_State *lua)
{
    int left;
    if (lua_gettop(lua) == 0)
    {
        mesh_query(&left);
        lua_pushinteger(lua, left);
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_mesh_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
}


