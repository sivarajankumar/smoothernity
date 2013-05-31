#include "render.h"
#include "vector.h"
#include <stdio.h>
#include "SDL.h"
#include "GL/glew.h"

/*
 * Wherever possible, target non-depricated functionality
 * intersection between:
 * - OpenGL ES 3.0, OpenGL 4.3 and OpenGL 3.0;
 * - GLSL ES 3.00, GLSL 4.30 and GLSL 1.30.
 */

static const GLint MIN_GL_VERSION = 3;

struct render_t
{
    int init;
    int width;
    int height;
};

static struct render_t g_render;

static int api_render_clear_color(lua_State *lua)
{
    GLfloat *v;
    struct vector_t *vec;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_clear_color: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vec = vector_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (vec == 0)
    {
        lua_pushstring(lua, "api_render_clear_color: invalid vector");
        lua_error(lua);
        return 0;
    }
    v = vec->value;
    glClearColor(v[0], v[1], v[2], v[3]);
    return 0;
}

static int api_render_clear_depth(lua_State *lua)
{
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_clear_depth: incorrect argument");
        lua_error(lua);
        return 0;
    }
    glClearDepthf((GLfloat)lua_tonumber(lua, 1));
    lua_pop(lua, 1);
    return 0;
}

static int api_render_clear(lua_State *lua)
{
    int flags;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_clear: incorrect argument");
        lua_error(lua);
        return 0;
    }
    flags = lua_tointeger(lua, 1);
    lua_pop(lua, 1);
    glClear(flags);
    return 0;
}

static int api_render_swap(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_render_swap: incorrect argument");
        lua_error(lua);
        return 0;
    }
    SDL_GL_SwapBuffers();
    return 0;
}

int render_init(lua_State *lua, int width, int height, int full_screen)
{
    int bpp, flags;
    const SDL_VideoInfo *info;
    GLint version;

    if (sizeof(float) != sizeof(GLfloat))
    {
        fprintf(stderr, "render_init: float<->GLfloat is not supported\n");
        goto cleanup;
    }

    if (sizeof(int) != sizeof(GLint))
    {
        fprintf(stderr, "render_init: int<->GLint is not supported\n");
        goto cleanup;
    }

    info = SDL_GetVideoInfo();
    if (info == 0)
        goto cleanup;

    bpp = info->vfmt->BitsPerPixel;
    SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 16);
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);

    flags = SDL_OPENGL | SDL_DOUBLEBUF;
    if (full_screen)
    {
        SDL_ShowCursor(SDL_DISABLE);
        flags |= SDL_FULLSCREEN;
    }

    if (SDL_SetVideoMode(width, height, bpp, flags) == 0)
        goto cleanup;

    if (glewInit() != GLEW_OK)
        goto cleanup;

    printf("render_init: GL: %s, GLSL: %s\n",
           glGetString(GL_VERSION),
           glGetString(GL_SHADING_LANGUAGE_VERSION));

    glGetIntegerv(GL_MAJOR_VERSION, &version);
    if (version < MIN_GL_VERSION)
        goto cleanup;

    g_render.width = width;
    g_render.height = height;
    g_render.init = 1;

    lua_register(lua, "api_render_clear_color", api_render_clear_color);
    lua_register(lua, "api_render_clear_depth", api_render_clear_depth);
    lua_register(lua, "api_render_clear", api_render_clear);
    lua_register(lua, "api_render_swap", api_render_swap);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, y);

    LUA_PUBLISH(GL_COLOR_BUFFER_BIT, "API_RENDER_CLEAR_COLOR");
    LUA_PUBLISH(GL_DEPTH_BUFFER_BIT, "API_RENDER_CLEAR_DEPTH");

    return 0;
cleanup:
    SDL_ShowCursor(SDL_ENABLE);
    g_render.init = 0;
    return 1;
}

void render_done(void)
{
    if (g_render.init == 0)
        return;
    SDL_ShowCursor(SDL_ENABLE);
    g_render.init = 0;
}

