#ifndef _shy_injections_platform_conditions_included
#define _shy_injections_platform_conditions_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/conditions/shy_conditions_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/conditions/shy_conditions_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/conditions/shy_conditions_injections.h"
#endif

#endif
