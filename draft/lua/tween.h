#pragma once

#include <lua.h>

int tween_init(lua_State *lua, int len);
void tween_done(void);
void tween_update(float dt);
struct tween_t * tween_get(int);
