#ifndef PLATFORM_MEMORY_H
#define PLATFORM_MEMORY_H

#ifdef COMPILER_IS_GNU
    #define ALIGNOF alignof
#endif

#ifdef COMPILER_IS_MSVC
    #define ALIGNOF __alignof
#endif

#endif /* PLATFORM_MEMORY_H */

