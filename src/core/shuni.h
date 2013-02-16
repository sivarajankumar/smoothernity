#pragma once

#include <lua.h>
#include <GL/glew.h>

#define SHUNI_ARGVS 1
#define SHUNI_ARGIS 1

enum shuni_e
{
    SHUNI_VACANT,
    SHUNI_CREATED,
    SHUNI_VECTOR,
    SHUNI_INTEGER
};

struct shuni_t
{
    GLuint loc_id;
    enum shuni_e state;
    struct shprog_t *shprog;
    struct mesh_t *mesh;
    struct vector_t *argv[SHUNI_ARGVS];
    int argi[SHUNI_ARGIS];
    struct shuni_t *next;
    struct shuni_t *shprog_prev;
    struct shuni_t *shprog_next;
    struct shuni_t *mesh_prev;
    struct shuni_t *mesh_next;
};

int shuni_init(lua_State *lua, int count);
void shuni_done(void);
void shuni_select(struct shuni_t*);
int shuni_update(struct shuni_t*, float dt, int update_tag, int force);
