#pragma once

int vbuf_init(int size, int count);
void vbuf_done(void);

void vbuf_query(int *size, int *left);

int vbuf_alloc();
void vbuf_free(int vbuf);

struct vbuf_t * vbuf_get(int vbuf);
void vbuf_select(struct vbuf_t *);

void vbuf_write(int vbuf, int data,
                float x, float y, float z,
                float r, float g, float b, float a,
                float u, float v);
void vbuf_bake(int vbuf);
