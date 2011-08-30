#ifndef _shy_injections_lib_std_cerr_included
#define _shy_injections_lib_std_cerr_included

#ifdef shy_build_for_iphone
    #include "main/iphone/lib/std/cerr/shy_cerr_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/lib/std/cerr/shy_cerr_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/lib/std/cerr/shy_cerr_injections.h"
#endif

#endif
