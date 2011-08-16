#ifndef _shy_injections_lib_std_cout_included
#define _shy_injections_lib_std_cout_included

#ifdef shy_build_for_iphone
    #include "../../../../main/iphone/lib/std/cout/shy_cout_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../../main/macosx/lib/std/cout/shy_cout_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../../main/win/lib/std/cout/shy_cout_injections.h"
#endif

#endif
