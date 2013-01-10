#include "space.h"
#include "scene.h"
#include "tween.h"
#include <stdlib.h>
#include <string.h>
#include <math.h>

enum space_axis_e
{
    SPACE_AXIS_X = 0,
    SPACE_AXIS_Y = 1,
    SPACE_AXIS_Z = 2,
    SPACE_AXES_TOTAL = 3
};

enum space_update_e
{
    SPACE_UPDATE_AUTO = 0,
    SPACE_UPDATE_MANUAL = 1,
    SPACE_UPDATES_TOTAL = 2
};

struct space_t
{
    int frame_tag; /* when this space was last updated */
    int vacant;
    GLfloat matrix[16];
    float offset[3];
    float scale[3];
    float rotangle;
    enum space_axis_e rotaxis;
    enum space_update_e update;
    struct tween_t *offset_tween[3];
    struct tween_t *scale_tween[3];
    struct tween_t *rotangle_tween;
    struct space_t *prev;
    struct space_t *next;
    struct space_t *parent;
};

struct spaces_t
{
    int left;
    int count;
    int nesting;
    struct space_t *pool;
    struct space_t *vacant;
};

static struct spaces_t g_spaces;

static void space_compute(struct space_t*);
static void space_mult(struct space_t*, struct space_t*, struct space_t*);

static int api_space_alloc(lua_State *lua)
{
    struct space_t *space;
    int update;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    update = lua_tointeger(lua, -1);
    lua_pop(lua, 1);

    if (update < 0 || update >= (int)SPACE_UPDATES_TOTAL)
    {
        lua_pushstring(lua, "api_space_alloc: update method out of range");
        lua_error(lua);
        return 0;
    }

    if (g_spaces.vacant == 0)
    {
        lua_pushstring(lua, "api_space_alloc: out of spaces");
        lua_error(lua);
        return 0;
    }

    --g_spaces.left;
    space = g_spaces.vacant;
    g_spaces.vacant = g_spaces.vacant->next;

    if (space->prev)
        space->prev->next = space->next;
    if (space->next)
        space->next->prev = space->prev;

    memset(space, 0, sizeof(struct space_t));

    space->scale[0] = 1.0f;
    space->scale[1] = 1.0f;
    space->scale[2] = 1.0f;
    space->update = (enum space_update_e)update;

    if (space->update == SPACE_UPDATE_MANUAL)
        space_compute(space);

    lua_pushinteger(lua, space - g_spaces.pool);
    return 1;
}

static int api_space_free(lua_State *lua)
{
    struct space_t *space;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    space = space_get(lua_tointeger(lua, -1));
    lua_pop(lua, 1);

    if (space == 0 || space->vacant)
    {
        lua_pushstring(lua, "api_space_free: invalid space");
        lua_error(lua);
        return 0;
    }

    space->vacant = 1;
    ++g_spaces.left;

    if (g_spaces.vacant)
        g_spaces.vacant->prev = space;
    space->prev = 0;
    space->next = g_spaces.vacant;
    g_spaces.vacant = space;
    return 0;
}

static int api_space_attach(lua_State *lua)
{
    struct space_t *space1;
    struct space_t *space2;
    struct space_t *s;
    int nesting;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, -1)
    || !lua_isnumber(lua, -2))
    {
        lua_pushstring(lua, "api_space_attach: incorrect argument");
        lua_error(lua);
        return 0;
    }

    space1 = space_get(lua_tointeger(lua, -2));
    space2 = space_get(lua_tointeger(lua, -1));
    lua_pop(lua, 2);

    if (space1 == 0 || space2 == 0)
    {
        lua_pushstring(lua, "api_space_attach: invalid space");
        lua_error(lua);
        return 0;
    }

    space1->parent = space2;

    nesting = 0;
    for (s = space1; s; s = s->parent)
    {
        if (++nesting > g_spaces.nesting)
        {
            lua_pushstring(lua, "api_space_attach: nesting is too deep");
            lua_error(lua);
            return 0;
        }
    }

    return 0;
}

static int api_space_mult(lua_State *lua)
{
    struct space_t *space;
    struct space_t *space1;
    struct space_t *space2;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_mult: incorrect argument");
        lua_error(lua);
        return 0;
    }

    space = space_get(lua_tointeger(lua, -3));
    space1 = space_get(lua_tointeger(lua, -2));
    space2 = space_get(lua_tointeger(lua, -1));
    lua_pop(lua, 3);

    if (space == 0 || space1 == 0 || space2 == 0)
    {
        lua_pushstring(lua, "api_space_mult: invalid space");
        lua_error(lua);
        return 0;
    }

    space_mult(space, space1, space2);
    return 0;
}

