#import <AudioToolbox/AudioToolbox.h>
#import <AudioToolbox/ExtendedAudioFile.h>
#import <Foundation/NSBundle.h>

@interface sound_loader : NSObject
{
}

- ( void ) load_16_bit_44100_khz_stereo_samples_from_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_max_samples_count_of : ( int ) max_samples_count
    put_loaded_samples_count_to : ( int * ) loaded_samples_count
    ;

@end
