#pragma once

#include <string.h>

struct mpool_t;

void * mpool_alloc(struct mpool_t *pool, void *ptr, size_t osize, size_t nsize);
struct mpool_t * mpool_create(const int sizes[], const int counts[], int len);
void mpool_destroy(struct mpool_t *pool);
void mpool_print(struct mpool_t *pool);
