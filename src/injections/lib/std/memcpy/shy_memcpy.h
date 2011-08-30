#ifndef _shy_injections_lib_std_memcpy_included
#define _shy_injections_lib_std_memcpy_included

#ifdef shy_build_for_iphone
    #include "main/iphone/lib/std/memcpy/shy_memcpy_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/lib/std/memcpy/shy_memcpy_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/lib/std/memcpy/shy_memcpy_injections.h"
#endif

#endif
