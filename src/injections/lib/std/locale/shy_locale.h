#ifndef _shy_injections_lib_std_locale_included
#define _shy_injections_lib_std_locale_included

#ifdef shy_build_for_iphone
    #include "main/iphone/lib/std/locale/shy_locale_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/lib/std/locale/shy_locale_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/lib/std/locale/shy_locale_injections.h"
#endif

#endif
