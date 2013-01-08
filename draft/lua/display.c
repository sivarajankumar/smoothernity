#include <SDL.h>
#include <GL/gl.h>
#include "display.h"

struct display_t
{
    SDL_Surface *screen;
    int width;
    int height;
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

    g_display.width = width;
    g_display.height = height;
    return 0;
}

void display_get_mode(int *width, int *height)
{
    *width = g_display.width;
    *height = g_display.height;
}

void display_show(void)
{
    SDL_GL_SwapBuffers();
}
