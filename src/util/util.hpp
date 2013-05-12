#pragma once

#include <stdlib.h>

extern "C"
void * util_malloc(size_t align, size_t size);

extern "C"
void util_free(void*);
