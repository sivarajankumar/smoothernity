#include "shprog.h"

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

int shprog_init(lua_State *lua, int count)
{
    lua_register(lua, "api_shprog_alloc", api_shprog_alloc);
    lua_register(lua, "api_shprog_free", api_shprog_free);
    lua_register(lua, "api_shprog_attach", api_shprog_attach); 
    lua_register(lua, "api_shprog_link", api_shprog_link);
    return 0;
}

void shprog_done(void)
{
}

struct shprog_t * shprog_get(int)
{
}

void shprog_select(struct shprog_t *shprog)
{
}
