#pragma once

#include <lua.h>

int physics_init(lua_State *lua, void *(*memalloc)(size_t),
                void (*memfree)(void*));
void physics_done(void);
