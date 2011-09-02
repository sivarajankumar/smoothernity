#ifndef _shy_injections_type_platform_render_texture_id_included
#define _shy_injections_type_platform_render_texture_id_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/render/texture/id/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/render/texture/id/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/render/texture/id/type/shy_type_injections.h"
#endif

#endif
