#ifndef _shy_injections_platform_sound_included
#define _shy_injections_platform_sound_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/sound/shy_sound_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/sound/shy_sound_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/sound/shy_sound_injections.h"
#endif

#endif
