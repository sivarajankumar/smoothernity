#pragma once

#include <lua.h>
#include <GL/glew.h>

enum vbuf_e
{
    VBUF_VACANT,
    VBUF_UNMAPPING,
    VBUF_UNMAPPED,
    VBUF_MAPPING,
    VBUF_MAPPED,
    VBUF_ERROR
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
    struct thread_mutex_t *mutex;
};

extern struct vbufs_t g_vbufs;

int vbuf_init(lua_State *lua, int size, int count);
void vbuf_done(void);
struct vbuf_t * vbuf_get(int vbuf);
void vbuf_select(struct vbuf_t *);
int vbuf_thread(void);
