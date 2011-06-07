#ifndef _shy_injections_platform_math_included
#define _shy_injections_platform_math_included

#ifdef shy_build_for_iphone
    #include "../../../main/iphone/platform/math/shy_math_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../main/macosx/platform/math/shy_math_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../main/win/platform/math/shy_math_injections.h"
#endif

#endif