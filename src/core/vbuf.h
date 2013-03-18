#pragma once

#include <lua.h>
#include <GL/glew.h>

enum vbuf_state_e
{
    VBUF_IDLE,
    VBUF_UNMAPPING,
    VBUF_MAPPING,
    VBUF_MAPPED,
    VBUF_ERROR
};

struct vbuf_t
{
    GLuint buf_id;
    int size;
    int mapped_ofs;
    int mapped_len;
    GLvoid *mapped;
    enum vbuf_state_e state;
};

struct vbufs_t
{
    int count;
    void *offset_pos;
    void *offset_tex;
    void *offset_color;
    char *pool;
    struct thread_mutex_t *mutex;
};

extern struct vbufs_t g_vbufs;

int vbuf_init(lua_State *lua, int *sizes, int count);
void vbuf_done(void);
void vbuf_reg_thread(lua_State *lua);
struct vbuf_t * vbuf_get(int vbuf);
void vbuf_select(struct vbuf_t *);
int vbuf_thread(void);
