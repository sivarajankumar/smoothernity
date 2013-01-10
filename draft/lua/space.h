#pragma once

#include <lua.h>

int space_init(lua_State *lua, int count, int nesting);
void space_done(void);
struct space_t * space_get(int space);
void space_select(struct space_t *space, int frame_tag);
