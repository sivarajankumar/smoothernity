#include "matrix.h"
#include "vector.h"
#include "physics.h"
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct matrices_t
{
    int count;
    int left;
    int nesting;
    struct matrix_t *pool;
    struct matrix_t *vacant;
};

static struct matrices_t g_matrices;

static void matrix_clear_args(struct matrix_t *matrix)
{
    int i;
    for (i = 0; i < MATRIX_ARGVS; ++i)
        matrix->argv[i] = 0;
    for (i = 0; i < MATRIX_ARGMS; ++i)
        matrix->argm[i] = 0;
}

static int api_matrix_alloc(lua_State *lua)
{
    struct matrix_t *matrix;

    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_matrix_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    if (g_matrices.vacant == 0)
    {
        lua_pushstring(lua, "api_matrix_alloc: out of matrices");
        lua_error(lua);
        return 0;
    }

    --g_matrices.left;
    matrix = g_matrices.vacant;
    g_matrices.vacant = g_matrices.vacant->next;

    memset(matrix, 0, sizeof(struct matrix_t));

    lua_pushinteger(lua, matrix - g_matrices.pool);
    return 1;
}

static int api_matrix_free(lua_State *lua)
{
    struct matrix_t *matrix;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_matrix_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (matrix == 0 || matrix->vacant)
    {
        lua_pushstring(lua, "api_matrix_free: invalid matrix");
        lua_error(lua);
        return 0;
    }

    matrix->vacant = 1;
    ++g_matrices.left;

    matrix->next = g_matrices.vacant;
    g_matrices.vacant = matrix;
    return 0;
}

static int api_matrix_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_matrix_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_matrices.left);
    return 1;
}

static int api_matrix_const(lua_State *lua)
{
    struct matrix_t *matrix;
    float value[16];
    int i;

    if (lua_gettop(lua) != 17)
    {
        lua_pushstring(lua, "api_matrix_const: incorrect argument");
        lua_error(lua);
        return 0;
    }
    for (i = 1; i <= 17; ++i)
    {
        if (!lua_isnumber(lua, i))
        {
            lua_pushstring(lua, "api_matrix_const: incorrect argument");
            lua_error(lua);
            return 0;
        }
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    for (i = 0; i < 16; ++i)
        value[i] = lua_tonumber(lua, i + 2);
    lua_pop(lua, 17);

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_matrix_const: invalid matrix");
        lua_error(lua);
        return 0;
    }

    matrix_clear_args(matrix);

    matrix->frame_tag = 0;
    matrix->type = MATRIX_CONST;
    memcpy(matrix->value, value, 16 * sizeof(GLfloat));

    return 0;
}

static int api_matrix_stop(lua_State *lua)
{
    struct matrix_t *matrix;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_matrix_stop: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_matrix_stop: invalid matrix");
        lua_error(lua);
        return 0;
    }

    matrix_clear_args(matrix);

    matrix->frame_tag = 0;
    matrix->type = MATRIX_CONST;

    return 0;
}

static int api_matrix_mul(lua_State *lua)
{
    struct matrix_t *matrix, *m0, *m1;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_matrix_mul: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    m0 = matrix_get(lua_tointeger(lua, 2));
    m1 = matrix_get(lua_tointeger(lua, 3));
    lua_pop(lua, 3);

    if (matrix == 0 || m0 == 0 || m1 == 0)
    {
        lua_pushstring(lua, "api_matrix_mul: invalid matrix");
        lua_error(lua);
        return 0;
    }

    matrix_clear_args(matrix);

    matrix->frame_tag = 0;
    matrix->type = MATRIX_MUL;
    matrix->argm[0] = m0;
    matrix->argm[1] = m1;

    if (matrix_nesting(matrix, g_matrices.nesting) == 0)
    {
        lua_pushstring(lua, "api_matrix_mul: nesting is too deep");
        lua_error(lua);
        return 0;
    }

    matrix_update(matrix, 0, 0, 1);

    return 0;
}

