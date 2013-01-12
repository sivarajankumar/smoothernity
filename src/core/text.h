#pragma once

#include <lua.h>

int text_init(lua_State *lua, int size, int count);
void text_done(void);
void text_draw(void);
