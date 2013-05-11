#include "prog.h"
#include "../util/util.h"
#include <GL/glew.h>
#include <string.h>
#include <stdio.h>

#define LOG_SIZE 2048

static const size_t PROG_SIZE = 4;

struct prog_t
{
    GLuint prog_id;
};

struct progs_t
{
    int count;
    char *pool;
};

static struct progs_t g_progs;

static struct prog_t * prog_get(int iprog)
{
    if (iprog >= 0 && iprog < g_progs.count)
        return (struct prog_t*)(g_progs.pool + PROG_SIZE * iprog);
    else
        return 0;
}

static int api_prog_alloc(lua_State *lua)
{
    struct prog_t *prog;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_prog_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    prog = prog_get(lua_tointeger(lua, 1 ));
    lua_pop(lua, 1);
    if (prog == 0 || prog->prog_id != 0)
    {
        lua_pushstring(lua, "api_prog_alloc: invalid prog");
        lua_error(lua);
        return 0;
    }
    prog->prog_id = glCreateProgram();
    return 0;
}

static int api_prog_free(lua_State *lua)
{
    struct prog_t *prog;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_prog_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    prog = prog_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (prog == 0 || prog->prog_id == 0)
    {
        lua_pushstring(lua, "api_prog_free: invalid prog");
        lua_error(lua);
        return 0;
    }
    glDeleteProgram(prog->prog_id);
    prog->prog_id = 0;
    return 0;
}

static int api_prog_attach(lua_State *lua)
{
    static char log[LOG_SIZE];
    struct prog_t *prog;
    int type;
    size_t data_len;
    const char *data;
    GLuint shader;
    GLint gldata_len, res, log_len;
    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isstring(lua, 3))
    {
        lua_pushstring(lua, "api_prog_attach: incorrect argument");
        lua_error(lua);
        return 0;
    }
    prog = prog_get(lua_tointeger(lua, 1));
    type = lua_tointeger(lua, 2);
    data = lua_tolstring(lua, 3, &data_len);
    lua_pop(lua, 3);
    if (prog == 0 || prog->prog_id == 0)
    {
        lua_pushstring(lua, "api_prog_attach: invalid prog");
        lua_error(lua);
        return 0;
    }
    if (type != (int)GL_VERTEX_SHADER && type != (int)GL_FRAGMENT_SHADER)
    {
        lua_pushstring(lua, "api_prog_attach: invalid type");
        lua_error(lua);
        return 0;
    }
    glGetProgramiv(prog->prog_id, GL_LINK_STATUS, &res);
    if (res == GL_TRUE)
    {
        lua_pushstring(lua, "api_prog_attach: prog is linked");
        lua_error(lua);
        return 0;
    }
    shader = glCreateShader((GLenum)type);
    gldata_len = (GLint)data_len;
    glShaderSource(shader, 1, &data, &gldata_len);
    glCompileShader(shader);
    glGetShaderiv(shader, GL_COMPILE_STATUS, &res);
    if (res == GL_FALSE)
    {
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &log_len);
        if (log_len >= LOG_SIZE)
            fprintf(stderr, "Log size is too small: %i\n", (int)log_len);
        else
        {
            glGetShaderInfoLog(shader, log_len, &res, log);
            fprintf(stderr, "Log:\n%s\n", log);
        }
        glDeleteShader(shader);
        lua_pushstring(lua, "api_prog_attach: compile error");
        lua_error(lua);
        return 0;
    }
    glAttachShader(prog->prog_id, shader);
    glDeleteShader(shader);
    if (glGetError() != GL_NO_ERROR)
    {
        lua_pushstring(lua, "api_prog_attach: GL error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_prog_link(lua_State *lua)
{
    static char log[LOG_SIZE];
    GLint res, len;
    struct prog_t *prog;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_prog_link: incorrect argument");
        lua_error(lua);
        return 0;
    }
    prog = prog_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (prog == 0 || prog->prog_id == 0)
    {
        lua_pushstring(lua, "api_prog_link: invalid prog");
        lua_error(lua);
        return 0;
    }

    glLinkProgram(prog->prog_id);
    glGetProgramiv(prog->prog_id, GL_LINK_STATUS, &res);
    if (res == GL_FALSE)
    {
        glGetProgramiv(prog->prog_id, GL_INFO_LOG_LENGTH, &len);
        if (len >= LOG_SIZE)
            fprintf(stderr, "Log size is too small: %i\n", (int)len);
        else
        {
            glGetProgramInfoLog(prog->prog_id, len, &res, log);
            fprintf(stderr, "Log:\n%s\n", log);
        }
        lua_pushstring(lua, "api_prog_link: link error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_prog_use(lua_State *lua)
{
    struct prog_t *prog;
    GLint res;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_prog_use: incorrect argument");
        lua_error(lua);
        return 0;
    }
    prog = prog_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (prog == 0 || prog->prog_id == 0)
    {
        lua_pushstring(lua, "api_prog_use: invalid prog");
        lua_error(lua);
        return 0;
    }
    glGetProgramiv(prog->prog_id, GL_LINK_STATUS, &res);
    if (res == GL_FALSE)
    {
        lua_pushstring(lua, "api_prog_use: prog is not linked");
        lua_error(lua);
        return 0;
    }
    glUseProgram(prog->prog_id);
    return 0;
}

int prog_init(lua_State *lua, int count)
{
    if (sizeof(struct prog_t) > PROG_SIZE)
    {
        fprintf(stderr, "Invalid size:\nsizeof(struct prog_t) == %i\n",
                (int)sizeof(struct prog_t));
        return 1;
    }
    g_progs.pool = util_malloc(PROG_SIZE, PROG_SIZE * count);
    if (g_progs.pool == 0)
        return 1;
    memset(g_progs.pool, 0, PROG_SIZE * count);
    g_progs.count = count;

    lua_register(lua, "api_prog_alloc", api_prog_alloc);
    lua_register(lua, "api_prog_free", api_prog_free);
    lua_register(lua, "api_prog_attach", api_prog_attach); 
    lua_register(lua, "api_prog_link", api_prog_link);
    lua_register(lua, "api_prog_use", api_prog_use);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, y);

    LUA_PUBLISH(GL_VERTEX_SHADER, "API_PROG_VERTEX");
    LUA_PUBLISH(GL_FRAGMENT_SHADER, "API_PROG_FRAGMENT");

    return 0;
}

void prog_done(void)
{
    int i;
    if (g_progs.pool == 0)
        return;
    for (i = 0; i < g_progs.count; ++i)
    {
        if (prog_get(i)->prog_id != 0)
        {
            fprintf(stderr, "prog_done: some progs are still active\n");
            break;
        }
    }
    util_free(g_progs.pool);
    g_progs.pool = 0;
}
