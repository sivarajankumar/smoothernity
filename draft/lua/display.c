#include <SDL.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include "display.h"
#include "tween.h"
#include "scene.h"
#include "vbuf.h"
#include "ibuf.h"
#include "space.h"
#include "mesh.h"
#include "text.h"

struct display_t
{
    int width;
    int height;
    int frame_tag;
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

    g_display.frame_tag = 1000;
    g_display.width = width;
    g_display.height = height;

    glShadeModel(GL_SMOOTH);
    glCullFace(GL_BACK);
    glFrontFace(GL_CCW);
    glEnable(GL_CULL_FACE);
    glViewport(0, 0, width, height);

    return 0;
}

void display_get_mode(int *width, int *height)
{
    *width = g_display.width;
    *height = g_display.height;
}

void display_update(void)
{
    struct vbuf_t *vbuf;
    struct ibuf_t *ibuf;
    struct mesh_t *mesh_vbuf;
    struct mesh_t *mesh_ibuf;
    float color[3];
    int i;

    ++g_display.frame_tag;

    /* clear */

    for (i = 0; i < 3; ++i)
    {
        if (g_display.clear_color_tween[i] != -1)
            color[i] = tween_value(g_display.clear_color_tween[i]);
        else
            color[i] = g_display.clear_color[i];
    }
    glClearColor(color[0], color[1], color[2], 1.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    /* frustum */

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    /* TODO: rewrite using proper mechanics */
    gluPerspective(60.0, (float)g_display.width / (float)g_display.height, 1.0, 1024.0);

    /* meshes */

    glMatrixMode(GL_MODELVIEW);
    if (g_vbufs.with_meshes < g_ibufs.with_meshes)
    {
        for (vbuf = g_vbufs.baked; vbuf; vbuf = vbuf->next)
        {
            if (vbuf->meshes == 0)
                continue;
            vbuf_select(vbuf);
            for (mesh_vbuf = vbuf->meshes; mesh_vbuf; mesh_vbuf = mesh_vbuf->next)
            {
                if (mesh_vbuf->frame_tag == g_display.frame_tag)
                    continue;
                ibuf = mesh_vbuf->ibuf;
                if (ibuf->mapped)
                    continue;
                ibuf_select(ibuf);
                for (mesh_ibuf = ibuf->meshes; mesh_ibuf; mesh_ibuf = mesh_ibuf->next)
                {
                    if (mesh_ibuf->frame_tag == g_display.frame_tag)
                        continue;
                    mesh_ibuf->frame_tag = g_display.frame_tag;
                    if (mesh_ibuf->space->frame_tag != g_display.frame_tag)
                    {
                        space_compute(mesh_ibuf->space);
                        mesh_ibuf->space->frame_tag = g_display.frame_tag;
                    }
                    space_select(mesh_ibuf->space);
                    mesh_draw(mesh_ibuf);
                }
            }
        }
    }
    else
    {
        for (ibuf = g_ibufs.baked; ibuf; ibuf = ibuf->next)
        {
            if (ibuf->meshes == 0)
                continue;
            ibuf_select(ibuf);
            for (mesh_ibuf = ibuf->meshes; mesh_ibuf; mesh_ibuf = mesh_ibuf->next)
            {
                if (mesh_ibuf->frame_tag == g_display.frame_tag)
                    continue;
                vbuf = mesh_ibuf->vbuf;
                if (vbuf->mapped)
                    continue;
                vbuf_select(vbuf);
                for (mesh_vbuf = vbuf->meshes; mesh_vbuf; mesh_vbuf = mesh_vbuf->next)
                {
                    if (mesh_vbuf->frame_tag == g_display.frame_tag)
                        continue;
                    mesh_vbuf->frame_tag = g_display.frame_tag;
                    if (mesh_vbuf->space->frame_tag != g_display.frame_tag)
                    {
                        space_compute(mesh_vbuf->space);
                        mesh_vbuf->space->frame_tag = g_display.frame_tag;
                    }
                    space_select(mesh_vbuf->space);
                    mesh_draw(mesh_vbuf);
                }
            }
        }
    }

    /* text */

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, g_display.width, g_display.height, 0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    text_draw();
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
