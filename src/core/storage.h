#pragma once

#include <lua.h>

int storage_init(lua_State*, int key_size, int data_size, int count);
void storage_done(void);
