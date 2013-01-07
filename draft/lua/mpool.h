#pragma once

#include <string.h>

struct mpool_t;

void * mpool_alloc(struct mpool_t *pool, void *ptr, size_t osize, size_t nsize);
int mpool_create(struct mpool_t **pool, const size_t sizes[], const size_t counts[], size_t len);
void mpool_destroy(struct mpool_t *pool);
void mpool_print(struct mpool_t *pool);
