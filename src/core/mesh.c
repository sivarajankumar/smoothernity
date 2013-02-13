#include "mesh.h"
#include "vbuf.h"
#include "ibuf.h"
#include "shuni.h"
#include "matrix.h"
#include "shprog.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>

static const size_t MESH_SIZE = 128;

struct meshes_t g_meshes;

enum mesh_type_e
{
    MESH_TRIANGLE_STRIP = 0,
    MESH_TRIANGLE_FAN = 1,
    MESH_TRIANGLES = 2,
    MESH_TYPES_TOTAL = 3
};

struct mesh_t * mesh_get(int meshi)
{
    if (meshi >= 0 && meshi < g_meshes.count)
        return (struct mesh_t*)(g_meshes.pool + MESH_SIZE * meshi);
    else
        return 0;
}

static int api_mesh_alloc(lua_State *lua)
{
    struct vbuf_t *vbuf;
    struct ibuf_t *ibuf;
    struct shprog_t *shprog;
    struct matrix_t *matrix;
    struct mesh_t *mesh, *mvbuf, *mibuf, *mshprog;
    int type, group, texi, ioffset, icount;

    if (lua_gettop(lua) != 9 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4) || !lua_isnumber(lua, 5)
    || !lua_isnumber(lua, 6) || !lua_isnumber(lua, 7)
    || !lua_isnumber(lua, 8) || !lua_isnumber(lua, 9))
    {
        lua_pushstring(lua, "api_mesh_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    group = lua_tointeger(lua, 1);
    type = lua_tointeger(lua, 2);
    vbuf = vbuf_get(lua_tointeger(lua, 3));
    ibuf = ibuf_get(lua_tointeger(lua, 4));
    texi = lua_tointeger(lua, 5);
    shprog = shprog_get(lua_tointeger(lua, 6));
    matrix = matrix_get(lua_tointeger(lua, 7));
    ioffset = lua_tointeger(lua, 8);
    icount = lua_tointeger(lua, 9);
    lua_pop(lua, 9);

    if (g_meshes.vacant == 0)
    {
        lua_pushstring(lua, "api_mesh_alloc: out of meshes");
        lua_error(lua);
        return 0;
    }

    if (vbuf == 0 || ibuf == 0 || texi != -1 || shprog == 0 || matrix == 0)
    {
        lua_pushstring(lua, "api_mesh_alloc: invalid object");
        lua_error(lua);
        return 0;
    }

    if (type < 0 || type > MESH_TYPES_TOTAL)
    {
        lua_pushstring(lua, "api_mesh_alloc: invalid type");
        lua_error(lua);
        return 0;
    }

    if (ioffset < 0 || ioffset >= g_ibufs.size
    ||  icount <= 0 || icount >= g_ibufs.size - ioffset)
    {
        lua_pushstring(lua, "api_mesh_alloc: number out of range");
        lua_error(lua);
        return 0;
    }

    ++g_meshes.allocs;
    --g_meshes.left;
    if (g_meshes.left < g_meshes.left_min)
        g_meshes.left_min = g_meshes.left;
    mesh = g_meshes.vacant;
    mesh->vacant = 0;
    g_meshes.vacant = g_meshes.vacant->next;

    if (mesh->prev)
        mesh->prev->next = mesh->next;
    if (mesh->next)
        mesh->next->prev = mesh->prev;

    mesh->group = group;
    mesh->ibuf = ibuf;
    mesh->vbuf = vbuf;
    mesh->shprog = shprog;
    mesh->matrix = matrix;
    mesh->ioffset = ioffset;
    mesh->icount = icount;

    if (type == MESH_TRIANGLE_STRIP)
        mesh->type = GL_TRIANGLE_STRIP;
    else if (type == MESH_TRIANGLE_FAN)
        mesh->type = GL_TRIANGLE_FAN;
    else
        mesh->type = GL_TRIANGLES;

    /*
       Maintain sorted order in the g_meshes.active list
       to minimize OpenGL state switches during draw.
       O(N), N = active meshes
    */

    mshprog = g_meshes.active;
    while (mshprog && mshprog->shprog != shprog)
        mshprog = mshprog->next;
    if (mshprog == 0)
    {
        mesh->prev = 0;
        mesh->next = g_meshes.active;
        if (g_meshes.active)
            g_meshes.active->prev = mesh;
        g_meshes.active = mesh;
    }
    else
    {
        mvbuf = mshprog;
        while (mvbuf && mvbuf->shprog == shprog && mvbuf->vbuf != vbuf)
            mvbuf = mvbuf->next;
        if (mvbuf == 0 || mvbuf->shprog != shprog)
        {
            mesh->prev = mshprog->prev;
            mesh->next = mshprog;
            if (g_meshes.active == mshprog)
                g_meshes.active = mesh;
            if (mshprog->prev)
                mshprog->prev->next = mesh;
            mshprog->prev = mesh;
        }
        else
        {
            mibuf = mvbuf;
            while (mibuf && mibuf->shprog == shprog &&
                   mibuf->vbuf == vbuf && mibuf->ibuf != ibuf)
            {
                mibuf = mibuf->next;
            }
            if (mibuf == 0 || mibuf->shprog != shprog || mibuf->vbuf != vbuf)
            {
                mesh->prev = mvbuf->prev;
                mesh->next = mvbuf;
                if (g_meshes.active == mvbuf)
                    g_meshes.active = mesh;
                if (mvbuf->prev)
                    mvbuf->prev->next = mesh;
                mvbuf->prev = mesh;
            }
            else
            {
                mesh->prev = mibuf;
                mesh->next = mibuf->next;
                if (mibuf->next)
                    mibuf->next->prev = mesh;
                mibuf->next = mesh;
            }
        }
    }

    lua_pushinteger(lua, ((char*)mesh - g_meshes.pool) / MESH_SIZE);
    return 1;
}

static int api_mesh_group(lua_State *lua)
{
    struct mesh_t *mesh;
    int group;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_mesh_group: incorrect argument");
        lua_error(lua);
        return 0;
    }

    mesh = mesh_get(lua_tointeger(lua, 1));
    group = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    if (mesh == 0)
    {
        lua_pushstring(lua, "api_mesh_group: invalid mesh");
        lua_error(lua);
        return 0;
    }
    mesh->group = group;
    return 0;
}

