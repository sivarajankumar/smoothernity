#include "shuni.h"

enum shuni_bind_e
{
    SHUNI_MESHES_ALL = -1 /* must be negative */
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
    lua_register(lua, "api_shuni_alloc", api_shuni_alloc);
    lua_register(lua, "api_shuni_free", api_shuni_free);
    lua_register(lua, "api_shuni_vector", api_shuni_vector);
    return 0;
}

void shuni_done(void)
{
}

void shuni_select(struct shuni_t *shuni)
{
}

int shuni_update(struct shuni_t *shuni, float dt, int frame_tag, int force)
{
}
