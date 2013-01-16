#pragma once

#include <lua.h>
#include <GL/gl.h>

#define VECTOR_ARGVS 5
#define VECTOR_ARGMS 1

enum vector_ipl_e
{
    VECTOR_IPL_LINEAR = 0,
    VECTOR_IPL_SPLINE = 1,
    VECTOR_IPLS_TOTAL = 2
};

enum vector_e
{
    VECTOR_CONST = 0,
    VECTOR_RUBBER = 1,
    VECTOR_WSUM = 2,
    VECTOR_SEQ = 3,
    VECTOR_MPOS = 4,
    VECTOR_CORD = 5,
    VECTOR_PICK = 6
};

struct vector_t
{
    enum vector_e type;
    GLfloat value[4];
    int frame_tag;
    int vacant;
    struct vector_t *next;
    struct vector_t *argv[VECTOR_ARGVS];
    struct matrix_t *argm[VECTOR_ARGMS];

    float cord_min;
    float cord_max;
    float seq_t;
    int seq_cur;
    int seq_start;
    int seq_len;
    int seq_loop;
    enum vector_ipl_e seq_ipl;
    struct buf_t *seq_buf;
};

int vector_init(lua_State *lua, int count, int nesting);
void vector_done(void);
struct vector_t * vector_get(int);
void vector_update(struct vector_t *vector, float dt, int frame_tag, int force);
int vector_nesting(struct vector_t *vector, int limit);
void vector_cross(GLfloat *out, GLfloat *v1, GLfloat *v2);
float vector_len(GLfloat *v);
void vector_wsum(GLfloat *out, float w1, GLfloat *v1, float w2, GLfloat *v2);
