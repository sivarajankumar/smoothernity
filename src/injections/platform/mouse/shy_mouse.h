#ifndef _shy_injections_platform_mouse_included
#define _shy_injections_platform_mouse_included

#ifdef shy_build_for_iphone
    #include "../../../main/iphone/platform/mouse/shy_mouse_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../main/macosx/platform/mouse/shy_mouse_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../main/win/platform/mouse/shy_mouse_injections.h"
#endif

#endif
