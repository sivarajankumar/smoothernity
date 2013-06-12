#ifndef CBUF_H
#define CBUF_H

#include "lua.h"

struct cbufs_t {
    int size;
    float *data;
};

extern struct cbufs_t g_cbufs;

int cbuf_init(lua_State *lua, int size);
void cbuf_done(void);
void cbuf_reg_thread(lua_State *lua);

#endif /* CBUF_H */

