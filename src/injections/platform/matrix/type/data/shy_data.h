#ifndef _shy_injections_type_platform_matrix_data_included
#define _shy_injections_type_platform_matrix_data_included

#ifdef shy_build_for_iphone
    #include "../../../../../main/iphone/platform/matrix/type/data/shy_data_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../../../main/macosx/platform/matrix/type/data/shy_data_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../../../main/win/platform/matrix/type/data/shy_data_injections.h"
#endif

#endif