static int api_matrix_mul_stop(lua_State *lua)
{
    struct matrix_t *matrix, *m0, *m1;
    GLfloat m[16];

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_matrix_mul_stop: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    m0 = matrix_get(lua_tointeger(lua, 2));
    m1 = matrix_get(lua_tointeger(lua, 3));
    lua_pop(lua, 3);

    if (matrix == 0 || m0 == 0 || m1 == 0)
    {
        lua_pushstring(lua, "api_matrix_mul_stop: invalid matrix");
        lua_error(lua);
        return 0;
    }

    matrix_clear_args(matrix);

    matrix->frame_tag = 0;
    matrix->type = MATRIX_CONST;

    matrix_update(m0, 0, 0, 1);
    matrix_update(m1, 0, 0, 1);

    matrix_mul(m, m0->value, m1->value);
    memcpy(matrix->value, m, 16 * sizeof(GLfloat));

    return 0;
}

static int api_matrix_inv(lua_State *lua)
{
    struct matrix_t *matrix, *m0;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_matrix_inv: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    m0 = matrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (matrix == 0 || m0 == 0)
    {
        lua_pushstring(lua, "api_matrix_inv: invalid matrix");
        lua_error(lua);
        return 0;
    }

    matrix_clear_args(matrix);

    matrix->frame_tag = 0;
    matrix->type = MATRIX_INV;
    matrix->argm[0] = m0;

    if (matrix_nesting(matrix, g_matrices.nesting) == 0)
    {
        lua_pushstring(lua, "api_matrix_inv: nesting is too deep");
        lua_error(lua);
        return 0;
    }

    matrix_update(matrix, 0, 0, 1);

    return 0;
}

static int api_matrix_pos_scl_rot(lua_State *lua)
{
    struct matrix_t *matrix;
    struct vector_t *v0, *v1, *v2;
    int rotaxis, rotanglei;

    if (lua_gettop(lua) != 6 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6))
    {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    v2 = vector_get(lua_tointeger(lua, 4));
    rotaxis = lua_tointeger(lua, 5);
    rotanglei = lua_tointeger(lua, 6);
    lua_pop(lua, 6);

    if (matrix == 0 || v0 == 0 || v1 == 0 || v2 == 0)
    {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: invalid objects");
        lua_error(lua);
        return 0;
    }

    if (rotaxis < 0 || rotaxis >= (int)MATRIX_AXES_TOTAL)
    {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: invalid rotation axis");
        lua_error(lua);
        return 0;
    }

    if (rotanglei < 0 || rotanglei >= 4)
    {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: "
                            "rotation angle index out of range");
        lua_error(lua);
        return 0;
    }

    matrix_clear_args(matrix);

    matrix->frame_tag = 0;
    matrix->type = MATRIX_POS_SCL_ROT;
    matrix->argv[0] = v0;
    matrix->argv[1] = v1;
    matrix->argv[2] = v2;
    matrix->rotaxis = (enum matrix_axis_e)rotaxis;
    matrix->rotanglei = rotanglei;

    if (matrix_nesting(matrix, g_matrices.nesting) == 0)
    {
        lua_pushstring(lua, "api_matrix_pos_scl_rot: nesting is too deep");
        lua_error(lua);
        return 0;
    }

    matrix_update(matrix, 0, 0, 1);

    return 0;
}

static int api_matrix_rigid_body(lua_State *lua)
{
    struct matrix_t *matrix;
    int rbi;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_matrix_rigid_body: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    rbi = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_matrix_rigid_body: invalid matrix");
        lua_error(lua);
        return 0;
    }

    matrix_clear_args(matrix);

    matrix->frame_tag = 0;
    matrix->type = MATRIX_RIGID_BODY;
    matrix->rigid_body = rbi;

    if (physics_rb_fetch_tm(rbi, matrix->value) != 0)
    {
        lua_pushstring(lua, "api_matrix_rigid_body: invalid rigid body");
        lua_error(lua);
        return 0;
    }

    return 0;
}

