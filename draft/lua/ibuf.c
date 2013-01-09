#include "ibuf.h"
#include "scene.h"
#include <stdlib.h>

struct ibufs_t g_ibufs;

int ibuf_init(int size, int count)
{
    int i;
    g_ibufs.pool = calloc(count, sizeof(struct ibuf_t));
    if (g_ibufs.pool == 0)
        return 1;
    for (i = 0; i < count; ++i)
    {
        g_ibufs.pool[i].vacant = 1;
        if (i > 0)
            g_ibufs.pool[i].prev = g_ibufs.pool + i - 1;
        if (i < count - 1)
            g_ibufs.pool[i].next = g_ibufs.pool + i + 1;
        glGenBuffers(1, &g_ibufs.pool[i].buf_id);
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, g_ibufs.pool[i].buf_id);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(struct ibuf_data_t) * size,
                     0, GL_STATIC_DRAW);
        if (glGetError() != GL_NO_ERROR)
            goto cleanup;
    }
    g_ibufs.vacant = g_ibufs.pool;
    g_ibufs.size = size;
    g_ibufs.count = count;
    g_ibufs.left = count;
    return 0;
cleanup:
    free(g_ibufs.pool);
    g_ibufs.pool = 0;
    return 1;
}

void ibuf_done(void)
{
    int i;
    if (g_ibufs.pool)
    {
        for (i = 0; i < g_ibufs.count; ++i)
            ibuf_free(i);
        free(g_ibufs.pool);
        g_ibufs.pool = 0;
    }
}

void ibuf_query(int *size, int *left)
{
    *size = g_ibufs.size;
    *left = g_ibufs.left;
}

int ibuf_alloc(void)
{
    struct ibuf_t *ibuf;
    if (g_ibufs.vacant)
    {
        ibuf = g_ibufs.vacant;
        ibuf->vacant = 0;
        --g_ibufs.left;

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
        ibuf->mapped = glMapBuffer(GL_ELEMENT_ARRAY_BUFFER, GL_WRITE_ONLY);

        if (g_ibufs.vacant == ibuf)
            g_ibufs.vacant = ibuf->next;

        if (ibuf->prev)
            ibuf->prev->next = ibuf->next;
        if (ibuf->next)
            ibuf->next->prev = ibuf->prev;

        if (g_ibufs.mapped)
            g_ibufs.mapped->prev = ibuf;
        ibuf->prev = 0;
        ibuf->next = g_ibufs.mapped;
        g_ibufs.mapped = ibuf;

        return ibuf - g_ibufs.pool;
    }
    else
        return -1;
}

void ibuf_free(int ibufi)
{
    struct ibuf_t *ibuf;
    if (ibufi < 0 || ibufi >= g_ibufs.count)
        return;

    ibuf = g_ibufs.pool + ibufi;
    if (ibuf->vacant == 1)
        return;

    ibuf->vacant = 1;
    ++g_ibufs.left;

    if (ibuf->mapped)
    {
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
        glUnmapBuffer(GL_ELEMENT_ARRAY_BUFFER);
        ibuf->mapped = 0;
        if (g_ibufs.mapped == ibuf)
            g_ibufs.mapped = ibuf->next;
    }
    else if (g_ibufs.baked == ibuf)
        g_ibufs.baked = ibuf->next;

    if (ibuf->prev)
        ibuf->prev->next = ibuf->next;
    if (ibuf->next)
        ibuf->next->prev = ibuf->prev;

    if (g_ibufs.vacant)
        g_ibufs.vacant->prev = ibuf;
    ibuf->prev = 0;
    ibuf->next = g_ibufs.vacant;
    g_ibufs.vacant = ibuf;
}

struct ibuf_t * ibuf_get(int ibufi)
{
    if (ibufi >= 0 && ibufi < g_ibufs.count)
        return g_ibufs.pool + ibufi;
    else
        return 0;
}

void ibuf_write(int ibufi, int datai, int index)
{
    struct ibuf_t *ibuf;
    struct ibuf_data_t *data;

    if (datai < 0 || datai >= g_ibufs.size)
        return;

    ibuf = ibuf_get(ibufi);
    if (ibuf == 0 || ibuf->mapped == 0)
        return;

    data = ibuf->mapped;
    data += datai;

    data->index = index;
}

void ibuf_bake(int ibufi)
{
    struct ibuf_t *ibuf;

    ibuf = ibuf_get(ibufi);
    if (ibuf == 0 || ibuf->mapped == 0)
        return;

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
    glUnmapBuffer(GL_ELEMENT_ARRAY_BUFFER);
    ibuf->mapped = 0;

    if (g_ibufs.mapped == ibuf)
        g_ibufs.mapped = ibuf->next;

    if (ibuf->prev)
        ibuf->prev->next = ibuf->next;
    if (ibuf->next)
        ibuf->next->prev = ibuf->prev;

    if (g_ibufs.baked)
        g_ibufs.baked->prev = ibuf;
    ibuf->prev = 0;
    ibuf->next = g_ibufs.baked;
    g_ibufs.baked = ibuf;
}

void ibuf_select(struct ibuf_t * ibuf)
{
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuf->buf_id);
}
