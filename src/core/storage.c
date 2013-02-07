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
    struct storage_t *active_head;
    struct storage_t *active_tail;
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

static int storage_alloc(void)
{
    struct storage_t *st;
    if (g_storages.vacant == 0)
        return -1;
    ++g_storages.allocs;
    --g_storages.left;
    if (g_storages.left < g_storages.left_min)
        g_storages.left_min = g_storages.left;
    st = g_storages.vacant;
    g_storages.vacant = g_storages.vacant->next;
    g_storages.vacant->prev = 0;
    if (g_storages.active_tail == 0 && g_storages.active_head == 0)
    {
        g_storages.active_head = g_storages.active_tail = st;
        st->prev = st->next = 0;
    }
    else
    {
        st->prev = g_storages.active_tail;
        st->next = 0;
        g_storages.active_tail->next = st;
        g_storages.active_tail = st;
    }
    return ((char*)st - g_storages.pool) / STORAGE_SIZE;
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
        for (st = g_storages.active_head; st; st = st->next)
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
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_storage_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_storages.left);
    return 1;
}

static int api_storage_alloc_r(lua_State *lua)
{
    struct storage_t *st;
    int sti;
    size_t key_len;
    const char *key;
    if (lua_gettop(lua) != 1 || !lua_isstring(lua, 1))
    {
        lua_pushstring(lua, "api_storage_alloc_r: incorrect argument");
        lua_error(lua);
        return 0;
    }
    key = lua_tolstring(lua, 1, &key_len);
    lua_pop(lua, 1);
    if (key_len >= (size_t)g_storages.key_size)
    {
        lua_pushstring(lua, "api_storage_alloc_r: key is too long");
        lua_error(lua);
        return 0;
    }
    sti = storage_alloc();
    st = storage_get(sti);
    if (st == 0)
    {
        lua_pushstring(lua, "api_storage_alloc_r: out of storages");
        lua_error(lua);
        return 0;
    }
    st->state = STORAGE_STATE_WAITING;
    st->cmd = STORAGE_CMD_READ;
    memcpy(st->key, key, key_len);
    st->key[key_len] = 0;
    lua_pushinteger(lua, sti);
    return 1;
}

static int api_storage_alloc_w(lua_State *lua)
{
    struct storage_t *st;
    int sti;
    size_t key_len, data_len;
    const char *key, *data;
    if (lua_gettop(lua) != 2 || !lua_isstring(lua, 1)
    || !lua_isstring(lua, 2))
    {
        lua_pushstring(lua, "api_storage_alloc_w: incorrect argument");
        lua_error(lua);
        return 0;
    }
    key = lua_tolstring(lua, 1, &key_len);
    data = lua_tolstring(lua, 2, &data_len);
    lua_pop(lua, 2);
    if (key_len >= (size_t)g_storages.key_size
    || data_len >= (size_t)g_storages.data_size)
    {
        lua_pushstring(lua, "api_storage_alloc_w: string is too long");
        lua_error(lua);
        return 0;
    }
    sti = storage_alloc();
    st = storage_get(sti);
    if (st == 0)
    {
        lua_pushstring(lua, "api_storage_alloc_w: out of storages");
        lua_error(lua);
        return 0;
    }
    st->state = STORAGE_STATE_WAITING;
    st->cmd = STORAGE_CMD_WRITE;
    memcpy(st->key, key, key_len);
    memcpy(st->data, data, data_len);
    st->key[key_len] = 0;
    st->data[data_len] = 0;
    lua_pushinteger(lua, sti);
    return 1;
}

static int api_storage_free(lua_State *lua)
{
    struct storage_t *st;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_storage_free: incorrect argument");
        lua_error(lua);
        return 0;
    }
    st = storage_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    pthread_mutex_lock(&g_storages.mutex);
    if (st == 0 || (st->state != STORAGE_STATE_DONE &&
                    st->state != STORAGE_STATE_ERROR))
    {
        pthread_mutex_unlock(&g_storages.mutex);
        lua_pushstring(lua, "api_storage_free: invalid storage");
        lua_error(lua);
        return 0;
    }
    pthread_mutex_unlock(&g_storages.mutex);
    st->state = STORAGE_STATE_VACANT;
    ++g_storages.left;
    ++g_storages.frees;
    if (st == g_storages.active_head)
        g_storages.active_head = st->next;
    if (st == g_storages.active_tail)
        g_storages.active_tail = st->prev;
    if (st->next)
        st->next->prev = st->prev;
    if (st->prev)
        st->prev->next = st->next;
    st->next = g_storages.vacant;
    st->prev = 0;
    g_storages.vacant = st;
    return 0;
}

static int api_storage_state(lua_State *lua)
{
    struct storage_t *st;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_storage_state: incorrect argument");
        lua_error(lua);
        return 0;
    }
    st = storage_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    pthread_mutex_lock(&g_storages.mutex);
    if (st == 0)
    {
        pthread_mutex_unlock(&g_storages.mutex);
        lua_pushstring(lua, "api_storage_state: invalid storage");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, (int)st->state);
    pthread_mutex_unlock(&g_storages.mutex);
    return 1;
}

static int api_storage_data(lua_State *lua)
{
    struct storage_t *st;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_storage_data: incorrect argument");
        lua_error(lua);
        return 0;
    }
    st = storage_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);
    pthread_mutex_lock(&g_storages.mutex);
    if (st == 0 || st->state != STORAGE_STATE_DONE)
    {
        pthread_mutex_unlock(&g_storages.mutex);
        lua_pushstring(lua, "api_storage_data: invalid storage");
        lua_error(lua);
        return 0;
    }
    lua_pushlstring(lua, st->data, st->size);
    pthread_mutex_unlock(&g_storages.mutex);
    return 1;
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
