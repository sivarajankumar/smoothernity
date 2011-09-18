#ifndef _shy_injections_platform_matrix_included
#define _shy_injections_platform_matrix_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/matrix/shy_matrix_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/matrix/shy_matrix_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/matrix/shy_matrix_injections.h"
#endif

#endif
