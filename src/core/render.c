#include <SDL.h>
#include <GL/gl.h>
#include <GL/glut.h>
#include "render.h"

struct render_t
{
    int init;
    int width;
    int height;
    SDL_Surface *screen;
};

static struct render_t g_render;

int render_init(int *argc, char **argv, int width, int height)
{
    int bpp;
    int flags;
    const SDL_VideoInfo *info;

    glutInit(argc, argv);
    if (SDL_Init(SDL_INIT_EVERYTHING) != 0)
        return 1;
    SDL_ShowCursor(SDL_DISABLE);

    info = SDL_GetVideoInfo();
    if (info == 0)
        goto cleanup;

    bpp = info->vfmt->BitsPerPixel;
    SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 16);
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);
    flags = SDL_OPENGL | SDL_FULLSCREEN;

    g_render.screen = SDL_SetVideoMode(width, height, bpp, flags);
    if (g_render.screen == 0)
        goto cleanup;

    g_render.width = width;
    g_render.height = height;
    g_render.init = 1;

    glShadeModel(GL_SMOOTH);
    glCullFace(GL_BACK);
    glFrontFace(GL_CCW);
    glEnable(GL_CULL_FACE);
    glEnable(GL_DEPTH_TEST);
    glViewport(0, 0, width, height);

    return 0;
cleanup:
    SDL_ShowCursor(SDL_ENABLE);
    SDL_Quit();
    return 1;
}

void render_done(void)
{
    if (g_render.init == 0)
        return;
    g_render.init = 0;
    SDL_ShowCursor(SDL_ENABLE);
    SDL_Quit();
}
