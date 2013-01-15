#pragma once

#include "lua.h"
#include "GL/gl.h"

#define MATRIX_ARGVS 3
#define MATRIX_ARGMS 2

enum matrix_e
{
    MATRIX_CONST = 0,
    MATRIX_MUL = 1,
    MATRIX_INV = 2,
    MATRIX_POS_SCL_ROT = 3,
    MATRIX_RIGID_BODY = 4,
    MATRIX_VEHICLE_CHASSIS = 5,
    MATRIX_VEHICLE_WHEEL = 6
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
    enum matrix_e type;
    GLfloat value[16];
    int frame_tag;
    int vacant;
    enum matrix_axis_e rotaxis;
    int rotanglei;
    int rigid_body;
    int vehicle;
    int wheel;
    struct vector_t *argv[MATRIX_ARGVS];
    struct matrix_t *argm[MATRIX_ARGMS];
    struct matrix_t *next;
};

int matrix_init(lua_State *lua, int count, int nesting);
void matrix_done(void);
struct matrix_t * matrix_get(int);
void matrix_update(struct matrix_t *matrix, float dt,
                   int frame_tag, int force);
int matrix_nesting(struct matrix_t *matrix, int limit);
void matrix_inv(GLfloat *out, GLfloat *m);
void matrix_mul(GLfloat *out, GLfloat *m1, GLfloat *m2);
void matrix_pos_scl_rot(GLfloat *out, GLfloat *pos, GLfloat *scl,
                        enum matrix_axis_e rotaxis, GLfloat rotangle);
