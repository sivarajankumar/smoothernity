#pragma once

#include <lua.h>

int render_init(lua_State *lua, int *argc, char **argv, int width, int height);
void render_done(void);
void render_update(float dt);
void render_draw(void);
