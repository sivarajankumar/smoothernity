#include <SDL.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include "render.h"
#include "vbuf.h"
#include "ibuf.h"
#include "mesh.h"
#include "text.h"
#include "vector.h"
#include "matrix.h"
#include "physics.h"
#include "timer.h"

struct render_t
{
    int init;
    int width;
    int height;
    int frame_tag;
    int draw_scene;
    SDL_Surface *screen;
    struct vector_t *clear_color;
    struct matrix_t *camera;
    struct matrix_t *proj;
    struct timer_t *timer;
    float last_update_time;
    float last_draw_time;
};

static struct render_t g_render;

static int api_render_clear_color(lua_State *lua)
{
    struct vector_t *vector;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_clear_color: incorrect argument");
        lua_error(lua);
        return 0;
    }

    vector = vector_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (vector == 0)
    {
        lua_pushstring(lua, "api_render_clear_color: invalid vector");
        lua_error(lua);
        return 0;
    }

    g_render.clear_color = vector;
    return 0;
}

static int api_render_camera(lua_State *lua)
{
    struct matrix_t *matrix;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_camera: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_render_camera: invalid matrix");
        lua_error(lua);
        return 0;
    }

    g_render.camera = matrix;
    return 0;
}

static int api_render_proj(lua_State *lua)
{
    struct matrix_t *matrix;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_proj: incorrect argument");
        lua_error(lua);
        return 0;
    }

    matrix = matrix_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (matrix == 0)
    {
        lua_pushstring(lua, "api_render_proj: invalid matrix");
        lua_error(lua);
        return 0;
    }

    g_render.proj = matrix;
    return 0;
}

static int api_render_draw_scene(lua_State *lua)
{
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_render_draw_scene: incorrect argument");
        lua_error(lua);
        return 0;
    }

    g_render.draw_scene = lua_tointeger(lua, 1);
    lua_pop(lua, 1);
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
    g_render.draw_scene = 1;

    glShadeModel(GL_SMOOTH);
    glCullFace(GL_BACK);
    glFrontFace(GL_CCW);
    glEnable(GL_CULL_FACE);
    glEnable(GL_DEPTH_TEST);
    glViewport(0, 0, width, height);

    lua_register(lua, "api_render_clear_color", api_render_clear_color);
    lua_register(lua, "api_render_camera", api_render_camera);
    lua_register(lua, "api_render_proj", api_render_proj);
    lua_register(lua, "api_render_draw_scene", api_render_draw_scene);
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

static void render_draw_meshes(void)
{
    struct vbuf_t *vbuf;
    struct ibuf_t *ibuf;
    struct mesh_t *mesh_vbuf;
    struct mesh_t *mesh_ibuf;
    if (g_vbufs.with_meshes < g_ibufs.with_meshes)
    {
        for (vbuf = g_vbufs.baked; vbuf; vbuf = vbuf->next)
        {
            if (vbuf->meshes == 0)
                continue;
            vbuf_select(vbuf);
            for (mesh_vbuf = vbuf->meshes; mesh_vbuf; mesh_vbuf = mesh_vbuf->vbuf_next)
            {
                if (mesh_vbuf->frame_tag == g_render.frame_tag)
                    continue;
                ibuf = mesh_vbuf->ibuf;
                if (ibuf->mapped)
                    continue;
                ibuf_select(ibuf);
                for (mesh_ibuf = ibuf->meshes; mesh_ibuf; mesh_ibuf = mesh_ibuf->ibuf_next)
                {
                    if (mesh_ibuf->frame_tag == g_render.frame_tag)
                        continue;
                    mesh_ibuf->frame_tag = g_render.frame_tag;
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
            for (mesh_ibuf = ibuf->meshes; mesh_ibuf; mesh_ibuf = mesh_ibuf->ibuf_next)
            {
                if (mesh_ibuf->frame_tag == g_render.frame_tag)
                    continue;
                vbuf = mesh_ibuf->vbuf;
                if (vbuf->mapped)
                    continue;
                vbuf_select(vbuf);
                for (mesh_vbuf = vbuf->meshes; mesh_vbuf; mesh_vbuf = mesh_vbuf->vbuf_next)
                {
                    if (mesh_vbuf->frame_tag == g_render.frame_tag)
                        continue;
                    mesh_vbuf->frame_tag = g_render.frame_tag;
                    mesh_draw(mesh_vbuf);
                }
            }
        }
    }
}

static void render_update_meshes(float dt)
{
    struct vbuf_t *vbuf;
    struct mesh_t *mesh_vbuf;
    for (vbuf = g_vbufs.baked; vbuf; vbuf = vbuf->next)
    {
        for (mesh_vbuf = vbuf->meshes; mesh_vbuf; mesh_vbuf = mesh_vbuf->vbuf_next)
        {
            if (mesh_vbuf->ibuf->mapped)
                continue;
            matrix_update(mesh_vbuf->matrix, dt, g_render.frame_tag, 0);
        }
    }
}

void render_update(float dt)
{
    timer_reset(g_render.timer);

    ++g_render.frame_tag;
    if (g_render.clear_color)
        vector_update(g_render.clear_color, dt, g_render.frame_tag, 0);
    if (g_render.camera)
        matrix_update(g_render.camera, dt, g_render.frame_tag, 0);
    if (g_render.proj)
        matrix_update(g_render.proj, dt, g_render.frame_tag, 0);
    render_update_meshes(dt);

    g_render.last_update_time = timer_passed(g_render.timer);
}

void render_draw(void)
{
    GLfloat *color;

    timer_reset(g_render.timer);

    /* clear */

    if (g_render.draw_scene && g_render.clear_color)
    {
        color = g_render.clear_color->value;
        glClearColor(color[0], color[1], color[2], color[3]);
    }
    else
        glClearColor(0, 0, 0, 1);

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    /* frustum */

    glMatrixMode(GL_PROJECTION);
    if (g_render.proj)
        glLoadMatrixf(g_render.proj->value);
    else
        glLoadIdentity();

    /* meshes */

    glMatrixMode(GL_MODELVIEW);
    if (g_render.camera)
        glLoadMatrixf(g_render.camera->value);
    else
        glLoadIdentity();

    if (g_render.draw_scene)
        render_draw_meshes();

    /* debug draw */

    physics_ddraw();

    /* text */

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, g_render.width, g_render.height, 0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    text_draw();

    /* show */

    SDL_GL_SwapBuffers();

    g_render.last_draw_time = timer_passed(g_render.timer);
}
