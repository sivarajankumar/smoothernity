#pragma once

#include <lua.h>

int display_init(lua_State *lua, int *argc, char **argv, int width, int height);
void display_done(void);

void display_get_mode(int *width, int *height);
void display_set_clear_color(float r, float g, float b);
void display_tween_clear_color(int r, int g, int b);
void display_update(void);
void display_show(void);
