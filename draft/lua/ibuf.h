#pragma once

int ibuf_init(int size, int count);
void ibuf_done(void);

void ibuf_query(int *size, int *left);

int ibuf_alloc(void);
void ibuf_free(int ibuf);

struct ibuf_t * ibuf_get(int ibuf);
void ibuf_select(struct ibuf_t *);

void ibuf_write(int ibuf, int data, int index);
void ibuf_bake(int ibuf);
