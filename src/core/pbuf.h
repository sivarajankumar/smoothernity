#pragma once

#include <lua.h>

int pbuf_init(lua_State *lua, int size, int count);
void pbuf_done(void);
