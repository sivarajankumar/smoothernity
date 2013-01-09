#pragma once

#include <lua.h>

int vbuf_init(lua_State *lua, int size, int count);
void vbuf_done(void);
struct vbuf_t * vbuf_get(int vbuf);
void vbuf_select(struct vbuf_t *);
