#ifndef _shy_injections_type_platform_render_index_buffer_mapped_data_included
#define _shy_injections_type_platform_render_index_buffer_mapped_data_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/render/index/buffer/mapped/data/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/render/index/buffer/mapped/data/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/render/index/buffer/mapped/data/type/shy_type_injections.h"
#endif

#endif
