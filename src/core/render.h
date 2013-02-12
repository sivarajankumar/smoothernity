#pragma once

#include <lua.h>

int render_init(lua_State *lua, int *argc, char **argv, int width, int height);
void render_done(void);
