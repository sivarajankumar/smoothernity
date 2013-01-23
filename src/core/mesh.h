#pragma once

#include <lua.h>
#include <GL/gl.h>

struct mesh_t
{
    struct ibuf_t *ibuf;
    struct vbuf_t *vbuf;
    struct matrix_t *matrix;
    GLenum type;
    int ioffset;
    int icount;
    int vacant;
    int frame_tag; /* when this mesh was last drawn */

    struct mesh_t *vbuf_prev;
    struct mesh_t *vbuf_next;

    struct mesh_t *ibuf_prev;
    struct mesh_t *ibuf_next;

    struct mesh_t *prev;
    struct mesh_t *next;
};

struct meshes_t
{
    int left;
    int left_min;
    int count;
    int allocs;
    int frees;
    struct mesh_t *pool;
    struct mesh_t *vacant;
};

extern struct meshes_t g_meshes;

int mesh_init(lua_State *lua, int count);
void mesh_done(void);
void mesh_draw(struct mesh_t *mesh);
