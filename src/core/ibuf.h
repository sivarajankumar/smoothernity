#pragma once

#include <GL/gl.h>
#include <lua.h>

struct ibuf_t
{
    GLuint buf_id;
    GLvoid *mapped;
    int vacant;
    struct ibuf_t *prev;
    struct ibuf_t *next;
    struct mesh_t *meshes;
    char padding[16];
};

struct ibuf_data_t
{
    GLuint index;
};

struct ibufs_t
{
    int size;
    int count;
    int left;
    int left_min;
    int with_meshes;
    int allocs;
    int frees;
    struct ibuf_t *pool;
    struct ibuf_t *vacant;
    struct ibuf_t *mapped;
    struct ibuf_t *baked;
};

extern struct ibufs_t g_ibufs;

int ibuf_init(lua_State *lua, int size, int count);
void ibuf_done(void);
struct ibuf_t * ibuf_get(int ibuf);
void ibuf_select(struct ibuf_t *);
