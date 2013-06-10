#include "util.h"

void * util_malloc(size_t align, size_t size) {
    void *mem, **ptr;
    size_t addr;
    if (align & (align - 1) ||
    (mem = malloc(size + align + sizeof(void*))) == NULL)
        return 0;
    addr = (char*)mem - (char*)0;
    addr = (addr + align + sizeof(void*)) & ~(align - 1);
    ptr = (void**)((char*)0 + addr);
    ptr[-1] = mem;
    return ptr;
}

void util_free(void *ptr) {
    free(((void**)ptr)[-1]);
}

