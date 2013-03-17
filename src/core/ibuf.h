#pragma once

#include <GL/glew.h>
#include <lua.h>

enum ibuf_e
{
    IBUF_UNMAPPED,
    IBUF_MAPPED,
    IBUF_ERROR
};

struct ibuf_t
{
    GLuint buf_id;
    int size;
    int mapped_ofs;
    int mapped_len;
    GLvoid *mapped;
    enum ibuf_e state;
};

typedef GLuint ibuf_data_t;

struct ibufs_t
{
    int count;
    char *pool;
    struct thread_mutex_t *mutex;
};

extern struct ibufs_t g_ibufs;

int ibuf_init(lua_State *lua, int *sizes, int count);
void ibuf_done(void);
void ibuf_reg_thread(lua_State *lua);
struct ibuf_t * ibuf_get(int);
void ibuf_select(struct ibuf_t*);
