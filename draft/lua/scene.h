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

struct vbuf_data_t
{
    GLfloat pos[3];
    GLfloat tex[2];
    GLubyte color[4];
};

struct vbufs_t
{
    int size;
    int count;
    int left;
    int with_meshes;
    void *offset_pos;
    void *offset_tex;
    void *offset_color;
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

struct ibuf_data_t
{
    GLushort index;
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

enum space_axis_e
{
    SPACE_AXIS_X = 0,
    SPACE_AXIS_Y = 1,
    SPACE_AXIS_Z = 2,
    SPACE_AXES_TOTAL = 3
};

struct space_t
{
    int frame_tag; /* when this space was last updated */
    int vacant;
    GLfloat matrix[16];
    float offset[3];
    float scale[3];
    float rotangle;
    enum space_axis_e rotaxis;
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

struct mesh_t
{
    struct ibuf_t *ibuf;
    struct vbuf_t *vbuf;
    struct space_t *space;
    GLenum type;
    int ioffset;
    int icount;
    int vacant;
    int frame_tag; /* when this mesh was last drawn */

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
