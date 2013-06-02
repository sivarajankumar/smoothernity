#ifndef CORE_BUF_H
#define CORE_BUF_H

#include "lua.h"

struct bufs_t {
    int size;
    float *data;
};

extern struct bufs_t g_bufs;

int buf_init(lua_State *lua, int size);
void buf_done(void);
void buf_reg_thread(lua_State *lua);

#endif /* CORE_BUF_H */

