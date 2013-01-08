#pragma once

int ibuf_init(int sizes[], int counts[], int len);
void ibuf_done(void);

int ibuf_alloc(int size);
void ibuf_free(int buf);

void ibuf_write(int ibuf, int i, int v);
void ibuf_bake(int ibuf);
