#ifndef _shy_injections_platform_static_array_included
#define _shy_injections_platform_static_array_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/static/array/shy_array_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/static/array/shy_array_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/static/array/shy_array_injections.h"
#endif

#endif
