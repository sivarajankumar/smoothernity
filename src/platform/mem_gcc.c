#include "mem.h"
#include <stdlib.h>

void * mem_alloc(size_t align, size_t size) {
    if (align & (align - 1) || align > _Alignof(max_align_t))
        return 0;
    return aligned_alloc(align, size);
}

void mem_free(void *ptr) {
    free(ptr);
}

