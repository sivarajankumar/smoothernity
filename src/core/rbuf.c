#include "rbuf.h"
#include "vao.h"
#include "../util/util.h"
#include "../thread/thread.h"
#include <stdio.h>
#include <string.h>

static const size_t RBUF_SIZE = 32;

struct rbufs_t
{
    int count;
    char *pool;
    struct thread_mutex_t *mutex;
};

struct rbufs_t g_rbufs;

static int safe_bind_buf(struct rbuf_t *rbuf)
{
    /*
     * If there's a VAO currently bound, we can mess up its state by calling
     * glBindBuffer with target GL_ARRAY_BUFFER or GL_ELEMENT_ARRAY_BUFFER.
     * So, to be on a safe side, it's better to ensure that no VAO is bound.
     */
    if (rbuf->target == GL_ARRAY_BUFFER
    || rbuf->target == GL_ELEMENT_ARRAY_BUFFER)
    {
        if (vao_bound())
            return 1;
    }
    glBindBuffer(rbuf->target, rbuf->buf_id);
    return 0;
}

static int api_rbuf_map(lua_State *lua)
{
    struct rbuf_t *rbuf;
    int ofs, len;
    GLintptr glofs;
    GLsizeiptr gllen;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_rbuf_map: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (rbuf == 0 || rbuf->buf_id == 0 || rbuf->mapped != 0)
    {
        lua_pushstring(lua, "api_rbuf_map: invalid rbuf");
        lua_error(lua);
        return 0;
    }
    if (len <= 0 || ofs < 0 || ofs > rbuf->size - len)
    {
        lua_pushstring(lua, "api_rbuf_map: invalid range");
        lua_error(lua);
        return 0;
    }

    thread_mutex_lock(g_rbufs.mutex);
    rbuf->mapped_ofs = ofs;
    rbuf->mapped_len = len;
    if (safe_bind_buf(rbuf) != 0)
    {
        lua_pushstring(lua, "api_rbuf_map: cannot bind buffer");
        lua_error(lua);
        return 0;
    }
    if (rbuf->item == GL_FLOAT)
    {
        glofs = (GLintptr)sizeof(GLfloat) * (GLintptr)rbuf->mapped_ofs;
        gllen = (GLsizeiptr)sizeof(GLfloat) * (GLsizeiptr)rbuf->mapped_len;
    }
    else /* rbuf->item == GL_INT */
    {
        glofs = (GLintptr)sizeof(GLint) * (GLintptr)rbuf->mapped_ofs;
        gllen = (GLsizeiptr)sizeof(GLint) * (GLsizeiptr)rbuf->mapped_len;
    }
    rbuf->mapped = glMapBufferRange(rbuf->target, glofs, gllen,
        GL_MAP_WRITE_BIT | GL_MAP_UNSYNCHRONIZED_BIT |
        GL_MAP_INVALIDATE_RANGE_BIT);
    if (rbuf->mapped == 0)
    {
        lua_pushstring(lua, "api_rbuf_map: cannot map buffer");
        lua_error(lua);
        return 0;
    }
    thread_mutex_unlock(g_rbufs.mutex);
    return 0;
}

static int api_rbuf_unmap(lua_State *lua)
{
    struct rbuf_t *rbuf;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_rbuf_unmap: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (rbuf == 0 || rbuf->buf_id == 0 || rbuf->mapped == 0)
    {
        lua_pushstring(lua, "api_rbuf_unmap: invalid rbuf");
        lua_error(lua);
        return 0;
    }

    thread_mutex_lock(g_rbufs.mutex);
    rbuf->mapped = 0;
    rbuf->mapped_ofs = 0;
    rbuf->mapped_len = 0;
    if (safe_bind_buf(rbuf) != 0)
    {
        lua_pushstring(lua, "api_rbuf_unmap: cannot bind buffer");
        lua_error(lua);
        return 0;
    }
    glUnmapBuffer(rbuf->target);
    thread_mutex_unlock(g_rbufs.mutex);
    return 0;
}

