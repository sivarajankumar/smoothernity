#ifndef _shy_injections_platform_mouse_included
#define _shy_injections_platform_mouse_included

#ifdef shy_build_for_macosx
    #include "../macosx/shy_macosx_platform_mouse.h"
    typedef shy_macosx_platform_mouse so_called_platform_mouse ;
#endif

#endif
