#ifndef _shy_injections_type_platform_static_array_data_included
#define _shy_injections_type_platform_static_array_data_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/static_array/type/data/shy_data_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/static_array/type/data/shy_data_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/static_array/type/data/shy_data_injections.h"
#endif

#endif
