#ifndef _shy_injections_platform_static_assert_included
#define _shy_injections_platform_static_assert_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/static/assert/shy_assert_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/static/assert/shy_assert_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/static/assert/shy_assert_injections.h"
#endif

#endif
