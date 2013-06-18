#ifndef PMEM_H
#define PMEM_H

#include <stddef.h>

#define PMEM_SIMD_ALIGN 16
#define PMEM_ALIGNOF _Alignof

void * pmem_alloc(size_t align, size_t size);
void pmem_free(void*);

#endif /* PMEM_H */