static int api_rbuf_set(lua_State *lua)
{
    struct rbuf_t *rbuf;
    int ofs, len, i, index;

    if (lua_gettop(lua) < 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_rbuf_set: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    ofs = lua_tointeger(lua, 2);
    len = lua_gettop(lua) - 2;

    thread_mutex_lock(g_rbufs.mutex);
    if (rbuf == 0 || rbuf->buf_id == 0 || rbuf->mapped == 0)
    {
        thread_mutex_unlock(g_rbufs.mutex);
        lua_pushstring(lua, "api_rbuf_set: invalid rbuf");
        lua_error(lua);
        return 0;
    }

    if (ofs < rbuf->mapped_ofs || ofs > rbuf->mapped_ofs + rbuf->mapped_len - len)
    {
        thread_mutex_unlock(g_rbufs.mutex);
        lua_pushstring(lua, "api_rbuf_set: data out of range");
        lua_error(lua);
        return 0;
    }

    for (i = 0; i < len; ++i)
    {
        if (!lua_isnumber(lua, 3 + i))
        {
            thread_mutex_unlock(g_rbufs.mutex);
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

    thread_mutex_unlock(g_rbufs.mutex);
    lua_pop(lua, lua_gettop(lua));
    return 0;
}

static int api_rbuf_alloc(lua_State *lua)
{
    struct rbuf_t *rbuf;
    int size, target, item, usage;
    GLsizeiptr glsize;

    if (lua_gettop(lua) != 5 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5))
    {
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

    if (rbuf == 0 || rbuf->buf_id != 0)
    {
        lua_pushstring(lua, "api_rbuf_alloc: invalid rbuf");
        lua_error(lua);
        return 0;
    }
    if (size <= 0)
    {
        lua_pushstring(lua, "api_rbuf_alloc: invalid size");
        lua_error(lua);
        return 0;
    }
    if (target != GL_ARRAY_BUFFER
    && target != GL_ELEMENT_ARRAY_BUFFER
    && target != GL_PIXEL_UNPACK_BUFFER)
    {
        lua_pushstring(lua, "api_rbuf_alloc: invalid target");
        lua_error(lua);
        return 0;
    }
    if (item != GL_FLOAT && item != GL_INT)
    {
        lua_pushstring(lua, "api_rbuf_alloc: invalid item");
        lua_error(lua);
        return 0;
    }
    if (usage != GL_STREAM_DRAW && usage != GL_STREAM_COPY
    && usage != GL_STATIC_DRAW && usage != GL_STATIC_COPY
    && usage != GL_DYNAMIC_DRAW && usage != GL_DYNAMIC_COPY)
    {
        lua_pushstring(lua, "api_rbuf_alloc: invalid usage");
        lua_error(lua);
        return 0;
    }

    thread_mutex_lock(g_rbufs.mutex);
    rbuf->size = size;
    rbuf->target = (GLenum)target;
    rbuf->item = (GLenum)item;
    glGenBuffers(1, &rbuf->buf_id);
    if (safe_bind_buf(rbuf) != 0)
    {
        lua_pushstring(lua, "api_rbuf_alloc: cannot bind buffer");
        lua_error(lua);
        return 0;
    }
    if (rbuf->item == GL_FLOAT)
        glsize = (GLsizeiptr)sizeof(GLfloat) * (GLsizeiptr)size;
    else /* rbuf->item == GL_INT */
        glsize = (GLsizeiptr)sizeof(GLint) * (GLsizeiptr)size;
    glBufferData(rbuf->target, glsize, 0, (GLenum)usage);
    if (glGetError() != GL_NO_ERROR)
    {
        lua_pushstring(lua, "api_rbuf_alloc: cannot alloc buffer data");
        lua_error(lua);
        return 0;
    }
    thread_mutex_unlock(g_rbufs.mutex);
    return 0;
}

static int api_rbuf_free(lua_State *lua)
{
    struct rbuf_t *rbuf;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_rbuf_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    rbuf = rbuf_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (rbuf == 0 || rbuf->buf_id == 0 || rbuf->mapped != 0)
    {
        lua_pushstring(lua, "api_rbuf_free: invalid rbuf");
        lua_error(lua);
        return 0;
    }

    thread_mutex_lock(g_rbufs.mutex);
    glDeleteBuffers(1, &rbuf->buf_id);
    rbuf->buf_id = 0;
    thread_mutex_unlock(g_rbufs.mutex);
    return 0;
}

void rbuf_reg_thread(lua_State *lua)
{
    lua_register(lua, "api_rbuf_set", api_rbuf_set);
}

int rbuf_init(lua_State *lua, int count)
{
    if (sizeof(struct rbuf_t) > RBUF_SIZE)
    {
        fprintf(stderr, "Invalid sizes:\nsizeof(struct rbuf_t) == %i\n",
                (int)sizeof(struct rbuf_t));
        return 1;
    }
    g_rbufs.pool = util_malloc(RBUF_SIZE, RBUF_SIZE * count);
    if (g_rbufs.pool == 0)
        return 1;
    memset(g_rbufs.pool, 0, RBUF_SIZE * count);
    g_rbufs.count = count;
    g_rbufs.mutex = thread_mutex_create();
    if (g_rbufs.mutex == 0)
        goto cleanup;

    lua_register(lua, "api_rbuf_alloc", api_rbuf_alloc);
    lua_register(lua, "api_rbuf_free", api_rbuf_free);
    lua_register(lua, "api_rbuf_map", api_rbuf_map);
    lua_register(lua, "api_rbuf_unmap", api_rbuf_unmap);
    lua_register(lua, "api_rbuf_set", api_rbuf_set);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, y);

    LUA_PUBLISH(GL_FLOAT, "API_RBUF_FLOAT");
    LUA_PUBLISH(GL_INT, "API_RBUF_INT");

    LUA_PUBLISH(GL_ARRAY_BUFFER, "API_RBUF_ARRAY");
    LUA_PUBLISH(GL_ELEMENT_ARRAY_BUFFER, "API_RBUF_ELEMENT_ARRAY");
    LUA_PUBLISH(GL_PIXEL_UNPACK_BUFFER, "API_RBUF_PIXEL_UNPACK");

    LUA_PUBLISH(GL_STREAM_DRAW, "API_RBUF_STREAM_DRAW");
    LUA_PUBLISH(GL_STREAM_COPY, "API_RBUF_STREAM_COPY");
    LUA_PUBLISH(GL_STATIC_DRAW, "API_RBUF_STATIC_DRAW");
    LUA_PUBLISH(GL_STATIC_COPY, "API_RBUF_STATIC_COPY");
    LUA_PUBLISH(GL_DYNAMIC_DRAW, "API_RBUF_DYNAMIC_DRAW");
    LUA_PUBLISH(GL_DYNAMIC_COPY, "API_RBUF_DYNAMIC_COPY");
    return 0;
cleanup:
    util_free(g_rbufs.pool);
    g_rbufs.pool = 0;
    return 1;
}

void rbuf_done(void)
{
    int i;
    if (g_rbufs.pool == 0)
        return;
    for (i = 0; i < g_rbufs.count; ++i)
    {
        if (rbuf_get(i)->buf_id != 0)
        {
            fprintf(stderr, "rbuf_done: some buffers are still active\n");
            break;
        }
    }
    util_free(g_rbufs.pool);
    g_rbufs.pool = 0;
    if (g_rbufs.mutex)
        thread_mutex_destroy(g_rbufs.mutex);
}

struct rbuf_t * rbuf_get(int rbufi)
{
    if (rbufi >= 0 && rbufi < g_rbufs.count)
        return (struct rbuf_t*)(g_rbufs.pool + RBUF_SIZE * rbufi);
    else
        return 0;
}

