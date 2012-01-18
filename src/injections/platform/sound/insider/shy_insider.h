#ifndef _shy_injections_platform_sound_insider_included
#define _shy_injections_platform_sound_insider_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/sound/insider/shy_insider_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/sound/insider/shy_insider_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/sound/insider/shy_insider_injections.h"
#endif

#endif

