#ifndef _shy_injections_lib_std_false_included
#define _shy_injections_lib_std_false_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/lib/std/false/shy_false_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/lib/std/false/shy_false_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/lib/std/false/shy_false_injections.h"
#endif

#endif
