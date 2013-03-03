#pragma once

#include <lua.h>

int tex_init(lua_State *lua, int *sizes, int len);
void tex_done(void);
int tex_thread(void);
