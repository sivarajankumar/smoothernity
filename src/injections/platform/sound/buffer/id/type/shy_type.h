#ifndef _shy_injections_type_platform_sound_buffer_id_included
#define _shy_injections_type_platform_sound_buffer_id_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/sound/buffer/id/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/sound/buffer/id/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/sound/buffer/id/type/shy_type_injections.h"
#endif

#endif
