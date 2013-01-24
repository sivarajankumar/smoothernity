#pragma once

#include <lua.h>

int rop_init(lua_State *lua, int count);
void rop_done(void);
struct rop_t * rop_get(int);
int rop_update(struct rop_t*, float dt, int frame_tag);
int rop_draw(struct rop_t*, int frame_tag);
