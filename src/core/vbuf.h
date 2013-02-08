#pragma once

#include <lua.h>
#include <GL/gl.h>

struct vbuf_t
{
    GLuint buf_id;
    GLvoid *mapped;
    int vacant;
    struct vbuf_t *prev;
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
    struct vbuf_t *mapped;
    struct vbuf_t *baked;
};

extern struct vbufs_t g_vbufs;

int vbuf_init(lua_State *lua, int size, int count);
void vbuf_done(void);
struct vbuf_t * vbuf_get(int vbuf);
void vbuf_select(struct vbuf_t *);
