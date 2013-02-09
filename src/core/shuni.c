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
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct shuni_t *vacant;
};

static struct shunis_t g_shunis;

static struct shuni_t * shuni_get(int ishuni)
{
    if (ishuni >= 0 && ishuni < g_shunis.count)
        return (struct shuni_t*)(g_shunis.pool + SHUNI_SIZE * ishuni);
    else
        return 0;
}

static int shuni_alloc(struct shprog_t *shprog, struct mesh_t *mesh)
{
    struct shuni_t *shuni;
    if (g_shunis.vacant == 0)
        return -1;

    ++g_shunis.allocs;
    --g_shunis.left;
    if (g_shunis.left < g_shunis.left_min)
        g_shunis.left_min = g_shunis.left;

    shuni = g_shunis.vacant;
    g_shunis.vacant = g_shunis.vacant->next;
    shuni->next = 0;
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
    return ((char*)shuni - g_shunis.pool) / SHUNI_SIZE;
}

static int api_shuni_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_shuni_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_shunis.left);
    return 1;
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

    ++g_shunis.frees;
    ++g_shunis.left;

    shuni->state = SHUNI_VACANT;
    shuni->next = g_shunis.vacant;
    g_shunis.vacant = shuni;

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
    int meshi, ishuni;
    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_shuni_alloc_vector: incorrect argument");
        lua_error(lua);
        return 0;
    }
    shprog = shprog_get(lua_tointeger(lua, 1));
    meshi = lua_tointeger(lua, 2);
    vector = vector_get(lua_tointeger(lua, 3));
    lua_pop(lua, 3);
    mesh = mesh_get(meshi);
    if (shprog == 0 || (mesh == 0 && meshi != SHUNI_ALL_MESHES) || vector == 0)
    {
        lua_pushstring(lua, "api_shuni_alloc_vector: invalid object");
        lua_error(lua);
        return 0;
    }
    ishuni = shuni_alloc(shprog, mesh);
    shuni = shuni_get(ishuni);
    if (shuni == 0)
    {
        lua_pushstring(lua, "api_shuni_alloc_vector: out of shunis");
        lua_error(lua);
        return 0;
    }
    shuni->state = SHUNI_VECTOR;
    shuni->argv[0] = vector;
    lua_pushinteger(lua, ishuni);
    return 1;
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
    g_shunis.left = count;
    g_shunis.left_min = count;
    g_shunis.vacant = shuni_get(0);
    for (i = 0; i < count; ++i)
    {
        shuni = shuni_get(i);
        if (i < count - 1)
            shuni->next = shuni_get(i + 1);
        shuni->state = SHUNI_VACANT;
    }
    lua_register(lua, "api_shuni_left", api_shuni_left);
    lua_register(lua, "api_shuni_alloc_vector", api_shuni_alloc_vector);
    lua_register(lua, "api_shuni_free", api_shuni_free);

    #define LUA_PUBLISH(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);

    LUA_PUBLISH(SHUNI_ALL_MESHES);

    return 0;
}

void shuni_done(void)
{
    if (g_shunis.pool == 0)
        return;
    printf("Shader uniforms usage: %i/%i, allocs/frees: %i/%i\n",
           g_shunis.count - g_shunis.left_min, g_shunis.count,
           g_shunis.allocs, g_shunis.frees);
    util_free(g_shunis.pool);
    g_shunis.pool = 0;
}

static void shuni_select_vector(struct shuni_t *shuni)
{
    /* TODO */
    if (shuni != 0)
        return;
}

void shuni_select(struct shuni_t *shuni)
{
    if (shuni->state == SHUNI_VECTOR)
        shuni_select_vector(shuni);
}

static int shuni_update_vector(struct shuni_t *shuni, float dt, int frame_tag, int force)
{
    return vector_update(shuni->argv[0], dt, frame_tag, force);
}

int shuni_update(struct shuni_t *shuni, float dt, int frame_tag, int force)
{
    if (shuni->state == SHUNI_VECTOR)
        return shuni_update_vector(shuni, dt, frame_tag, force);
    return 0;
}
