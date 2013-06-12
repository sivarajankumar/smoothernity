#ifndef PMEM_HPP
#define PMEM_HPP

#include <stddef.h>

#ifdef COMPILER_IS_GNU
    #define PMEM_ALIGNOF alignof
#endif

#ifdef COMPILER_IS_MSVC
    #define PMEM_ALIGNOF __alignof
#endif

extern "C" void * pmem_alloc(size_t align, size_t size);
extern "C" void pmem_free(void*);

#endif /* PMEM_HPP */

