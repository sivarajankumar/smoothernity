#pragma once

int ibuf_init(int size, int count, int len);
void ibuf_done(void);

void ibuf_query(int *size, int *left, int *with_meshes);

int ibuf_alloc(void);
void ibuf_free(int ibuf);

void ibuf_write(int ibuf, int data, int index);
void ibuf_bake(int ibuf);
