#pragma once

#include <lua.h>

int vao_init(lua_State *lua, int count);
void vao_done(void);
int vao_bound(void);

