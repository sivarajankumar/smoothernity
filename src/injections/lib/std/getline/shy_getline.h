#ifndef _shy_injections_lib_std_getline_included
#define _shy_injections_lib_std_getline_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/lib/std/getline/shy_getline_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/lib/std/getline/shy_getline_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/lib/std/getline/shy_getline_injections.h"
#endif

#endif
