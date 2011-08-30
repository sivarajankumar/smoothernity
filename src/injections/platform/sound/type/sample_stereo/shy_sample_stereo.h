#ifndef _shy_injections_type_platform_sound_sample_stereo_included
#define _shy_injections_type_platform_sound_sample_stereo_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/sound/type/sample_stereo/shy_sample_stereo_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/sound/type/sample_stereo/shy_sample_stereo_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/sound/type/sample_stereo/shy_sample_stereo_injections.h"
#endif

#endif

