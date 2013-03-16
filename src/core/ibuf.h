#pragma once

#include <GL/glew.h>
#include <lua.h>

enum ibuf_e
{
    IBUF_IDLE,
    IBUF_UNMAPPING,
    IBUF_MAPPING,
    IBUF_MAPPED,
    IBUF_COPYING_FROM,
    IBUF_COPYING_TO,
    IBUF_ERROR
};

struct ibuf_t
{
    GLuint buf_id;
    int mapped_ofs;
    int mapped_len;
    int copy_ofs;
    int copy_len;
    struct ibuf_t *copy_to;
    GLvoid *mapped;
    enum ibuf_e state;
};

typedef GLuint ibuf_data_t;

struct ibufs_t
{
    int size;
    int count;
    char *pool;
    struct thread_mutex_t *mutex;
};

extern struct ibufs_t g_ibufs;

int ibuf_init(lua_State *lua, int size, int count);
void ibuf_done(void);
void ibuf_reg_thread(lua_State *lua);
struct ibuf_t * ibuf_get(int);
void ibuf_select(struct ibuf_t*);
int ibuf_thread(void);
