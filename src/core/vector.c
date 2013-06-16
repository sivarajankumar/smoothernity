#include "vector.h"
#include "cmatrix.h"
#include "cbuf.h"
#include "cphysics.h"
#include "cinterp.h"
#include "util.h"
#include "pmem.h"
#include <math.h>

#define VECTOR_SIZE 256

enum vectors_e {
    VECTOR_FORCED_UPDATE = -1 /* special update_tag */
};

struct vectors_t {
    int count, nesting;
    char *pool;
};

_Static_assert(sizeof(struct vector_t) <= VECTOR_SIZE, "Invalid vector_t size");

static struct vectors_t g_vectors;

static void vector_clear_args(struct vector_t *vector) {
    for (int i = 0; i < VECTOR_ARGVS; ++i)
        vector->argv[i] = 0;
    for (int i = 0; i < VECTOR_ARGMS; ++i)
        vector->argm[i] = 0;
}

static int api_vector_get(lua_State *lua) {
    struct vector_t *vector;

    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_vector_get: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (!vector) {
        lua_pushstring(lua, "api_vector_get: invalid vector");
        lua_error(lua);
        return 0;
    }
    lua_pushnumber(lua, vector->value[0]);
    lua_pushnumber(lua, vector->value[1]);
    lua_pushnumber(lua, vector->value[2]);
    lua_pushnumber(lua, vector->value[3]);
    return 4;
}

