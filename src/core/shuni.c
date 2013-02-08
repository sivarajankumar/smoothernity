#include "shuni.h"

#define SHUNI_ARGVS 1

enum shuni_e
{
    SHUNI_3_F
};

struct shuni_t
{
    enum shuni_e type;
    int vacant;
    struct shprog_t *shprog;
    struct shuni_t *next;
    struct shuni_t *shprog_prev;
    struct shuni_t *shprog_next;
};

struct shunis_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct shuni_t *vacant;
};

static struct shunis_t g_shunis;

int shuni_init(lua_State *lua, int count)
{
    lua_register(lua, "api_shuni_alloc_3f", api_shuni_alloc_3f);
    lua_register(lua, "api_shuni_free", api_shuni_free);
    return 0;
}

void shuni_done(void)
{
}
