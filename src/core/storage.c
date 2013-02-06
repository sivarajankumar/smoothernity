#include "storage.h"
#include "../util/util.h"
#include <string.h>
#include <stdio.h>
#include <pthread.h>

static const size_t STORAGE_SIZE = 64;
static const size_t STORAGE_KEY_ALIGN = 16;
static const size_t STORAGE_DATA_ALIGN = 16;

enum storage_state_e
{
    STORAGE_STATE_VACANT,
    STORAGE_STATE_WAITING,
    STORAGE_STATE_PROGRESS,
    STORAGE_STATE_DONE,
    STORAGE_STATE_ERROR
};

enum storage_cmd_e
{
    STORAGE_CMD_NONE,
    STORAGE_CMD_READ,
    STORAGE_CMD_WRITE
};

struct storage_t
{
    char *key;
    char *data;
    int size;
    enum storage_cmd_e cmd;
    enum storage_state_e state;
    struct storage_t *next;
    struct storage_t *prev;
};

struct storages_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    int key_size;
    int data_size;
    char *pool;
    pthread_mutex_t mutex;
    pthread_cond_t engage;
    pthread_t thread;
    int quit;
    struct storage_t *vacant;
    struct storage_t *active;
    struct storage_t *current;
};

static struct storages_t g_storages;

static struct storage_t * storage_get(int sti)
{
    if (sti >= 0 && sti < g_storages.count)
        return (struct storage_t*)(g_storages.pool + STORAGE_SIZE * sti);
    else
        return 0;
}

static void* storage_thread(void *param)
{
    FILE *f;
    struct storage_t **cur = &g_storages.current;
    if (param != 0)
        return 0;
    while (g_storages.quit == 0)
    {
        pthread_mutex_lock(&g_storages.mutex);
        pthread_cond_wait(&g_storages.engage, &g_storages.mutex);
        if (*cur == 0)
            pthread_mutex_unlock(&g_storages.mutex);
        else
        {
            pthread_mutex_unlock(&g_storages.mutex);
            if ((*cur)->cmd == STORAGE_CMD_READ)
                f = fopen((*cur)->key, "r");
            else if ((*cur)->cmd == STORAGE_CMD_WRITE)
                f = fopen((*cur)->key, "w");
            if (f == 0)
            {
                pthread_mutex_lock(&g_storages.mutex);
                (*cur)->state = STORAGE_STATE_ERROR;
                *cur = 0;
                pthread_mutex_unlock(&g_storages.mutex);
            }
            else
            {
                if ((*cur)->cmd == STORAGE_CMD_READ)
                    (*cur)->size = fread((*cur)->data, 1, g_storages.data_size, f);
                else if ((*cur)->cmd == STORAGE_CMD_WRITE)
                    fwrite((*cur)->data, 1, (*cur)->size, f);
                fclose(f);
                pthread_mutex_lock(&g_storages.mutex);
                (*cur)->state = ferror(f) ? STORAGE_STATE_ERROR : STORAGE_STATE_DONE;
                *cur = 0;
                pthread_mutex_unlock(&g_storages.mutex);
            }
        }
    }
    return 0;
}

static int api_storage_update(lua_State *lua)
{
    struct storage_t *st;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_storage_update: incorrect argument");
        lua_error(lua);
        return 0;
    }
    pthread_mutex_lock(&g_storages.mutex);
    if (g_storages.current == 0)
    {
        for (st = g_storages.active; st; st = st->next)
        {
            if (st->state == STORAGE_STATE_WAITING)
            {
                st->state = STORAGE_STATE_PROGRESS;
                g_storages.current = st;
                pthread_cond_signal(&g_storages.engage);
                break;
            }
        }
    }
    pthread_mutex_unlock(&g_storages.mutex);
    return 0;
}

static int api_storage_left(lua_State *lua)
{
    lua_error(lua);
    return 0;
}

static int api_storage_alloc_r(lua_State *lua)
{
    lua_error(lua);
    return 0;
}

static int api_storage_alloc_w(lua_State *lua)
{
    lua_error(lua);
    return 0;
}

static int api_storage_free(lua_State *lua)
{
    lua_error(lua);
    return 0;
}

