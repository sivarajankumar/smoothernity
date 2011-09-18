#ifndef _shy_injections_type_platform_sound_sample_mono_included
#define _shy_injections_type_platform_sound_sample_mono_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/sound/sample/mono/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/sound/sample/mono/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/sound/sample/mono/type/shy_type_injections.h"
#endif

#endif

