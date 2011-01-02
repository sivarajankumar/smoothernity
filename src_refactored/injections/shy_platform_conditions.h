#ifndef _shy_injections_platform_conditions_included
#define _shy_injections_platform_conditions_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_conditions.h"
    typedef shy_macosx_platform_conditions so_called_platform_conditions ;
#endif

#endif
