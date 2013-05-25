#ifndef CORE_MATRIX_H
#define CORE_MATRIX_H

#include "lua.h"

#define MATRIX_ARGVS 3
#define MATRIX_ARGMS 2

enum matrix_e
{
    MATRIX_CONST,
    MATRIX_MUL,
    MATRIX_INV,
    MATRIX_FRUSTUM,
    MATRIX_ORTHO,
    MATRIX_POS_SCL_ROT,
    MATRIX_FROM_TO_UP,
    MATRIX_RIGID_BODY,
    MATRIX_VEHICLE_CHASSIS,
    MATRIX_VEHICLE_WHEEL
};

enum matrix_axis_e
{
    MATRIX_AXIS_X = 0,
    MATRIX_AXIS_Y = 1,
    MATRIX_AXIS_Z = 2,
    MATRIX_AXES_TOTAL = 3
};

struct matrix_t
{
    float value[16]; /* must go first to ensure alignment */
    enum matrix_e type;
    int update_tag;
    enum matrix_axis_e rotaxis;
    int rotanglei;
    int zneari;
    int zfari;
    int rigid_body;
    int vehicle;
    int wheel;
    struct vector_t *argv[MATRIX_ARGVS];
    struct matrix_t *argm[MATRIX_ARGMS];
};

int matrix_init(lua_State *lua, int count, int nesting);
void matrix_done(void);
struct matrix_t * matrix_get(int);
int matrix_update(struct matrix_t *matrix, float dt,
                  int update_tag, int force);
int matrix_nesting(struct matrix_t *matrix, int limit);
void matrix_inv(float *out, float *m);
void matrix_mul(float *out, float *m1, float *m2);
void matrix_pos_scl_rot(float *out, float *pos, float *scl,
                        enum matrix_axis_e rotaxis, float rotangle);
void matrix_pos_axes(float *out, float *pos, float *ax,
                     float *ay, float *az);
void matrix_from_to_up(float *out, float *from, float *to, float *up);
void matrix_frustum(float *out, float left, float right, float bottom,
                    float top, float znear, float zfar);
void matrix_ortho(float *out, float left, float right, float bottom,
                  float top, float znear, float zfar);

#endif /* CORE_MATRIX_H */

