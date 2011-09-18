#ifndef _shy_injections_lib_std_true_included
#define _shy_injections_lib_std_true_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/lib/std/true/shy_true_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/lib/std/true/shy_true_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/lib/std/true/shy_true_injections.h"
#endif

#endif
