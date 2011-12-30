#ifndef _shy_injections_lib_openal_included
#define _shy_injections_lib_openal_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/lib/openal/shy_openal_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/lib/openal/shy_openal_injections.h"
#endif

#endif