int matrix_init(lua_State *lua, int count, int nesting)
{
    int i;
    g_matrices.pool = calloc(count, sizeof(struct matrix_t));
    if (g_matrices.pool == 0)
        return 1;
    g_matrices.count = count;
    g_matrices.left = count;
    g_matrices.nesting = nesting;
    g_matrices.vacant = g_matrices.pool;
    for (i = 0; i < count; ++i)
    {
        if (i < count - 1)
            g_matrices.pool[i].next = g_matrices.pool + i + 1;
        g_matrices.pool[i].vacant = 1;
    }
    lua_register(lua, "api_matrix_alloc", api_matrix_alloc);
    lua_register(lua, "api_matrix_free", api_matrix_free);
    lua_register(lua, "api_matrix_left", api_matrix_left);
    lua_register(lua, "api_matrix_const", api_matrix_const);
    lua_register(lua, "api_matrix_stop", api_matrix_stop);
    lua_register(lua, "api_matrix_inv", api_matrix_inv);
    lua_register(lua, "api_matrix_mul", api_matrix_mul);
    lua_register(lua, "api_matrix_mul_stop", api_matrix_mul_stop);
    lua_register(lua, "api_matrix_pos_scl_rot", api_matrix_pos_scl_rot);
    lua_register(lua, "api_matrix_rigid_body", api_matrix_rigid_body);
    return 0;
}

void matrix_done(void)
{
    if (g_matrices.pool)
    {
        free(g_matrices.pool);
        g_matrices.pool = 0;
    }
}

struct matrix_t * matrix_get(int i)
{
    if (i >= 0 && i < g_matrices.count)
        return g_matrices.pool + i;
    else
        return 0;
}

int matrix_nesting(struct matrix_t *matrix, int limit)
{
    int i, min, cur;
    if (limit > 0)
    {
        min = limit;
        for (i = 0; i < MATRIX_ARGVS; ++i)
        {
            if (matrix->argv[i] == 0)
                continue;
            cur = vector_nesting(matrix->argv[i], limit - 1);
            if (cur < min)
                min = cur;
        }
        for (i = 0; i < MATRIX_ARGMS; ++i)
        {
            if (matrix->argm[i] == 0)
                continue;
            cur = matrix_nesting(matrix->argm[i], limit - 1);
            if (cur < min)
                min = cur;
        }
        return min;
    }
    else
        return limit;
}

void matrix_update(struct matrix_t *matrix, float dt,
                   int frame_tag, int force)
{
    GLfloat *v0, *v1, *v2;
    GLfloat *m0, *m1;
    if (matrix->type == MATRIX_CONST)
        return;
    if (force == 0 && matrix->frame_tag == frame_tag)
        return;
    matrix->frame_tag = frame_tag;
    if (matrix->type == MATRIX_MUL)
    {
        matrix_update(matrix->argm[0], dt, frame_tag, force);
        matrix_update(matrix->argm[1], dt, frame_tag, force);
        m0 = matrix->argm[0]->value;
        m1 = matrix->argm[1]->value;
        matrix_mul(matrix->value, m0, m1);
    }
    else if (matrix->type == MATRIX_INV)
    {
        matrix_update(matrix->argm[0], dt, frame_tag, force);
        m0 = matrix->argm[0]->value;
        matrix_inv(matrix->value, m0);
    }
    else if (matrix->type == MATRIX_POS_SCL_ROT)
    {
        vector_update(matrix->argv[0], dt, frame_tag, force);
        vector_update(matrix->argv[1], dt, frame_tag, force);
        vector_update(matrix->argv[2], dt, frame_tag, force);
        v0 = matrix->argv[0]->value;
        v1 = matrix->argv[1]->value;
        v2 = matrix->argv[2]->value;
        matrix_pos_scl_rot(matrix->value, v0, v1,
                           matrix->rotaxis, v2[matrix->rotanglei]);
    }
    else if (matrix->type == MATRIX_RIGID_BODY)
        physics_rb_fetch_tm(matrix->rigid_body, matrix->value);
}

