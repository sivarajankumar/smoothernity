#ifndef PLATFORM_MEM_HPP
#define PLATFORM_MEM_HPP

#include <stddef.h>

#ifdef COMPILER_IS_GNU
    #define MEM_ALIGNOF alignof
#endif

#ifdef COMPILER_IS_MSVC
    #define MEM_ALIGNOF __alignof
#endif

extern "C" void * mem_alloc(size_t align, size_t size);
extern "C" void mem_free(void*);

#endif /* PLATFORM_MEM_HPP */

