#include "query.h"
#include "../util/util.h"
#include <string.h>
#include <stdio.h>
#include <GL/glew.h>

static const size_t QUERY_SIZE = 32;

enum query_state_e
{
    QUERY_STATE_VACANT,
    QUERY_STATE_BEGIN,
    QUERY_STATE_WAITING,
    QUERY_STATE_READY
};

struct query_t
{
    GLuint query_id;
    enum query_state_e state;
    struct query_t *next;
};

struct queries_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    int inside;
    char *pool;
    struct query_t *vacant;
};

static struct queries_t g_queries;

static struct query_t * query_get(int queryi)
{
    if (queryi >= 0 && queryi < g_queries.count)
        return (struct query_t*)(g_queries.pool + QUERY_SIZE * queryi);
    else
        return 0;
}

static int api_query_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_query_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_queries.left);
    return 1;
}

static int query_alloc(void)
{
    struct query_t *query;
    if (g_queries.vacant == 0)
        return -1;
    ++g_queries.allocs;
    --g_queries.left;
    if (g_queries.left < g_queries.left_min)
        g_queries.left_min = g_queries.left;
    query = g_queries.vacant;
    g_queries.vacant = g_queries.vacant->next;
    query->next = 0;
    return ((char*)query - g_queries.pool) / QUERY_SIZE;
}

static int api_query_alloc_time(lua_State *lua)
{
    struct query_t *query;
    int iquery;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_query_alloc_time: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (g_queries.inside == 1)
    {
        lua_pushstring(lua, "api_query_alloc_time: recursive query opening");
        lua_error(lua);
        return 0;
    }
    iquery = query_alloc();
    query = query_get(iquery);
    if (query == 0)
    {
        lua_pushstring(lua, "api_query_alloc_time: out of queries");
        lua_error(lua);
        return 0;
    }
    query->state = QUERY_STATE_BEGIN;
    g_queries.inside = 1;
    glBeginQuery(GL_TIME_ELAPSED, query->query_id);
    lua_pushinteger(lua, iquery);
    return 1;
}

static int api_query_alloc_stamp(lua_State *lua)
{
    struct query_t *query;
    int iquery;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_query_alloc_stamp: incorrect argument");
        lua_error(lua);
        return 0;
    }
    iquery = query_alloc();
    query = query_get(iquery);
    if (query == 0)
    {
        lua_pushstring(lua, "api_query_alloc_stamp: out of queries");
        lua_error(lua);
        return 0;
    }
    query->state = QUERY_STATE_WAITING;
    glQueryCounter(GL_TIMESTAMP, query->query_id);
    lua_pushinteger(lua, iquery);
    return 1;
}

static int api_query_free(lua_State *lua)
{
    struct query_t *query;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_query_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    query = query_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (query == 0 || query->state != QUERY_STATE_READY)
    {
        lua_pushstring(lua, "api_query_free: invalid query");
        lua_error(lua);
        return 0;
    }
    ++g_queries.frees;
    ++g_queries.left;
    query->state = QUERY_STATE_VACANT;
    query->next = g_queries.vacant;
    g_queries.vacant = query;
    return 0;
}

static int api_query_end(lua_State *lua)
{
    struct query_t *query;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_query_end: incorrect argument");
        lua_error(lua);
        return 0;
    }
    query = query_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (query == 0 || query->state != QUERY_STATE_BEGIN)
    {
        lua_pushstring(lua, "api_query_end: invalid query");
        lua_error(lua);
        return 0;
    }
    query->state = QUERY_STATE_WAITING;
    g_queries.inside = 0;
    glEndQuery(GL_TIME_ELAPSED);
    return 0;
}

static int api_query_ready(lua_State *lua)
{
    GLint ready;
    struct query_t *query;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_query_ready: incorrect argument");
        lua_error(lua);
        return 0;
    }
    query = query_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (query == 0 || query->state == QUERY_STATE_VACANT)
    {
        lua_pushstring(lua, "api_query_ready: invalid query");
        lua_error(lua);
        return 0;
    }
    glGetQueryObjectiv(query->query_id, GL_QUERY_RESULT_AVAILABLE, &ready);
    if (ready == GL_TRUE)
        query->state = QUERY_STATE_READY;
    lua_pushinteger(lua, query->state == QUERY_STATE_READY);
    return 1;
}

static int api_query_result(lua_State *lua)
{
    GLuint64 result;
    struct query_t *query;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_query_ready: incorrect argument");
        lua_error(lua);
        return 0;
    }
    query = query_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (query == 0 || query->state != QUERY_STATE_READY)
    {
        lua_pushstring(lua, "api_query_ready: invalid query");
        lua_error(lua);
        return 0;
    }
    glGetQueryObjectui64v(query->query_id, GL_QUERY_RESULT, &result);
    lua_pushnumber(lua, result);
    return 1;
}

int query_init(lua_State *lua, int count)
{
    int i;
    struct query_t *query;
    if (sizeof(struct query_t) > QUERY_SIZE)
    {
        fprintf(stderr, "Invalid size:\nsizeof(struct query_t) == %i\n",
                (int)sizeof(struct query_t));
        return 1;
    }
    g_queries.pool = util_malloc(QUERY_SIZE, QUERY_SIZE * count);
    if (g_queries.pool == 0)
        return 1;
    memset(g_queries.pool, 0, QUERY_SIZE * count);
    g_queries.count = count;
    g_queries.left = count;
    g_queries.left_min = count;
    g_queries.vacant = query_get(0);
    for (i = 0; i < count; ++i)
    {
        query = query_get(i);
        query->next = query_get(i + 1);
        query->state = QUERY_STATE_VACANT;
        glGenQueries(1, &query->query_id);
    }
    lua_register(lua, "api_query_left", api_query_left);
    lua_register(lua, "api_query_alloc_time", api_query_alloc_time);
    lua_register(lua, "api_query_alloc_stamp", api_query_alloc_stamp);
    lua_register(lua, "api_query_free", api_query_free);
    lua_register(lua, "api_query_end", api_query_end);
    lua_register(lua, "api_query_ready", api_query_ready);
    lua_register(lua, "api_query_result", api_query_result);
    return 0;
}

void query_done(void)
{
    int i;
    if (g_queries.pool == 0)
        return;
    printf("Queries usage: %i/%i, allocs/frees: %i/%i\n",
           g_queries.count - g_queries.left_min, g_queries.count,
           g_queries.allocs, g_queries.frees);
    for (i = 0; i < g_queries.count; ++i)
        glDeleteQueries(1, &query_get(i)->query_id);
    util_free(g_queries.pool);
    g_queries.pool = 0;
}
