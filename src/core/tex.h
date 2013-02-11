#pragma once

#include <lua.h>

int tex_init(lua_State *lua, int size, int count);
void tex_done(void);
