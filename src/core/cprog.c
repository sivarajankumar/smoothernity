#include "cprog.h"
#include "cutil.h"
#include "pmem.h"
#include "vlog.h"

#define CPROG_LOG_SIZE 2048

static const int CPROG_NONE = -1;

struct cprogs_t {
    int count;
    struct cprog_t *pool;
};

static struct cprogs_t g_cprogs;

struct cprog_t * cprog_get(int iprog) {
    if (iprog >= 0 && iprog < g_cprogs.count)
        return g_cprogs.pool + iprog;
    else
        return 0;
}

static int cprog_attach
(struct cprog_t *prog, GLenum type, size_t data_len, const char *data) {
    static char log[CPROG_LOG_SIZE];
    GLuint shader;
    GLint gldata_len, res, log_len;

    shader = glCreateShader(type);
    gldata_len = (GLint)data_len;
    glShaderSource(shader, 1, &data, &gldata_len);
    glCompileShader(shader);
    glGetShaderiv(shader, GL_COMPILE_STATUS, &res);
    if (res == GL_FALSE) {
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &log_len);
        if (log_len >= CPROG_LOG_SIZE)
            VLOG_ERROR("Log size is too small: %i", (int)log_len);
        else {
            glGetShaderInfoLog(shader, log_len, &res, log);
            VLOG_ERROR("Log:\n%s", log);
        }
        glDeleteShader(shader);
        return 1;
    }
    glAttachShader(prog->prog_id, shader);
    glDeleteShader(shader);
    if (glGetError() != GL_NO_ERROR)
        return 1;
    return 0;
}

static int api_prog_alloc(lua_State *lua) {
    /*
     * OpenGL ES 3.0 supports only 1 shader executable of each type.
     * For the sake of portability, enforce every program to contain
     * exactly 2 shaders: vertex and fragment.
     */
    struct cprog_t *prog;
    size_t vert_len, frag_len;
    const char *vert, *frag;
    static char log[CPROG_LOG_SIZE];
    GLint res, len;

    if (lua_gettop(lua) != 3 || !cutil_isint(lua, 1) ||
    !lua_isstring(lua, 2) || !lua_isstring(lua, 3)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    prog = cprog_get(lua_tointeger(lua, 1));
    vert = lua_tolstring(lua, 2, &vert_len);
    frag = lua_tolstring(lua, 3, &frag_len);
    lua_pop(lua, 3);

    if (!prog || prog->prog_id) {
        lua_pushstring(lua, "invalid prog");
        lua_error(lua);
        return 0;
    }
    prog->prog_id = glCreateProgram();
    if (cprog_attach(prog, GL_VERTEX_SHADER, vert_len, vert) ||
    cprog_attach(prog, GL_FRAGMENT_SHADER, frag_len, frag)) {
        lua_pushstring(lua, "cannot attach shaders");
        lua_error(lua);
        return 0;
    }
    glLinkProgram(prog->prog_id);
    glGetProgramiv(prog->prog_id, GL_LINK_STATUS, &res);
    if (res == GL_FALSE) {
        glGetProgramiv(prog->prog_id, GL_INFO_LOG_LENGTH, &len);
        if (len >= CPROG_LOG_SIZE)
            VLOG_ERROR("Log size is too small: %i", (int)len);
        else {
            glGetProgramInfoLog(prog->prog_id, len, &res, log);
            VLOG_ERROR("Log:\n%s", log);
        }
        lua_pushstring(lua, "link error");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_prog_free(lua_State *lua) {
    struct cprog_t *prog;
    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    prog = cprog_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (!prog || !prog->prog_id) {
        lua_pushstring(lua, "invalid prog");
        lua_error(lua);
        return 0;
    }
    glDeleteProgram(prog->prog_id);
    prog->prog_id = 0;
    return 0;
}

static int api_prog_use(lua_State *lua) {
    int iprog;
    struct cprog_t *prog;
    if (lua_gettop(lua) != 1 || !cutil_isint(lua, 1)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    iprog = lua_tointeger(lua, 1);
    lua_pop(lua, 1);
    if (iprog == CPROG_NONE)
        glUseProgram(0);
    else {
        prog = cprog_get(iprog);
        if (!prog || !prog->prog_id) {
            lua_pushstring(lua, "invalid prog");
            lua_error(lua);
            return 0;
        }
        glUseProgram(prog->prog_id);
    }
    return 0;
}

int cprog_init(lua_State *lua, int count) {
    g_cprogs.count = count;
    g_cprogs.pool = pmem_alloc(PMEM_ALIGNOF(struct cprog_t),
                               sizeof(struct cprog_t) * count);
    if (!g_cprogs.pool)
        return 1;
    for (int i = 0; i < count; ++i)
        cprog_get(i)->prog_id = 0;

    lua_register(lua, "api_prog_alloc", api_prog_alloc);
    lua_register(lua, "api_prog_free", api_prog_free);
    lua_register(lua, "api_prog_use", api_prog_use);

    lua_pushinteger(lua, CPROG_NONE);
    lua_setglobal(lua, "API_PROG_NONE");
    return 0;
}

void cprog_done(void) {
    if (!g_cprogs.pool)
        return;
    for (int i = 0; i < g_cprogs.count; ++i)
        if (cprog_get(i)->prog_id) {
            VLOG_ERROR("some progs are still active");
            break;
        }
    pmem_free(g_cprogs.pool);
    g_cprogs.pool = 0;
}

