#pragma once

#include <lua.h>

int ibuf_init(lua_State *lua, int size, int count);
void ibuf_done(void);
struct ibuf_t * ibuf_get(int ibuf);
void ibuf_select(struct ibuf_t *);