static int api_space_query(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_space_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_spaces.left);
    return 1;
}

static int api_space_offset(lua_State *lua)
{
    struct space_t *space;
    float x, y, z;

    if (lua_gettop(lua) != 4
    || !lua_isnumber(lua, -4) || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_offset: incorrect argument");
        lua_error(lua);
        return 0;
    }

    space = space_get(lua_tointeger(lua, -4));
    x = (float)lua_tonumber(lua, -3);
    y = (float)lua_tonumber(lua, -2);
    z = (float)lua_tonumber(lua, -1);
    lua_pop(lua, 4);

    if (space == 0)
    {
        lua_pushstring(lua, "api_space_offset: invalid space");
        lua_error(lua);
        return 0;
    }

    space->frame_tag = 0;
    space->offset[0] = x;
    space->offset[1] = y;
    space->offset[2] = z;
    if (space->update == SPACE_UPDATE_MANUAL)
        space_compute(space);
    return 0;
}

static int api_space_offset_tween(lua_State *lua)
{
    struct space_t *space;
    struct tween_t *x, *y, *z;

    if (lua_gettop(lua) != 4
    || !lua_isnumber(lua, -4) || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_offset_tween: incorrect argument");
        lua_error(lua);
        return 0;
    }

    space = space_get(lua_tointeger(lua, -4));
    x = tween_get(lua_tointeger(lua, -3));
    y = tween_get(lua_tointeger(lua, -2));
    z = tween_get(lua_tointeger(lua, -1));
    lua_pop(lua, 4);

    if (space == 0)
    {
        lua_pushstring(lua, "api_space_offset_tween: invalid space");
        lua_error(lua);
        return 0;
    }

    space->frame_tag = 0;
    space->offset_tween[0] = x;
    space->offset_tween[1] = y;
    space->offset_tween[2] = z;
    return 0;
}

static int api_space_scale(lua_State *lua)
{
    struct space_t *space;
    float x, y, z;

    if (lua_gettop(lua) != 4
    || !lua_isnumber(lua, -4) || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_scale: incorrect argument");
        lua_error(lua);
        return 0;
    }

    space = space_get(lua_tointeger(lua, -4));
    x = (float)lua_tonumber(lua, -3);
    y = (float)lua_tonumber(lua, -2);
    z = (float)lua_tonumber(lua, -1);
    lua_pop(lua, 4);

    if (space == 0)
    {
        lua_pushstring(lua, "api_space_scale: invalid space");
        lua_error(lua);
        return 0;
    }

    space->frame_tag = 0;
    space->scale[0] = x;
    space->scale[1] = y;
    space->scale[2] = z;
    if (space->update == SPACE_UPDATE_MANUAL)
        space_compute(space);
    return 0;
}

static int api_space_scale_tween(lua_State *lua)
{
    struct space_t *space;
    struct tween_t *x, *y, *z;

    if (lua_gettop(lua) != 4
    || !lua_isnumber(lua, -4) || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_scale_tween: incorrect argument");
        lua_error(lua);
        return 0;
    }

    space = space_get(lua_tointeger(lua, -4));
    x = tween_get(lua_tointeger(lua, -3));
    y = tween_get(lua_tointeger(lua, -2));
    z = tween_get(lua_tointeger(lua, -1));
    lua_pop(lua, 4);

    if (space == 0)
    {
        lua_pushstring(lua, "api_space_scale_tween: invalid space");
        lua_error(lua);
        return 0;
    }

    space->frame_tag = 0;
    space->scale_tween[0] = x;
    space->scale_tween[1] = y;
    space->scale_tween[2] = z;
    return 0;
}

static int api_space_rotation(lua_State *lua)
{
    struct space_t *space;
    int axis;
    float angle;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_rotation: incorrect argument");
        lua_error(lua);
        return 0;
    }
    space = space_get(lua_tointeger(lua, -3));
    axis = lua_tointeger(lua, -2);
    angle = (float)lua_tonumber(lua, -1);
    lua_pop(lua, 3);

    if (space == 0)
    {
        lua_pushstring(lua, "api_space_rotation: invalid space");
        lua_error(lua);
        return 0;
    }

    if (axis < 0 || axis > (int)SPACE_AXES_TOTAL)
    {
        lua_pushstring(lua, "api_space_rotation: invalid axis");
        lua_error(lua);
        return 0;
    }

    space->frame_tag = 0;
    space->rotangle = angle;
    space->rotaxis = (enum space_axis_e)axis;
    if (space->update == SPACE_UPDATE_MANUAL)
        space_compute(space);
    return 0;
}

