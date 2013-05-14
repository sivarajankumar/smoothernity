#pragma once

#ifdef COMPILER_IS_GNU
    #define ALIGNOF alignof
#endif

#ifdef COMPILER_IS_MSVC
    #define ALIGNOF __alignof
#endif

