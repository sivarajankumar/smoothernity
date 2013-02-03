#pragma once

#include <string.h>

int mpool_init(const int sizes[], const int counts[], int len);
void mpool_done(void);
void * mpool_alloc(size_t size);
void mpool_free(void *ptr);
