#pragma once

#include <lua.h>
#include <GL/gl.h>

struct mesh_t
{
    struct ibuf_t *ibuf;
    struct vbuf_t *vbuf;
    struct shprog_t *shprog;
    struct shuni_t *shunis;
    struct matrix_t *matrix;
    GLenum type;
    int ioffset;
    int icount;
    int group;
    int vacant;
    int frame_tag; /* when this mesh was last drawn */

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
    char *pool;
    struct mesh_t *vacant;
    struct mesh_t *active; /* sorted */
};

extern struct meshes_t g_meshes;

int mesh_init(lua_State *lua, int count);
void mesh_done(void);
void mesh_draw(struct mesh_t *mesh);
struct mesh_t * mesh_get(int);
