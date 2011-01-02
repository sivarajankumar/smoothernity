#ifndef _shy_injections_platform_sound_included
#define _shy_injections_platform_sound_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_sound.h"
    typedef shy_macosx_platform_sound so_called_platform_sound ;
#endif

#endif
