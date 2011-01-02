#ifndef _shy_injections_type_platform_sound_buffer_id_included
#define _shy_injections_type_platform_sound_buffer_id_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_type_macosx_platform_sound_buffer_id.h"
    typedef shy_type_macosx_platform_sound_buffer_id so_called_type_platform_sound_buffer_id ;
#endif

#endif