void matrix_mul(GLfloat *out, GLfloat *m1, GLfloat *m2)
{
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

void matrix_pos_scl_rot(GLfloat *out, GLfloat *pos, GLfloat *scl,
                        enum matrix_axis_e rotaxis, GLfloat rotangle)
{
    GLfloat axisx[3], axisy[3], axisz[3];
    GLfloat rcos, rsin;

    rcos = cos(rotangle);
    rsin = sin(rotangle);
    if (rotaxis == MATRIX_AXIS_X)
    {
        axisx[0] = 1; axisx[1] =     0; axisx[2] =    0; 
        axisy[0] = 0; axisy[1] =  rcos; axisy[2] = rsin; 
        axisz[0] = 0; axisz[1] = -rsin; axisz[2] = rcos; 
    }
    else if (rotaxis == MATRIX_AXIS_Y)
    {
        axisx[0] = rcos; axisx[1] = 0; axisx[2] = -rsin; 
        axisy[0] =    0; axisy[1] = 1; axisy[2] =     0; 
        axisz[0] = rsin; axisz[1] = 0; axisz[2] =  rcos; 
    }
    else if (rotaxis == MATRIX_AXIS_Z)
    {
        axisx[0] =  rcos; axisx[1] = rsin; axisx[2] = 0;
        axisy[0] = -rsin; axisy[1] = rcos; axisy[2] = 0;
        axisz[0] =     0; axisz[1] =    0; axisz[2] = 1;
    }

    axisx[0] *= scl[0]; axisx[1] *= scl[0]; axisx[2] *= scl[0];
    axisy[0] *= scl[1]; axisy[1] *= scl[1]; axisy[2] *= scl[1];
    axisz[0] *= scl[2]; axisz[1] *= scl[2]; axisz[2] *= scl[2];

    out[ 0] = axisx[0]; out[ 1] = axisx[1]; out[ 2] = axisx[2]; out[ 3] = 0;
    out[ 4] = axisy[0]; out[ 5] = axisy[1]; out[ 6] = axisy[2]; out[ 7] = 0;
    out[ 8] = axisz[0]; out[ 9] = axisz[1]; out[10] = axisz[2]; out[11] = 0;
    out[12] =   pos[0]; out[13] =   pos[1]; out[14] =   pos[2]; out[15] = 1;
}

void matrix_inv(GLfloat *out, GLfloat *m)
{
    double inv[16], det;
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

    inv[8] = m[4]  * m[9] * m[15] - 
             m[4]  * m[11] * m[13] - 
             m[8]  * m[5] * m[15] + 
             m[8]  * m[7] * m[13] + 
             m[12] * m[5] * m[11] - 
             m[12] * m[7] * m[9];

    inv[12] = -m[4]  * m[9] * m[14] + 
               m[4]  * m[10] * m[13] +
               m[8]  * m[5] * m[14] - 
               m[8]  * m[6] * m[13] - 
               m[12] * m[5] * m[10] + 
               m[12] * m[6] * m[9];

    inv[1] = -m[1]  * m[10] * m[15] + 
              m[1]  * m[11] * m[14] + 
              m[9]  * m[2] * m[15] - 
              m[9]  * m[3] * m[14] - 
              m[13] * m[2] * m[11] + 
              m[13] * m[3] * m[10];

    inv[5] = m[0]  * m[10] * m[15] - 
             m[0]  * m[11] * m[14] - 
             m[8]  * m[2] * m[15] + 
             m[8]  * m[3] * m[14] + 
             m[12] * m[2] * m[11] - 
             m[12] * m[3] * m[10];

    inv[9] = -m[0]  * m[9] * m[15] + 
              m[0]  * m[11] * m[13] + 
              m[8]  * m[1] * m[15] - 
              m[8]  * m[3] * m[13] - 
              m[12] * m[1] * m[11] + 
              m[12] * m[3] * m[9];

    inv[13] = m[0]  * m[9] * m[14] - 
              m[0]  * m[10] * m[13] - 
              m[8]  * m[1] * m[14] + 
              m[8]  * m[2] * m[13] + 
              m[12] * m[1] * m[10] - 
              m[12] * m[2] * m[9];

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

    if (det == 0)
        return;

    det = 1.0f / det;

    for (i = 0; i < 16; i++)
        out[i] = inv[i] * det;
}
