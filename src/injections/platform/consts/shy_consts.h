#ifndef _shy_injections_platform_consts_included
#define _shy_injections_platform_consts_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/consts/shy_consts_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/consts/shy_consts_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/consts/shy_consts_injections.h"
#endif

#endif

