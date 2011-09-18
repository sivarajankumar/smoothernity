#ifndef _shy_injections_lib_std_memcpy_included
#define _shy_injections_lib_std_memcpy_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/lib/std/memcpy/shy_memcpy_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/lib/std/memcpy/shy_memcpy_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/lib/std/memcpy/shy_memcpy_injections.h"
#endif

#endif
