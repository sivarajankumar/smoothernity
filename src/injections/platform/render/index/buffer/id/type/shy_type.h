#ifndef _shy_injections_type_platform_render_index_buffer_id_included
#define _shy_injections_type_platform_render_index_buffer_id_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/render/index/buffer/id/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/render/index/buffer/id/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/render/index/buffer/id/type/shy_type_injections.h"
#endif

#endif
