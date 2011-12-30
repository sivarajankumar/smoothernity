#ifndef _shy_injections_type_platform_pointer_data_included
#define _shy_injections_type_platform_pointer_data_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/pointer/data/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/pointer/data/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/pointer/data/type/shy_type_injections.h"
#endif

#endif
