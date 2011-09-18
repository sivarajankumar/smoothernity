#ifndef _shy_injections_lib_std_set_included
#define _shy_injections_lib_std_set_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/lib/std/set/shy_set_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/lib/std/set/shy_set_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/lib/std/set/shy_set_injections.h"
#endif

#endif
