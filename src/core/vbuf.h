#pragma once

#include <lua.h>
#include <GL/gl.h>

enum vbuf_e
{
    VBUF_VACANT,
    VBUF_UNMAPPED,
    VBUF_MAPPED
};

struct vbuf_t
{
    GLuint buf_id;
    int mapped_ofs;
    int mapped_len;
    GLvoid *mapped;
    enum vbuf_e state;
    struct vbuf_t *next;
};

struct vbufs_t
{
    int size;
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    void *offset_pos;
    void *offset_tex;
    void *offset_color;
    char *pool;
    struct vbuf_t *vacant;
};

extern struct vbufs_t g_vbufs;

int vbuf_init(lua_State *lua, int size, int count);
void vbuf_done(void);
struct vbuf_t * vbuf_get(int vbuf);
void vbuf_select(struct vbuf_t *);
