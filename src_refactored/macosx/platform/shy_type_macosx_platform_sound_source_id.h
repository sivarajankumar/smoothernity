#ifndef _shy_type_macosx_platform_sound_source_id_included
#define _shy_type_macosx_platform_sound_source_id_included

#include <OpenAL/al.h>

class shy_type_macosx_platform_sound_source_id
{
    friend class shy_macosx_platform_sound ;
public :
    shy_type_macosx_platform_sound_source_id ( ) ;
private :
    ALuint _source_id ;
} ;

#endif
