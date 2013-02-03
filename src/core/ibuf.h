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
};

typedef GLuint ibuf_data_t;

struct ibufs_t
{
    int size;
    int count;
    int left;
    int left_min;
    int with_meshes;
    int allocs;
    int frees;
    char *pool;
    struct ibuf_t *vacant;
    struct ibuf_t *mapped;
    struct ibuf_t *baked;
};

extern struct ibufs_t g_ibufs;

int ibuf_init(lua_State *lua, int size, int count);
void ibuf_done(void);
struct ibuf_t * ibuf_get(int);
void ibuf_select(struct ibuf_t*);
