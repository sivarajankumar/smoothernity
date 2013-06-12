#ifndef PLATFORM_MEM_H
#define PLATFORM_MEM_H

#include <stddef.h>

#define MEM_ALIGNOF _Alignof

void * mem_alloc(size_t align, size_t size);
void mem_free(void*);

#endif /* PLATFORM_MEM_H */

