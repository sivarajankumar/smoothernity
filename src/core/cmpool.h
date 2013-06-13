#ifndef CMPOOL_H
#define CMPOOL_H

#include <stddef.h>

struct cmpool_t;

struct cmpool_t * cmpool_create(const int sizes[], const int counts[], int len);
void cmpool_destroy(struct cmpool_t*);
void * cmpool_alloc(struct cmpool_t*, size_t);
void cmpool_free(void*);

#endif /* CMPOOL_H */

