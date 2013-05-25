#ifndef UTIL_UTIL_H
#define UTIL_UTIL_H

#include <stdlib.h>

void * util_malloc(size_t align, size_t size);
void util_free(void*);

#endif /* UTIL_UTIL_H */

