#include "rop.h"
#include "vector.h"
#include "matrix.h"
#include "timer.h"
#include "vbuf.h"
#include "ibuf.h"
#include "mesh.h"
#include "shuni.h"
#include "shprog.h"
#include "physics.h"
#include "text.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>
#include <GL/gl.h>
#include <SDL.h>

#define ROP_ARGVS 2
#define ROP_ARGMS 1

static const size_t ROP_SIZE = 128;

enum rop_e
{
    ROP_ROOT,
    ROP_TIME_SCALE,
    ROP_CLEAR,
    ROP_PROJ,
    ROP_MVIEW,
    ROP_DRAW_MESHES,
    ROP_DBG_PHYSICS,
    ROP_DBG_TEXT,
    ROP_SWAP,
    ROP_FOG_OFF,
    ROP_FOG_LIN
};

struct rop_t
{
    enum rop_e type;
    int flags;
    int depthi;
    int tscalei;
    int neari;
    int fari;
    int wldi;
    int group;
    int vacant;
    struct rop_t *vacant_next;
    struct rop_t *chain_next;
    struct vector_t *argv[ROP_ARGVS];
    struct matrix_t *argm[ROP_ARGMS];
};

struct rops_t
{
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct rop_t *vacant;
};

static struct rops_t g_rops;

static struct rop_t * rop_get(int ropi)
{
    if (ropi >= 0 && ropi < g_rops.count)
        return (struct rop_t*)(g_rops.pool + ROP_SIZE * ropi);
    else
        return 0;
}

static int rop_update_meshes(float dt, int update_tag, int group)
{
    struct shuni_t *shuni;
    struct mesh_t *mesh;
    for (mesh = g_meshes.active; mesh; mesh = mesh->next)
    {
        if (mesh->group != group)
            continue;
        if (matrix_update(mesh->matrix, dt, update_tag, 0) != 0)
            return 1;
        for (shuni = mesh->shprog->shunis; shuni; shuni = shuni->shprog_next)
        {
            if (shuni_update(shuni, dt, update_tag, 0) != 0)
                return 1;
        }
        for (shuni = mesh->shunis; shuni; shuni = shuni->mesh_next)
        {
            if (shuni_update(shuni, dt, update_tag, 0) != 0)
                return 1;
        }
    }
    return 0;
}

static int api_rop_update(lua_State *lua)
{
    float dt0, dt;
    int update_tag;
    struct rop_t *root, *rop;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_rop_update: incorrect argument");
        lua_error(lua);
        return 0;
    }

    root = rop_get(lua_tointeger(lua, 1));
    dt0 = lua_tonumber(lua, 2);
    update_tag = lua_tointeger(lua, 3);

    if (root == 0)
    {
        lua_pushstring(lua, "api_rop_update: invalid rop");
        lua_error(lua);
        return 0;
    }

    if (dt0 < 0.0f)
    {
        lua_pushstring(lua, "api_rop_update: negative dt");
        lua_error(lua);
        return 0;
    }

    dt = dt0;
    for (rop = root; rop; rop = rop->chain_next)
    {
        if (rop->type == ROP_TIME_SCALE)
        {
            if (vector_update(rop->argv[0], dt, update_tag, 0) != 0)
                goto error;
            dt = dt0 * rop->argv[0]->value[rop->tscalei];
        }
        else if (rop->type == ROP_PROJ)
        {
            if (matrix_update(rop->argm[0], dt, update_tag, 0) != 0)
                goto error;
        }
        else if (rop->type == ROP_MVIEW)
        {
            if (matrix_update(rop->argm[0], dt, update_tag, 0) != 0)
                goto error;
        }
        else if (rop->type == ROP_DRAW_MESHES)
        {
            if (rop_update_meshes(dt, update_tag, rop->group) != 0)
                goto error;
        }
        else if (rop->type == ROP_FOG_LIN)
        {
            if (vector_update(rop->argv[0], dt, update_tag, 0) != 0)
                goto error;
            if (vector_update(rop->argv[1], dt, update_tag, 0) != 0)
                goto error;
        }
    }
    return 0;
