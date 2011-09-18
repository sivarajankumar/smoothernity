#ifndef _shy_injections_platform_touch_included
#define _shy_injections_platform_touch_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/touch/shy_touch_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/touch/shy_touch_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/touch/shy_touch_injections.h"
#endif

#endif
