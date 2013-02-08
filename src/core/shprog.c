#include "shprog.h"
#include "GL/gl.h"

struct shprog_t
{
    GLuint prog_id;
    int vacant;
    struct shprog_t *next;
    struct shprog_t *prev;
    struct mesh_t *meshes;
    struct shuni_t *shunis;
};

struct shprogs_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct shprog_t *vacant;
    struct shprog_t *created;
    struct shprog_t *linked;
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
