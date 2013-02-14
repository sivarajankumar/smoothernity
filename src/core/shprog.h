#pragma once

#include <lua.h>
#include <GL/glew.h>

enum shprog_e
{
    SHPROG_VACANT,
    SHPROG_CREATED,
    SHPROG_LINKED
};

struct shprog_t
{
    GLuint prog_id;
    enum shprog_e state;
    struct shprog_t *next;
    struct shuni_t *shunis;
};

int shprog_init(lua_State *lua, int count);
void shprog_done(void);
struct shprog_t * shprog_get(int);
void shprog_select(struct shprog_t*);
