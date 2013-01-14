#include "vector.h"
#include "consts.h"
#include <stdlib.h>
#include <math.h>
#include <string.h>

struct vectors_t
{
    int count;
    int left;
    int nesting;
    struct vector_t *pool;
    struct vector_t *vacant;
};

static struct vectors_t g_vectors;

static void vector_clear_args(struct vector_t *vector)
{
    int i;
    for (i = 0; i < VECTOR_ARGVS; ++i)
        vector->argv[i] = 0;
}

static int api_vector_alloc(lua_State *lua)
{
    struct vector_t *vector;

    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_vector_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    if (g_vectors.vacant == 0)
    {
        lua_pushstring(lua, "api_vector_alloc: out of vectors");
        lua_error(lua);
        return 0;
    }

    --g_vectors.left;
    vector = g_vectors.vacant;
    g_vectors.vacant = g_vectors.vacant->next;

    memset(vector, 0, sizeof(struct vector_t));

    lua_pushinteger(lua, vector - g_vectors.pool);
    return 1;
}

static int api_vector_free(lua_State *lua)
{
    struct vector_t *vector;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_vector_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vector = vector_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (vector == 0 || vector->vacant)
    {
        lua_pushstring(lua, "api_vector_free: invalid vector");
        lua_error(lua);
        return 0;
    }

    vector->vacant = 1;
    ++g_vectors.left;

    vector->next = g_vectors.vacant;
    g_vectors.vacant = vector;
    return 0;
}

static int api_vector_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_vector_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_vectors.left);
    return 1;
}

