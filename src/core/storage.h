#pragma once

#include <lua.h>

int storage_init(lua_State*, int size, int count);
void storage_done(void);
