#include "render.h"
#include <stdio.h>

struct render_t
{
    int init;
    int width;
    int height;
};

static struct render_t g_render;

void render_engage(void)
{
    printf("render_engage: TODO\n");
}

int render_init(lua_State *lua, int width, int height, int full_screen)
{
    if (full_screen)
        printf("render_init: full screen TODO\n");
    g_render.width = width;
    g_render.height = height;
    g_render.init = 1;
    if (lua)
        printf("render_init: lua mapping TODO\n");
    return 0;
}

void render_done(void)
{
    if (g_render.init == 0)
        return;
    g_render.init = 0;
}

void render_thread_done(void)
{
    printf("render_thread_done: TODO\n");
}
