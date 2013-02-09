#pragma once

#include <GL/gl.h>
#include <lua.h>

struct ibuf_t
{
    GLuint buf_id;
    GLvoid *mapped;
    int vacant;
    struct ibuf_t *prev; /* TODO: remove */
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
    struct ibuf_t *mapped; /* TODO: remove */
    struct ibuf_t *baked; /* TODO: remove */
};

extern struct ibufs_t g_ibufs;

int ibuf_init(lua_State *lua, int size, int count);
void ibuf_done(void);
struct ibuf_t * ibuf_get(int);
void ibuf_select(struct ibuf_t*);
