#ifndef _shy_injections_platform_static_assert_included
#define _shy_injections_platform_static_assert_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_static_assert.h"
    typedef shy_macosx_platform_static_assert so_called_platform_static_assert ;
#endif

#endif
