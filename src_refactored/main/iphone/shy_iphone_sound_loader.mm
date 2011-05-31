#include "./iphone_sound_loader.h"

#include "../../injections/lib/std/false/shy_false.h"
#include "../../injections/lib/std/true/shy_true.h"

@implementation shy_iphone_sound_loader

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
    NSAutoreleasePool * pool = [ [ NSAutoreleasePool alloc ] init ] ;
    [ NSThread setThreadPriority : 0.0 ] ;
    while ( ! _should_quit )
    {
        [ NSThread sleepForTimeInterval : 0.1 ] ;
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
    NSBundle * bundle = [ NSBundle mainBundle ] ;
    CFURLRef file_url = ( CFURLRef ) [ [ NSURL fileURLWithPath : [ bundle 
        pathForResource : [ NSString stringWithFormat : @"stereo_sound_resource_%i" , _resource_index ] 
        ofType : @"mp3" 
        ] ] retain ] ;
        
    SInt64 file_length_in_frames = 0 ;
    AudioStreamBasicDescription file_format ;
    UInt32 property_size = sizeof ( file_format ) ;
    ExtAudioFileRef ext_ref = 0 ;
    AudioStreamBasicDescription output_format ;
                 
    ExtAudioFileOpenURL ( file_url , & ext_ref ) ;
    ExtAudioFileGetProperty ( ext_ref , kExtAudioFileProperty_FileDataFormat , & property_size , & file_format ) ;
                    
    output_format . mSampleRate = 44100 ;
    output_format . mChannelsPerFrame = 2 ;
    output_format . mFormatID = kAudioFormatLinearPCM ;
    output_format . mBytesPerPacket = 2 * output_format . mChannelsPerFrame ;
    output_format . mFramesPerPacket = 1 ;
    output_format . mBytesPerFrame = 2 * output_format . mChannelsPerFrame ;
    output_format . mBitsPerChannel = 16 ;
    output_format . mFormatFlags = kAudioFormatFlagsNativeEndian | kAudioFormatFlagIsPacked | kAudioFormatFlagIsSignedInteger ;
                    
    ExtAudioFileSetProperty ( ext_ref , kExtAudioFileProperty_ClientDataFormat , sizeof ( output_format ) , & output_format ) ;
    property_size = sizeof ( file_length_in_frames ) ;
    ExtAudioFileGetProperty ( ext_ref , kExtAudioFileProperty_FileLengthFrames , & property_size , & file_length_in_frames ) ;
    
    AudioBufferList data_buffer ;
    data_buffer . mNumberBuffers = 1 ;
    data_buffer . mBuffers [ 0 ] . mDataByteSize = file_length_in_frames * output_format . mBytesPerFrame ;
    data_buffer . mBuffers [ 0 ] . mNumberChannels = output_format . mChannelsPerFrame ;
    data_buffer . mBuffers [ 0 ] . mData = _buffer ;
    
    ExtAudioFileRead ( ext_ref , ( UInt32 * ) & file_length_in_frames , & data_buffer ) ;
    _loaded_samples_count = ( so_called_lib_std_int32_t ) file_length_in_frames ;
    ExtAudioFileDispose ( ext_ref ) ;
    CFRelease ( file_url ) ;
}

@end