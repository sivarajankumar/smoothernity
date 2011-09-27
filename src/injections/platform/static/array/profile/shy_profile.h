#ifndef _shy_injections_platform_static_array_profile_included
#define _shy_injections_platform_static_array_profile_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/static/array/profile/shy_profile_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/static/array/profile/shy_profile_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/static/array/profile/shy_profile_injections.h"
#endif

#endif
