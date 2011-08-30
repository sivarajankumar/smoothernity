#ifndef _shy_injections_lib_std_bool_included
#define _shy_injections_lib_std_bool_included

#ifdef shy_build_for_iphone
    #include "main/iphone/lib/std/bool/shy_bool_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/lib/std/bool/shy_bool_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/lib/std/bool/shy_bool_injections.h"
#endif

#endif
