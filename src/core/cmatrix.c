#include "cmatrix.h"
#include "vector.h"
#include "physics.h"
#include "util.h"
#include "pmem.h"
#include <math.h>
#include <stdio.h>
#include <string.h>

#define CMATRIX_SIZE 256

enum cmatrices_e {
    CMATRIX_FORCED_UPDATE = -1 /* special update_tag */
};

struct cmatrices_t {
    int count, nesting;
    char *pool;
};

_Static_assert(sizeof(struct cmatrix_t) <= CMATRIX_SIZE,
               "Invalid cmatrix_t size");

static struct cmatrices_t g_cmatrices;

static void cmatrix_clear_args(struct cmatrix_t *matrix) {
    for (int i = 0; i < CMATRIX_ARGVS; ++i)
        matrix->argv[i] = 0;
    for (int i = 0; i < CMATRIX_ARGMS; ++i)
        matrix->argm[i] = 0;
}

static int api_matrix_copy(lua_State *lua) {
    struct cmatrix_t *matrix, *msrc;

    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_matrix_copy: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    msrc = cmatrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (!matrix || !msrc) {
        lua_pushstring(lua, "api_matrix_copy: invalid matrix");
        lua_error(lua);
        return 0;
    }
    memcpy(matrix, msrc, CMATRIX_SIZE);
    return 0;
}

static int api_matrix_stop(lua_State *lua) {
    struct cmatrix_t *matrix;

    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_matrix_stop: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (!matrix) {
        lua_pushstring(lua, "api_matrix_stop: invalid matrix");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);
    matrix->update_tag = 0;
    matrix->type = CMATRIX_CONST;

    return 0;
}

