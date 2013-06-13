#include "vao.h"
#include "cprog.h"
#include "rbuf.h"
#include "util.h"

struct vao_t {
    GLint vao_id;
};

int vao_bound(void) {
    GLint vao_id;
    glGetIntegerv(GL_VERTEX_ARRAY_BINDING, &vao_id);
    return !!vao_id;
}

static struct vao_t * vao_get(int ivao) {
    return 0; /* TODO */
}

static int api_vao_alloc(lua_State *lua) {
    /*
     * No VAO must be currently bound.
     * Every attribute is a 4D floating-point vector.
     * Attributes are stored in vertex buffer sequentially
     * in the same order as attribute names arguments.
     * First attribute is stored at the very beginning of the buffer.
     */
    struct vao_t *vao;
    struct cprog_t *prog;
    struct rbuf_t *vbuf, *ibuf;

    if (lua_gettop(lua) < 5 || !util_isint(lua, 1) ||
    !util_isint(lua, 2) || !util_isint(lua, 3) || !util_isint(lua, 4)) {
        lua_pushstring(lua, "api_vao_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    vao = vao_get(lua_tointeger(lua, 1));
    prog = cprog_get(lua_tointeger(lua, 2));
    vbuf = rbuf_get(lua_tointeger(lua, 3));
    ibuf = rbuf_get(lua_tointeger(lua, 4));

    if (!vao || vao->vao_id) {
        lua_pushstring(lua, "api_vao_alloc: invalid vao");
        lua_error(lua);
        return 0;
    }
    if (!prog || !prog->prog_id) {
        lua_pushstring(lua, "api_vao_alloc: invalid prog");
        lua_error(lua);
        return 0;
    }
    if (!vbuf || !vbuf->buf_id ||
    vbuf->target != GL_ARRAY_BUFFER || vbuf->item != GL_FLOAT) {
        lua_pushstring(lua, "api_vao_alloc: invalid vertex buffer");
        lua_error(lua);
        return 0;
    }
    if (!ibuf || !ibuf->buf_id ||
    ibuf->target != GL_ELEMENT_ARRAY_BUFFER || ibuf->item != GL_INT) {
        lua_pushstring(lua, "api_vao_alloc: invalid index buffer");
        lua_error(lua);
        return 0;
    }
    /*
     * If there's a VAO currently bound, we'll definitely mess up its state.
     * So, to be on a safe side, it's better to ensure that no VAO is bound.
     */
    if (vao_bound()) {
        lua_pushstring(lua, "api_vao_alloc: vao is currently bound");
        lua_error(lua);
        return 0;
    }
    for (int i = 5; i <= lua_gettop(lua); ++i) {
        if (!lua_isstring(lua, i)) {
            lua_pushstring(lua, "api_vao_alloc: incorrect attribute name");
            lua_error(lua);
            return 0;
        }
        /* TODO */
    }
    return 0;
}

static int api_vao_free(lua_State *lua) {
    /* TODO */
    return 0;
}

static int api_vao_use(lua_State *lua) {
    /* TODO */
    return 0;
}

int vao_init(lua_State *lua, int count) {
    lua_register(lua, "api_vao_alloc", api_vao_alloc);
    lua_register(lua, "api_vao_free", api_vao_free);
    lua_register(lua, "api_vao_use", api_vao_use);
    return 0;
}

void vao_done(void) {
}

