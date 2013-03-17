#pragma once

#include <lua.h>

int sync_init(lua_State *lua, int count);
void sync_done(void);
