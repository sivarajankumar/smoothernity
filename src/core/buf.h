#pragma once

#include <lua.h>

struct buf_t
{
    float *data;
    int vacant;
    struct buf_t *next;
};

struct bufs_t
{
    int size;
    int count;
    int left;
    struct buf_t *pool;
    struct buf_t *vacant;
};

extern struct bufs_t g_bufs;

int buf_init(lua_State *lua, int size, int count);
void buf_done(void);
struct buf_t * buf_get(int);
