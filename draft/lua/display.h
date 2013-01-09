#pragma once

#include <lua.h>

int display_init(lua_State *lua, int *argc, char **argv, int width, int height);
void display_done(void);
void display_update(void);
void display_show(void);
