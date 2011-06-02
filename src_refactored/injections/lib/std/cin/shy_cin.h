#ifndef _shy_injections_lib_std_cin_included
#define _shy_injections_lib_std_cin_included

#ifdef shy_build_for_iphone
    #include "../../../../main/iphone/lib/std/cin/shy_cin_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../../main/macosx/lib/std/cin/shy_cin_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../../main/win/lib/std/cin/shy_cin_injections.h"
#endif

#endif
