#pragma once

#include <GL/gl.h>
#include <lua.h>

enum ibuf_e
{
    IBUF_VACANT,
    IBUF_MAPPED,
    IBUF_BAKED
};

struct ibuf_t
{
    GLuint buf_id;
    GLvoid *mapped;
    enum ibuf_e state;
    struct ibuf_t *next;
};

typedef GLuint ibuf_data_t;

struct ibufs_t
{
    int size;
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct ibuf_t *vacant;
};

extern struct ibufs_t g_ibufs;

int ibuf_init(lua_State *lua, int size, int count);
void ibuf_done(void);
struct ibuf_t * ibuf_get(int);
void ibuf_select(struct ibuf_t*);
