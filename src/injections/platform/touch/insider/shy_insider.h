#ifndef _shy_injections_platform_touch_insider_included
#define _shy_injections_platform_touch_insider_included

#ifdef shy_build_for_iphone
    #include "../../../../main/iphone/platform/touch/insider/shy_insider_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../../main/macosx/platform/touch/insider/shy_insider_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../../main/win/platform/touch/insider/shy_insider_injections.h"
#endif

#endif