#include "query.h"
#include "../util/util.h"
#include <string.h>
#include <stdio.h>
#include <GL/gl.h>

static const size_t QUERY_SIZE = 32;

struct query_t
{
    GLuint query_id;
    int vacant;
    struct query_t *next;
};

struct queries_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
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

static int api_query_alloc(lua_State *lua)
{
    struct query_t *query;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_query_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (g_queries.vacant == 0)
    {
        lua_pushstring(lua, "api_query_alloc: out of queries");
        lua_error(lua);
        return 0;
    }

    ++g_queries.allocs;
    --g_queries.left;
    if (g_queries.left < g_queries.left_min)
        g_queries.left_min = g_queries.left;

    query = g_queries.vacant;
    g_queries.vacant = g_queries.vacant->next;
    query->next = 0;
    query->vacant = 0;
    lua_pushinteger(lua, ((char*)query - g_queries.pool) / QUERY_SIZE);
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
    if (query == 0 || query->vacant == 1)
    {
        lua_pushstring(lua, "api_query_free: invalid query");
        lua_error(lua);
        return 0;
    }
    ++g_queries.frees;
    ++g_queries.left;
    query->vacant = 1;
    query->next = g_queries.vacant;
    g_queries.vacant = query;
    return 0;
}

static int api_query_ready(lua_State *lua)
{
    struct query_t *query;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_query_ready: incorrect argument");
        lua_error(lua);
        return 0;
    }
    query = query_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (query == 0 || query->vacant == 1)
    {
        lua_pushstring(lua, "api_query_ready: invalid query");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, 0);
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
        query->vacant = 1;
        glGenQueries(1, &query->query_id);
    }
    lua_register(lua, "api_query_left", api_query_left);
    lua_register(lua, "api_query_alloc", api_query_alloc);
    lua_register(lua, "api_query_free", api_query_free);
    lua_register(lua, "api_query_ready", api_query_ready);
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

