#pragma once

#include <lua.h>

int render_init(lua_State *lua, int width, int height);
void render_done(void);
void render_thread_done(void);
void render_engage(void);
