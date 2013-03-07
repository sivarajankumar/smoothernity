#include "sync.h"
#include "../util/util.h"
#include <string.h>
#include <stdio.h>
#include <GL/glew.h>

static const size_t SYNC_SIZE = 32;

struct sync_t
{
    GLsync sync_id;
    int vacant;
};

struct syncs_t
{
    int count;
    char *pool;
    struct sync_t *vacant;
};

static struct syncs_t g_syncs;

static struct sync_t * sync_get(int synci)
{
    if (synci >= 0 && synci < g_syncs.count)
        return (struct sync_t*)(g_syncs.pool + SYNC_SIZE * synci);
    else
        return 0;
}

static int api_sync_alloc(lua_State *lua)
{
    struct sync_t *sync;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_sync_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    sync = sync_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (sync == 0 || sync->vacant == 0)
    {
        lua_pushstring(lua, "api_sync_alloc: invalid sync");
        lua_error(lua);
        return 0;
    }
    sync->vacant = 0;
    sync->sync_id = glFenceSync(GL_SYNC_GPU_COMMANDS_COMPLETE, 0);
    return 0;
}

static int api_sync_free(lua_State *lua)
{
    struct sync_t *sync;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_sync_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    sync = sync_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (sync == 0 || sync->vacant == 1)
    {
        lua_pushstring(lua, "api_sync_free: invalid sync");
        lua_error(lua);
        return 0;
    }
    sync->vacant = 1;
    glDeleteSync(sync->sync_id);
    return 0;
}

static int api_sync_ready(lua_State *lua)
{
    struct sync_t *sync;
    GLint status;
    GLsizei len;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_sync_ready: incorrect argument");
        lua_error(lua);
        return 0;
    }
    sync = sync_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (sync == 0 || sync->vacant == 1)
    {
        lua_pushstring(lua, "api_sync_ready: invalid sync");
        lua_error(lua);
        return 0;
    }
    glGetSynciv(sync->sync_id, GL_SYNC_STATUS, 1, &len, &status);
    lua_pushboolean(lua, status == GL_SIGNALED);
    return 1;
}

int sync_init(lua_State *lua, int count)
{
    int i;
    struct sync_t *sync;
    if (sizeof(struct sync_t) > SYNC_SIZE)
    {
        fprintf(stderr, "Invalid size:\nsizeof(struct sync_t) == %i\n",
                (int)sizeof(struct sync_t));
        return 1;
    }
    g_syncs.pool = util_malloc(SYNC_SIZE, SYNC_SIZE * count);
    if (g_syncs.pool == 0)
        return 1;
    memset(g_syncs.pool, 0, SYNC_SIZE * count);
    g_syncs.count = count;
    for (i = 0; i < count; ++i)
    {
        sync = sync_get(i);
        sync->vacant = 1;
    }
    lua_register(lua, "api_sync_alloc", api_sync_alloc);
    lua_register(lua, "api_sync_free", api_sync_free);
    lua_register(lua, "api_sync_ready", api_sync_ready);
    return 0;
}

void sync_done(void)
{
    if (g_syncs.pool == 0)
        return;
    util_free(g_syncs.pool);
    g_syncs.pool = 0;
}

