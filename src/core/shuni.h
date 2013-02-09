#pragma once

#include <lua.h>

#define SHUNI_ARGVS 1

enum shuni_e
{
    SHUNI_VECTOR
};

struct shuni_t
{
    enum shuni_e type;
    int vacant;
    struct shprog_t *shprog;
    struct mesh_t *mesh;
    struct shuni_t *next;
    struct shuni_t *shprog_prev;
    struct shuni_t *shprog_next;
    struct shuni_t *mesh_prev;
    struct shuni_t *mesh_next;
};

int shuni_init(lua_State *lua, int count);
void shuni_done(void);
void shuni_select(struct shuni_t*);
int shuni_update(struct shuni_t*, float dt, int frame_tag, int force);
