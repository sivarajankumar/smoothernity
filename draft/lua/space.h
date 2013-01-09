#pragma once

#include <lua.h>

int space_init(lua_State *lua, int count);
void space_done(void);
struct space_t * space_get(int space);
void space_compute(struct space_t *space);
void space_select(struct space_t *space);
