#ifndef _shy_injections_platform_conditions_included
#define _shy_injections_platform_conditions_included

#ifdef shy_build_for_iphone
    #include "../../../main/iphone/platform/conditions/shy_conditions_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../main/macosx/platform/conditions/shy_conditions_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../main/win/platform/conditions/shy_conditions_injections.h"
#endif

#endif
