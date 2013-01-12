#pragma once

#include <lua.h>

int physics_init(lua_State *lua, int colshape_count);
void physics_done(void);
