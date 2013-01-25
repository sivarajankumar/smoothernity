#include "rop.h"
#include "vector.h"
#include "matrix.h"
#include "vbuf.h"
#include "ibuf.h"
#include "mesh.h"
#include "physics.h"
#include "text.h"
#include <stdlib.h>
#include <stdio.h>
#include <GL/gl.h>

#define ROP_ARGVS 1
#define ROP_ARGMS 1

enum rop_e
{
    ROP_ROOT,
    ROP_TIME_SCALE,
    ROP_CLEAR_COLOR,
    ROP_CLEAR_DEPTH,
    ROP_CLEAR,
    ROP_PROJ,
    ROP_MVIEW,
    ROP_DRAW_MESHES,
    ROP_DBG_PHYSICS,
    ROP_DBG_TEXT
};

struct rop_t
{
    enum rop_e type;
    int flags;
    int depthi;
    int tscalei;
    int wldi;
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
    struct rop_t *pool;
    struct rop_t *vacant;
};

static struct rops_t g_rops;

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
    return rop - g_rops.pool;
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

static int api_rop_alloc_clear_color(lua_State *lua)
{
    struct rop_t *rop, *prev;
    struct vector_t *color;
    int ropi;
    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1) || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_rop_alloc_clear_color: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    color = vector_get(lua_tointeger(lua, 2));
    lua_pop(lua, 2);

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_clear_color: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || color == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_clear_color: invalid object");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_CLEAR_COLOR;
    rop->argv[0] = color;
    prev->chain_next = rop;

    lua_pushinteger(lua, ropi);
    return 1;
}

static int api_rop_alloc_clear_depth(lua_State *lua)
{
    struct rop_t *rop, *prev;
    struct vector_t *depth;
    int ropi, depthi;
    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_rop_alloc_clear_depth: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    depth = vector_get(lua_tointeger(lua, 2));
    depthi = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

    if (depthi < 0 || depthi > 3)
    {
        lua_pushstring(lua, "api_rop_alloc_clear_depth: invalid depth index");
        lua_error(lua);
        return 0;
    }

    ropi = rop_alloc();
    rop = rop_get(ropi);
    if (rop == 0)
    {
        lua_pushstring(lua, "api_rop_alloc_clear_depth: out of rops");
        lua_error(lua);
        return 0;
    }

    if (prev == 0 || depth == 0 || rop == prev)
    {
        lua_pushstring(lua, "api_rop_alloc_clear_depth: invalid object");
        lua_error(lua);
        return 0;
    }

    rop->type = ROP_CLEAR_DEPTH;
    rop->argv[0] = depth;
    rop->depthi = depthi;
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
    int ropi;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_rop_alloc_draw_meshes: incorrect argument");
        lua_error(lua);
        return 0;
    }

    prev = rop_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

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

int rop_init(lua_State *lua, int count)
{
    int i;
    struct rop_t *rop;

    g_rops.pool = calloc(count, sizeof(struct rop_t));
    if (g_rops.pool == 0)
        return 1;
    g_rops.vacant = g_rops.pool;
    g_rops.count = count;
    g_rops.left = count;
    g_rops.left_min = count;
    for (i = 0; i < count; ++i)
    {
        rop = g_rops.pool + i;
        rop->vacant = 1;
        if (i < count - 1)
            rop->vacant_next = g_rops.pool + i + 1;
    }

    lua_register(lua, "api_rop_left", api_rop_left);
    lua_register(lua, "api_rop_free", api_rop_free);
    lua_register(lua, "api_rop_alloc_root", api_rop_alloc_root);
    lua_register(lua, "api_rop_alloc_tscale", api_rop_alloc_tscale);
    lua_register(lua, "api_rop_alloc_clear_color", api_rop_alloc_clear_color);
    lua_register(lua, "api_rop_alloc_clear_depth", api_rop_alloc_clear_depth);
    lua_register(lua, "api_rop_alloc_clear", api_rop_alloc_clear);
    lua_register(lua, "api_rop_alloc_proj", api_rop_alloc_proj);
    lua_register(lua, "api_rop_alloc_mview", api_rop_alloc_mview);
    lua_register(lua, "api_rop_alloc_draw_meshes", api_rop_alloc_draw_meshes);
    lua_register(lua, "api_rop_alloc_dbg_physics", api_rop_alloc_dbg_physics);
    lua_register(lua, "api_rop_alloc_dbg_text", api_rop_alloc_dbg_text);

    #define LUA_PUBLISH(x, y) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, y);

    LUA_PUBLISH(GL_COLOR_BUFFER_BIT, "API_ROP_CLEAR_COLOR");
    LUA_PUBLISH(GL_DEPTH_BUFFER_BIT, "API_ROP_CLEAR_DEPTH");

    return 0;
}

void rop_done(void)
{
    if (g_rops.pool == 0)
        return;
    printf("Render operations usage: %i/%i, allocs/frees: %i/%i\n",
           g_rops.count - g_rops.left_min, g_rops.count,
           g_rops.allocs, g_rops.frees);
    free(g_rops.pool);
    g_rops.pool = 0;
}

struct rop_t * rop_get(int ropi)
{
    if (ropi >= 0 && ropi < g_rops.count)
        return g_rops.pool + ropi;
    else
        return 0;
}

