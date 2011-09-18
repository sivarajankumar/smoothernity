#ifndef _shy_injections_platform_vector_insider_included
#define _shy_injections_platform_vector_insider_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/vector/insider/shy_insider_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/vector/insider/shy_insider_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/vector/insider/shy_insider_injections.h"
#endif

#endif
