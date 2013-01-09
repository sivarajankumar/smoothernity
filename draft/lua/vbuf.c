#include "vbuf.h"
#include "scene.h"
#include <stdlib.h>

struct vbuf_data_t
{
    GLfloat pos[3];
    GLfloat tex[2];
    GLubyte color[4];
};

struct vbufs_t g_vbufs;

int vbuf_init(int size, int count)
{
    int i;
    g_vbufs.pool = calloc(count, sizeof(struct vbuf_t));
    if (g_vbufs.pool == 0)
        return 1;
    for (i = 0; i < count; ++i)
    {
        g_vbufs.pool[i].vacant = 1;
        if (i > 0)
            g_vbufs.pool[i].prev = g_vbufs.pool + i - 1;
        if (i < count - 1)
            g_vbufs.pool[i].next = g_vbufs.pool + i + 1;
        glGenBuffers(1, &g_vbufs.pool[i].buf_id);
        glBindBuffer(GL_ARRAY_BUFFER, g_vbufs.pool[i].buf_id);
        glBufferData(GL_ARRAY_BUFFER, sizeof(struct vbuf_data_t) * size,
                     0, GL_STATIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    g_vbufs.vacant = g_vbufs.pool;
    g_vbufs.size = size;
    g_vbufs.count = count;
    g_vbufs.left = count;
    return 0;
cleanup:
    free(g_vbufs.pool);
    g_vbufs.pool = 0;
    return 1;
}

void vbuf_done(void)
{
    int i;
    if (g_vbufs.pool)
    {
        for (i = 0; i < g_vbufs.count; ++i)
            vbuf_free(i);
        free(g_vbufs.pool);
        g_vbufs.pool = 0;
    }
}

void vbuf_query(int *size, int *left, int *with_meshes)
{
    *size = g_vbufs.size;
    *left = g_vbufs.left;
    *with_meshes = g_vbufs.with_meshes;
}

int vbuf_alloc(void)
{
    struct vbuf_t *vbuf;
    if (g_vbufs.vacant)
    {
        vbuf = g_vbufs.vacant;
        vbuf->vacant = 0;
        --g_vbufs.left;

        if (vbuf->mapped == 0)
        {
            glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
            vbuf->mapped = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY);
        }

        if (vbuf->prev)
            vbuf->prev->next = vbuf->next;
        if (vbuf->next)
            vbuf->next->prev = vbuf->prev;

        if (g_vbufs.mapped)
            g_vbufs.mapped->prev = vbuf;
        vbuf->prev = 0;
        vbuf->next = g_vbufs.mapped;
        g_vbufs.mapped = vbuf;

        return vbuf - g_vbufs.pool;
    }
    else
        return -1;
}

void vbuf_free(int vbufi)
{
    struct vbuf_t *vbuf;
    if (vbufi < 0 || vbufi >= g_vbufs.count)
        return;

    vbuf = g_vbufs.pool + vbufi;
    if (vbuf->vacant == 1)
        return;

    vbuf->vacant = 1;
    ++g_vbufs.left;

    if (vbuf->mapped)
    {
        glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
        glUnmapBuffer(GL_ARRAY_BUFFER);
        vbuf->mapped = 0;
    }

    if (vbuf->prev)
        vbuf->prev->next = vbuf->next;
    if (vbuf->next)
        vbuf->next->prev = vbuf->prev;

    if (g_vbufs.vacant)
        g_vbufs.vacant->prev = vbuf;
    vbuf->prev = 0;
    vbuf->next = g_vbufs.vacant;
    g_vbufs.vacant = vbuf;
}

void vbuf_write(int vbufi, int datai,
                float x, float y, float z,
                float r, float g, float b, float a,
                float u, float v)
{
    struct vbuf_t *vbuf;
    struct vbuf_data_t *data;

    if (vbufi < 0 || vbufi >= g_vbufs.count
     || datai < 0 || datai >= g_vbufs.size)
    {
        return;
    }

    vbuf = g_vbufs.pool + vbufi;
    if (vbuf->mapped == 0)
        return;

    data = vbuf->mapped;
    data += datai;

    data->pos[0] = x;
    data->pos[1] = y;
    data->pos[2] = z;

    data->tex[0] = u;
    data->tex[1] = v;

    data->color[0] = (GLubyte) (r * 255.0f);
    data->color[1] = (GLubyte) (g * 255.0f);
    data->color[2] = (GLubyte) (b * 255.0f);
    data->color[3] = (GLubyte) (a * 255.0f);
}

void vbuf_bake(int vbufi)
{
    struct vbuf_t *vbuf;
    if (vbufi < 0 || vbufi >= g_vbufs.count)
        return;

    vbuf = g_vbufs.pool + vbufi;
    if (vbuf->mapped == 0)
        return;

    glBindBuffer(GL_ARRAY_BUFFER, vbuf->buf_id);
    glUnmapBuffer(GL_ARRAY_BUFFER);
    vbuf->mapped = 0;

    if (vbuf->prev)
        vbuf->prev->next = vbuf->next;
    if (vbuf->next)
        vbuf->next->prev = vbuf->prev;

    if (g_vbufs.baked)
        g_vbufs.baked->prev = vbuf;
    vbuf->prev = 0;
    vbuf->next = g_vbufs.baked;
    g_vbufs.baked = vbuf;
}
