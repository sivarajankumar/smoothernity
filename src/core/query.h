#pragma once

#include <lua.h>

int query_init(lua_State *lua, int count);
void query_done(void);
