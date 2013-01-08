#pragma once

int vbuf_init(int sizes[], int counts[], int len);
void vbuf_done(void);

int vbuf_alloc(int size);
void vbuf_free(int buf);

void vbuf_write(int vbuf, int i,
                float x, float y, float z,
                float r, float g, float b, float a,
                float u, float v);
void vbuf_bake(int vbuf);
