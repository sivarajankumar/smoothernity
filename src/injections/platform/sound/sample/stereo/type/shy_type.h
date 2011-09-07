#ifndef _shy_injections_type_platform_sound_sample_stereo_included
#define _shy_injections_type_platform_sound_sample_stereo_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/sound/sample/stereo/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/sound/sample/stereo/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/sound/sample/stereo/type/shy_type_injections.h"
#endif

#endif
