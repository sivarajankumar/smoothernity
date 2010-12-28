#ifndef _shy_injections_platform_math_consts_included
#define _shy_injections_platform_math_consts_included

#ifdef build_for_macosx
    #include "../macosx/macosx_platform_math_consts.h"
    typedef shy_macosx_platform_math_consts so_called_platform_math_consts ;
#endif

#endif

