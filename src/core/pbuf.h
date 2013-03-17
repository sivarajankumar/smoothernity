#pragma once

#include <lua.h>
#include <GL/glew.h>

enum pbuf_e
{
    PBUF_UNMAPPED,
    PBUF_MAPPED,
    PBUF_ERROR
};

struct pbuf_t
{
    GLuint buf_id;
    int mapped_ofs;
    int mapped_len;
    GLvoid *mapped;
    enum pbuf_e state;
};

struct pbuf_data_t
{
    GLubyte color[4];
};

struct pbufs_t
{
    int size;
    int count;
    char *pool;
    struct thread_mutex_t *mutex;
};

extern struct pbufs_t g_pbufs;

int pbuf_init(lua_State *lua, int size, int count);
void pbuf_done(void);
void pbuf_reg_thread(lua_State *lua);
struct pbuf_t * pbuf_get(int);
