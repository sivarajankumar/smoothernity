#include <SDL.h>
#include <GL/gl.h>
#include <GL/glut.h>
#include "render.h"
#include "timer.h"
#include "rop.h"

struct render_t
{
    int init;
    int width;
    int height;
    int frame_tag;
    SDL_Surface *screen;
    struct timer_t *timer;
    struct rop_t *rop;
    float last_update_time;
    float last_draw_time;
};

static struct render_t g_render;

static int api_render_engage(lua_State *lua)
{
    struct rop_t *rop;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_engage: incorrect argument");
        lua_error(lua);
        return 0;
    }

    rop = rop_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (rop == 0)
    {
        lua_pushstring(lua, "api_render_engage: invalid rop");
        lua_error(lua);
        return 0;
    }

    g_render.rop = rop;
    return 0;
}

static int api_render_timing(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_render_timing: incorrect argument");
        lua_error(lua);
        return 0;
    }

    lua_pushnumber(lua, g_render.last_update_time);
    lua_pushnumber(lua, g_render.last_draw_time);
    return 2;
}

int render_init(lua_State *lua, int *argc, char **argv, int width, int height)
{
    int bpp;
    int flags;
    const SDL_VideoInfo *info;

    g_render.timer = timer_create();
    if (g_render.timer == 0)
        return 1;

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

    g_render.frame_tag = 1000;
    g_render.width = width;
    g_render.height = height;
    g_render.init = 1;

    glShadeModel(GL_SMOOTH);
    glCullFace(GL_BACK);
    glFrontFace(GL_CCW);
    glEnable(GL_CULL_FACE);
    glEnable(GL_DEPTH_TEST);
    glViewport(0, 0, width, height);

    lua_register(lua, "api_render_engage", api_render_engage);
    lua_register(lua, "api_render_timing", api_render_timing);

    return 0;
cleanup:
    SDL_ShowCursor(SDL_ENABLE);
    SDL_Quit();
    if (g_render.timer)
    {
        timer_destroy(g_render.timer);
        g_render.timer = 0;
    }
    return 1;
}

void render_done(void)
{
    if (g_render.init == 0)
        return;
    if (g_render.timer)
    {
        timer_destroy(g_render.timer);
        g_render.timer = 0;
    }
    g_render.init = 0;
    SDL_ShowCursor(SDL_ENABLE);
    SDL_Quit();
}

void render_update(float dt)
{
    timer_reset(g_render.timer);
    ++g_render.frame_tag;
    if (g_render.rop)
        rop_update(g_render.rop, dt, g_render.frame_tag);
    g_render.last_update_time = timer_passed(g_render.timer);
}

int render_draw(void)
{
    timer_reset(g_render.timer);
    if (g_render.rop)
    {
        if (rop_draw(g_render.rop, g_render.frame_tag) != 0)
            return 1;
    }
    SDL_GL_SwapBuffers();
    g_render.last_draw_time = timer_passed(g_render.timer);
    return 0;
}
