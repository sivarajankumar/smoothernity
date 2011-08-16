#ifndef _shy_injections_lib_std_new_included
#define _shy_injections_lib_std_new_included

#ifdef shy_build_for_iphone
    #include "../../../../main/iphone/lib/std/new/shy_new_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../../main/macosx/lib/std/new/shy_new_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../../main/win/lib/std/new/shy_new_injections.h"
#endif

#endif
