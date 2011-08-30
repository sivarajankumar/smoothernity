#ifndef _shy_injections_type_platform_render_index_data_included
#define _shy_injections_type_platform_render_index_data_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/render/type/index_data/shy_index_data_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/render/type/index_data/shy_index_data_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/render/type/index_data/shy_index_data_injections.h"
#endif

#endif
