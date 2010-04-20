#import <AudioToolbox/AudioToolbox.h>
#import <AudioToolbox/ExtendedAudioFile.h>
#import <Foundation/NSBundle.h>

@interface shy_macosx_sound_loader : NSObject
{
@private
    bool _is_ready ;
    int _resource_index ;
    void * _buffer ;
    int _max_samples_count ;
    int * _loaded_samples_count ;
}

- ( bool ) loader_ready ;
- ( void ) load_16_bit_44100_khz_stereo_samples_from_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_max_samples_count_of : ( int ) max_samples_count
    put_loaded_samples_count_to : ( int * ) loaded_samples_count
    ;
- ( void ) _thread_main_method ;

@end
