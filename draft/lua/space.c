#include "space.h"
#include "scene.h"
#include "tween.h"
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct spaces_t g_spaces;

int space_init(int count)
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
    g_spaces.vacant = g_spaces.pool;
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

void space_query(int *left)
{
    *left = g_spaces.left;
}

int space_alloc(void)
{
    struct space_t *space;
    if (g_spaces.vacant == 0)
        return -1;
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

    return space - g_spaces.pool;
}

void space_free(int spacei)
{
    struct space_t *space;
    if (spacei < 0 || spacei >= g_spaces.count)
        return;
    space = g_spaces.pool + spacei;
    if (space->vacant)
        return;
    space->vacant = 1;
    ++g_spaces.left;

    if (g_spaces.vacant)
        g_spaces.vacant->prev = space;
    space->prev = 0;
    space->next = g_spaces.vacant;
    g_spaces.vacant = space;
}

struct space_t * space_get(int spacei)
{
    if (spacei >= 0 && spacei < g_spaces.count)
        return g_spaces.pool + spacei;
    else
        return 0;
}

void space_offset(int spacei, float x, float y, float z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->frame_tag = 0;
    space->offset[0] = x;
    space->offset[1] = y;
    space->offset[2] = z;
}

void space_offset_tween(int spacei, struct tween_t *x,
                        struct tween_t *y, struct tween_t *z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->frame_tag = 0;
    space->offset_tween[0] = x;
    space->offset_tween[1] = y;
    space->offset_tween[2] = z;
}

void space_scale(int spacei, float x, float y, float z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->frame_tag = 0;
    space->scale[0] = x;
    space->scale[1] = y;
    space->scale[2] = z;
}

void space_scale_tween(int spacei, struct tween_t *x,
                       struct tween_t *y, struct tween_t *z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->frame_tag = 0;
    space->scale_tween[0] = x;
    space->scale_tween[1] = y;
    space->scale_tween[2] = z;
}

void space_rotation(int spacei, int axis, float angle)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    if (axis < 0 || axis > (int)SPACE_AXES_TOTAL)
        return;
    space->frame_tag = 0;
    space->rotangle = angle;
    space->rotaxis = (enum space_axis_e)axis;
}

void space_rotation_tween(int spacei, int axis, struct tween_t *angle)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    if (axis < 0 || axis > (int)SPACE_AXES_TOTAL)
        return;
    space->frame_tag = 0;
    space->rotangle_tween = angle;
    space->rotaxis = (enum space_axis_e)axis;
}

void space_compute(struct space_t *space)
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

void space_select(struct space_t *space)
{
    glLoadMatrixf(space->matrix);
}
