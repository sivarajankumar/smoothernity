#pragma once

#include "lua.h"

struct bufs_t
{
    int size;
    float *data;
};

extern struct bufs_t g_bufs;

int buf_init(lua_State *lua, int size);
void buf_done(void);
void buf_reg_thread(lua_State *lua);