static int api_vector_update(lua_State *lua) {
    struct vector_t *vector;
    int update_tag, force;
    float dt;

    if (lua_gettop(lua) != 3 || !util_isint(lua, 1) ||
    !util_isfloat(lua, 2) || !util_isint(lua, 3)) {
        lua_pushstring(lua, "api_vector_update: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    dt = (float)lua_tonumber(lua, 2);
    update_tag = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (!vector) {
        lua_pushstring(lua, "api_vector_update: invalid vector");
        lua_error(lua);
        return 0;
    }
    force = update_tag == VECTOR_FORCED_UPDATE;
    if (vector_update(vector, dt, update_tag, force)) {
        lua_pushstring(lua, "api_vector_update: update error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_const(lua_State *lua) {
    struct vector_t *vector;
    float value[4];

    if (lua_gettop(lua) != 5 || !util_isint(lua, 1) ||
    !util_isfloat(lua, 2) || !util_isfloat(lua, 3) ||
    !util_isfloat(lua, 4) || !util_isfloat(lua, 5)) {
        lua_pushstring(lua, "api_vector_const: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    value[0] = (float)lua_tonumber(lua, 2);
    value[1] = (float)lua_tonumber(lua, 3);
    value[2] = (float)lua_tonumber(lua, 4);
    value[3] = (float)lua_tonumber(lua, 5);
    lua_pop(lua, 5);

    if (!vector) {
        lua_pushstring(lua, "api_vector_const: invalid vector");
        lua_error(lua);
        return 0;
    }
    vector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = VECTOR_CONST;
    vector->value[0] = value[0];
    vector->value[1] = value[1];
    vector->value[2] = value[2];
    vector->value[3] = value[3];

    return 0;
}

static int api_vector_rubber(lua_State *lua) {
    struct vector_t *vector, *v0, *v1;

    if (lua_gettop(lua) != 3 || !util_isint(lua, 1) ||
    !util_isint(lua, 2) || !util_isint(lua, 3)) {
        lua_pushstring(lua, "api_vector_rubber: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    lua_pop(lua, 3);

    if (!vector || !v0 || !v1) {
        lua_pushstring(lua, "api_vector_rubber: invalid vector");
        lua_error(lua);
        return 0;
    }
    vector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = VECTOR_RUBBER;
    vector->argv[0] = v0;
    vector->argv[1] = v1;

    if (!vector_nesting(vector, g_vectors.nesting)) {
        lua_pushstring(lua, "api_vector_rubber: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_cord(lua_State *lua) {
    struct vector_t *vector, *v0;
    float min, max;

    if (lua_gettop(lua) != 4 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isfloat(lua, 3) || !util_isfloat(lua, 4)) {
        lua_pushstring(lua, "api_vector_cord: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    min = (float)lua_tonumber(lua, 3);
    max = (float)lua_tonumber(lua, 4);
    lua_pop(lua, 4);

    if (!vector || !v0) {
        lua_pushstring(lua, "api_vector_cord: invalid vector");
        lua_error(lua);
        return 0;
    }
    if (min < 0.0f || max < 0.0f) {
        lua_pushstring(lua, "api_vector_cord: limits are out of range");
        lua_error(lua);
        return 0;
    }
    if (min > max) {
        lua_pushstring(lua, "api_vector_cord: min > max");
        lua_error(lua);
        return 0;
    }
    vector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = VECTOR_CORD;
    vector->cord_min = min;
    vector->cord_max = max;
    vector->argv[0] = v0;

    if (!vector_nesting(vector, g_vectors.nesting)) {
        lua_pushstring(lua, "api_vector_cord: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_mpos(lua_State *lua) {
    struct vector_t *vector;
    struct cmatrix_t *m0;

    if (lua_gettop(lua) != 2 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_vector_mpos: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    m0 = cmatrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (!vector) {
        lua_pushstring(lua, "api_vector_mpos: invalid vector");
        lua_error(lua);
        return 0;
    }
    if (!m0) {
        lua_pushstring(lua, "api_vector_mpos: invalid matrix");
        lua_error(lua);
        return 0;
    }
    vector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = VECTOR_MPOS;
    vector->argm[0] = m0;

    if (!vector_nesting(vector, g_vectors.nesting)) {
        lua_pushstring(lua, "api_vector_mpos: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_wsum(lua_State *lua) {
    struct vector_t *vector, *v0, *v1, *v2, *v3, *v4;

    if (lua_gettop(lua) != 6 ||
    !util_isint(lua, 1) || !util_isint(lua, 2) || !util_isint(lua, 3) ||
    !util_isint(lua, 4) || !util_isint(lua, 5) || !util_isint(lua, 6)) {
        lua_pushstring(lua, "api_vector_wsum: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    v2 = vector_get(lua_tointeger(lua, 4));
    v3 = vector_get(lua_tointeger(lua, 5));
    v4 = vector_get(lua_tointeger(lua, 6));
    lua_pop(lua, 6);

    if (!vector || !v0 || !v1 || !v2 || !v3 || !v4) {
        lua_pushstring(lua, "api_vector_wsum: invalid vector");
        lua_error(lua);
        return 0;
    }
    vector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = VECTOR_WSUM;
    vector->argv[0] = v0;
    vector->argv[1] = v1;
    vector->argv[2] = v2;
    vector->argv[3] = v3;
    vector->argv[4] = v4;

    if (!vector_nesting(vector, g_vectors.nesting)) {
        lua_pushstring(lua, "api_vector_wsum: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_pick(lua_State *lua) {
    struct vector_t *vector, *v0, *v1, *v2, *v3;

    if (lua_gettop(lua) != 5 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isint(lua, 5)) {
        lua_pushstring(lua, "api_vector_pick: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    v2 = vector_get(lua_tointeger(lua, 4));
    v3 = vector_get(lua_tointeger(lua, 5));
    lua_pop(lua, 5);

    if (!vector || !v0 || !v1 || !v2 || !v3) {
        lua_pushstring(lua, "api_vector_pick: invalid vector");
        lua_error(lua);
        return 0;
    }
    vector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = VECTOR_PICK;
    vector->argv[0] = v0;
    vector->argv[1] = v1;
    vector->argv[2] = v2;
    vector->argv[3] = v3;

    if (!vector_nesting(vector, g_vectors.nesting)) {
        lua_pushstring(lua, "api_vector_pick: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_seq(lua_State *lua) {
    struct vector_t *vector;
    int start, len, loop, ipl;

    if (lua_gettop(lua) != 5 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isint(lua, 5)) {
        lua_pushstring(lua, "api_vector_seq: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    start = lua_tointeger(lua, 2);
    len = lua_tointeger(lua, 3);
    loop = !!lua_tointeger(lua, 4);
    ipl = lua_tointeger(lua, 5);
    lua_pop(lua, 5);

    if (!vector) {
        lua_pushstring(lua, "api_vector_seq: invalid vector");
        lua_error(lua);
        return 0;
    }
    if (start < 0 || start >= g_cbufs.size - 5) {
        lua_pushstring(lua, "api_vector_seq: start index out of range");
        lua_error(lua);
        return 0;
    }
    if (len < 2 || len > (g_cbufs.size - start) / 5) {
        lua_pushstring(lua, "api_vector_seq: len out of range");
        lua_error(lua);
        return 0;
    }
    if (ipl < 0 || ipl >= VECTOR_IPLS_TOTAL) {
        lua_pushstring(lua, "api_vector_seq: interpolation type out of range");
        lua_error(lua);
        return 0;
    }
    vector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = VECTOR_SEQ;
    vector->seq_t = 0;
    vector->seq_start = start;
    vector->seq_cur = start;
    vector->seq_len = len;
    vector->seq_loop = loop;
    vector->seq_ipl = (enum vector_ipl_e)ipl;

    return 0;
}

static int api_vector_cast(lua_State *lua) {
    struct vector_t *vector;
    struct cmatrix_t *m0, *m1;
    int wldi, csi;

    if (lua_gettop(lua) != 5 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isint(lua, 5)) {
        lua_pushstring(lua, "api_vector_cast: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = vector_get(lua_tointeger(lua, 1));
    wldi = lua_tointeger(lua, 2);
    csi = lua_tointeger(lua, 3);
    m0 = cmatrix_get(lua_tointeger(lua, 4));
    m1 = cmatrix_get(lua_tointeger(lua, 5));
    lua_pop(lua, 5);

    if (!vector || !m0 || !m1) {
        lua_pushstring(lua, "api_vector_cast: invalid object");
        lua_error(lua);
        return 0;
    }
    vector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = VECTOR_CAST;
    vector->argm[0] = m0;
    vector->argm[1] = m1;
    vector->cast_wldi = wldi;
    vector->cast_csi = csi;

    if (!vector_nesting(vector, g_vectors.nesting)) {
        lua_pushstring(lua, "api_vector_cast: nesting is too deep");
        lua_error(lua);
        return 0;
    }
    if (cphysics_wld_cast(wldi, csi, m0->value, m1->value, vector->value)) {
        lua_pushstring(lua, "api_vector_cast: invalid physics object");
        lua_error(lua);
        return 0;
    }
    return 0;
}

int vector_init(lua_State *lua, int count, int nesting) {
    struct vector_t *vec;
    g_vectors.count = count;
    g_vectors.pool = pmem_alloc(PMEM_ALIGNOF(struct vector_t),
                                VECTOR_SIZE * count);
    if (!g_vectors.pool)
        return 1;
    for (int i = 0; i < count; ++i) {
        vec = vector_get(i);
        for (int j = 0; j < 4; ++j)
            vec->value[j] = 0;
        vec->type = VECTOR_CONST;
    }
    g_vectors.nesting = nesting;
    #define REGF(x) lua_register(lua, #x, x)
    REGF(api_vector_get);
    REGF(api_vector_update);
    REGF(api_vector_const);
    REGF(api_vector_rubber);
    REGF(api_vector_wsum);
    REGF(api_vector_pick);
    REGF(api_vector_seq);
    REGF(api_vector_mpos);
    REGF(api_vector_cord);
    REGF(api_vector_cast);
    #undef REGF
    #define REGN(x) lua_pushinteger(lua, x); lua_setglobal(lua, "API_"#x)
    REGN(VECTOR_IPL_LINEAR);
    REGN(VECTOR_IPL_SPLINE);
    REGN(VECTOR_FORCED_UPDATE);
    #undef REGN
    return 0;
}

void vector_done(void) {
    if (!g_vectors.pool)
        return;
    pmem_free(g_vectors.pool);
    g_vectors.pool = 0;
}

struct vector_t * vector_get(int i) {
    if (i >= 0 && i < g_vectors.count)
        return (struct vector_t*)(g_vectors.pool + VECTOR_SIZE * i);
    else
        return 0;
}

int vector_nesting(struct vector_t *vector, int limit) {
    int min, cur;
    if (limit > 0) {
        min = limit;
        for (int i = 0; i < VECTOR_ARGVS; ++i) {
            if (!vector->argv[i])
                continue;
            cur = vector_nesting(vector->argv[i], limit - 1);
            if (cur < min)
                min = cur;
        }
        for (int i = 0; i < VECTOR_ARGMS; ++i) {
            if (!vector->argm[i])
                continue;
            cur = cmatrix_nesting(vector->argm[i], limit - 1);
            if (cur < min)
                min = cur;
        }
        return min;
    }
    else
        return limit;
}

static float vector_seq_dt(int i) {
    return g_cbufs.data[i + 4];
}

static float * vector_seq_value(int i) {
    return g_cbufs.data + i;
}

static int vector_seq_next(struct vector_t *v, int i) {
    if (i + 5 < v->seq_start + v->seq_len * 5)
        return i + 5;
    else if (v->seq_loop)
        return v->seq_start;
    else
        return i;
}

static int vector_seq_prev(struct vector_t *v, int i) {
    if (i - 5 >= v->seq_start)
        return i - 5;
    else if (v->seq_loop)
        return v->seq_start + (v->seq_len - 1) * 5;
    else
        return i;
}

static int vector_update_rubber(struct vector_t *v, float dt, int force) {
    float *v0, *v1;
    for (int i = 0; i < 2; ++i)
        if (vector_update(v->argv[i], dt, v->update_tag, force))
            return 1;
    v0 = v->argv[0]->value;
    v1 = v->argv[1]->value;
    for (int i = 0; i < 4; ++i)
        v->value[i] += (v0[i] - v->value[i]) * v1[i];
    return 0;
}

static int vector_update_cord(struct vector_t *v, float dt, int force) {
    static const float THRESHOLD = 0.1f;
    float dist, scale;
    float diff[4];
    float *v0;

    if (vector_update(v->argv[0], dt, v->update_tag, force))
        return 1;
    v0 = v->argv[0]->value;

    vector_wsum(diff, 1, v->value, -1, v0);
    dist = vector_len(diff);
    if (dist < THRESHOLD)
        return 0;
    if (dist < v->cord_min)
        scale = v->cord_min / dist;
    else if (dist > v->cord_max)
        scale = v->cord_max / dist;
    else
        scale = 1;
    vector_wsum(v->value, 1, v0, scale, diff);
    return 0;
}

static int vector_update_mpos(struct vector_t *v, float dt, int force) {
    float *m0;
    if (cmatrix_update(v->argm[0], dt, v->update_tag, force))
        return 1;
    m0 = v->argm[0]->value;
    v->value[0] = m0[12];
    v->value[1] = m0[13];
    v->value[2] = m0[14];
    v->value[3] = 0;
    return 0;
}

static int vector_update_wsum(struct vector_t *v, float dt, int force) {
    float *v0, *v1, *v2, *v3, *v4;
    for (int i = 0; i < 5; ++i)
        if (vector_update(v->argv[i], dt, v->update_tag, force))
            return 1;
    v0 = v->argv[0]->value;
    v1 = v->argv[1]->value;
    v2 = v->argv[2]->value;
    v3 = v->argv[3]->value;
    v4 = v->argv[4]->value;
    for (int i = 0; i < 4; ++i)
        v->value[i] = (v0[0] * v1[i]) + (v0[1] * v2[i]) +
                      (v0[2] * v3[i]) + (v0[3] * v4[i]);
    return 0;
}

static int vector_update_pick(struct vector_t *v, float dt, int force) {
    float *v0, *v1, *v2, *v3;
    for (int i = 0; i < 4; ++i)
        if (vector_update(v->argv[i], dt, v->update_tag, force))
            return 1;
    v0 = v->argv[0]->value;
    v1 = v->argv[1]->value;
    v2 = v->argv[2]->value;
    v3 = v->argv[3]->value;
    v->value[0] = v0[0];
    v->value[1] = v1[1];
    v->value[2] = v2[2];
    v->value[3] = v3[3];
    return 0;
}

static int vector_update_cast(struct vector_t *v, float dt, int force) {
    float *m0, *m1;
    for (int i = 0; i < 2; ++i)
        if (cmatrix_update(v->argm[i], dt, v->update_tag, force))
            return 1;
    m0 = v->argm[0]->value;
    m1 = v->argm[1]->value;
    return cphysics_wld_cast(v->cast_wldi, v->cast_csi, m0, m1, v->value);
}

static void vector_update_seq(struct vector_t *v, float dt) {
    static const int SEQ_SKIP_MAX = 5;
    int i, i0, i1, i2, i3;
    float *v0, *v1, *v2, *v3;
    float t;

    v->seq_t += dt;
    for (i = 0; i < SEQ_SKIP_MAX; ++i) {
        if (v->seq_t < vector_seq_dt(v->seq_cur))
            break;
        v->seq_t -= vector_seq_dt(v->seq_cur);
        v->seq_cur = vector_seq_next(v, v->seq_cur);
    }
    if (v->seq_ipl == VECTOR_IPL_LINEAR) {
        v0 = vector_seq_value(v->seq_cur);
        v1 = vector_seq_value(vector_seq_next(v, v->seq_cur));
        t = v->seq_t / vector_seq_dt(v->seq_cur);
        for (i = 0; i < 4; ++i)
            v->value[i] = cinterp_linear(t, v0[i], v1[i]);
    }
    else if (v->seq_ipl == VECTOR_IPL_SPLINE) {
        i0 = vector_seq_prev(v, v->seq_cur);
        i1 = v->seq_cur;
        i2 = vector_seq_next(v, v->seq_cur);
        i3 = vector_seq_next(v, i2);

        v0 = vector_seq_value(i0);
        v1 = vector_seq_value(i1);
        v2 = vector_seq_value(i2);
        v3 = vector_seq_value(i3);

        t = v->seq_t / vector_seq_dt(v->seq_cur);
        for (i = 0; i < 4; ++i)
            v->value[i] = cinterp_spline(t, v0[i], v1[i], v2[i], v3[i]);
    }
}

int vector_update(struct vector_t *v, float dt, int update_tag, int force) {
    if (v->type == VECTOR_CONST)
        return 0;
    if (!force && v->update_tag == update_tag)
        return 0;
    v->update_tag = update_tag;
    if (v->type == VECTOR_RUBBER)
        return vector_update_rubber(v, dt, force);
    else if (v->type == VECTOR_WSUM)
        return vector_update_wsum(v, dt, force);
    else if (v->type == VECTOR_SEQ)
        vector_update_seq(v, dt);
    else if (v->type == VECTOR_MPOS)
        return vector_update_mpos(v, dt, force);
    else if (v->type == VECTOR_CORD)
        return vector_update_cord(v, dt, force);
    else if (v->type == VECTOR_PICK)
        return vector_update_pick(v, dt, force);
    else if (v->type == VECTOR_CAST)
        return vector_update_cast(v, dt, force);
    return 0;
}

void vector_cross(float *out, float *v1, float *v2) {
    out[0] = v1[1]*v2[2] - v2[1]*v1[2];
    out[1] = v1[2]*v2[0] - v2[2]*v1[0];
    out[2] = v1[0]*v2[1] - v2[0]*v1[1];
}

float vector_len(float *v) {
    return sqrtf(v[0]*v[0] + v[1]*v[1] + v[2]*v[2] + v[3]*v[3]);
}

void vector_wsum(float *out, float w1, float *v1, float w2, float *v2) {
    out[0] = w1*v1[0] + w2*v2[0];
    out[1] = w1*v1[1] + w2*v2[1];
    out[2] = w1*v1[2] + w2*v2[2];
    out[3] = w1*v1[3] + w2*v2[3];
}

