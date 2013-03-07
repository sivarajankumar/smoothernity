#pragma once

#include <lua.h>
#include <GL/glew.h>

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
    int draw_tag;

    struct mesh_t *prev;
    struct mesh_t *next;
};

struct meshes_t
{
    int count;
    char *pool;
    struct mesh_t *active; /* sorted */
};

extern struct meshes_t g_meshes;

int mesh_init(lua_State *lua, int count);
void mesh_done(void);
struct mesh_t * mesh_get(int);
