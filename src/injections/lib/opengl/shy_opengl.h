#ifndef _shy_injections_lib_opengl_included
#define _shy_injections_lib_opengl_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/lib/opengl/shy_opengl_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/lib/opengl/shy_opengl_injections.h"
#endif

#endif
