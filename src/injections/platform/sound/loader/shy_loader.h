#ifndef _shy_injections_platform_sound_loader_included
#define _shy_injections_platform_sound_loader_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/sound/loader/shy_loader_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/sound/loader/shy_loader_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/sound/loader/shy_loader_injections.h"
#endif

#endif

