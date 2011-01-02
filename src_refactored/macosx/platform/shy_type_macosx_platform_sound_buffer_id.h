#ifndef _shy_type_macosx_platform_sound_buffer_id_included
#define _shy_type_macosx_platform_sound_buffer_id_included

#include <OpenAL/al.h>

class shy_type_macosx_platform_sound_buffer_id
{
    friend class shy_macosx_platform_sound ;
public :
    shy_type_macosx_platform_sound_buffer_id ( ) ;
private :
    ALuint _buffer_id ;
} ;

#endif
