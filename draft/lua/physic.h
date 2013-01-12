#pragma once

#include <lua.h>

int physic_init(lua_State *lua, void *(*memalloc)(size_t), void (*memfree)(void*));
void physic_done(void);
