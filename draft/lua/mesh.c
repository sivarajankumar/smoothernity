#include "mesh.h"
#include "vbuf.h"
#include "ibuf.h"
#include "space.h"
#include <stdlib.h>

struct meshes_t g_meshes;

enum mesh_type_e
{
    MESH_TRIANGLE_STRIP = 0,
    MESH_TRIANGLE_FAN = 1,
    MESH_TRIANGLES = 2,
    MESH_TYPES_TOTAL = 3
};

static struct mesh_t * mesh_get(int meshi)
{
    if (meshi >= 0 && meshi < g_meshes.count)
        return g_meshes.pool + meshi;
    else
        return 0;
}

static int api_mesh_alloc(lua_State *lua)
{
    struct vbuf_t *vbuf;
    struct ibuf_t *ibuf;
    struct space_t *space;
    struct mesh_t *mesh;
    int type, texi, ioffset, icount;

    if (lua_gettop(lua) != 7 || !lua_isnumber(lua, -7)
    || !lua_isnumber(lua, -6) || !lua_isnumber(lua, -5)
    || !lua_isnumber(lua, -4) || !lua_isnumber(lua, -3)
    || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_mesh_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }

    type = lua_tointeger(lua, -7);
    vbuf = vbuf_get(lua_tointeger(lua, -6));
    ibuf = ibuf_get(lua_tointeger(lua, -5));
    texi = lua_tointeger(lua, -4);
    space = space_get(lua_tointeger(lua, -3));
    ioffset = lua_tointeger(lua, -2);
    icount = lua_tointeger(lua, -1);
    lua_pop(lua, 7);

    if (texi != -1)
    {
        lua_pushstring(lua, "api_mesh_alloc: no textures yet");
        lua_error(lua);
        return 0;
    }

    if (g_meshes.vacant == 0)
    {
        lua_pushstring(lua, "api_mesh_alloc: out of meshes");
        lua_error(lua);
        return 0;
    }

    if (vbuf == 0)
    {
        lua_pushstring(lua, "api_mesh_alloc: invalid vbuf");
        lua_error(lua);
        return 0;
    }
    
    if (ibuf == 0)
    {
        lua_pushstring(lua, "api_mesh_alloc: invalid ibuf");
        lua_error(lua);
        return 0;
    }

    if (space == 0)
    {
        lua_pushstring(lua, "api_mesh_alloc: invalid space");
        lua_error(lua);
        return 0;
    }

    if (type < 0 || type > MESH_TYPES_TOTAL)
    {
        lua_pushstring(lua, "api_mesh_alloc: invalid type");
        lua_error(lua);
        return 0;
    }

    if (ioffset < 0 || ioffset >= g_ibufs.size)
    {
        lua_pushstring(lua, "api_mesh_alloc: offset out of range");
        lua_error(lua);
        return 0;
    }

    if (icount <= 0 || icount >= g_ibufs.size - ioffset)
    {
        lua_pushstring(lua, "api_mesh_alloc: count out of range");
        lua_error(lua);
        return 0;
    }

    mesh = g_meshes.vacant;
    mesh->vacant = 0;
    g_meshes.vacant = g_meshes.vacant->next;

    if (mesh->prev)
        mesh->prev->next = mesh->next;
    if (mesh->next)
        mesh->next->prev = mesh->prev;

    mesh->prev = 0;
    mesh->next = 0;

    mesh->ibuf = ibuf;
    mesh->vbuf = vbuf;
    mesh->space = space;
    mesh->ioffset = ioffset;
    mesh->icount = icount;

    if (type == MESH_TRIANGLE_STRIP)
        mesh->type = GL_TRIANGLE_STRIP;
    else if (type == MESH_TRIANGLE_FAN)
        mesh->type = GL_TRIANGLE_FAN;
    else
        mesh->type = GL_TRIANGLES;

    if (vbuf->meshes)
        vbuf->meshes->vbuf_prev = mesh;
    else
        ++g_vbufs.with_meshes;
    mesh->vbuf_next = vbuf->meshes;
    vbuf->meshes = mesh;

    if (ibuf->meshes)
        ibuf->meshes->ibuf_prev = mesh;
    else
        ++g_ibufs.with_meshes;
    mesh->ibuf_next = ibuf->meshes;
    ibuf->meshes = mesh;

    lua_pushinteger(lua, mesh - g_meshes.pool);
    return 1;
}

static int api_mesh_free(lua_State *lua)
{
    struct mesh_t *mesh;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_mesh_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    mesh = mesh_get(lua_tointeger(lua, -1));
    lua_pop(lua, 1);

    if (mesh == 0 || mesh->vacant)
    {
        lua_pushstring(lua, "api_mesh_free: invalid mesh");
        lua_error(lua);
        return 0;
    }

    mesh->vacant = 1;

    if (mesh->vbuf->meshes == mesh)
    {
        mesh->vbuf->meshes = mesh->vbuf->meshes->next;
        if (mesh->vbuf->meshes == 0)
            --g_vbufs.with_meshes;
    }
    if (mesh->vbuf_next)
        mesh->vbuf_next->vbuf_prev = mesh->vbuf_prev;
    if (mesh->vbuf_prev)
        mesh->vbuf_prev->vbuf_next = mesh->vbuf_next;
    mesh->vbuf_next = 0;
    mesh->vbuf_prev = 0;

    if (mesh->ibuf->meshes == mesh)
    {
        mesh->ibuf->meshes = mesh->ibuf->meshes->next;
        if (mesh->ibuf->meshes == 0)
            --g_ibufs.with_meshes;
    }
    if (mesh->ibuf_next)
        mesh->ibuf_next->ibuf_prev = mesh->ibuf_prev;
    if (mesh->ibuf_prev)
        mesh->ibuf_prev->ibuf_next = mesh->ibuf_next;
    mesh->ibuf_next = 0;
    mesh->ibuf_prev = 0;

    if (g_meshes.vacant)
        g_meshes.vacant->prev = mesh;
    mesh->next = g_meshes.vacant;
    g_meshes.vacant = mesh;

    mesh->ibuf = 0;
    mesh->vbuf = 0;
    mesh->space = 0;
    return 0;
}

static int api_mesh_query(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_mesh_query: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_meshes.left);
    return 1;
}

int mesh_init(lua_State *lua, int count)
{
    int i;
    g_meshes.pool = calloc(count, sizeof(struct mesh_t));
    if (g_meshes.pool == 0)
        return 1;
    for (i = 0; i < count; ++i)
    {
        if (i > 0)
            g_meshes.pool[i].prev = g_meshes.pool + i - 1;
        if (i < count - 1)
            g_meshes.pool[i].next = g_meshes.pool + i + 1;
        g_meshes.pool[i].vacant = 1;
    }
    g_meshes.left = count;
    g_meshes.count = count;
    g_meshes.vacant = g_meshes.pool;

    lua_register(lua, "api_mesh_alloc", api_mesh_alloc);
    lua_register(lua, "api_mesh_free", api_mesh_free);
    lua_register(lua, "api_mesh_query", api_mesh_query);

    return 0;
}

void mesh_done(void)
{
    if (g_meshes.pool)
    {
        free(g_meshes.pool);
        g_meshes.pool = 0;
    }
}

void mesh_draw(struct mesh_t *mesh)
{
    glDrawElements(mesh->type, mesh->icount, GL_UNSIGNED_SHORT,
                   (struct ibuf_data_t*)0 + mesh->ioffset);
}
