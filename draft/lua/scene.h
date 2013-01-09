#pragma once

#include <GL/gl.h>

struct vbuf_t
{
    GLuint buf_id;
    GLvoid *mapped;
    int vacant;
    struct vbuf_t *prev;
    struct vbuf_t *next;
    struct mesh_t *meshes;
};

struct vbufs_t
{
    int size;
    int count;
    int left;
    int with_meshes;
    struct vbuf_t *pool;
    struct vbuf_t *vacant;
    struct vbuf_t *mapped;
    struct vbuf_t *baked;
};

extern struct vbufs_t g_vbufs;

struct ibuf_t
{
    GLuint buf_id;
    GLvoid *mapped;
    int vacant;
    struct ibuf_t *prev;
    struct ibuf_t *next;
    struct mesh_t *meshes;
};

struct ibufs_t
{
    int size;
    int count;
    int left;
    int with_meshes;
    struct ibuf_t *pool;
    struct ibuf_t *vacant;
    struct ibuf_t *mapped;
    struct ibuf_t *baked;
};

extern struct ibufs_t g_ibufs;

struct space_t
{
    int tag; /* when this space was last updated */
    GLfloat matrix[16];
    float offset[3];
    float scale[3];
    float rotaxis[3];
    float rotangle;
    int offset_tween[3];
    int scale_tween[3];
    int rotangle_tween;
    struct space_t *prev;
    struct space_t *next;
};

struct spaces_t
{
    int left;
    int count;
    struct space_t *pool;
    struct space_t *vacant;
    struct space_t *active;
};

extern struct spaces_t g_spaces;
