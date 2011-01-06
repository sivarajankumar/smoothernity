#ifndef _shy_type_macosx_platform_sound_sample_mono_included
#define _shy_type_macosx_platform_sound_sample_mono_included

#include <OpenAL/al.h>

class shy_type_macosx_platform_sound_sample_mono
{
    friend class shy_macosx_platform_sound ;
public :
    shy_type_macosx_platform_sound_sample_mono ( ) ;
private :
    ALubyte _value ;
} ;

#endif
