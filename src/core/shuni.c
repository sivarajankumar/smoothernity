#include "shuni.h"
#include "shprog.h"
#include "vector.h"
#include "mesh.h"
#include "../util/util.h"
#include <string.h>
#include <stdio.h>

static const size_t SHUNI_SIZE = 128;

enum shuni_bind_e
{
    SHUNI_ALL_MESHES = -1 /* must be negative */
};

struct shunis_t
{
    int count;
    char *pool;
};

static struct shunis_t g_shunis;

static struct shuni_t * shuni_get(int ishuni)
{
    if (ishuni >= 0 && ishuni < g_shunis.count)
        return (struct shuni_t*)(g_shunis.pool + SHUNI_SIZE * ishuni);
    else
        return 0;
}

static void shuni_alloc(struct shuni_t *shuni, struct shprog_t *shprog,
                        struct mesh_t *mesh)
{
    shuni->state = SHUNI_CREATED;

    shuni->shprog = shprog;
    shuni->shprog_prev = 0;
    shuni->shprog_next = shprog->shunis;
    if (shprog->shunis)
        shprog->shunis->shprog_prev = shuni;
    shprog->shunis = shuni;

    shuni->mesh = mesh;
    if (mesh)
    {
        shuni->mesh_prev = 0;
        shuni->mesh_next = mesh->shunis;
        if (mesh->shunis)
            mesh->shunis->mesh_prev = shuni;
        mesh->shunis = shuni;
    }
}

static int api_shuni_free(lua_State *lua)
{
    struct shuni_t *shuni;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_shuni_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    shuni = shuni_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    if (shuni == 0 || shuni->state == SHUNI_VACANT)
    {
        lua_pushstring(lua, "api_shuni_free: invalid shuni");
        lua_error(lua);
        return 0;
    }

    shuni->state = SHUNI_VACANT;

    if (shuni->shprog_prev)
        shuni->shprog_prev->shprog_next = shuni->shprog_next;
    if (shuni->shprog_next)
        shuni->shprog_next->shprog_prev = shuni->shprog_prev;
    if (shuni->shprog->shunis == shuni)
        shuni->shprog->shunis = shuni->shprog_next;
    shuni->shprog_prev = 0;
    shuni->shprog_next = 0;

    if (shuni->mesh_prev)
        shuni->mesh_prev->mesh_next = shuni->mesh_next;
    if (shuni->mesh_next)
        shuni->mesh_next->mesh_prev = shuni->mesh_prev;
    if (shuni->mesh && shuni->mesh->shunis == shuni)
        shuni->mesh->shunis = shuni->mesh_next;
    shuni->mesh_prev = 0;
    shuni->mesh_next = 0;
    return 0;
}

static int api_shuni_alloc_vector(lua_State *lua)
{
    struct shuni_t *shuni;
    struct shprog_t *shprog;
    struct mesh_t *mesh;
    struct vector_t *vector;
    int meshi;
    const char *name;
    if (lua_gettop(lua) != 5 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isstring(lua, 4) || !lua_isnumber(lua, 5))
    {
        lua_pushstring(lua, "api_shuni_alloc_vector: incorrect argument");
        lua_error(lua);
        return 0;
    }
    shuni = shuni_get(lua_tointeger(lua, 1));
    shprog = shprog_get(lua_tointeger(lua, 2));
    meshi = lua_tointeger(lua, 3);
    name = lua_tostring(lua, 4);
    vector = vector_get(lua_tointeger(lua, 5));
    lua_pop(lua, 5);
    mesh = mesh_get(meshi);
    if (shuni == 0 || shuni->state != SHUNI_VACANT
    || shprog == 0 || shprog->state != SHPROG_LINKED
    || (mesh == 0 && meshi != SHUNI_ALL_MESHES) || vector == 0)
    {
        lua_pushstring(lua, "api_shuni_alloc_vector: invalid object");
        lua_error(lua);
        return 0;
    }
    shuni_alloc(shuni, shprog, mesh);
    shuni->loc_id = glGetUniformLocation(shprog->prog_id, name);
    shuni->state = SHUNI_VECTOR;
    shuni->argv[0] = vector;
    return 0;
}

static int api_shuni_alloc_int(lua_State *lua)
{
    struct shuni_t *shuni;
    struct shprog_t *shprog;
    struct mesh_t *mesh;
    int meshi, argi;
    const char *name;
    if (lua_gettop(lua) != 5 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isstring(lua, 4) || !lua_isnumber(lua, 5))
    {
        lua_pushstring(lua, "api_shuni_alloc_int: incorrect argument");
        lua_error(lua);
        return 0;
    }
    shuni = shuni_get(lua_tointeger(lua, 1));
    shprog = shprog_get(lua_tointeger(lua, 2));
    meshi = lua_tointeger(lua, 3);
    name = lua_tostring(lua, 4);
    argi = lua_tointeger(lua, 5);
    lua_pop(lua, 5);
    mesh = mesh_get(meshi);
    if (shuni == 0 || shuni->state != SHUNI_VACANT
    || shprog == 0 || shprog->state != SHPROG_LINKED
    || (mesh == 0 && meshi != SHUNI_ALL_MESHES))
    {
        lua_pushstring(lua, "api_shuni_alloc_int: invalid object");
        lua_error(lua);
        return 0;
    }
    shuni_alloc(shuni, shprog, mesh);
    shuni->loc_id = glGetUniformLocation(shprog->prog_id, name);
    shuni->state = SHUNI_INTEGER;
    shuni->argi[0] = argi;
    return 0;
}

int shuni_init(lua_State *lua, int count)
{
    int i;
    struct shuni_t *shuni;
    if (sizeof(struct shuni_t) > SHUNI_SIZE)
    {
        fprintf(stderr, "Invalid size:\nsizeof(struct shuni_t) == %i\n",
                (int)sizeof(struct shuni_t));
        return 1;
    }
    g_shunis.pool = util_malloc(SHUNI_SIZE, SHUNI_SIZE * count);
    if (g_shunis.pool == 0)
        return 1;
    memset(g_shunis.pool, 0, SHUNI_SIZE * count);
    g_shunis.count = count;
    for (i = 0; i < count; ++i)
    {
        shuni = shuni_get(i);
        shuni->state = SHUNI_VACANT;
    }
    lua_register(lua, "api_shuni_alloc_vector", api_shuni_alloc_vector);
    lua_register(lua, "api_shuni_alloc_int", api_shuni_alloc_int);
    lua_register(lua, "api_shuni_free", api_shuni_free);

    #define LUA_PUBLISH(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);

    LUA_PUBLISH(SHUNI_ALL_MESHES);
    return 0;
}

void shuni_done(void)
{
    if (g_shunis.pool)
        util_free(g_shunis.pool);
    g_shunis.pool = 0;
}

void shuni_select(struct shuni_t *shuni)
{
    if (shuni->state == SHUNI_VECTOR)
        glUniform4fv(shuni->loc_id, 1, shuni->argv[0]->value);
    else if (shuni->state == SHUNI_INTEGER)
        glUniform1i(shuni->loc_id, shuni->argi[0]);
}

int shuni_update(struct shuni_t *shuni, float dt, int update_tag, int force)
{
    if (shuni->state == SHUNI_VECTOR)
        return vector_update(shuni->argv[0], dt, update_tag, force);
    return 0;
}