static int api_matrix_update(lua_State *lua) {
    struct cmatrix_t *matrix;
    int update_tag, force;
    float dt;

    if (lua_gettop(lua) != 3 || !util_isint(lua, 1) ||
    !util_isfloat(lua, 2) || !util_isint(lua, 3)) {
        lua_pushstring(lua, "api_matrix_update: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    dt = (float)lua_tonumber(lua, 2);
    update_tag = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (!matrix) {
        lua_pushstring(lua, "api_matrix_update: invalid matrix");
        lua_error(lua);
        return 0;
    }
    force = update_tag == CMATRIX_FORCED_UPDATE;
    if (cmatrix_update(matrix, dt, update_tag, force)) {
        lua_pushstring(lua, "api_matrix_update: update error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_mul(lua_State *lua) {
    struct cmatrix_t *matrix, *m0, *m1;

    if (lua_gettop(lua) != 3 || !util_isint(lua, 1) ||
    !util_isint(lua, 2) || !util_isint(lua, 3)) {
        lua_pushstring(lua, "api_matrix_mul: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    m0 = cmatrix_get(lua_tointeger(lua, 2));
    m1 = cmatrix_get(lua_tointeger(lua, 3));
    lua_pop(lua, 3);

    if (!matrix || !m0 || !m1) {
        lua_pushstring(lua, "api_matrix_mul: invalid matrix");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_MUL;
    matrix->argm[0] = m0;
    matrix->argm[1] = m1;

    if (!cmatrix_nesting(matrix, g_cmatrices.nesting)) {
        lua_pushstring(lua, "api_matrix_mul: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_mul_stop(lua_State *lua) {
    struct cmatrix_t *matrix, *m0, *m1;
    float m[16];

    if (lua_gettop(lua) != 3 || !util_isint(lua, 1) ||
    !util_isint(lua, 2) || !util_isint(lua, 3)) {
        lua_pushstring(lua, "api_matrix_mul_stop: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    m0 = cmatrix_get(lua_tointeger(lua, 2));
    m1 = cmatrix_get(lua_tointeger(lua, 3));
    lua_pop(lua, 3);

    if (!matrix || !m0 || !m1) {
        lua_pushstring(lua, "api_matrix_mul_stop: invalid matrix");
        lua_error(lua);
        return 0;
    }
    cmatrix_mul(m, m0->value, m1->value);

    cmatrix_clear_args(matrix);
    matrix->update_tag = 0;
    matrix->type = CMATRIX_CONST;
    memcpy(matrix->value, m, 16 * sizeof(float));

    return 0;
}

static int api_matrix_inv(lua_State *lua) {
    struct cmatrix_t *matrix, *m0;

    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_matrix_inv: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    m0 = cmatrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (!matrix || !m0) {
        lua_pushstring(lua, "api_matrix_inv: invalid matrix");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_INV;
    matrix->argm[0] = m0;

    if (!cmatrix_nesting(matrix, g_cmatrices.nesting)) {
        lua_pushstring(lua, "api_matrix_inv: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_frustum(lua_State *lua) {
    struct cmatrix_t *matrix;
    struct vector_t *v0, *v1;
    int zneari, zfari;

    if (lua_gettop(lua) != 5 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isint(lua, 5)) {
        lua_pushstring(lua, "api_matrix_frustum: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    zneari = lua_tointeger(lua, 4);
    zfari = lua_tointeger(lua, 5);
    lua_pop(lua, 5);

    if (!matrix || !v0 || !v1) {
        lua_pushstring(lua, "api_matrix_frustum: invalid objects");
        lua_error(lua);
        return 0;
    }
    if (zneari < 0 || zneari > 3 || zfari < 0 || zfari > 3) {
        lua_pushstring(lua, "api_matrix_frustum: znear/zfar out of range");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_FRUSTUM;
    matrix->argv[0] = v0;
    matrix->argv[1] = v1;
    matrix->zneari = zneari;
    matrix->zfari = zfari;

    if (!cmatrix_nesting(matrix, g_cmatrices.nesting)) {
        lua_pushstring(lua, "api_matrix_frustum: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_ortho(lua_State *lua) {
    struct cmatrix_t *matrix;
    struct vector_t *v0, *v1;
    int zneari, zfari;

    if (lua_gettop(lua) != 5 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isint(lua, 5)) {
        lua_pushstring(lua, "api_matrix_ortho: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    zneari = lua_tointeger(lua, 4);
    zfari = lua_tointeger(lua, 5);
    lua_pop(lua, 5);

    if (!matrix || !v0 || !v1) {
        lua_pushstring(lua, "api_matrix_ortho: invalid objects");
        lua_error(lua);
        return 0;
    }
    if (zneari < 0 || zneari > 3 || zfari < 0 || zfari > 3) {
        lua_pushstring(lua, "api_matrix_ortho: znear/zfar out of range");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_ORTHO;
    matrix->argv[0] = v0;
    matrix->argv[1] = v1;
    matrix->zneari = zneari;
    matrix->zfari = zfari;

    if (!cmatrix_nesting(matrix, g_cmatrices.nesting)) {
        lua_pushstring(lua, "api_matrix_ortho: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_pos_scl_rot(lua_State *lua) {
    struct cmatrix_t *matrix;
    struct vector_t *v0, *v1, *v2;
    int rotaxis, rotanglei;

    if (lua_gettop(lua) != 6 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) ||
    !util_isint(lua, 5) || !util_isint(lua, 6)) {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    v2 = vector_get(lua_tointeger(lua, 4));
    rotaxis = lua_tointeger(lua, 5);
    rotanglei = lua_tointeger(lua, 6);
    lua_pop(lua, 6);

    if (!matrix || !v0 || !v1 || !v2) {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: invalid objects");
        lua_error(lua);
        return 0;
    }
    if (rotaxis < 0 || rotaxis >= CMATRIX_AXES_TOTAL) {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: invalid rotation axis");
        lua_error(lua);
        return 0;
    }
    if (rotanglei < 0 || rotanglei > 3) {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: rot angle out of range");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_POS_SCL_ROT;
    matrix->argv[0] = v0;
    matrix->argv[1] = v1;
    matrix->argv[2] = v2;
    matrix->rotaxis = (enum cmatrix_axis_e)rotaxis;
    matrix->rotanglei = rotanglei;

    if (!cmatrix_nesting(matrix, g_cmatrices.nesting)) {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_from_to_up(lua_State *lua) {
    struct cmatrix_t *matrix;
    struct vector_t *v0, *v1, *v2;

    if (lua_gettop(lua) != 4 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4)) {
        lua_pushstring(lua, "api_matrix_from_to_up: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    v2 = vector_get(lua_tointeger(lua, 4));
    lua_pop(lua, 4);

    if (!matrix || !v0 || !v1 || !v2) {
        lua_pushstring(lua, "api_matrix_from_to_up: invalid objects");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_FROM_TO_UP;
    matrix->argv[0] = v0;
    matrix->argv[1] = v1;
    matrix->argv[2] = v2;

    if (!cmatrix_nesting(matrix, g_cmatrices.nesting)) {
        lua_pushstring(lua, "api_matrix_from_to_up: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_rigid_body(lua_State *lua) {
    struct cmatrix_t *matrix;
    int rbi;

    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_matrix_rigid_body: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    rbi = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    if (!matrix) {
        lua_pushstring(lua, "api_matrix_rigid_body: invalid matrix");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_RIGID_BODY;
    matrix->rigid_body = rbi;

    if (physics_rb_fetch_tm(rbi, matrix->value)) {
        lua_pushstring(lua, "api_matrix_rigid_body: invalid rigid body");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_vehicle_chassis(lua_State *lua) {
    struct cmatrix_t *matrix;
    int vehi;

    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_matrix_vehicle_chassis: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    vehi = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    if (!matrix) {
        lua_pushstring(lua, "api_matrix_vehicle_chassis: invalid matrix");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_VEHICLE_CHASSIS;
    matrix->vehicle = vehi;

    if (physics_veh_fetch_chassis_tm(vehi, matrix->value)) {
        lua_pushstring(lua, "api_matrix_vehicle_chassis: invalid vehicle");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_matrix_vehicle_wheel(lua_State *lua) {
    struct cmatrix_t *matrix;
    int vehi, wheel;

    if (lua_gettop(lua) != 3 || !util_isint(lua, 1) ||
    !util_isint(lua, 2) || !util_isint(lua, 3)) {
        lua_pushstring(lua, "api_matrix_vehicle_wheel: incorrect argument");
        lua_error(lua);
        return 0;
    }
    matrix = cmatrix_get(lua_tointeger(lua, 1));
    vehi = lua_tointeger(lua, 2);
    wheel = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (!matrix) {
        lua_pushstring(lua, "api_matrix_vehicle_wheel: invalid matrix");
        lua_error(lua);
        return 0;
    }
    cmatrix_clear_args(matrix);

    matrix->update_tag = 0;
    matrix->type = CMATRIX_VEHICLE_WHEEL;
    matrix->vehicle = vehi;
    matrix->wheel = wheel;

    if (physics_veh_fetch_wheel_tm(vehi, wheel, matrix->value)) {
        lua_pushstring(lua, "api_matrix_vehicle_wheel: invalid object");
        lua_error(lua);
        return 0;
    }
    return 0;
}

int cmatrix_init(lua_State *lua, int count, int nesting) {
    struct cmatrix_t *m;
    g_cmatrices.count = count;
    g_cmatrices.pool = pmem_alloc(PMEM_ALIGNOF(struct cmatrix_t),
                                 CMATRIX_SIZE * count);
    if (!g_cmatrices.pool)
        return 1;
    for (int i = 0; i < count; ++i) {
        m = cmatrix_get(i);
        for (int j = 0; j < 16; ++j)
            m->value[j] = 0;
        m->type = CMATRIX_CONST;
    }
    g_cmatrices.nesting = nesting;

    #define REGF(x) lua_register(lua, #x, x)
    REGF(api_matrix_copy);
    REGF(api_matrix_stop);
    REGF(api_matrix_update);
    REGF(api_matrix_inv);
    REGF(api_matrix_mul);
    REGF(api_matrix_mul_stop);
    REGF(api_matrix_frustum);
    REGF(api_matrix_ortho);
    REGF(api_matrix_pos_scl_rot);
    REGF(api_matrix_from_to_up);
    REGF(api_matrix_rigid_body);
    REGF(api_matrix_vehicle_chassis);
    REGF(api_matrix_vehicle_wheel);
    #undef REGF
    #define REGN(x) lua_pushinteger(lua, C##x); lua_setglobal(lua, "API_"#x)
    REGN(MATRIX_AXIS_X);
    REGN(MATRIX_AXIS_Y);
    REGN(MATRIX_AXIS_Z);
    REGN(MATRIX_FORCED_UPDATE);
    #undef REGN
    return 0;
}

void cmatrix_done(void) {
    if (!g_cmatrices.pool)
        return;
    pmem_free(g_cmatrices.pool);
    g_cmatrices.pool = 0;
}

struct cmatrix_t * cmatrix_get(int i) {
    if (i >= 0 && i < g_cmatrices.count)
        return (struct cmatrix_t*)(g_cmatrices.pool + CMATRIX_SIZE * i);
    else
        return 0;
}

int cmatrix_nesting(struct cmatrix_t *matrix, int limit) {
    int min, cur;
    if (limit > 0) {
        min = limit;
        for (int i = 0; i < CMATRIX_ARGVS; ++i) {
            if (!matrix->argv[i])
                continue;
            cur = vector_nesting(matrix->argv[i], limit - 1);
            if (cur < min)
                min = cur;
        }
        for (int i = 0; i < CMATRIX_ARGMS; ++i) {
            if (!matrix->argm[i])
                continue;
            cur = cmatrix_nesting(matrix->argm[i], limit - 1);
            if (cur < min)
                min = cur;
        }
        return min;
    }
    else
        return limit;
}

static int cmatrix_update_mul(struct cmatrix_t *m, float dt, int force) {
    float *m0, *m1;
    for (int i = 0; i < 2; ++i)
        if (cmatrix_update(m->argm[i], dt, m->update_tag, force))
            return 1;
    m0 = m->argm[0]->value;
    m1 = m->argm[1]->value;
    cmatrix_mul(m->value, m0, m1);
    return 0;
}

static int cmatrix_update_inv(struct cmatrix_t *m, float dt, int force) {
    float *m0;
    if (cmatrix_update(m->argm[0], dt, m->update_tag, force))
        return 1;
    m0 = m->argm[0]->value;
    cmatrix_inv(m->value, m0);
    return 0;
}

static int cmatrix_update_frustum(struct cmatrix_t *m, float dt, int force) {
    float *v0, *v1;
    for (int i = 0; i < 2; ++i)
        if (vector_update(m->argv[i], dt, m->update_tag, force))
            return 1;
    v0 = m->argv[0]->value;
    v1 = m->argv[1]->value;
    cmatrix_frustum(m->value, v0[0], v0[1], v0[2], v0[3],
                    v1[m->zneari], v1[m->zfari]);
    return 0;
}

static int cmatrix_update_ortho(struct cmatrix_t *m, float dt, int force) {
    float *v0, *v1;
    for (int i = 0; i < 2; ++i)
        if (vector_update(m->argv[i], dt, m->update_tag, force))
            return 1;
    v0 = m->argv[0]->value;
    v1 = m->argv[1]->value;
    cmatrix_ortho(m->value, v0[0], v0[1], v0[2], v0[3],
                  v1[m->zneari], v1[m->zfari]);
    return 0;
}

static int cmatrix_update_pos_scl_rot(struct cmatrix_t *m, float dt, int force) {
    float *v0, *v1, *v2;
    for (int i = 0; i < 3; ++i)
        if (vector_update(m->argv[i], dt, m->update_tag, force))
            return 1;
    v0 = m->argv[0]->value;
    v1 = m->argv[1]->value;
    v2 = m->argv[2]->value;
    cmatrix_pos_scl_rot(m->value, v0, v1, m->rotaxis, v2[m->rotanglei]);
    return 0;
}

static int cmatrix_update_from_to_up(struct cmatrix_t *m, float dt, int force) {
    float *v0, *v1, *v2;
    for (int i = 0; i < 3; ++i)
        if (vector_update(m->argv[i], dt, m->update_tag, force))
            return 1;
    v0 = m->argv[0]->value;
    v1 = m->argv[1]->value;
    v2 = m->argv[2]->value;
    cmatrix_from_to_up(m->value, v0, v1, v2);
    return 0;
}

int cmatrix_update(struct cmatrix_t *m, float dt, int update_tag, int force) {
    if (m->type == CMATRIX_CONST)
        return 0;
    if (!force && m->update_tag == update_tag)
        return 0;
    m->update_tag = update_tag;
    if (m->type == CMATRIX_MUL)
        return cmatrix_update_mul(m, dt, force);
    else if (m->type == CMATRIX_INV)
        return cmatrix_update_inv(m, dt, force);
    else if (m->type == CMATRIX_FRUSTUM)
        return cmatrix_update_frustum(m, dt, force);
    else if (m->type == CMATRIX_ORTHO)
        return cmatrix_update_ortho(m, dt, force);
    else if (m->type == CMATRIX_POS_SCL_ROT)
        return cmatrix_update_pos_scl_rot(m, dt, force);
    else if (m->type == CMATRIX_FROM_TO_UP)
        return cmatrix_update_from_to_up(m, dt, force);
    else if (m->type == CMATRIX_RIGID_BODY)
        return physics_rb_fetch_tm(m->rigid_body, m->value);
    else if (m->type == CMATRIX_VEHICLE_CHASSIS)
        return physics_veh_fetch_chassis_tm(m->vehicle, m->value);
    else if (m->type == CMATRIX_VEHICLE_WHEEL)
        return physics_veh_fetch_wheel_tm(m->vehicle, m->wheel, m->value);
    return 0;
}

void cmatrix_mul(float *out, float *m1, float *m2) {
    out[0] = m1[0]*m2[0] + m1[4]*m2[1] + m1[ 8]*m2[2] + m1[12]*m2[3];
    out[1] = m1[1]*m2[0] + m1[5]*m2[1] + m1[ 9]*m2[2] + m1[13]*m2[3];
    out[2] = m1[2]*m2[0] + m1[6]*m2[1] + m1[10]*m2[2] + m1[14]*m2[3];
    out[3] = m1[3]*m2[0] + m1[7]*m2[1] + m1[11]*m2[2] + m1[15]*m2[3];

    out[4] = m1[0]*m2[4] + m1[4]*m2[5] + m1[ 8]*m2[6] + m1[12]*m2[7];
    out[5] = m1[1]*m2[4] + m1[5]*m2[5] + m1[ 9]*m2[6] + m1[13]*m2[7];
    out[6] = m1[2]*m2[4] + m1[6]*m2[5] + m1[10]*m2[6] + m1[14]*m2[7];
    out[7] = m1[3]*m2[4] + m1[7]*m2[5] + m1[11]*m2[6] + m1[15]*m2[7];

    out[ 8] = m1[0]*m2[8] + m1[4]*m2[9] + m1[ 8]*m2[10] + m1[12]*m2[11];
    out[ 9] = m1[1]*m2[8] + m1[5]*m2[9] + m1[ 9]*m2[10] + m1[13]*m2[11];
    out[10] = m1[2]*m2[8] + m1[6]*m2[9] + m1[10]*m2[10] + m1[14]*m2[11];
    out[11] = m1[3]*m2[8] + m1[7]*m2[9] + m1[11]*m2[10] + m1[15]*m2[11];

    out[12] = m1[0]*m2[12] + m1[4]*m2[13] + m1[ 8]*m2[14] + m1[12]*m2[15];
    out[13] = m1[1]*m2[12] + m1[5]*m2[13] + m1[ 9]*m2[14] + m1[13]*m2[15];
    out[14] = m1[2]*m2[12] + m1[6]*m2[13] + m1[10]*m2[14] + m1[14]*m2[15];
    out[15] = m1[3]*m2[12] + m1[7]*m2[13] + m1[11]*m2[14] + m1[15]*m2[15];
}

void cmatrix_from_to_up(float *out, float *from, float *to, float *up) {
    static const float THRESHOLD = 0.1f;
    float diff[4], az[4], ax[4], ay[4], len;
    vector_wsum(diff, 1, to, -1, from);
    len = vector_len(diff);
    if (len < THRESHOLD)
        return;
    vector_wsum(az, -1.0f / len, diff, 0, diff);
    vector_cross(ax, up, az);
    vector_cross(ay, az, ax);
    cmatrix_pos_axes(out, from, ax, ay, az);
}

void cmatrix_pos_axes(float *out, float *pos, float *ax, float *ay, float *az) {
    out[ 0] =  ax[0]; out[ 1] =  ax[1]; out[ 2] =  ax[2]; out[ 3] = 0;
    out[ 4] =  ay[0]; out[ 5] =  ay[1]; out[ 6] =  ay[2]; out[ 7] = 0;
    out[ 8] =  az[0]; out[ 9] =  az[1]; out[10] =  az[2]; out[11] = 0;
    out[12] = pos[0]; out[13] = pos[1]; out[14] = pos[2]; out[15] = 1;
}

void cmatrix_pos_scl_rot(float *out, float *pos, float *scl,
enum cmatrix_axis_e rotaxis, float rotangle) {
    float axisx[3], axisy[3], axisz[3], rcos, rsin;

    rcos = cosf(rotangle);
    rsin = sinf(rotangle);
    if (rotaxis == CMATRIX_AXIS_X) {
        axisx[0] = 1; axisx[1] =     0; axisx[2] =    0; 
        axisy[0] = 0; axisy[1] =  rcos; axisy[2] = rsin; 
        axisz[0] = 0; axisz[1] = -rsin; axisz[2] = rcos; 
    }
    else if (rotaxis == CMATRIX_AXIS_Y) {
        axisx[0] = rcos; axisx[1] = 0; axisx[2] = -rsin; 
        axisy[0] =    0; axisy[1] = 1; axisy[2] =     0; 
        axisz[0] = rsin; axisz[1] = 0; axisz[2] =  rcos; 
    }
    else if (rotaxis == CMATRIX_AXIS_Z) {
        axisx[0] =  rcos; axisx[1] = rsin; axisx[2] = 0;
        axisy[0] = -rsin; axisy[1] = rcos; axisy[2] = 0;
        axisz[0] =     0; axisz[1] =    0; axisz[2] = 1;
    }
    axisx[0] *= scl[0]; axisx[1] *= scl[0]; axisx[2] *= scl[0];
    axisy[0] *= scl[1]; axisy[1] *= scl[1]; axisy[2] *= scl[1];
    axisz[0] *= scl[2]; axisz[1] *= scl[2]; axisz[2] *= scl[2];

    cmatrix_pos_axes(out, pos, axisx, axisy, axisz);
}

void cmatrix_inv(float *out, float *m) {
    float inv[16], det;
    int i;

    inv[0] = m[5]  * m[10] * m[15] - 
             m[5]  * m[11] * m[14] - 
             m[9]  * m[6]  * m[15] + 
             m[9]  * m[7]  * m[14] +
             m[13] * m[6]  * m[11] - 
             m[13] * m[7]  * m[10];

    inv[4] = -m[4]  * m[10] * m[15] + 
              m[4]  * m[11] * m[14] + 
              m[8]  * m[6]  * m[15] - 
              m[8]  * m[7]  * m[14] - 
              m[12] * m[6]  * m[11] + 
              m[12] * m[7]  * m[10];

    inv[8] = m[4]  * m[9]  * m[15] - 
             m[4]  * m[11] * m[13] - 
             m[8]  * m[5]  * m[15] + 
             m[8]  * m[7]  * m[13] + 
             m[12] * m[5]  * m[11] - 
             m[12] * m[7]  * m[9];

    inv[12] = -m[4]  * m[9]  * m[14] + 
               m[4]  * m[10] * m[13] +
               m[8]  * m[5]  * m[14] - 
               m[8]  * m[6]  * m[13] - 
               m[12] * m[5]  * m[10] + 
               m[12] * m[6]  * m[9];

    inv[1] = -m[1]  * m[10] * m[15] + 
              m[1]  * m[11] * m[14] + 
              m[9]  * m[2]  * m[15] - 
              m[9]  * m[3]  * m[14] - 
              m[13] * m[2]  * m[11] + 
              m[13] * m[3]  * m[10];

    inv[5] = m[0]  * m[10] * m[15] - 
             m[0]  * m[11] * m[14] - 
             m[8]  * m[2]  * m[15] + 
             m[8]  * m[3]  * m[14] + 
             m[12] * m[2]  * m[11] - 
             m[12] * m[3]  * m[10];

    inv[9] = -m[0]  * m[9]  * m[15] + 
              m[0]  * m[11] * m[13] + 
              m[8]  * m[1]  * m[15] - 
              m[8]  * m[3]  * m[13] - 
              m[12] * m[1]  * m[11] + 
              m[12] * m[3]  * m[9];

    inv[13] = m[0]  * m[9]  * m[14] - 
              m[0]  * m[10] * m[13] - 
              m[8]  * m[1]  * m[14] + 
              m[8]  * m[2]  * m[13] + 
              m[12] * m[1]  * m[10] - 
              m[12] * m[2]  * m[9];

    inv[2] = m[1]  * m[6] * m[15] - 
             m[1]  * m[7] * m[14] - 
             m[5]  * m[2] * m[15] + 
             m[5]  * m[3] * m[14] + 
             m[13] * m[2] * m[7] - 
             m[13] * m[3] * m[6];

    inv[6] = -m[0]  * m[6] * m[15] + 
              m[0]  * m[7] * m[14] + 
              m[4]  * m[2] * m[15] - 
              m[4]  * m[3] * m[14] - 
              m[12] * m[2] * m[7] + 
              m[12] * m[3] * m[6];

    inv[10] = m[0]  * m[5] * m[15] - 
              m[0]  * m[7] * m[13] - 
              m[4]  * m[1] * m[15] + 
              m[4]  * m[3] * m[13] + 
              m[12] * m[1] * m[7] - 
              m[12] * m[3] * m[5];

    inv[14] = -m[0]  * m[5] * m[14] + 
               m[0]  * m[6] * m[13] + 
               m[4]  * m[1] * m[14] - 
               m[4]  * m[2] * m[13] - 
               m[12] * m[1] * m[6] + 
               m[12] * m[2] * m[5];

    inv[3] = -m[1] * m[6] * m[11] + 
              m[1] * m[7] * m[10] + 
              m[5] * m[2] * m[11] - 
              m[5] * m[3] * m[10] - 
              m[9] * m[2] * m[7] + 
              m[9] * m[3] * m[6];

    inv[7] = m[0] * m[6] * m[11] - 
             m[0] * m[7] * m[10] - 
             m[4] * m[2] * m[11] + 
             m[4] * m[3] * m[10] + 
             m[8] * m[2] * m[7] - 
             m[8] * m[3] * m[6];

    inv[11] = -m[0] * m[5] * m[11] + 
               m[0] * m[7] * m[9] + 
               m[4] * m[1] * m[11] - 
               m[4] * m[3] * m[9] - 
               m[8] * m[1] * m[7] + 
               m[8] * m[3] * m[5];

    inv[15] = m[0] * m[5] * m[10] - 
              m[0] * m[6] * m[9] - 
              m[4] * m[1] * m[10] + 
              m[4] * m[2] * m[9] + 
              m[8] * m[1] * m[6] - 
              m[8] * m[2] * m[5];

    det = m[0] * inv[0] + m[1] * inv[4] + m[2] * inv[8] + m[3] * inv[12];
    if (!det)
        return;
    det = 1.0f / det;
    for (i = 0; i < 16; i++)
        out[i] = inv[i] * det;
}

void cmatrix_frustum(float *out, float left, float right,
float bottom, float top, float znear, float zfar) {
    float temp, temp2, temp3, temp4;
    temp = 2.0f * znear;
    temp2 = right - left;
    temp3 = top - bottom;
    temp4 = zfar - znear;

    out[0] = temp / temp2;
    out[1] = 0;
    out[2] = 0;
    out[3] = 0;

    out[4] = 0;
    out[5] = temp / temp3;
    out[6] = 0;
    out[7] = 0;

    out[8] = (right + left) / temp2;
    out[9] = (top + bottom) / temp3;
    out[10] = (-zfar - znear) / temp4;
    out[11] = -1;

    out[12] = 0;
    out[13] = 0;
    out[14] = (-temp * zfar) / temp4;
    out[15] = 0;
}

void cmatrix_ortho(float *out, float left, float right,
float bottom, float top, float znear, float zfar) {
    out[0] = 2.0f / (right - left);
    out[1] = 0;
    out[2] = 0;
    out[3] = 0;

    out[4] = 0;
    out[5] = 2.0f / (top - bottom);
    out[6] = 0;
    out[7] = 0;

    out[8] = 0;
    out[9] = 0;
    out[10] = -2.0f / (zfar - znear);
    out[11] = 0;

    out[12] = -(right + left) / (right - left);
    out[13] = -(top + bottom) / (top - bottom);
    out[14] = -(zfar + znear) / (zfar - znear);
    out[15] = 1;
}

