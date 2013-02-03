#pragma once

#include "lua.h"
#include "GL/gl.h"

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
    GLfloat value[16]; /* should be first to ensure alignment */
    enum matrix_e type;
    int frame_tag;
    int vacant;
    enum matrix_axis_e rotaxis;
    int rotanglei;
    int zneari;
    int zfari;
    int rigid_body;
    int vehicle;
    int wheel;
    struct vector_t *argv[MATRIX_ARGVS];
    struct matrix_t *argm[MATRIX_ARGMS];
    struct matrix_t *next;
    char padding[104];
};

int matrix_init(lua_State *lua, int count, int nesting);
void matrix_done(void);
struct matrix_t * matrix_get(int);
int matrix_update(struct matrix_t *matrix, float dt,
                  int frame_tag, int force);
int matrix_nesting(struct matrix_t *matrix, int limit);
void matrix_inv(GLfloat *out, GLfloat *m);
void matrix_mul(GLfloat *out, GLfloat *m1, GLfloat *m2);
void matrix_pos_scl_rot(GLfloat *out, GLfloat *pos, GLfloat *scl,
                        enum matrix_axis_e rotaxis, GLfloat rotangle);
void matrix_pos_axes(GLfloat *out, GLfloat *pos, GLfloat *ax,
                     GLfloat *ay, GLfloat *az);
void matrix_from_to_up(GLfloat *out, GLfloat *from, GLfloat *to, GLfloat *up);
void matrix_frustum(GLfloat *out, GLfloat left, GLfloat right, GLfloat bottom,
                    GLfloat top, GLfloat znear, GLfloat zfar);
void matrix_ortho(GLfloat *out, GLfloat left, GLfloat right, GLfloat bottom,
                  GLfloat top, GLfloat znear, GLfloat zfar);
