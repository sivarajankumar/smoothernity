#ifndef _shy_injections_platform_render_included
#define _shy_injections_platform_render_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_render.h"
    typedef shy_macosx_platform_render so_called_platform_render ;
#endif

#endif
