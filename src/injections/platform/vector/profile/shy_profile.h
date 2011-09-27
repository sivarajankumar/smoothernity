#ifndef _shy_injections_platform_vector_profile_included
#define _shy_injections_platform_vector_profile_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/vector/profile/shy_profile_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/vector/profile/shy_profile_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/vector/profile/shy_profile_injections.h"
#endif

#endif