error:
    lua_pushstring(lua, "api_rop_update: error");
    lua_error(lua);
    return 0;
}

static void rop_proj(struct rop_t *rop)
{
    glMatrixMode(GL_PROJECTION);
    glLoadMatrixf(rop->argm[0]->value);
}

static void rop_mview(struct rop_t *rop)
{
    glMatrixMode(GL_MODELVIEW);
    glLoadMatrixf(rop->argm[0]->value);
}

static void rop_draw_meshes(int draw_tag, int group)
{
    struct vbuf_t *vbuf;
    struct ibuf_t *ibuf;
    struct shprog_t *shprog;
    struct mesh_t *mesh;
    struct shuni_t *shuni;
    vbuf = 0;
    ibuf = 0;
    shprog = 0;
    for (mesh = g_meshes.active; mesh; mesh = mesh->next)
    {
        if (mesh->draw_tag == draw_tag || mesh->group != group)
            continue;
        if (vbuf != mesh->vbuf)
        {
            vbuf = mesh->vbuf;
            vbuf_select(vbuf);
        }
        if (ibuf != mesh->ibuf)
        {
            ibuf = mesh->ibuf;
            ibuf_select(ibuf);
        }
        if (shprog != mesh->shprog)
        {
            shprog = mesh->shprog;
            shprog_select(shprog);
            for (shuni = shprog->shunis; shuni; shuni = shuni->shprog_next)
                shuni_select(shuni);
        }
        for (shuni = mesh->shunis; shuni; shuni = shuni->mesh_next)
            shuni_select(shuni);
        mesh->draw_tag = draw_tag;
        mesh_draw(mesh);
    }
}

static void rop_fog_lin(struct rop_t *rop)
{
    glEnable(GL_FOG);
    glFogi(GL_FOG_MODE, GL_LINEAR);
    glFogfv(GL_FOG_COLOR, rop->argv[0]->value);
    glFogf(GL_FOG_START, rop->argv[1]->value[rop->neari]);
    glFogf(GL_FOG_END, rop->argv[1]->value[rop->fari]);
    glFogi(GL_FOG_COORD_SRC, GL_FRAGMENT_DEPTH);
}

static int api_rop_draw(lua_State *lua)
{
    int draw_tag;
    struct rop_t *rop, *root;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_rop_draw: incorrect argument");
        lua_error(lua);
        return 0;
    }

    root = rop_get(lua_tointeger(lua, 1));
    draw_tag = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    if (root == 0)
    {
        lua_pushstring(lua, "api_rop_draw: invalid rop");
        lua_error(lua);
        return 0;
    }

    glDisable(GL_FOG);
    for (rop = root; rop; rop = rop->chain_next)
    {
        if (rop->type == ROP_CLEAR)
            glClear(rop->flags);
        else if (rop->type == ROP_PROJ)
            rop_proj(rop);
        else if (rop->type == ROP_MVIEW)
            rop_mview(rop);
        else if (rop->type == ROP_DRAW_MESHES)
            rop_draw_meshes(draw_tag, rop->group);
        else if (rop->type == ROP_DBG_PHYSICS)
        {
            if (physics_wld_ddraw(rop->wldi) != 0)
            {
                lua_pushstring(lua, "api_rop_draw: physics world debug draw error");
                lua_error(lua);
                return 0;
            }
        }
        else if (rop->type == ROP_DBG_TEXT)
            text_draw();
        else if (rop->type == ROP_SWAP)
            SDL_GL_SwapBuffers();
        else if (rop->type == ROP_FOG_OFF)
            glDisable(GL_FOG);
        else if (rop->type == ROP_FOG_LIN)
            rop_fog_lin(rop);
    }
    return 0;
}

