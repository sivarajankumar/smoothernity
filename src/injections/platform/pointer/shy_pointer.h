#ifndef _shy_injections_platform_pointer_included
#define _shy_injections_platform_pointer_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/pointer/shy_pointer_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/pointer/shy_pointer_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/pointer/shy_pointer_injections.h"
#endif

#endif
