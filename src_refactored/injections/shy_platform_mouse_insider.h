#ifndef _shy_injections_platform_mouse_insider_included
#define _shy_injections_platform_mouse_insider_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_mouse_insider.h"
    typedef shy_macosx_platform_mouse_insider so_called_platform_mouse_insider ;
#endif

#endif