static int rop_alloc(void)
{
    struct rop_t *rop;
    if (g_rops.vacant == 0)
        return -1;

    ++g_rops.allocs;
    --g_rops.left;
    if (g_rops.left < g_rops.left_min)
        g_rops.left_min = g_rops.left;

    rop = g_rops.vacant;
    g_rops.vacant = g_rops.vacant->vacant_next;
    rop->vacant_next = 0;
    rop->vacant = 0;
    return ((char*)rop - g_rops.pool) / ROP_SIZE;
}

static int api_rop_free(lua_State *lua)
{
    int i;
    struct rop_t *rop;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_rop_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    rop = rop_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (rop == 0 || rop->vacant)
    {
        lua_pushstring(lua, "api_rop_free: invalid rop");
        lua_error(lua);
        return 0;
    }

    rop->vacant = 1;
    rop->chain_next = 0;
    ++g_rops.left;
    ++g_rops.frees;

    for (i = 0; i < ROP_ARGVS; ++i)
        rop->argv[i] = 0;

    for (i = 0; i < ROP_ARGMS; ++i)
        rop->argm[i] = 0;

    rop->vacant_next = g_rops.vacant;
    g_rops.vacant = rop;
    return 0;
}

static int api_rop_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_rop_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_rops.left);
    return 1;
}

