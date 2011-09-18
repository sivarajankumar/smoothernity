#ifndef _shy_injections_platform_vector_included
#define _shy_injections_platform_vector_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/vector/shy_vector_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/vector/shy_vector_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/vector/shy_vector_injections.h"
#endif

#endif
