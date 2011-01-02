#ifndef _shy_injections_platform_pointer_included
#define _shy_injections_platform_pointer_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_pointer.h"
    typedef shy_macosx_platform_pointer so_called_platform_pointer ;
#endif

#endif
