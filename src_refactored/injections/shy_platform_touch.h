#ifndef _shy_injections_platform_touch_included
#define _shy_injections_platform_touch_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_touch.h"
    typedef shy_macosx_platform_touch so_called_platform_touch ;
#endif

#endif