static int api_mesh_free(lua_State *lua)
{
    struct mesh_t *mesh;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_mesh_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    mesh = mesh_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (mesh == 0 || mesh->vacant)
    {
        lua_pushstring(lua, "api_mesh_free: invalid mesh");
        lua_error(lua);
        return 0;
    }

    ++g_meshes.left;
    ++g_meshes.frees;
    mesh->vacant = 1;

    if (mesh->prev)
        mesh->prev->next = mesh->next;
    if (mesh->next)
        mesh->next->prev = mesh->prev;
    if (g_meshes.active == mesh)
        g_meshes.active = mesh->next;

    if (g_meshes.vacant)
        g_meshes.vacant->prev = mesh;
    mesh->prev = 0;
    mesh->next = g_meshes.vacant;
    g_meshes.vacant = mesh;

    mesh->ibuf = 0;
    mesh->vbuf = 0;
    mesh->shprog = 0;
    mesh->matrix = 0;
    return 0;
}

static int api_mesh_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_mesh_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_meshes.left);
    return 1;
}

static int api_mesh_update(lua_State *lua)
{
    struct shuni_t *shuni;
    struct mesh_t *mesh;
    int group, update_tag;
    float dt;

    if (lua_gettop(lua) != 3 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3))
    {
        lua_pushstring(lua, "api_mesh_update: incorrect argument");
        lua_error(lua);
        return 0;
    }

    group = lua_tointeger(lua, 1);
    dt = lua_tonumber(lua, 2);
    update_tag = lua_tointeger(lua, 3);
    lua_pop(lua, 3);

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

static int api_mesh_draw(lua_State *lua)
{
    struct vbuf_t *vbuf;
    struct ibuf_t *ibuf;
    struct shprog_t *shprog;
    struct mesh_t *mesh;
    struct shuni_t *shuni;
    int group, draw_tag;

    if (lua_gettop(lua) != 2 || !lua_isnumber(lua, 1)
    || !lua_isnumber(lua, 2))
    {
        lua_pushstring(lua, "api_mesh_draw: incorrect argument");
        lua_error(lua);
        return 0;
    }

    group = lua_tointeger(lua, 1);
    draw_tag = lua_tointeger(lua, 2);
    lua_pop(lua, 2);

    vbuf = 0;
    ibuf = 0;
    shprog = 0;
    glMatrixMode(GL_MODELVIEW);
    for (mesh = g_meshes.active; mesh; mesh = mesh->next)
    {
        if (mesh->draw_tag == draw_tag
        ||  mesh->group != group
        ||  mesh->shprog->state != SHPROG_LINKED)
        {
            continue;
        }
        mesh->draw_tag = draw_tag;
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
        glPushMatrix();
        glMultMatrixf(mesh->matrix->value);
        glDrawElements(mesh->type, mesh->icount, GL_UNSIGNED_INT,
                       (ibuf_data_t*)0 + mesh->ioffset);
        glPopMatrix();
    }
    return 0;
}

int mesh_init(lua_State *lua, int count)
{
    int i;
    struct mesh_t *mesh;
    if (sizeof(struct mesh_t) > MESH_SIZE)
    {
        fprintf(stderr, "Invalid size:\n"
                        "sizeof(struct mesh_t) == %i\n",
                (int)sizeof(struct mesh_t));
        return 1;
    }
    g_meshes.pool = util_malloc(MESH_SIZE, MESH_SIZE * count);
    if (g_meshes.pool == 0)
        return 1;
    memset(g_meshes.pool, 0, MESH_SIZE * count);
    g_meshes.left = count;
    g_meshes.left_min = count;
    g_meshes.count = count;
    g_meshes.vacant = mesh_get(0);
    for (i = 0; i < count; ++i)
    {
        mesh = mesh_get(i);
        mesh->prev = mesh_get(i - 1);
        mesh->next = mesh_get(i + 1);
        mesh->vacant = 1;
    }

    lua_register(lua, "api_mesh_draw", api_mesh_draw);
    lua_register(lua, "api_mesh_update", api_mesh_update);
    lua_register(lua, "api_mesh_alloc", api_mesh_alloc);
    lua_register(lua, "api_mesh_group", api_mesh_group);
    lua_register(lua, "api_mesh_free", api_mesh_free);
    lua_register(lua, "api_mesh_left", api_mesh_left);

    #define LUA_PUBLISH(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);

    LUA_PUBLISH(MESH_TRIANGLE_STRIP);
    LUA_PUBLISH(MESH_TRIANGLE_FAN);
    LUA_PUBLISH(MESH_TRIANGLES);

    return 0;
}

void mesh_done(void)
{
    if (g_meshes.pool == 0)
        return;
    printf("Meshes usage: %i/%i, allocs/frees: %i/%i\n",
           g_meshes.count - g_meshes.left_min, g_meshes.count,
           g_meshes.allocs, g_meshes.frees);
    util_free(g_meshes.pool);
    g_meshes.pool = 0;
}
