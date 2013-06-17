#include "cvector.h"
#include "cmatrix.h"
#include "cbuf.h"
#include "cphysics.h"
#include "cinterp.h"
#include "cutil.h"
#include "pmem.h"
#include <math.h>

#define CVECTOR_SIZE 256

enum cvectors_e {
    CVECTOR_FORCED_UPDATE = -1 /* special update_tag */
};

struct cvectors_t {
    int count, nesting;
    char *pool;
};

_Static_assert(sizeof(struct cvector_t) <= CVECTOR_SIZE,
               "Invalid cvector_t size");

static struct cvectors_t g_cvectors;

static void cvector_clear_args(struct cvector_t *vector) {
    for (int i = 0; i < CVECTOR_ARGVS; ++i)
        vector->argv[i] = 0;
    for (int i = 0; i < CVECTOR_ARGMS; ++i)
        vector->argm[i] = 0;
}

static int api_vector_get(lua_State *lua) {
    struct cvector_t *vector;

    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (!vector) {
        lua_pushstring(lua, "invalid vector");
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
    struct cvector_t *vector;
    int update_tag, force;
    float dt;

    if (lua_gettop(lua) != 3 || !cutil_isint(lua, 1) ||
    !cutil_isfloat(lua, 2) || !cutil_isint(lua, 3)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    dt = (float)lua_tonumber(lua, 2);
    update_tag = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (!vector) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    force = update_tag == CVECTOR_FORCED_UPDATE;
    if (cvector_update(vector, dt, update_tag, force)) {
        lua_pushstring(lua, "update error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_const(lua_State *lua) {
    struct cvector_t *vector;
    float value[4];

    if (lua_gettop(lua) != 5 || !cutil_isint(lua, 1) ||
    !cutil_isfloat(lua, 2) || !cutil_isfloat(lua, 3) ||
    !cutil_isfloat(lua, 4) || !cutil_isfloat(lua, 5)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    value[0] = (float)lua_tonumber(lua, 2);
    value[1] = (float)lua_tonumber(lua, 3);
    value[2] = (float)lua_tonumber(lua, 4);
    value[3] = (float)lua_tonumber(lua, 5);
    lua_pop(lua, 5);

    if (!vector) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    cvector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = CVECTOR_CONST;
    vector->value[0] = value[0];
    vector->value[1] = value[1];
    vector->value[2] = value[2];
    vector->value[3] = value[3];

    return 0;
}

static int api_vector_rubber(lua_State *lua) {
    struct cvector_t *vector, *v0, *v1;

    if (lua_gettop(lua) != 3 || !cutil_isint(lua, 1) ||
    !cutil_isint(lua, 2) || !cutil_isint(lua, 3)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    v0 = cvector_get(lua_tointeger(lua, 2));
    v1 = cvector_get(lua_tointeger(lua, 3));
    lua_pop(lua, 3);

    if (!vector || !v0 || !v1) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    cvector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = CVECTOR_RUBBER;
    vector->argv[0] = v0;
    vector->argv[1] = v1;

    if (!cvector_nesting(vector, g_cvectors.nesting)) {
        lua_pushstring(lua, "nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_cord(lua_State *lua) {
    struct cvector_t *vector, *v0;
    float min, max;

    if (lua_gettop(lua) != 4 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isfloat(lua, 3) || !cutil_isfloat(lua, 4)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    v0 = cvector_get(lua_tointeger(lua, 2));
    min = (float)lua_tonumber(lua, 3);
    max = (float)lua_tonumber(lua, 4);
    lua_pop(lua, 4);

    if (!vector || !v0) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    if (min < 0.0f || max < 0.0f) {
        lua_pushstring(lua, "limits are out of range");
        lua_error(lua);
        return 0;
    }
    if (min > max) {
        lua_pushstring(lua, "min > max");
        lua_error(lua);
        return 0;
    }
    cvector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = CVECTOR_CORD;
    vector->cord_min = min;
    vector->cord_max = max;
    vector->argv[0] = v0;

    if (!cvector_nesting(vector, g_cvectors.nesting)) {
        lua_pushstring(lua, "nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_mpos(lua_State *lua) {
    struct cvector_t *vector;
    struct cmatrix_t *m0;

    if (lua_gettop(lua) != 2 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    m0 = cmatrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    if (!vector) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    if (!m0) {
        lua_pushstring(lua, "invalid matrix");
        lua_error(lua);
        return 0;
    }
    cvector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = CVECTOR_MPOS;
    vector->argm[0] = m0;

    if (!cvector_nesting(vector, g_cvectors.nesting)) {
        lua_pushstring(lua, "nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_wsum(lua_State *lua) {
    struct cvector_t *vector, *v0, *v1, *v2, *v3, *v4;

    if (lua_gettop(lua) != 6 ||
    !cutil_isint(lua, 1) || !cutil_isint(lua, 2) || !cutil_isint(lua, 3) ||
    !cutil_isint(lua, 4) || !cutil_isint(lua, 5) || !cutil_isint(lua, 6)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    v0 = cvector_get(lua_tointeger(lua, 2));
    v1 = cvector_get(lua_tointeger(lua, 3));
    v2 = cvector_get(lua_tointeger(lua, 4));
    v3 = cvector_get(lua_tointeger(lua, 5));
    v4 = cvector_get(lua_tointeger(lua, 6));
    lua_pop(lua, 6);

    if (!vector || !v0 || !v1 || !v2 || !v3 || !v4) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    cvector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = CVECTOR_WSUM;
    vector->argv[0] = v0;
    vector->argv[1] = v1;
    vector->argv[2] = v2;
    vector->argv[3] = v3;
    vector->argv[4] = v4;

    if (!cvector_nesting(vector, g_cvectors.nesting)) {
        lua_pushstring(lua, "nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_pick(lua_State *lua) {
    struct cvector_t *vector, *v0, *v1, *v2, *v3;

    if (lua_gettop(lua) != 5 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isint(lua, 3) || !cutil_isint(lua, 4) || !cutil_isint(lua, 5)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    v0 = cvector_get(lua_tointeger(lua, 2));
    v1 = cvector_get(lua_tointeger(lua, 3));
    v2 = cvector_get(lua_tointeger(lua, 4));
    v3 = cvector_get(lua_tointeger(lua, 5));
    lua_pop(lua, 5);

    if (!vector || !v0 || !v1 || !v2 || !v3) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    cvector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = CVECTOR_PICK;
    vector->argv[0] = v0;
    vector->argv[1] = v1;
    vector->argv[2] = v2;
    vector->argv[3] = v3;

    if (!cvector_nesting(vector, g_cvectors.nesting)) {
        lua_pushstring(lua, "nesting is too deep");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_vector_seq(lua_State *lua) {
    struct cvector_t *vector;
    int start, len, loop, ipl;

    if (lua_gettop(lua) != 5 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isint(lua, 3) || !cutil_isint(lua, 4) || !cutil_isint(lua, 5)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    start = lua_tointeger(lua, 2);
    len = lua_tointeger(lua, 3);
    loop = !!lua_tointeger(lua, 4);
    ipl = lua_tointeger(lua, 5);
    lua_pop(lua, 5);

    if (!vector) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    if (start < 0 || start >= g_cbufs.size - 5) {
        lua_pushstring(lua, "start index out of range");
        lua_error(lua);
        return 0;
    }
    if (len < 2 || len > (g_cbufs.size - start) / 5) {
        lua_pushstring(lua, "len out of range");
        lua_error(lua);
        return 0;
    }
    if (ipl < 0 || ipl >= CVECTOR_IPLS_TOTAL) {
        lua_pushstring(lua, "interpolation type out of range");
        lua_error(lua);
        return 0;
    }
    cvector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = CVECTOR_SEQ;
    vector->seq_t = 0;
    vector->seq_start = start;
    vector->seq_cur = start;
    vector->seq_len = len;
    vector->seq_loop = loop;
    vector->seq_ipl = ipl;

    return 0;
}

static int api_vector_cast(lua_State *lua) {
    struct cvector_t *vector;
    struct cmatrix_t *m0, *m1;
    int wldi, csi;

    if (lua_gettop(lua) != 5 || !cutil_isint(lua, 1) || !cutil_isint(lua, 2) ||
    !cutil_isint(lua, 3) || !cutil_isint(lua, 4) || !cutil_isint(lua, 5)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vector = cvector_get(lua_tointeger(lua, 1));
    wldi = lua_tointeger(lua, 2);
    csi = lua_tointeger(lua, 3);
    m0 = cmatrix_get(lua_tointeger(lua, 4));
    m1 = cmatrix_get(lua_tointeger(lua, 5));
    lua_pop(lua, 5);

    if (!vector || !m0 || !m1) {
        lua_pushstring(lua, "invalid object");
        lua_error(lua);
        return 0;
    }
    cvector_clear_args(vector);

    vector->update_tag = 0;
    vector->type = CVECTOR_CAST;
    vector->argm[0] = m0;
    vector->argm[1] = m1;
    vector->cast_wldi = wldi;
    vector->cast_csi = csi;

    if (!cvector_nesting(vector, g_cvectors.nesting)) {
        lua_pushstring(lua, "nesting is too deep");
        lua_error(lua);
        return 0;
    }
    if (cphysics_wld_cast(wldi, csi, m0->value, m1->value, vector->value)) {
        lua_pushstring(lua, "invalid physics object");
        lua_error(lua);
        return 0;
    }
    return 0;
}

int cvector_init(lua_State *lua, int count, int nesting) {
    struct cvector_t *vec;
    g_cvectors.count = count;
    g_cvectors.pool = pmem_alloc(PMEM_ALIGNOF(struct cvector_t),
                                CVECTOR_SIZE * count);
    if (!g_cvectors.pool)
        return 1;
    for (int i = 0; i < count; ++i) {
        vec = cvector_get(i);
        for (int j = 0; j < 4; ++j)
            vec->value[j] = 0;
        vec->type = CVECTOR_CONST;
    }
    g_cvectors.nesting = nesting;
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
    #define REGN(x) lua_pushinteger(lua, C##x); lua_setglobal(lua, "API_"#x)
    REGN(VECTOR_IPL_LINEAR);
    REGN(VECTOR_IPL_SPLINE);
    REGN(VECTOR_FORCED_UPDATE);
    #undef REGN
    return 0;
}

void cvector_done(void) {
    if (!g_cvectors.pool)
        return;
    pmem_free(g_cvectors.pool);
    g_cvectors.pool = 0;
}

struct cvector_t * cvector_get(int i) {
    if (i >= 0 && i < g_cvectors.count)
        return (struct cvector_t*)(g_cvectors.pool + CVECTOR_SIZE * i);
    else
        return 0;
}

int cvector_nesting(struct cvector_t *vector, int limit) {
    int min, cur;
    if (limit > 0) {
        min = limit;
        for (int i = 0; i < CVECTOR_ARGVS; ++i) {
            if (!vector->argv[i])
                continue;
            cur = cvector_nesting(vector->argv[i], limit - 1);
            if (cur < min)
                min = cur;
        }
        for (int i = 0; i < CVECTOR_ARGMS; ++i) {
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

static float cvector_seq_dt(int i) {
    return g_cbufs.data[i + 4];
}

static float * cvector_seq_value(int i) {
    return g_cbufs.data + i;
}

static int cvector_seq_next(struct cvector_t *v, int i) {
    if (i + 5 < v->seq_start + v->seq_len * 5)
        return i + 5;
    else if (v->seq_loop)
        return v->seq_start;
    else
        return i;
}

static int cvector_seq_prev(struct cvector_t *v, int i) {
    if (i - 5 >= v->seq_start)
        return i - 5;
    else if (v->seq_loop)
        return v->seq_start + (v->seq_len - 1) * 5;
    else
        return i;
}

static int cvector_update_rubber(struct cvector_t *v, float dt, int force) {
    float *v0, *v1;
    for (int i = 0; i < 2; ++i)
        if (cvector_update(v->argv[i], dt, v->update_tag, force))
            return 1;
    v0 = v->argv[0]->value;
    v1 = v->argv[1]->value;
    for (int i = 0; i < 4; ++i)
        v->value[i] += (v0[i] - v->value[i]) * v1[i];
    return 0;
}

static int cvector_update_cord(struct cvector_t *v, float dt, int force) {
    static const float THRESHOLD = 0.1f;
    float dist, scale;
    float diff[4];
    float *v0;

    if (cvector_update(v->argv[0], dt, v->update_tag, force))
        return 1;
    v0 = v->argv[0]->value;

    cvector_wsum(diff, 1, v->value, -1, v0);
    dist = cvector_len(diff);
    if (dist < THRESHOLD)
        return 0;
    if (dist < v->cord_min)
        scale = v->cord_min / dist;
    else if (dist > v->cord_max)
        scale = v->cord_max / dist;
    else
        scale = 1;
    cvector_wsum(v->value, 1, v0, scale, diff);
    return 0;
}

static int cvector_update_mpos(struct cvector_t *v, float dt, int force) {
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

static int cvector_update_wsum(struct cvector_t *v, float dt, int force) {
    float *v0, *v1, *v2, *v3, *v4;
    for (int i = 0; i < 5; ++i)
        if (cvector_update(v->argv[i], dt, v->update_tag, force))
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

static int cvector_update_pick(struct cvector_t *v, float dt, int force) {
    float *v0, *v1, *v2, *v3;
    for (int i = 0; i < 4; ++i)
        if (cvector_update(v->argv[i], dt, v->update_tag, force))
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

static int cvector_update_cast(struct cvector_t *v, float dt, int force) {
    float *m0, *m1;
    for (int i = 0; i < 2; ++i)
        if (cmatrix_update(v->argm[i], dt, v->update_tag, force))
            return 1;
    m0 = v->argm[0]->value;
    m1 = v->argm[1]->value;
    return cphysics_wld_cast(v->cast_wldi, v->cast_csi, m0, m1, v->value);
}

static void cvector_update_seq(struct cvector_t *v, float dt) {
    static const int SEQ_SKIP_MAX = 5;
    int i, i0, i1, i2, i3;
    float *v0, *v1, *v2, *v3;
    float t;

    v->seq_t += dt;
    for (i = 0; i < SEQ_SKIP_MAX; ++i) {
        if (v->seq_t < cvector_seq_dt(v->seq_cur))
            break;
        v->seq_t -= cvector_seq_dt(v->seq_cur);
        v->seq_cur = cvector_seq_next(v, v->seq_cur);
    }
    if (v->seq_ipl == CVECTOR_IPL_LINEAR) {
        v0 = cvector_seq_value(v->seq_cur);
        v1 = cvector_seq_value(cvector_seq_next(v, v->seq_cur));
        t = v->seq_t / cvector_seq_dt(v->seq_cur);
        for (i = 0; i < 4; ++i)
            v->value[i] = cinterp_linear(t, v0[i], v1[i]);
    }
    else if (v->seq_ipl == CVECTOR_IPL_SPLINE) {
        i0 = cvector_seq_prev(v, v->seq_cur);
        i1 = v->seq_cur;
        i2 = cvector_seq_next(v, v->seq_cur);
        i3 = cvector_seq_next(v, i2);

        v0 = cvector_seq_value(i0);
        v1 = cvector_seq_value(i1);
        v2 = cvector_seq_value(i2);
        v3 = cvector_seq_value(i3);

        t = v->seq_t / cvector_seq_dt(v->seq_cur);
        for (i = 0; i < 4; ++i)
            v->value[i] = cinterp_spline(t, v0[i], v1[i], v2[i], v3[i]);
    }
}

int cvector_update(struct cvector_t *v, float dt, int update_tag, int force) {
    if (v->type == CVECTOR_CONST)
        return 0;
    if (!force && v->update_tag == update_tag)
        return 0;
    v->update_tag = update_tag;
    if (v->type == CVECTOR_RUBBER)
        return cvector_update_rubber(v, dt, force);
    else if (v->type == CVECTOR_WSUM)
        return cvector_update_wsum(v, dt, force);
    else if (v->type == CVECTOR_SEQ)
        cvector_update_seq(v, dt);
    else if (v->type == CVECTOR_MPOS)
        return cvector_update_mpos(v, dt, force);
    else if (v->type == CVECTOR_CORD)
        return cvector_update_cord(v, dt, force);
    else if (v->type == CVECTOR_PICK)
        return cvector_update_pick(v, dt, force);
    else if (v->type == CVECTOR_CAST)
        return cvector_update_cast(v, dt, force);
    return 0;
}

void cvector_cross(float *out, float *v1, float *v2) {
    out[0] = v1[1]*v2[2] - v2[1]*v1[2];
    out[1] = v1[2]*v2[0] - v2[2]*v1[0];
    out[2] = v1[0]*v2[1] - v2[0]*v1[1];
}

float cvector_len(float *v) {
    return sqrtf(v[0]*v[0] + v[1]*v[1] + v[2]*v[2] + v[3]*v[3]);
}

void cvector_wsum(float *out, float w1, float *v1, float w2, float *v2) {
    out[0] = w1*v1[0] + w2*v2[0];
    out[1] = w1*v1[1] + w2*v2[1];
    out[2] = w1*v1[2] + w2*v2[2];
    out[3] = w1*v1[3] + w2*v2[3];
}

