#include "render.h"
#include "vector.h"
#include "matrix.h"
#include "ibuf.h"
#include "vbuf.h"
#include "pbuf.h"
#include "tex.h"
#include "../thread/thread.h"
#include "../platform/render.h"
#include <SDL.h>
#include <GL/glew.h>

struct render_t
{
    int init;
    int width;
    int height;
    SDL_Surface *screen;
    struct thread_mutex_t *mutex;
    struct thread_cond_t *engage;
    struct thread_t *thread;
    struct pfm_render_ctx_t *ctx;
    int quit;
};

static struct render_t g_render;

static void render_thread(void)
{
    int count;
    pfm_render_select_ctx(g_render.ctx);
    while (g_render.quit == 0)
    {
        thread_mutex_lock(g_render.mutex);
        thread_cond_wait(g_render.engage, g_render.mutex);
        thread_mutex_unlock(g_render.mutex);
        do
        {
            count = 0;
            count += vbuf_thread();
            count += ibuf_thread();
            count += pbuf_thread();
            count += tex_thread();
        } while (count > 0);
    }
    pfm_render_unselect_ctx();
}

void render_engage(void)
{
    thread_cond_signal(g_render.engage);
}

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
    struct vector_t *vec;
    int depthi;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_render_clear_depth: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vec = vector_get(lua_tointeger(lua, 1));
    depthi = lua_tointeger(lua, 2);
    lua_pop(lua, 2);
    if (depthi < 0 || depthi > 3)
    {
        lua_pushstring(lua, "api_render_clear_depth: invalid depth index");
        lua_error(lua);
        return 0;
    }
    if (vec == 0)
    {
        lua_pushstring(lua, "api_render_clear_depth: invalid vector");
        lua_error(lua);
        return 0;
    }
    glClearDepthf(vec->value[depthi]);
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

static int api_render_proj(lua_State *lua)
{
    struct matrix_t *m;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_proj: incorrect argument");
        lua_error(lua);
        return 0;
    }
    m = matrix_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (m == 0)
    {
        lua_pushstring(lua, "api_render_proj: invalid matrix");
        lua_error(lua);
        return 0;
    }
    glMatrixMode(GL_PROJECTION);
    glLoadMatrixf(m->value);
    return 0;
}

static int api_render_mview(lua_State *lua)
{
    struct matrix_t *m;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_mview: incorrect argument");
        lua_error(lua);
        return 0;
    }
    m = matrix_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (m == 0)
    {
        lua_pushstring(lua, "api_render_mview: invalid matrix");
        lua_error(lua);
        return 0;
    }
    glMatrixMode(GL_MODELVIEW);
    glLoadMatrixf(m->value);
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

int render_init(lua_State *lua, int width, int height)
{
    int bpp;
    int flags;
    const SDL_VideoInfo *info;

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

    if (glewInit() != GLEW_OK)
        goto cleanup;

    if (!GLEW_ARB_timer_query || !GLEW_EXT_texture_array || !GLEW_EXT_gpu_shader4)
        goto cleanup;

    g_render.width = width;
    g_render.height = height;
    g_render.init = 1;

    g_render.ctx = pfm_render_create_shared_ctx();
    if (g_render.ctx == 0)
        goto cleanup;
    g_render.mutex = thread_mutex_create();
    if (g_render.mutex == 0)
        goto cleanup;
    g_render.engage = thread_cond_create();
    if (g_render.engage == 0)
        goto cleanup;
    g_render.thread = thread_create(render_thread);
    if (g_render.thread == 0)
        goto cleanup;

    glShadeModel(GL_SMOOTH);
    glCullFace(GL_BACK);
    glFrontFace(GL_CCW);
    glEnable(GL_CULL_FACE);
    glEnable(GL_DEPTH_TEST);
    glViewport(0, 0, width, height);

    lua_register(lua, "api_render_clear_color", api_render_clear_color);
    lua_register(lua, "api_render_clear_depth", api_render_clear_depth);
    lua_register(lua, "api_render_clear", api_render_clear);
    lua_register(lua, "api_render_proj", api_render_proj);
    lua_register(lua, "api_render_mview", api_render_mview);
    lua_register(lua, "api_render_swap", api_render_swap);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, y);

    LUA_PUBLISH(GL_COLOR_BUFFER_BIT, "API_RENDER_CLEAR_COLOR");
    LUA_PUBLISH(GL_DEPTH_BUFFER_BIT, "API_RENDER_CLEAR_DEPTH");

    return 0;
cleanup:
    if (g_render.ctx)
        pfm_render_destroy_ctx(g_render.ctx);
    g_render.ctx = 0;
    if (g_render.mutex)
        thread_mutex_destroy(g_render.mutex);
    g_render.mutex = 0;
    if (g_render.engage)
        thread_cond_destroy(g_render.engage);
    g_render.engage = 0;
    SDL_ShowCursor(SDL_ENABLE);
    SDL_Quit();
    return 1;
}

void render_done(void)
{
    if (g_render.init == 0)
        return;
    g_render.init = 0;
    g_render.quit = 1;
    if (g_render.engage)
        thread_cond_signal(g_render.engage);
    if (g_render.thread)
        thread_destroy(g_render.thread);
    if (g_render.mutex)
        thread_mutex_destroy(g_render.mutex);
    if (g_render.engage)
        thread_cond_destroy(g_render.engage);
    if (g_render.ctx)
        pfm_render_destroy_ctx(g_render.ctx);
    SDL_ShowCursor(SDL_ENABLE);
    SDL_Quit();
}
