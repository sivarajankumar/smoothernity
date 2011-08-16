#ifndef _shy_injections_platform_render_included
#define _shy_injections_platform_render_included

#ifdef shy_build_for_iphone
    #include "../../../main/iphone/platform/render/shy_render_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../main/macosx/platform/render/shy_render_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../main/win/platform/render/shy_render_injections.h"
#endif

#endif
