#ifndef _shy_injections_type_platform_render_index_data_included
#define _shy_injections_type_platform_render_index_data_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/render/index/data/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/render/index/data/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/render/index/data/type/shy_type_injections.h"
#endif

#endif
