#pragma once

int mpool_init(const int sizes[], const int counts[], int len);
void mpool_done(void);
void * mpool_alloc(int size);
void mpool_free(void *ptr);
