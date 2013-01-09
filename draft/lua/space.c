#include "space.h"
#include "scene.h"
#include <stdlib.h>

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

int space_spawn(void)
{
    struct space_t *space;
    if (g_spaces.vacant == 0)
        return -1;
    --g_spaces.left;
    space = g_spaces.vacant;
    space->vacant = 0;
    g_spaces.vacant = g_spaces.vacant->next;

    if (space->prev)
        space->prev->next = space->next;
    if (space->next)
        space->next->prev = space->prev;

    space->prev = 0;
    space->next = 0;

    return space - g_spaces.pool;
}

void space_kill(int spacei)
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

void space_identity(int spacei)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->tag = 0;
    space->offset[0] = 0.0f;
    space->offset[1] = 0.0f;
    space->offset[2] = 0.0f;
    space->scale[0] = 1.0f;
    space->scale[1] = 1.0f;
    space->scale[2] = 1.0f;
    space->rotaxis[0] = 1.0f;
    space->rotaxis[1] = 0.0f;
    space->rotaxis[2] = 0.0f;
    space->rotangle = 0.0f;
    space->offset_tween[0] = -1;
    space->offset_tween[1] = -1;
    space->offset_tween[2] = -1;
    space->scale_tween[0] = -1;
    space->scale_tween[1] = -1;
    space->scale_tween[2] = -1;
    space->rotangle_tween = -1;
}

void space_offset(int spacei, float x, float y, float z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->tag = 0;
    space->offset[0] = x;
    space->offset[1] = y;
    space->offset[2] = z;
}

void space_offset_tween(int spacei, int x, int y, int z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->tag = 0;
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
    space->tag = 0;
    space->scale[0] = x;
    space->scale[1] = y;
    space->scale[2] = z;
}

void space_scale_tween(int spacei, int x, int y, int z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->tag = 0;
    space->scale_tween[0] = x;
    space->scale_tween[1] = y;
    space->scale_tween[2] = z;
}

void space_rotation(int spacei, float angle, float x, float y, float z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->tag = 0;
    space->rotaxis[0] = x;
    space->rotaxis[1] = y;
    space->rotaxis[2] = z;
    space->rotangle = angle;
}

void space_rotation_tween(int spacei, int angle, float x, float y, float z)
{
    struct space_t *space;
    space = space_get(spacei);
    if (space == 0)
        return;
    space->tag = 0;
    space->rotaxis[0] = x;
    space->rotaxis[1] = y;
    space->rotaxis[2] = z;
    space->rotangle_tween = angle;
}
