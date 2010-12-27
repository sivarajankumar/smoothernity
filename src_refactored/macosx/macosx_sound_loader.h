#ifndef _macosx_sound_loader_included
#define _macosx_sound_loader_included

#include <AudioToolbox/AudioToolbox.h>
#include <AudioToolbox/ExtendedAudioFile.h>
#include <Foundation/NSBundle.h>

@interface shy_macosx_sound_loader : NSObject
{
@private
    bool _is_ready ;
    bool _should_quit ;
    int _resource_index ;
    void * _buffer ;
    int _max_samples_count ;
    int _loaded_samples_count ;
}

- ( void ) thread_run ;
- ( void ) thread_stop ;
- ( bool ) loader_ready ;
- ( int ) loaded_samples_count ;
- ( void ) load_16_bit_44100_khz_stereo_samples_from_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_max_samples_count_of : ( int ) max_samples_count
    ;
- ( void ) _thread_main_method ;
- ( void ) _perform_load ;

@end

#endif
