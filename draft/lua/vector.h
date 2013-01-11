#pragma once

#include "lua.h"
#include "GL/gl.h"

#define VECTOR_ARGVS 2

enum vector_e
{
    VECTOR_CONST = 0,
    VECTOR_SINE = 1,
    VECTOR_SAW = 2,
    VECTOR_RUBBER = 3
};

struct vector_t
{
    enum vector_e type;
    GLfloat value[4];
    float rubber;
    float period;
    float t;
    int frame_tag;
    int vacant;
    struct vector_t *argv[VECTOR_ARGVS];
    struct vector_t *next;
};

int vector_init(lua_State *lua, int count, int nesting);
void vector_done(void);
struct vector_t * vector_get(int);
void vector_update(struct vector_t *vector, float dt, int frame_tag, int force);
int vector_nesting(struct vector_t *vector, int limit);
void vector_cross(GLfloat *out, GLfloat *v1, GLfloat *v2);
