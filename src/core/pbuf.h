#pragma once

#include <lua.h>
#include <GL/gl.h>

enum pbuf_e
{
    PBUF_VACANT,
    PBUF_UNMAPPED,
    PBUF_MAPPED
};

struct pbuf_t
{
    GLuint buf_id;
    int mapped_ofs;
    int mapped_len;
    GLvoid *mapped;
    enum pbuf_e state;
    struct pbuf_t *next;
};

struct pbuf_data_t
{
    GLubyte color[4];
};

struct pbufs_t
{
    int size;
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct pbuf_t *vacant;
};

extern struct pbufs_t g_pbufs;

int pbuf_init(lua_State *lua, int size, int count);
void pbuf_done(void);
struct pbuf_t * pbuf_get(int);
