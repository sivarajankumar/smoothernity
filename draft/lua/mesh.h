#pragma once

#include <lua.h>

struct mesh_t;

int mesh_init(lua_State *lua, int count);
void mesh_done(void);
void mesh_draw(struct mesh_t *mesh);
