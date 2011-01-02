#ifndef _shy_injections_platform_static_array_included
#define _shy_injections_platform_static_array_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_static_array.h"
    typedef shy_macosx_platform_static_array so_called_platform_static_array ;
#endif

#endif
