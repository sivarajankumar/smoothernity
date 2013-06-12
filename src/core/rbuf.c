#include "rbuf.h"
#include "vao.h"
#include "util.h"
#include "../platform/mem.h"
#include <stdio.h>

#define RBUF_SIZE 32

struct rbufs_t {
    int count;
    char *pool;
};

_Static_assert(sizeof(struct rbuf_t) <= RBUF_SIZE, "Invalid rbuf_t size");

struct rbufs_t g_rbufs;

static int safe_bind_buf(struct rbuf_t *rbuf) {
    /*
     * If there's a VAO currently bound, we can mess up its state by calling
     * glBindBuffer with target GL_ARRAY_BUFFER or GL_ELEMENT_ARRAY_BUFFER.
     * So, to be on a safe side, it's better to ensure that no VAO is bound.
     */
    if (rbuf->target == GL_ARRAY_BUFFER ||
    rbuf->target == GL_ELEMENT_ARRAY_BUFFER)
        if (vao_bound())
            return 1;
    glBindBuffer(rbuf->target, rbuf->buf_id);
    return 0;
}

static int api_rbuf_map(lua_State *lua) {
    struct rbuf_t *rbuf;
    int ofs, len;
    GLintptr glofs;
    GLsizeiptr gllen;

    if (lua_gettop(lua) != 3 || !util_isint(lua, 1) ||
    !util_isint(lua, 2) || !util_isint(lua, 3)) {
        lua_pushstring(lua, "api_rbuf_map: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (!rbuf || !rbuf->buf_id || rbuf->mapped) {
        lua_pushstring(lua, "api_rbuf_map: invalid rbuf");
        lua_error(lua);
        return 0;
    }
    if (len <= 0 || ofs < 0 || ofs > rbuf->size - len) {
        lua_pushstring(lua, "api_rbuf_map: invalid range");
        lua_error(lua);
        return 0;
    }
    rbuf->mapped_ofs = ofs;
    rbuf->mapped_len = len;
    if (safe_bind_buf(rbuf)) {
        lua_pushstring(lua, "api_rbuf_map: cannot bind buffer");
        lua_error(lua);
        return 0;
    }
    if (rbuf->item == GL_FLOAT) {
        glofs = (GLintptr)sizeof(GLfloat) * (GLintptr)rbuf->mapped_ofs;
        gllen = (GLsizeiptr)sizeof(GLfloat) * (GLsizeiptr)rbuf->mapped_len;
    }
    else /* rbuf->item == GL_INT */ {
        glofs = (GLintptr)sizeof(GLint) * (GLintptr)rbuf->mapped_ofs;
        gllen = (GLsizeiptr)sizeof(GLint) * (GLsizeiptr)rbuf->mapped_len;
    }
    rbuf->mapped = glMapBufferRange(rbuf->target, glofs, gllen,
        GL_MAP_WRITE_BIT | GL_MAP_UNSYNCHRONIZED_BIT |
        GL_MAP_INVALIDATE_RANGE_BIT);
    if (!rbuf->mapped) {
        lua_pushstring(lua, "api_rbuf_map: cannot map buffer");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_rbuf_unmap(lua_State *lua) {
    struct rbuf_t *rbuf;

    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_rbuf_unmap: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (!rbuf || !rbuf->buf_id || !rbuf->mapped) {
        lua_pushstring(lua, "api_rbuf_unmap: invalid rbuf");
        lua_error(lua);
        return 0;
    }
    rbuf->mapped = 0;
    rbuf->mapped_ofs = 0;
    rbuf->mapped_len = 0;
    if (safe_bind_buf(rbuf)) {
        lua_pushstring(lua, "api_rbuf_unmap: cannot bind buffer");
        lua_error(lua);
        return 0;
    }
    glUnmapBuffer(rbuf->target);
    return 0;
}

static int api_rbuf_set(lua_State *lua) {
    struct rbuf_t *rbuf;
    int ofs, len, index;

    if (lua_gettop(lua) < 3 || !util_isint(lua, 1) || !util_isint(lua, 2)) {
        lua_pushstring(lua, "api_rbuf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = lua_gettop(lua) - 2;

    if (!rbuf || !rbuf->buf_id || !rbuf->mapped) {
        lua_pushstring(lua, "api_rbuf_set: invalid rbuf");
        lua_error(lua);
        return 0;
    }
    if (ofs < rbuf->mapped_ofs ||
    ofs > rbuf->mapped_ofs + rbuf->mapped_len - len) {
        lua_pushstring(lua, "api_rbuf_set: data out of range");
        lua_error(lua);
        return 0;
    }
    for (int i = 0; i < len; ++i) {
        if ((rbuf->item == GL_FLOAT && !util_isfloat(lua, 3 + i)) ||
        (/* rbuf->item == GL_INT && */ !util_isint(lua, 3 + i))) {
            lua_pushstring(lua, "api_rbuf_set: incorrect data type");
            lua_error(lua);
            return 0;
        }
        index = ofs - rbuf->mapped_ofs + i;
        if (rbuf->item == GL_FLOAT)
            ((GLfloat*)rbuf->mapped)[index] = (GLfloat)lua_tonumber(lua, 3 + i);
        else /* rbuf->item == GL_INT */
            ((GLint*)rbuf->mapped)[index] = (GLint)lua_tointeger(lua, 3 + i);
    }
    lua_pop(lua, lua_gettop(lua));
    return 0;
}

static int api_rbuf_alloc(lua_State *lua) {
    struct rbuf_t *rbuf;
    int size, target, item, usage;
    GLsizeiptr glsize;

    if (lua_gettop(lua) != 5 || !util_isint(lua, 1) || !util_isint(lua, 2) ||
    !util_isint(lua, 3) || !util_isint(lua, 4) || !util_isint(lua, 5)) {
        lua_pushstring(lua, "api_rbuf_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    size = lua_tointeger(lua, 2);
    target = lua_tointeger(lua, 3);
    item = lua_tointeger(lua, 4);
    usage = lua_tointeger(lua, 5);
    lua_pop(lua, 5);

    if (!rbuf || rbuf->buf_id) {
        lua_pushstring(lua, "api_rbuf_alloc: invalid rbuf");
        lua_error(lua);
        return 0;
    }
    if (size <= 0) {
        lua_pushstring(lua, "api_rbuf_alloc: invalid size");
        lua_error(lua);
        return 0;
    }
    if (target != GL_ARRAY_BUFFER && target != GL_ELEMENT_ARRAY_BUFFER &&
    target != GL_PIXEL_UNPACK_BUFFER) {
        lua_pushstring(lua, "api_rbuf_alloc: invalid target");
        lua_error(lua);
        return 0;
    }
    if (item != GL_FLOAT && item != GL_INT) {
        lua_pushstring(lua, "api_rbuf_alloc: invalid item");
        lua_error(lua);
        return 0;
    }
    if (usage != GL_STREAM_DRAW && usage != GL_STREAM_COPY &&
    usage != GL_STATIC_DRAW && usage != GL_STATIC_COPY &&
    usage != GL_DYNAMIC_DRAW && usage != GL_DYNAMIC_COPY) {
        lua_pushstring(lua, "api_rbuf_alloc: invalid usage");
        lua_error(lua);
        return 0;
    }
    rbuf->size = size;
    rbuf->target = (GLenum)target;
    rbuf->item = (GLenum)item;
    rbuf->mapped = 0;
    glGenBuffers(1, &rbuf->buf_id);
    if (safe_bind_buf(rbuf)) {
        lua_pushstring(lua, "api_rbuf_alloc: cannot bind buffer");
        lua_error(lua);
        return 0;
    }
    if (rbuf->item == GL_FLOAT)
        glsize = (GLsizeiptr)sizeof(GLfloat) * (GLsizeiptr)size;
    else /* rbuf->item == GL_INT */
        glsize = (GLsizeiptr)sizeof(GLint) * (GLsizeiptr)size;
    glBufferData(rbuf->target, glsize, 0, (GLenum)usage);
    if (glGetError() != GL_NO_ERROR) {
        lua_pushstring(lua, "api_rbuf_alloc: cannot alloc buffer data");
        lua_error(lua);
        return 0;
    }
    return 0;
}

static int api_rbuf_free(lua_State *lua) {
    struct rbuf_t *rbuf;

    if (lua_gettop(lua) != 1 || !util_isint(lua, 1)) {
        lua_pushstring(lua, "api_rbuf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (!rbuf || !rbuf->buf_id || rbuf->mapped) {
        lua_pushstring(lua, "api_rbuf_free: invalid rbuf");
        lua_error(lua);
        return 0;
    }
    glDeleteBuffers(1, &rbuf->buf_id);
    rbuf->buf_id = 0;
    return 0;
}

void rbuf_reg_thread(lua_State *lua) {
    lua_register(lua, "api_rbuf_set", api_rbuf_set);
}

int rbuf_init(lua_State *lua, int count) {
    struct rbuf_t *rbuf;

    g_rbufs.count = count;
    g_rbufs.pool = mem_alloc(MEM_ALIGNOF(struct rbuf_t), RBUF_SIZE * count);
    if (!g_rbufs.pool)
        return 1;
    for (int i = 0; i < count; ++i) {
        rbuf = rbuf_get(i);
        rbuf->buf_id = 0;
    }
    #define REGF(x) lua_register(lua, #x, x)
    REGF(api_rbuf_alloc);
    REGF(api_rbuf_free);
    REGF(api_rbuf_map);
    REGF(api_rbuf_unmap);
    REGF(api_rbuf_set);
    #undef REGF
    #define REGN(x) lua_pushinteger(lua, GL_##x); \
                    lua_setglobal(lua, "API_RBUF_"#x);
    REGN(FLOAT);
    REGN(INT);
    REGN(ARRAY_BUFFER);
    REGN(ELEMENT_ARRAY_BUFFER);
    REGN(PIXEL_UNPACK_BUFFER);
    REGN(STREAM_DRAW);
    REGN(STREAM_COPY);
    REGN(STATIC_DRAW);
    REGN(STATIC_COPY);
    REGN(DYNAMIC_DRAW);
    REGN(DYNAMIC_COPY);
    #undef REGN
    return 0;
}

void rbuf_done(void) {
    if (!g_rbufs.pool)
        return;
    for (int i = 0; i < g_rbufs.count; ++i)
        if (rbuf_get(i)->buf_id) {
            fprintf(stderr, "rbuf_done: some buffers are still active\n");
            break;
        }
    mem_free(g_rbufs.pool);
    g_rbufs.pool = 0;
}

struct rbuf_t * rbuf_get(int rbufi) {
    if (rbufi >= 0 && rbufi < g_rbufs.count)
        return (struct rbuf_t*)(g_rbufs.pool + RBUF_SIZE * rbufi);
    else
        return 0;
}