static int api_vector_const(lua_State *lua)
{
    struct vector_t *vector;
    float value[4];

    if (lua_gettop(lua) != 5 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5))
    {
        lua_pushstring(lua, "api_vector_const: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vector = vector_get(lua_tointeger(lua, 1));
    value[0] = lua_tonumber(lua, 2);
    value[1] = lua_tonumber(lua, 3);
    value[2] = lua_tonumber(lua, 4);
    value[3] = lua_tonumber(lua, 5);
    lua_pop(lua, 5);

    if (vector == 0)
    {
        lua_pushstring(lua, "api_vector_const: invalid vector");
        lua_error(lua);
        return 0;
    }

    vector_clear_args(vector);

    vector->frame_tag = 0;
    vector->type = VECTOR_CONST;
    vector->value[0] = value[0];
    vector->value[1] = value[1];
    vector->value[2] = value[2];
    vector->value[3] = value[3];

    return 0;
}

static int api_vector_sine(lua_State *lua)
{
    struct vector_t *vector, *v0, *v1;
    float period;

    if (lua_gettop(lua) != 4 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4))
    {
        lua_pushstring(lua, "api_vector_sine: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vector = vector_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    period = lua_tonumber(lua, 4);
    lua_pop(lua, 4);

    if (vector == 0 || v0 == 0 || v1 == 0)
    {
        lua_pushstring(lua, "api_vector_sine: invalid vector");
        lua_error(lua);
        return 0;
    }

    if (period <= 0.0f)
    {
        lua_pushstring(lua, "api_vector_sine: invalid period");
        lua_error(lua);
        return 0;
    }

    vector_clear_args(vector);

    vector->frame_tag = 0;
    vector->type = VECTOR_SINE;
    vector->period = period;
    vector->argv[0] = v0;
    vector->argv[1] = v1;

    if (vector_nesting(vector, g_vectors.nesting) == 0)
    {
        lua_pushstring(lua, "api_vector_sine: nesting is too deep");
        lua_error(lua);
        return 0;
    }

    return 0;
}

static int api_vector_saw(lua_State *lua)
{
    struct vector_t *vector, *v0, *v1;
    float period;

    if (lua_gettop(lua) != 4 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4))
    {
        lua_pushstring(lua, "api_vector_saw: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vector = vector_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    v1 = vector_get(lua_tointeger(lua, 3));
    period = lua_tonumber(lua, 4);
    lua_pop(lua, 4);

    if (vector == 0 || v0 == 0 || v1 == 0)
    {
        lua_pushstring(lua, "api_vector_saw: invalid vector");
        lua_error(lua);
        return 0;
    }

    if (period <= 0.0f)
    {
        lua_pushstring(lua, "api_vector_saw: invalid period");
        lua_error(lua);
        return 0;
    }

    vector_clear_args(vector);

    vector->frame_tag = 0;
    vector->type = VECTOR_SAW;
    vector->period = period;
    vector->argv[0] = v0;
    vector->argv[1] = v1;

    if (vector_nesting(vector, g_vectors.nesting) == 0)
    {
        lua_pushstring(lua, "api_vector_saw: nesting is too deep");
        lua_error(lua);
        return 0;
    }

    return 0;
}

static int api_vector_rubber(lua_State *lua)
{
    struct vector_t *vector, *v0;
    float rubber;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_vector_rubber: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vector = vector_get(lua_tointeger(lua, 1));
    v0 = vector_get(lua_tointeger(lua, 2));
    rubber = lua_tonumber(lua, 3);
    lua_pop(lua, 3);

    if (vector == 0 || v0 == 0)
    {
        lua_pushstring(lua, "api_vector_rubber: invalid vector");
        lua_error(lua);
        return 0;
    }

    if (rubber < 0.0f || rubber > 1.0f)
    {
        lua_pushstring(lua, "api_vector_rubber: rubber is out of range");
        lua_error(lua);
        return 0;
    }

    vector_clear_args(vector);

    vector->frame_tag = 0;
    vector->type = VECTOR_RUBBER;
    vector->rubber = rubber;
    vector->argv[0] = v0;

    if (vector_nesting(vector, g_vectors.nesting) == 0)
    {
        lua_pushstring(lua, "api_vector_rubber: nesting is too deep");
        lua_error(lua);
        return 0;
    }

    return 0;
}

static int api_vector_wsum(lua_State *lua)
{
    struct vector_t *vector, *v0, *v1, *v2, *v3, *v4;

    if (lua_gettop(lua) != 6 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6))
    {
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

    if (vector == 0 || v0 == 0 || v1 == 0 || v2 == 0 || v3 == 0 || v4 == 0)
    {
        lua_pushstring(lua, "api_vector_wsum: invalid vector");
        lua_error(lua);
        return 0;
    }

    vector_clear_args(vector);

    vector->frame_tag = 0;
    vector->type = VECTOR_WSUM;
    vector->argv[0] = v0;
    vector->argv[1] = v1;
    vector->argv[2] = v2;
    vector->argv[3] = v3;
    vector->argv[4] = v4;

    if (vector_nesting(vector, g_vectors.nesting) == 0)
    {
        lua_pushstring(lua, "api_vector_wsum: nesting is too deep");
        lua_error(lua);
        return 0;
    }

    return 0;
}

int vector_init(lua_State *lua, int count, int nesting)
{
    int i;
    g_vectors.pool = calloc(count, sizeof(struct vector_t));
    if (g_vectors.pool == 0)
        return 1;
    g_vectors.count = count;
    g_vectors.left = count;
    g_vectors.nesting = nesting;
    g_vectors.vacant = g_vectors.pool;
    for (i = 0; i < count; ++i)
    {
        if (i < count - 1)
            g_vectors.pool[i].next = g_vectors.pool + i + 1;
        g_vectors.pool[i].vacant = 1;
    }
    lua_register(lua, "api_vector_alloc", api_vector_alloc);
    lua_register(lua, "api_vector_free", api_vector_free);
    lua_register(lua, "api_vector_left", api_vector_left);
    lua_register(lua, "api_vector_const", api_vector_const);
    lua_register(lua, "api_vector_sine", api_vector_sine);
    lua_register(lua, "api_vector_saw", api_vector_saw);
    lua_register(lua, "api_vector_rubber", api_vector_rubber);
    lua_register(lua, "api_vector_wsum", api_vector_wsum);
    return 0;
}

void vector_done(void)
{
    if (g_vectors.pool)
    {
        free(g_vectors.pool);
        g_vectors.pool = 0;
    }
}

struct vector_t * vector_get(int i)
{
    if (i >= 0 && i < g_vectors.count)
        return g_vectors.pool + i;
    else
        return 0;
}

int vector_nesting(struct vector_t *vector, int limit)
{
    int i, min, cur;
    if (limit > 0)
    {
        min = limit;
        for (i = 0; i < VECTOR_ARGVS; ++i)
        {
            if (vector->argv[i] == 0)
                continue;
            cur = vector_nesting(vector->argv[i], limit - 1);
            if (cur < min)
                min = cur;
        }
        return min;
    }
    else
        return limit;
}

void vector_update(struct vector_t *vector, float dt, int frame_tag, int force)
{
    int i;
    GLfloat *v0, *v1, *v2, *v3, *v4;
    if (vector->type == VECTOR_CONST)
        return;
    if (force == 0 && vector->frame_tag == frame_tag)
        return;
    vector->frame_tag = frame_tag;
    if (vector->type == VECTOR_SINE)
    {
        vector_update(vector->argv[0], dt, frame_tag, force);
        vector_update(vector->argv[1], dt, frame_tag, force);
        vector->t += dt;
        while (vector->t > vector->period)
            vector->t -= vector->period;
        v0 = vector->argv[0]->value;
        v1 = vector->argv[1]->value;
        for (i = 0; i < 4; ++i)
        {
            vector->value[i] = (0.5f * (v1[i] + v0[i])) +
                               (0.5f * (v1[i] - v0[i]) * 
                               sin(2.0f*M_PI*vector->t / vector->period));
        }
    }
    else if (vector->type == VECTOR_SAW)
    {
        vector_update(vector->argv[0], dt, frame_tag, force);
        vector_update(vector->argv[1], dt, frame_tag, force);
        vector->t += dt;
        while (vector->t > vector->period)
            vector->t -= vector->period;
        v0 = vector->argv[0]->value;
        v1 = vector->argv[1]->value;
        for (i = 0; i < 4; ++i)
        {
            vector->value[i] = v0[i] + ((v1[i] - v0[i]) *
                                vector->t / vector->period);
        }
    }
    else if (vector->type == VECTOR_RUBBER)
    {
        vector_update(vector->argv[0], dt, frame_tag, force);
        v0 = vector->argv[0]->value;
        for (i = 0; i < 4; ++i)
            vector->value[i] += (v0[i] - vector->value[i]) * vector->rubber;
    }
    else if (vector->type == VECTOR_WSUM)
    {
        vector_update(vector->argv[0], dt, frame_tag, force);
        vector_update(vector->argv[1], dt, frame_tag, force);
        vector_update(vector->argv[2], dt, frame_tag, force);
        vector_update(vector->argv[3], dt, frame_tag, force);
        vector_update(vector->argv[4], dt, frame_tag, force);
        v0 = vector->argv[0]->value;
        v1 = vector->argv[1]->value;
        v2 = vector->argv[2]->value;
        v3 = vector->argv[3]->value;
        v4 = vector->argv[4]->value;
        for (i = 0; i < 4; ++i)
        {
            vector->value[i] = (v0[0] * v1[i]) + (v0[1] * v2[i]) +
                               (v0[2] * v3[i]) + (v0[3] * v4[i]);
        }
    }
}

void vector_cross(GLfloat *out, GLfloat *v1, GLfloat *v2)
{
    out[0] = v1[1]*v2[2] - v2[1]*v1[2];
    out[1] = v1[2]*v2[0] - v2[2]*v1[0];
    out[2] = v1[0]*v2[1] - v2[0]*v1[1];
}
