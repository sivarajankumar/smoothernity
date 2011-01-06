#ifndef _shy_type_macosx_platform_sound_sample_stereo_included
#define _shy_type_macosx_platform_sound_sample_stereo_included

#include <OpenAL/al.h>

class shy_type_macosx_platform_sound_sample_stereo
{
    friend class shy_macosx_platform_sound ;
public :
    shy_type_macosx_platform_sound_sample_stereo ( ) ;
private :
    ALushort _left_channel_value ;
    ALushort _right_channel_value ; 
} ;

#endif
