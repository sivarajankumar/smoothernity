#include "mesh.h"
#include "vbuf.h"
#include "ibuf.h"
#include "space.h"
#include "scene.h"
#include <stdlib.h>

struct meshes_t g_meshes;

int mesh_init(int count)
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

void mesh_query(int *left)
{
    *left = g_meshes.left;
}

int mesh_spawn(int type, int vbufi, int ibufi, int texi, int spacei)
{
    struct vbuf_t *vbuf;
    struct ibuf_t *ibuf;
    struct space_t *space;
    struct mesh_t *mesh;

    /* reserved for textures */
    if (texi != -1)
        return -1;

    if (g_meshes.vacant == 0)
        return -1;

    vbuf = vbuf_get(vbufi);
    ibuf = ibuf_get(ibufi);
    space = space_get(spacei);
    if (vbuf == 0 || ibuf == 0 || space == 0)
        return -1;

    if (type < 0 || type > MESH_TYPES_TOTAL)
        return -1;

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
    mesh->type = type;

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

    return mesh - g_meshes.pool;
}

void mesh_kill(int meshi)
{
    struct mesh_t *mesh;
    if (meshi < 0 || meshi >= g_meshes.count)
        return;
    mesh = g_meshes.pool + meshi;

    if (mesh->vacant)
        return;

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
}