static int api_rop_alloc_root(lua_State *lua)
{
    struct rop_t *rop;
    int ropi;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_rop_alloc_root: incorrect argument");
        lua_error(lua);
        return 0;
    }

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_root: out of rops");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_ROOT;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_tscale(lua_State *lua)
{
    struct rop_t *rop, *prev;
    struct vector_t *tscale;
    int ropi, tscalei;
    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_rop_alloc_tscale: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    tscale = vector_get(lua_tointeger(lua, 2));
    tscalei = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (tscalei < 0 || tscalei > 3)
    {
        lua_pushstring(lua, "api_rop_alloc_tscale: invalid time scale index");
        lua_error(lua);
        return 0;
    }

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_tscale: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || tscale == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_tscale: invalid object");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_TIME_SCALE;
    rop->argv[0] = tscale;
    rop->tscalei = tscalei;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_clear(lua_State *lua)
{
    struct rop_t *rop, *prev;
    int ropi, flags;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_rop_alloc_clear: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    flags = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_clear: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_clear: invalid rop");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_CLEAR;
    rop->flags = flags;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_proj(lua_State *lua)
{
    struct rop_t *rop, *prev;
    struct matrix_t *proj;
    int ropi;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_rop_alloc_proj: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    proj = matrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_proj: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || proj == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_proj: invalid object");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_PROJ;
    rop->argm[0] = proj;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_mview(lua_State *lua)
{
    struct rop_t *rop, *prev;
    struct matrix_t *mview;
    int ropi;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_rop_alloc_mview: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    mview = matrix_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_mview: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || mview == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_mview: invalid object");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_MVIEW;
    rop->argm[0] = mview;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_draw_meshes(lua_State *lua)
{
    struct rop_t *rop, *prev;
    int ropi, group;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_rop_alloc_draw_meshes: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    group = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_draw_meshes: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_draw_meshes: invalid rop");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_DRAW_MESHES;
    rop->group = group;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_dbg_physics(lua_State *lua)
{
    struct rop_t *rop, *prev;
    int ropi, wldi;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_rop_alloc_dbg_physics: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    wldi = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_dbg_physics: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_dbg_physics: invalid rop");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_DBG_PHYSICS;
    rop->wldi = wldi;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_dbg_text(lua_State *lua)
{
    struct rop_t *rop, *prev;
    int ropi;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_rop_alloc_dbg_text: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_dbg_text: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_dbg_text: invalid rop");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_DBG_TEXT;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_swap(lua_State *lua)
{
    struct rop_t *rop, *prev;
    int ropi;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_rop_alloc_swap: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_swap: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_swap: invalid rop");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_SWAP;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_fog_off(lua_State *lua)
{
    struct rop_t *rop, *prev;
    int ropi;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_rop_alloc_fog_off: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_fog_off: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_fog_off: invalid rop");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_FOG_OFF;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_fog_lin(lua_State *lua)
{
    struct rop_t *rop, *prev;
    struct vector_t *color, *dist;
    int ropi, neari, fari;
    if (lua_gettop(lua) != 5 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5))
    {
        lua_pushstring(lua, "api_rop_alloc_fog_lin: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    color = vector_get(lua_tointeger(lua, 2));
    dist = vector_get(lua_tointeger(lua, 3));
    neari = lua_tointeger(lua, 4);
    fari = lua_tointeger(lua, 5);
    lua_pop(lua, 5);

    if (color == 0 || dist == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_fog_lin: invalid vector");
        lua_error(lua);
        return 0;
    }

    if (neari < 0 || neari > 3 || fari < 0 || fari > 3)
    {
        lua_pushstring(lua, "api_rop_alloc_fog_lin: invalid distance index");
        lua_error(lua);
        return 0;
    }

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_fog_lin: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_fog_lin: invalid rop");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_FOG_LIN;
    rop->argv[0] = color;
    rop->argv[1] = dist;
    rop->neari = neari;
    rop->fari = fari;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

int rop_init(lua_State *lua, int count)
{
    int i;
    struct rop_t *rop;
    if (sizeof(struct rop_t) > ROP_SIZE)
    {
        fprintf(stderr, "Invalid size:\n"
                        "sizeof(struct rop_t) == %i\n",
                (int)sizeof(struct rop_t));
        return 1;
    }
    g_rops.pool = util_malloc(ROP_SIZE, ROP_SIZE * count);
    if (g_rops.pool == 0)
        goto cleanup;
    memset(g_rops.pool, 0, ROP_SIZE * count);
    g_rops.count = count;
    g_rops.left = count;
    g_rops.left_min = count;
    g_rops.vacant = rop_get(0);
    for (i = 0; i < count; ++i)
    {
        rop = rop_get(i);
        rop->vacant = 1;
        rop->vacant_next = rop_get(i + 1);
    }

    lua_register(lua, "api_rop_left", api_rop_left);
    lua_register(lua, "api_rop_update", api_rop_update);
    lua_register(lua, "api_rop_draw", api_rop_draw);
    lua_register(lua, "api_rop_free", api_rop_free);
    lua_register(lua, "api_rop_alloc_root", api_rop_alloc_root);
    lua_register(lua, "api_rop_alloc_tscale", api_rop_alloc_tscale);
    lua_register(lua, "api_rop_alloc_clear", api_rop_alloc_clear);
    lua_register(lua, "api_rop_alloc_proj", api_rop_alloc_proj);
    lua_register(lua, "api_rop_alloc_mview", api_rop_alloc_mview);
    lua_register(lua, "api_rop_alloc_draw_meshes", api_rop_alloc_draw_meshes);
    lua_register(lua, "api_rop_alloc_dbg_physics", api_rop_alloc_dbg_physics);
    lua_register(lua, "api_rop_alloc_dbg_text", api_rop_alloc_dbg_text);
    lua_register(lua, "api_rop_alloc_swap", api_rop_alloc_swap);
    lua_register(lua, "api_rop_alloc_fog_off", api_rop_alloc_fog_off);
    lua_register(lua, "api_rop_alloc_fog_lin", api_rop_alloc_fog_lin);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, y);

    LUA_PUBLISH(GL_COLOR_BUFFER_BIT, "API_ROP_CLEAR_COLOR");
    LUA_PUBLISH(GL_DEPTH_BUFFER_BIT, "API_ROP_CLEAR_DEPTH");

    return 0;
cleanup:
    if (g_rops.pool)
    {
        util_free(g_rops.pool);
        g_rops.pool = 0;
    }
    return 1;
}

void rop_done(void)
{
    if (g_rops.pool == 0)
        return;
    printf("Render operations usage: %i/%i, allocs/frees: %i/%i\n",
           g_rops.count - g_rops.left_min, g_rops.count,
           g_rops.allocs, g_rops.frees);
    util_free(g_rops.pool);
    g_rops.pool = 0;
}

