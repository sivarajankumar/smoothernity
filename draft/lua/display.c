#include <SDL.h>
#include <GL/gl.h>
#include "display.h"
#include "tween.h"

struct display_t
{
    SDL_Surface *screen;
    float clear_color[3];
    int clear_color_tween[3];
};

static struct display_t g_display;

int display_set_mode(int width, int height)
{
    int bpp;
    int flags;
    const SDL_VideoInfo *info;

    info = SDL_GetVideoInfo();
    if (info == 0)
        return 1;

    bpp = info->vfmt->BitsPerPixel;
    SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 16);
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);
    flags = SDL_OPENGL | SDL_FULLSCREEN;

    g_display.screen = SDL_SetVideoMode(width, height, bpp, flags);
    if (g_display.screen == 0)
        return 1;

    g_display.clear_color_tween[0] = -1;
    g_display.clear_color_tween[1] = -1;
    g_display.clear_color_tween[2] = -1;

    return 0;
}

void display_update(void)
{
    float color[3];
    int i;
    for (i = 0; i < 3; ++i)
    {
        if (g_display.clear_color_tween[i] != -1)
            color[i] = tween_value(g_display.clear_color_tween[i]);
        else
            color[i] = g_display.clear_color[i];
    }
    glClearColor(color[0], color[1], color[2], 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);
}

void display_show(void)
{
    SDL_GL_SwapBuffers();
}

void display_set_clear_color(float r, float g, float b)
{
    g_display.clear_color[0] = r;
    g_display.clear_color[1] = g;
    g_display.clear_color[2] = b;
}

void display_tween_clear_color(int r, int g, int b)
{
    g_display.clear_color_tween[0] = r;
    g_display.clear_color_tween[1] = g;
    g_display.clear_color_tween[2] = b;
}
