#ifndef _shy_injections_type_platform_render_texture_loader_resource_id_included
#define _shy_injections_type_platform_render_texture_loader_resource_id_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/render/texture/loader/resource/id/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/render/texture/loader/resource/id/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/render/texture/loader/resource/id/type/shy_type_injections.h"
#endif

#endif
