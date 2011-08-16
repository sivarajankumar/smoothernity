#ifndef _shy_injections_platform_render_texture_loader_included
#define _shy_injections_platform_render_texture_loader_included

#ifdef shy_build_for_iphone
    #include "../../../../main/iphone/platform/render/texture_loader/shy_texture_loader_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../../main/macosx/platform/render/texture_loader/shy_texture_loader_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../../main/win/platform/render/texture_loader/shy_texture_loader_injections.h"
#endif

#endif