static int api_space_rotation_tween(lua_State *lua)
{
    struct space_t *space;
    int axis;
    struct tween_t *angle;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_space_rotation_tween: incorrect argument");
        lua_error(lua);
        return 0;
    }

    space = space_get(lua_tointeger(lua, -3));
    axis = lua_tointeger(lua, -2);
    angle = tween_get(lua_tointeger(lua, -1));
    lua_pop(lua, 3);

    if (space == 0)
    {
        lua_pushstring(lua, "api_space_rotation_tween: invalid space");
        lua_error(lua);
        return 0;
    }

    if (axis < 0 || axis > (int)SPACE_AXES_TOTAL)
    {
        lua_pushstring(lua, "api_space_rotation_tween: invalid axis");
        lua_error(lua);
        return 0;
    }

    space->frame_tag = 0;
    space->rotangle_tween = angle;
    space->rotaxis = (enum space_axis_e)axis;
    return 0;
}

int space_init(lua_State *lua, int count, int nesting)
{
    int i;
    g_spaces.pool = calloc(count, sizeof(struct space_t));
    if (g_spaces.pool == 0)
        return 1;
    for (i = 0; i < count; ++i)
    {
        if (i > 0)
            g_spaces.pool[i].prev = g_spaces.pool + i - 1;
        if (i < count - 1)
            g_spaces.pool[i].next = g_spaces.pool + i + 1;
        g_spaces.pool[i].vacant = 1;
    }
    g_spaces.left = count;
    g_spaces.count = count;
    g_spaces.nesting = nesting;
    g_spaces.vacant = g_spaces.pool;

    lua_register(lua, "api_space_alloc", api_space_alloc);
    lua_register(lua, "api_space_free", api_space_free);
    lua_register(lua, "api_space_attach", api_space_attach);
    lua_register(lua, "api_space_mult", api_space_mult);
    lua_register(lua, "api_space_query", api_space_query);
    lua_register(lua, "api_space_offset", api_space_offset);
    lua_register(lua, "api_space_offset_tween", api_space_offset_tween);
    lua_register(lua, "api_space_scale", api_space_scale);
    lua_register(lua, "api_space_scale_tween", api_space_scale_tween);
    lua_register(lua, "api_space_rotation", api_space_rotation);
    lua_register(lua, "api_space_rotation_tween", api_space_rotation_tween);

    return 0;
}

void space_done(void)
{
    if (g_spaces.pool)
    {
        free(g_spaces.pool);
        g_spaces.pool = 0;
    }
}

struct space_t * space_get(int spacei)
{
    if (spacei >= 0 && spacei < g_spaces.count)
        return g_spaces.pool + spacei;
    else
        return 0;
}