static int api_storage_state(lua_State *lua)
{
    lua_error(lua);
    return 0;
}

static int api_storage_data(lua_State *lua)
{
    lua_error(lua);
    return 0;
}

int storage_init(lua_State *lua, int key_size, int data_size, int count)
{
    int i;
    struct storage_t *st;
    if (sizeof(struct storage_t) > STORAGE_SIZE
    || (key_size & (key_size - 1)) != 0
    || (data_size & (data_size - 1)) != 0)
    {
        fprintf(stderr, "Invalid sizes:\n"
                        "sizeof(struct storage_t) == %i\n"
                        "key_size == %i\n"
                        "data_size == %i\n",
                (int)sizeof(struct storage_t), key_size, data_size);
        return 1;
    }
    g_storages.pool = util_malloc(STORAGE_SIZE, STORAGE_SIZE * count);
    if (g_storages.pool == 0)
        return 1;
    memset(g_storages.pool, 0, STORAGE_SIZE * count);
    g_storages.key_size = key_size;
    g_storages.data_size = data_size;
    g_storages.count = count;
    g_storages.left = count;
    g_storages.left_min = count;
    g_storages.quit = 0;
    g_storages.vacant = storage_get(0);
    for (i = 0; i < count; ++i)
    {
        st = storage_get(i);
        if (i > 0)
            st->prev = storage_get(i - 1);
        if (i < count - 1)
            st->next = storage_get(i + 1);
        st->key = util_malloc(STORAGE_KEY_ALIGN, key_size);
        st->data = util_malloc(STORAGE_DATA_ALIGN, data_size);
        if (st->key == 0 || st->data == 0)
            goto cleanup;
        memset(st->key, 0, key_size);
        memset(st->data, 0, data_size);
        st->state = STORAGE_STATE_VACANT;
        st->cmd = STORAGE_CMD_NONE;
    }
    if (pthread_mutex_init(&g_storages.mutex, 0) != 0)
        goto cleanup;
    if (pthread_cond_init(&g_storages.engage, 0) != 0)
    {
        pthread_mutex_destroy(&g_storages.mutex);
        goto cleanup;
    }
    if (pthread_create(&g_storages.thread, 0, storage_thread, 0) != 0)
    {
        pthread_mutex_destroy(&g_storages.mutex);
        pthread_cond_destroy(&g_storages.engage);
        goto cleanup;
    }
    lua_register(lua, "api_storage_update", api_storage_update);
    lua_register(lua, "api_storage_left", api_storage_left);
    lua_register(lua, "api_storage_alloc_r", api_storage_alloc_r);
    lua_register(lua, "api_storage_alloc_w", api_storage_alloc_w);
    lua_register(lua, "api_storage_free", api_storage_free);
    lua_register(lua, "api_storage_state", api_storage_state);
    lua_register(lua, "api_storage_data", api_storage_data);
    #define LUA_PUBLISH(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);
    LUA_PUBLISH(STORAGE_STATE_VACANT);
    LUA_PUBLISH(STORAGE_STATE_PROGRESS);
    LUA_PUBLISH(STORAGE_STATE_DONE);
    LUA_PUBLISH(STORAGE_STATE_ERROR);
    return 0;
cleanup:
    for (i = 0; i < count; ++i)
    {
        st = storage_get(i);
        if (st->key)
            util_free(st->key);
        if (st->data)
            util_free(st->data);
    }
    util_free(g_storages.pool);
    g_storages.pool = 0;
    return 1;
}

void storage_done(void)
{
    int i;
    struct storage_t *st;
    if (g_storages.pool == 0)
        return;
    printf("Storages usage: %i/%i, allocs/frees: %i/%i\n",
           g_storages.count - g_storages.left_min, g_storages.count,
           g_storages.allocs, g_storages.frees);
    g_storages.quit = 1;
    pthread_cond_signal(&g_storages.engage);
    pthread_join(g_storages.thread, 0);
    pthread_mutex_destroy(&g_storages.mutex);
    pthread_cond_destroy(&g_storages.engage);
    for (i = 0; i < g_storages.count; ++i)
    {
        st = storage_get(i);
        util_free(st->key);
        util_free(st->data);
    }
    util_free(g_storages.pool);
}
