#include "crender.h"
#include "vector.h"
#include "cutil.h"
#include "vlog.h"
#include "SDL.h"
#include "GL/glew.h"

/*
 * Wherever possible, target non-depricated functionality
 * intersection between:
 * - OpenGL ES 3.0, OpenGL 4.3 and OpenGL 3.0;
 * - GLSL ES 3.00, GLSL 4.30 and GLSL 1.30.
 */

static const GLint MIN_GL_VERSION = 3;

struct crender_t {
    int init, width, height;
};

_Static_assert(sizeof(float) == sizeof(GLfloat),
               "float<->GLfloat is not supported");
_Static_assert(sizeof(int) == sizeof(GLint),
               "int<->GLint is not supported");

static struct crender_t g_crender;

static int api_render_clear_color(lua_State *lua) {
    GLfloat *v;
    struct vector_t *vec;
    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    vec = vector_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (!vec) {
        lua_pushstring(lua, "invalid vector");
        lua_error(lua);
        return 0;
    }
    v = vec->value;
    glClearColor(v[0], v[1], v[2], v[3]);
    return 0;
}

static int api_render_clear_depth(lua_State *lua) {
    if (lua_gettop(lua) != 1 || !cutil_isfloat(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    glClearDepthf((GLfloat)lua_tonumber(lua, 1));
    lua_pop(lua, 1);
    return 0;
}

static int api_render_clear(lua_State *lua) {
    int flags;
    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    flags = lua_tointeger(lua, 1);
    lua_pop(lua, 1);
    glClear(flags);
    return 0;
}

static int api_render_swap(lua_State *lua) {
    if (lua_gettop(lua)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    SDL_GL_SwapBuffers();
    return 0;
}

int crender_init(lua_State *lua, int width, int height, int full_screen) {
    int bpp, flags;
    const SDL_VideoInfo *info;
    GLint version;

    info = SDL_GetVideoInfo();
    if (!info)
        goto cleanup;

    bpp = info->vfmt->BitsPerPixel;
    SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 5);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 16);
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);

    flags = SDL_OPENGL | SDL_DOUBLEBUF;
    if (full_screen) {
        SDL_ShowCursor(SDL_DISABLE);
        flags |= SDL_FULLSCREEN;
    }

    if (!SDL_SetVideoMode(width, height, bpp, flags))
        goto cleanup;

    if (glewInit() != GLEW_OK)
        goto cleanup;

    VLOG_INFO("GL: %s, GLSL: %s",
              glGetString(GL_VERSION),
              glGetString(GL_SHADING_LANGUAGE_VERSION));

    glGetIntegerv(GL_MAJOR_VERSION, &version);
    if (version < MIN_GL_VERSION)
        goto cleanup;

    g_crender.width = width;
    g_crender.height = height;
    g_crender.init = 1;

    #define REGF(x) lua_register(lua, #x, x)
    REGF(api_render_clear_color);
    REGF(api_render_clear_depth);
    REGF(api_render_clear);
    REGF(api_render_swap);
    #undef REGF
    #define REGN(x) lua_pushinteger(lua, GL_##x); \
                    lua_setglobal(lua, "API_RENDER_"#x);
    REGN(COLOR_BUFFER_BIT);
    REGN(DEPTH_BUFFER_BIT);
    #undef REGN
    return 0;
cleanup:
    SDL_ShowCursor(SDL_ENABLE);
    g_crender.init = 0;
    return 1;
}

void crender_done(void) {
    if (!g_crender.init)
        return;
    SDL_ShowCursor(SDL_ENABLE);
    g_crender.init = 0;
}

