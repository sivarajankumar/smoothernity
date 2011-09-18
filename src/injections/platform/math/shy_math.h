#ifndef _shy_injections_platform_math_included
#define _shy_injections_platform_math_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/math/shy_math_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/math/shy_math_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/math/shy_math_injections.h"
#endif

#endif
