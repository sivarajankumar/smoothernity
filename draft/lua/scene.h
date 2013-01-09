#pragma once

#include <GL/gl.h>

struct vbuf_t
{
    GLuint buf_id;
    void * mapped;
    int vacant;
    struct vbuf_t * prev;
    struct vbuf_t * next;
    struct mesh_t * meshes;
};

struct vbufs_t
{
    int size;
    int count;
    int left;
    int with_meshes;
    struct vbuf_t * pool;
    struct vbuf_t * vacant;
    struct vbuf_t * mapped;
    struct vbuf_t * baked;
};

extern struct vbufs_t g_vbufs;

struct ibuf_t
{
    GLuint buf_id;
    void * mapped;
    int vacant;
    struct ibuf_t * prev;
    struct ibuf_t * next;
    struct mesh_t * meshes;
};

struct ibufs_t
{
    int size;
    int count;
    int left;
    int with_meshes;
    struct ibuf_t * pool;
    struct ibuf_t * vacant;
    struct ibuf_t * mapped;
    struct ibuf_t * baked;
};

extern struct ibufs_t g_ibufs;