static int rop_update_meshes(float dt, int frame_tag)
{
    struct vbuf_t *vbuf;
    struct mesh_t *mesh_vbuf;
    for (vbuf = g_vbufs.baked; vbuf; vbuf = vbuf->next)
    {
        for (mesh_vbuf = vbuf->meshes; mesh_vbuf; mesh_vbuf = mesh_vbuf->vbuf_next)
        {
            if (mesh_vbuf->ibuf->mapped)
                continue;
            if (matrix_update(mesh_vbuf->matrix, dt, frame_tag, 0) != 0)
                return 1;
        }
    }
    return 0;
}

int rop_update(struct rop_t *root, float dt, int frame_tag)
{
    struct rop_t *rop;
    for (rop = root; rop; rop = rop->chain_next)
    {
        if (rop->type == ROP_TIME_SCALE)
        {
            if (vector_update(rop->argv[0], dt, frame_tag, 0) != 0)
                return 1;
            dt *= rop->argv[0]->value[rop->tscalei];
        }
        else if (rop->type == ROP_CLEAR_COLOR)
        {
            if (vector_update(rop->argv[0], dt, frame_tag, 0) != 0)
                return 1;
        }
        else if (rop->type == ROP_CLEAR_DEPTH)
        {
            if (vector_update(rop->argv[0], dt, frame_tag, 0) != 0)
                return 1;
        }
        else if (rop->type == ROP_PROJ)
        {
            if (matrix_update(rop->argm[0], dt, frame_tag, 0) != 0)
                return 1;
        }
        else if (rop->type == ROP_MVIEW)
        {
            if (matrix_update(rop->argm[0], dt, frame_tag, 0) != 0)
                return 1;
        }
        else if (rop->type == ROP_DRAW_MESHES)
        {
            if (rop_update_meshes(dt, frame_tag) != 0)
                return 1;
        }
    }
    return 0;
}

static void rop_clear_color(struct rop_t *rop)
{
    GLfloat *v;
    v = rop->argv[0]->value;
    glClearColor(v[0], v[1], v[2], v[3]);
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

static void rop_draw_meshes(int frame_tag)
{
    struct vbuf_t *vbuf;
    struct ibuf_t *ibuf;
    struct mesh_t *mesh_vbuf;
    struct mesh_t *mesh_ibuf;
    int vbuf_selected;
    int ibuf_selected;
    if (g_vbufs.with_meshes < g_ibufs.with_meshes)
    {
        for (vbuf = g_vbufs.baked; vbuf; vbuf = vbuf->next)
        {
            if (vbuf->meshes == 0)
                continue;
            vbuf_selected = 0;
            for (mesh_vbuf = vbuf->meshes; mesh_vbuf; mesh_vbuf = mesh_vbuf->vbuf_next)
            {
                if (mesh_vbuf->frame_tag == frame_tag)
                    continue;
                ibuf = mesh_vbuf->ibuf;
                if (ibuf->mapped)
                    continue;
                ibuf_selected = 0;
                for (mesh_ibuf = ibuf->meshes; mesh_ibuf; mesh_ibuf = mesh_ibuf->ibuf_next)
                {
                    if (mesh_ibuf->frame_tag == frame_tag)
                        continue;
                    if (vbuf_selected == 0)
                    {
                        vbuf_selected = 1;
                        vbuf_select(vbuf);
                    }
                    if (ibuf_selected == 0)
                    {
                        ibuf_selected = 1;
                        ibuf_select(ibuf);
                    }
                    mesh_ibuf->frame_tag = frame_tag;
                    mesh_draw(mesh_ibuf);
                }
            }
        }
    }
    else
    {
        for (ibuf = g_ibufs.baked; ibuf; ibuf = ibuf->next)
        {
            if (ibuf->meshes == 0)
                continue;
            ibuf_selected = 0;
            for (mesh_ibuf = ibuf->meshes; mesh_ibuf; mesh_ibuf = mesh_ibuf->ibuf_next)
            {
                if (mesh_ibuf->frame_tag == frame_tag)
                    continue;
                vbuf = mesh_ibuf->vbuf;
                if (vbuf->mapped)
                    continue;
                vbuf_selected = 0;
                for (mesh_vbuf = vbuf->meshes; mesh_vbuf; mesh_vbuf = mesh_vbuf->vbuf_next)
                {
                    if (mesh_vbuf->frame_tag == frame_tag)
                        continue;
                    if (vbuf_selected == 0)
                    {
                        vbuf_selected = 1;
                        vbuf_select(vbuf);
                    }
                    if (ibuf_selected == 0)
                    {
                        ibuf_selected = 1;
                        ibuf_select(ibuf);
                    }
                    mesh_vbuf->frame_tag = frame_tag;
                    mesh_draw(mesh_vbuf);
                }
            }
        }
    }
}

int rop_draw(struct rop_t *root, int frame_tag)
{
    struct rop_t *rop;
    for (rop = root; rop; rop = rop->chain_next)
    {
        if (rop->type == ROP_CLEAR_COLOR)
            rop_clear_color(rop);
        else if (rop->type == ROP_CLEAR_DEPTH)
            glClearDepthf(rop->argv[0]->value[rop->depthi]);
        else if (rop->type == ROP_CLEAR)
            glClear(rop->flags);
        else if (rop->type == ROP_PROJ)
            rop_proj(rop);
        else if (rop->type == ROP_MVIEW)
            rop_mview(rop);
        else if (rop->type == ROP_DRAW_MESHES)
            rop_draw_meshes(frame_tag);
        else if (rop->type == ROP_DBG_PHYSICS)
        {
            if (physics_wld_ddraw(rop->wldi) != 0)
                return 1;
        }
        else if (rop->type == ROP_DBG_TEXT)
            text_draw();
    }
    return 0;
}

