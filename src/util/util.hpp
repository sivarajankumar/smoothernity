#ifndef UTIL_UTIL_HPP
#define UTIL_UTIL_HPP

#include <stdlib.h>

extern "C" void * util_malloc(size_t align, size_t size);
extern "C" void util_free(void*);

#endif /* UTIL_UTIL_HPP */

