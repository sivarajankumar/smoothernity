#include "tex.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>

int tex_init(lua_State *lua, int size, int count)
{
    lua_register(lua, "api_tex_left", api_tex_left);
    lua_register(lua, "api_tex_alloc", api_tex_alloc);
    lua_register(lua, "api_tex_free", api_tex_free);
    lua_register(lua, "api_tex_set", api_tex_set);
}

void tex_done(void)
{
}
