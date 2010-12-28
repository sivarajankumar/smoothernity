#ifndef _shy_injections_platform_math_included
#define _shy_injections_platform_math_included

#ifdef shy_build_for_macosx
    #include "../macosx/macosx_platform_math.h"
    typedef shy_macosx_platform_math so_called_platform_math ;
#endif

#endif
