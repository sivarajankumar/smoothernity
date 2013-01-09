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
    int frame_tag; /* when this space was last updated */
    int vacant;
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
};

extern struct spaces_t g_spaces;

enum mesh_type_e
{
    MESH_TRIANGLE_STRIP = 0,
    MESH_TRIANGLE_FAN = 1,
    MESH_TRIANGLES = 2,
    MESH_TYPES_TOTAL = 3
};

struct mesh_t
{
    struct ibuf_t *ibuf;
    struct vbuf_t *vbuf;
    struct space_t *space;
    enum mesh_type_e type;
    int vacant;

    struct mesh_t *vbuf_prev;
    struct mesh_t *vbuf_next;

    struct mesh_t *ibuf_prev;
    struct mesh_t *ibuf_next;

    struct mesh_t *prev;
    struct mesh_t *next;
};

struct meshes_t
{
    int left;
    int count;
    struct mesh_t *pool;
    struct mesh_t *vacant;
};

extern struct meshes_t g_meshes;
