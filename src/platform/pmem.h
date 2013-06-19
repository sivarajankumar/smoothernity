#ifndef PMEM_H
#define PMEM_H

#include <stddef.h>

#define PMEM_ALIGN_SIMD 16
#define PMEM_ALIGNOF _Alignof
#define PMEM_ALIGNAS _Alignas

void * pmem_alloc(size_t align, size_t size);
void pmem_free(void*);

#endif /* PMEM_H */

