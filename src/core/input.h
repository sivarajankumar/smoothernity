#pragma once

#include <lua.h>

int input_init(lua_State *lua);
void input_done(void);
void input_update(void);
