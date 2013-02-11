#include "shprog.h"
#include "../util/util.h"
#include <string.h>
#include <stdio.h>

static const size_t SHPROG_SIZE = 32;
#define LOG_SIZE 1024

struct shprogs_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct shprog_t *vacant;
};

static struct shprogs_t g_shprogs;

struct shprog_t * shprog_get(int ishprog)
{
    if (ishprog >= 0 && ishprog < g_shprogs.count)
        return (struct shprog_t*)(g_shprogs.pool + SHPROG_SIZE * ishprog);
    else
        return 0;
}

static int api_shprog_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_shprog_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_shprogs.left);
    return 1;
}

static int api_shprog_alloc(lua_State *lua)
{
    struct shprog_t *shprog;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_shprog_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (g_shprogs.vacant == 0)
    {
        lua_pushstring(lua, "api_shprog_alloc: out of shprogs");
        lua_error(lua);
        return 0;
    }

    ++g_shprogs.allocs;
    --g_shprogs.left;
    if (g_shprogs.left < g_shprogs.left_min)
        g_shprogs.left_min = g_shprogs.left;

    shprog = g_shprogs.vacant;
    g_shprogs.vacant = g_shprogs.vacant->next;
    shprog->next = 0;
    shprog->state = SHPROG_CREATED;
    shprog->prog_id = glCreateProgram();

    lua_pushinteger(lua, ((char*)shprog - g_shprogs.pool) / SHPROG_SIZE);
    return 1;
}

static int api_shprog_free(lua_State *lua)
{
    struct shprog_t *shprog;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_shprog_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    shprog = shprog_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (shprog == 0 || shprog->state == SHPROG_VACANT)
    {
        lua_pushstring(lua, "api_shprog_free: invalid shprog");
        lua_error(lua);
        return 0;
    }

    ++g_shprogs.frees;
    ++g_shprogs.left;

    shprog->state = SHPROG_VACANT;
    shprog->next = g_shprogs.vacant;
    g_shprogs.vacant = shprog;

    glDeleteProgram(shprog->prog_id);

    return 0;
}

static int api_shprog_attach(lua_State *lua)
{
    static char log[LOG_SIZE];
    struct shprog_t *shprog;
    int type;
    size_t data_len;
    const char *data;
    GLuint shader;
    GLint gldata_len, res, log_len;
    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isstring(lua, 3))
    {
        lua_pushstring(lua, "api_shprog_attach: incorrect argument");
        lua_error(lua);
        return 0;
    }
    shprog = shprog_get(lua_tointeger(lua, 1));
    type = lua_tointeger(lua, 2);
    data = lua_tolstring(lua, 3, &data_len);
    lua_pop(lua, 3);
    if (shprog == 0 || shprog->state != SHPROG_CREATED)
    {
        lua_pushstring(lua, "api_shprog_attach: invalid shprog");
        lua_error(lua);
        return 0;
    }
    if (type != (int)GL_VERTEX_SHADER && type != (int)GL_FRAGMENT_SHADER)
    {
        lua_pushstring(lua, "api_shprog_attach: invalid type");
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
            fprintf(stderr, "Log size is to small: %i\n", (int)log_len);
        else
        {
            glGetShaderInfoLog(shader, log_len, &res, log);
            fprintf(stderr, "Log:\n%s\n", log);
        }
        glDeleteShader(shader);
        lua_pushstring(lua, "api_shprog_attach: compile error");
        lua_error(lua);
        return 0;
    }
    glAttachShader(shprog->prog_id, shader);
    glDeleteShader(shader);
    return 0;
}

static int api_shprog_link(lua_State *lua)
{
    static char log[LOG_SIZE];
    GLint res, len;
    struct shprog_t *shprog;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_shprog_link: incorrect argument");
        lua_error(lua);
        return 0;
    }
    shprog = shprog_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (shprog == 0 || shprog->state != SHPROG_CREATED)
    {
        lua_pushstring(lua, "api_shprog_link: invalid shprog");
        lua_error(lua);
        return 0;
    }

    glLinkProgram(shprog->prog_id);
    glGetProgramiv(shprog->prog_id, GL_LINK_STATUS, &res);
    if (res == GL_FALSE)
    {
        glGetProgramiv(shprog->prog_id, GL_INFO_LOG_LENGTH, &len);
        if (len >= LOG_SIZE)
            fprintf(stderr, "Log size is too small: %i\n", (int)len);
        else
        {
            glGetProgramInfoLog(shprog->prog_id, len, &res, log);
            fprintf(stderr, "Log:\n%s\n", log);
        }
        lua_pushstring(lua, "api_shprog_link: link error");
        lua_error(lua);
        return 0;
    }

    shprog->state = SHPROG_LINKED;
    return 0;
}

int shprog_init(lua_State *lua, int count)
{
    int i;
    struct shprog_t *shprog;
    if (sizeof(struct shprog_t) > SHPROG_SIZE)
    {
        fprintf(stderr, "Invalid size:\nsizeof(struct shprog_t) == %i\n",
                (int)sizeof(struct shprog_t));
        return 1;
    }
    g_shprogs.pool = util_malloc(SHPROG_SIZE, SHPROG_SIZE * count);
    if (g_shprogs.pool == 0)
        return 1;
    memset(g_shprogs.pool, 0, SHPROG_SIZE * count);
    g_shprogs.count = count;
    g_shprogs.left = count;
    g_shprogs.left_min = count;
    g_shprogs.vacant = shprog_get(0);
    for (i = 0; i < count; ++i)
    {
        shprog = shprog_get(i);
        shprog->next = shprog_get(i + 1);
        shprog->state = SHPROG_VACANT;
    }
    lua_register(lua, "api_shprog_left", api_shprog_left);
    lua_register(lua, "api_shprog_alloc", api_shprog_alloc);
    lua_register(lua, "api_shprog_free", api_shprog_free);
    lua_register(lua, "api_shprog_attach", api_shprog_attach); 
    lua_register(lua, "api_shprog_link", api_shprog_link);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, y);

    LUA_PUBLISH(GL_VERTEX_SHADER, "API_SHPROG_VERTEX");
    LUA_PUBLISH(GL_FRAGMENT_SHADER, "API_SHPROG_FRAGMENT");

    return 0;
}

void shprog_done(void)
{
    if (g_shprogs.pool == 0)
        return;
    printf("Shader programs usage: %i/%i, allocs/frees: %i/%i\n",
           g_shprogs.count - g_shprogs.left_min, g_shprogs.count,
           g_shprogs.allocs, g_shprogs.frees);
    util_free(g_shprogs.pool);
    g_shprogs.pool = 0;
}

void shprog_select(struct shprog_t *shprog)
{
    if (shprog->state == SHPROG_LINKED)
        glUseProgram(shprog->prog_id);
}