static void space_compute(struct space_t *space)
{
    float axisx[3];
    float axisy[3];
    float axisz[3];
    float offset[3];
    float scale[3];
    float rotangle;
    float rcos;
    float rsin;
    GLfloat *m;

    /* offset */

    if (space->offset_tween[0])
        offset[0] = space->offset_tween[0]->value;
    else
        offset[0] = space->offset[0];
    if (space->offset_tween[1])
        offset[1] = space->offset_tween[1]->value;
    else
        offset[1] = space->offset[1];
    if (space->offset_tween[2])
        offset[2] = space->offset_tween[2]->value;
    else
        offset[2] = space->offset[2];

    /* rotation */

    if (space->rotangle_tween)
        rotangle = space->rotangle_tween->value;
    else
        rotangle = space->rotangle;

    /* scale */

    if (space->scale_tween[0])
        scale[0] = space->scale_tween[0]->value;
    else
        scale[0] = space->scale[0];
    if (space->scale_tween[1])
        scale[1] = space->scale_tween[1]->value;
    else
        scale[1] = space->scale[1];
    if (space->scale_tween[2])
        scale[2] = space->scale_tween[2]->value;
    else
        scale[2] = space->scale[2];

    /* axes */

    rcos = cos(rotangle);
    rsin = sin(rotangle);
    if (space->rotaxis == SPACE_AXIS_X)
    {
        axisx[0] = 1; axisx[1] =     0; axisx[2] =    0; 
        axisy[0] = 0; axisy[1] =  rcos; axisy[2] = rsin; 
        axisz[0] = 0; axisz[1] = -rsin; axisz[2] = rcos; 
    }
    else if (space->rotaxis == SPACE_AXIS_Y)
    {
        axisx[0] = rcos; axisx[1] = 0; axisx[2] = -rsin; 
        axisy[0] =    0; axisy[1] = 1; axisy[2] =     0; 
        axisz[0] = rsin; axisz[1] = 0; axisz[2] =  rcos; 
    }
    else if (space->rotaxis == SPACE_AXIS_Z)
    {
        axisx[0] =  rcos; axisx[1] = rsin; axisx[2] = 0;
        axisy[0] = -rsin; axisy[1] = rcos; axisy[2] = 0;
        axisz[0] =     0; axisz[1] =    0; axisz[2] = 1;
    }

    axisx[0] *= scale[0]; axisx[1] *= scale[0]; axisx[2] *= scale[0];
    axisy[0] *= scale[1]; axisy[1] *= scale[1]; axisy[2] *= scale[1];
    axisz[0] *= scale[2]; axisz[1] *= scale[2]; axisz[2] *= scale[2];

    /* build final matrix */

    m = space->matrix;
    m[ 0] =  axisx[0]; m[ 1] =  axisx[1]; m[ 2] =  axisx[2]; m[ 3] = 0;
    m[ 4] =  axisy[0]; m[ 5] =  axisy[1]; m[ 6] =  axisy[2]; m[ 7] = 0;
    m[ 8] =  axisz[0]; m[ 9] =  axisz[1]; m[10] =  axisz[2]; m[11] = 0;
    m[12] = offset[0]; m[13] = offset[1]; m[14] = offset[2]; m[15] = 1;
}

static void space_mult(struct space_t *space,
                       struct space_t *space1, struct space_t *space2)
{
    GLfloat *m1, *m2;
    GLfloat m[16];

    m1 = space1->matrix;
    m2 = space2->matrix;

    m[0] = m1[0]*m2[0] + m1[4]*m2[1] + m1[ 8]*m2[2] + m1[12]*m2[3];
    m[1] = m1[1]*m2[0] + m1[5]*m2[1] + m1[ 9]*m2[2] + m1[13]*m2[3];
    m[2] = m1[2]*m2[0] + m1[6]*m2[1] + m1[10]*m2[2] + m1[14]*m2[3];
    m[3] = m1[3]*m2[0] + m1[7]*m2[1] + m1[11]*m2[2] + m1[15]*m2[3];

    m[4] = m1[0]*m2[4] + m1[4]*m2[5] + m1[ 8]*m2[6] + m1[12]*m2[7];
    m[5] = m1[1]*m2[4] + m1[5]*m2[5] + m1[ 9]*m2[6] + m1[13]*m2[7];
    m[6] = m1[2]*m2[4] + m1[6]*m2[5] + m1[10]*m2[6] + m1[14]*m2[7];
    m[7] = m1[3]*m2[4] + m1[7]*m2[5] + m1[11]*m2[6] + m1[15]*m2[7];

    m[ 8] = m1[0]*m2[8] + m1[4]*m2[9] + m1[ 8]*m2[10] + m1[12]*m2[11];
    m[ 9] = m1[1]*m2[8] + m1[5]*m2[9] + m1[ 9]*m2[10] + m1[13]*m2[11];
    m[10] = m1[2]*m2[8] + m1[6]*m2[9] + m1[10]*m2[10] + m1[14]*m2[11];
    m[11] = m1[3]*m2[8] + m1[7]*m2[9] + m1[11]*m2[10] + m1[15]*m2[11];

    m[12] = m1[0]*m2[12] + m1[4]*m2[13] + m1[ 8]*m2[14] + m1[12]*m2[15];
    m[13] = m1[1]*m2[12] + m1[5]*m2[13] + m1[ 9]*m2[14] + m1[13]*m2[15];
    m[14] = m1[2]*m2[12] + m1[6]*m2[13] + m1[10]*m2[14] + m1[14]*m2[15];
    m[15] = m1[3]*m2[12] + m1[7]*m2[13] + m1[11]*m2[14] + m1[15]*m2[15];

    memcpy(space->matrix, m, sizeof(GLfloat) * 16);
}

void space_select(struct space_t *space, int frame_tag)
{
    if (space->frame_tag != frame_tag)
    {
        if (space->update == SPACE_UPDATE_AUTO)
            space_compute(space);
        space->frame_tag = frame_tag;
    }
    if (space->parent)
        space_select(space->parent, frame_tag);
    glMultMatrixf(space->matrix);
}
