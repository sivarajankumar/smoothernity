#ifndef _shy_injections_lib_cocoa_included
#define _shy_injections_lib_cocoa_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/lib/cocoa/shy_cocoa_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/lib/cocoa/shy_cocoa_injections.h"
#endif

#endif
