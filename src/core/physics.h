#pragma once

#include <lua.h>

int physics_init(lua_State *lua, int cs_count, int rb_count);
void physics_done(void);
