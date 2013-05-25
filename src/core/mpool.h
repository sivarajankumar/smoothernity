#ifndef CORE_MPOOL_H
#define CORE_MPOOL_H

#include <string.h>

struct mpool_t;

struct mpool_t * mpool_create(const int sizes[], const int counts[], int len);
void mpool_destroy(struct mpool_t*);
void * mpool_alloc(struct mpool_t*, size_t);
void mpool_free(void*);

#endif /* CORE_MPOOL_H */

