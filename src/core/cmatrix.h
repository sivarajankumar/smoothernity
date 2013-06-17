#ifndef CMATRIX_H
#define CMATRIX_H

#include "lua.h"

#define CMATRIX_ARGVS 3
#define CMATRIX_ARGMS 2

enum cmatrix_e {
    CMATRIX_CONST,
    CMATRIX_MUL,
    CMATRIX_INV,
    CMATRIX_FRUSTUM,
    CMATRIX_ORTHO,
    CMATRIX_POS_SCL_ROT,
    CMATRIX_FROM_TO_UP,
    CMATRIX_RIGID_BODY,
    CMATRIX_VEHICLE_CHASSIS,
    CMATRIX_VEHICLE_WHEEL
};

enum cmatrix_axis_e {
    CMATRIX_AXIS_X,
    CMATRIX_AXIS_Y,
    CMATRIX_AXIS_Z,
    CMATRIX_AXES_TOTAL
};

struct cmatrix_t {
    float value[16]; /* Must go first to ensure alignment. */
    enum cmatrix_e type;
    enum cmatrix_axis_e rotaxis;
    int update_tag, rotanglei, zneari, zfari, rigid_body, vehicle, wheel;
    struct cvector_t *argv[CMATRIX_ARGVS];
    struct cmatrix_t *argm[CMATRIX_ARGMS];
};

int cmatrix_init(lua_State *lua, int count, int nesting);
void cmatrix_done(void);
struct cmatrix_t * cmatrix_get(int);
int cmatrix_update(struct cmatrix_t *matrix, float dt,
                   int update_tag, int force);
int cmatrix_nesting(struct cmatrix_t *matrix, int limit);
void cmatrix_inv(float *out, float *m);
void cmatrix_mul(float *out, float *m1, float *m2);
void cmatrix_pos_scl_rot(float *out, float *pos, float *scl,
                         enum cmatrix_axis_e rotaxis, float rotangle);
void cmatrix_pos_axes(float *out, float *pos, float *ax,
                      float *ay, float *az);
void cmatrix_from_to_up(float *out, float *from, float *to, float *up);
void cmatrix_frustum(float *out, float left, float right, float bottom,
                     float top, float znear, float zfar);
void cmatrix_ortho(float *out, float left, float right, float bottom,
                   float top, float znear, float zfar);

#endif /* CMATRIX_H */

