#include "./shy_macosx_sound_loader.h"

#include "../../injections/lib/cocoa/shy_cocoa.h"
#include "../../injections/lib/std/false/shy_false.h"
#include "../../injections/lib/std/float/shy_float.h"
#include "../../injections/lib/std/true/shy_true.h"

namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_float sleep_delay = 0.1f ;
    }
}

@implementation shy_macosx_sound_loader

- ( id ) init
{
    self = [ super init ] ;
    _is_ready = so_called_lib_std_true ;
    _should_quit = so_called_lib_std_false ;
    _resource_index = 0 ;
    _buffer = 0 ;
    _max_samples_count = 0 ;
    _loaded_samples_count = 0 ;
    return self ;
}

- ( void ) dealloc
{
    [ super dealloc ] ;
}

- ( so_called_lib_std_bool ) loader_ready
{
    return _is_ready ;
}

- ( so_called_lib_std_int32_t ) loaded_samples_count
{
    return _loaded_samples_count ;
}

- ( void ) thread_run
{
    [ self performSelectorInBackground : @selector ( _thread_main_method ) withObject : nil ] ;
}

- ( void ) thread_stop
{
    _should_quit = so_called_lib_std_true ;
}

- ( void ) load_16_bit_44100_khz_stereo_samples_from_resource : ( so_called_lib_std_int32_t ) resource_index
    to_buffer : ( void * ) buffer
    with_max_samples_count_of : ( so_called_lib_std_int32_t ) max_samples_count
{
    if ( _is_ready )
    {
        _resource_index = resource_index ;
        _buffer = buffer ;
        _max_samples_count = max_samples_count ;
        _loaded_samples_count = 0 ;
        _is_ready = so_called_lib_std_false ;
    }
}

- ( void ) _thread_main_method
{
    so_called_lib_cocoa_NSAutoreleasePool * pool = [ [ so_called_lib_cocoa_NSAutoreleasePool alloc ] init ] ;
    while ( ! _should_quit )
    {
        [ so_called_lib_cocoa_NSThread sleepForTimeInterval : shy_guts :: consts :: sleep_delay ] ;
        if ( ! _is_ready )
        {
            [ self _perform_load ] ;
            _is_ready = so_called_lib_std_true ;
        }
    }
    [ pool release ] ;
    [ self release ] ;
}

- ( void ) _perform_load
{
    so_called_lib_cocoa_NSBundle * bundle = [ so_called_lib_cocoa_NSBundle mainBundle ] ;
    so_called_lib_cocoa_CFURLRef file_url = ( so_called_lib_cocoa_CFURLRef ) 
        [ 
            [ so_called_lib_cocoa_NSURL 
                fileURLWithPath : 
                    [ bundle 
                        pathForResource : 
                            [ so_called_lib_cocoa_NSString stringWithFormat : @"stereo_sound_resource_%i" 
                                , ( so_called_lib_std_int32_t ) _resource_index 
                            ] 
                        ofType : @"mp3" 
                    ] 
            ] retain 
        ] ;
        
    so_called_lib_cocoa_SInt64 file_length_in_frames = 0 ;
    so_called_lib_cocoa_AudioStreamBasicDescription file_format ;
    so_called_lib_cocoa_AudioStreamBasicDescription output_format ;
    so_called_lib_cocoa_UInt32 property_size = sizeof ( file_format ) ;
    so_called_lib_cocoa_ExtAudioFileRef ext_ref = 0 ;
    so_called_lib_cocoa_AudioBufferList data_buffer ;
                 
    so_called_lib_cocoa_ExtAudioFileOpenURL ( file_url , & ext_ref ) ;
    so_called_lib_cocoa_ExtAudioFileGetProperty 
        ( ext_ref 
        , so_called_lib_cocoa_kExtAudioFileProperty_FileDataFormat 
        , & property_size 
        , & file_format 
        ) ;

    output_format . mSampleRate = 44100 ;
    output_format . mChannelsPerFrame = 2 ;
    output_format . mFormatID = so_called_lib_cocoa_kAudioFormatLinearPCM ;
    output_format . mBytesPerPacket = 2 * output_format . mChannelsPerFrame ;
    output_format . mFramesPerPacket = 1 ;
    output_format . mBytesPerFrame = 2 * output_format . mChannelsPerFrame ;
    output_format . mBitsPerChannel = 16 ;
    output_format . mFormatFlags 
        = so_called_lib_cocoa_kAudioFormatFlagsNativeEndian
        | so_called_lib_cocoa_kAudioFormatFlagIsPacked
        | so_called_lib_cocoa_kAudioFormatFlagIsSignedInteger
        ;
    so_called_lib_cocoa_ExtAudioFileSetProperty
        ( ext_ref 
        , so_called_lib_cocoa_kExtAudioFileProperty_ClientDataFormat 
        , sizeof ( output_format ) 
        , & output_format 
        ) ;

    property_size = sizeof ( file_length_in_frames ) ;
    so_called_lib_cocoa_ExtAudioFileGetProperty 
        ( ext_ref 
        , so_called_lib_cocoa_kExtAudioFileProperty_FileLengthFrames
        , & property_size
        , & file_length_in_frames
        ) ;
    
    data_buffer . mNumberBuffers = 1 ;
    data_buffer . mBuffers [ 0 ] . mDataByteSize = ( so_called_lib_std_int32_t ) ( file_length_in_frames ) * output_format . mBytesPerFrame ;
    data_buffer . mBuffers [ 0 ] . mNumberChannels = output_format . mChannelsPerFrame ;
    data_buffer . mBuffers [ 0 ] . mData = _buffer ;
    
    so_called_lib_cocoa_ExtAudioFileRead 
        ( ext_ref 
        , ( so_called_lib_cocoa_UInt32 * ) & file_length_in_frames 
        , & data_buffer 
        ) ;
    _loaded_samples_count = ( so_called_lib_std_int32_t ) file_length_in_frames ;
    so_called_lib_cocoa_ExtAudioFileDispose ( ext_ref ) ;
    so_called_lib_cocoa_CFRelease ( file_url ) ;
}

@end
