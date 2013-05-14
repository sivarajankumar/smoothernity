#pragma once

#include <lua.h>

#define VECTOR_ARGVS 5
#define VECTOR_ARGMS 2

enum vector_ipl_e
{
    VECTOR_IPL_LINEAR = 0,
    VECTOR_IPL_SPLINE = 1,
    VECTOR_IPLS_TOTAL = 2
};

enum vector_e
{
    VECTOR_CONST,
    VECTOR_RUBBER,
    VECTOR_WSUM,
    VECTOR_SEQ,
    VECTOR_MPOS,
    VECTOR_CORD,
    VECTOR_PICK,
    VECTOR_CAST
};

struct vector_t
{
    float value[4]; /* must go first to ensure alignment */
    enum vector_e type;
    int update_tag;
    struct vector_t *argv[VECTOR_ARGVS];
    struct matrix_t *argm[VECTOR_ARGMS];

    int cast_wldi;
    int cast_csi;
    float cord_min;
    float cord_max;
    float seq_t;
    int seq_cur;
    int seq_start;
    int seq_len;
    int seq_loop;
    enum vector_ipl_e seq_ipl;
};

int vector_init(lua_State *lua, int count, int nesting);
void vector_done(void);
struct vector_t * vector_get(int);
int vector_update(struct vector_t *vector, float dt, int update_tag, int force);
int vector_nesting(struct vector_t *vector, int limit);
void vector_cross(float *out, float *v1, float *v2);
float vector_len(float *v);
void vector_wsum(float *out, float w1, float *v1, float w2, float *v2);

