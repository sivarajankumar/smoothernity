#ifndef _shy_injections_type_platform_vector_data_included
#define _shy_injections_type_platform_vector_data_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/vector/data/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/vector/data/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/vector/data/type/shy_type_injections.h"
#endif

#endif
