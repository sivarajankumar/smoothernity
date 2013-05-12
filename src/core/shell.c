#include "shell.h"
#include "../platform/shell.h"

static int api_shell_rmfile(lua_State *lua)
{
    if (lua_gettop(lua) != 1 || !lua_isstring(lua, 1))
    {
        lua_pushstring(lua, "api_shell_rmfile: incorrect argument");
        lua_error(lua);
        return 0;
    }
    pfm_shell_rmfile(lua_tostring(lua, 1));
    lua_pop(lua, 1);
    return 0;
}

void shell_reg_thread(lua_State *lua)
{
    lua_register(lua, "api_shell_rmfile", api_shell_rmfile);
}
