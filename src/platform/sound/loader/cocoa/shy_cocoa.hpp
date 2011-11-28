@class shy_guts_platform_sound_loader_cocoa_type ;

namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char resource_name_extension [ ] = "mp3" ;
        static const so_called_lib_std_char resource_name_prefix [ ] = "stereo_sound_resource_" ;
        static const so_called_lib_std_float sleep_delay = 0.1f ;
        static const so_called_lib_std_int32_t sound_bits_per_channel = 16 ;
        static const so_called_lib_std_int32_t sound_bytes_per_channel = 2 ;
        static const so_called_lib_std_int32_t sound_channels_per_frame = 2 ;
        static const so_called_lib_std_int32_t sound_frames_per_packet = 1 ;
        static const so_called_lib_std_int32_t sound_sample_rate = 44100 ;
    }
    static shy_guts_platform_sound_loader_cocoa_type * loader = 0 ;
}

@interface shy_guts_platform_sound_loader_cocoa_type : so_called_lib_cocoa_NSObject
{
@private
    so_called_lib_std_bool _is_ready ;
    so_called_lib_std_bool _should_quit ;
    so_called_lib_std_int32_t _resource_index ;
    void * _buffer ;
    so_called_lib_std_int32_t _max_samples_count ;
    so_called_lib_std_int32_t _loaded_samples_count ;
}
- ( void ) thread_run ;
- ( void ) thread_stop ;
- ( so_called_lib_std_bool ) loader_ready ;
- ( so_called_lib_std_int32_t ) loaded_samples_count ;
- ( void ) load_16_bit_44100_khz_stereo_samples_from_resource : ( so_called_lib_std_int32_t ) resource_index
    to_buffer : ( void * ) buffer
    with_max_samples_count_of : ( so_called_lib_std_int32_t ) max_samples_count
    ;
- ( void ) _thread_main_method ;
- ( void ) _perform_load ;
@end

@implementation shy_guts_platform_sound_loader_cocoa_type

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
                            [ so_called_lib_cocoa_NSString stringWithFormat : @"%s%i"
                                , shy_guts :: consts :: resource_name_prefix 
                                , ( so_called_lib_std_int32_t ) _resource_index 
                            ] 
                        ofType : 
                            [ so_called_lib_cocoa_NSString stringWithFormat : @"%s"
                                , shy_guts :: consts :: resource_name_extension
                            ]
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

    output_format . mSampleRate = shy_guts :: consts :: sound_sample_rate ;
    output_format . mChannelsPerFrame = shy_guts :: consts :: sound_channels_per_frame ;
    output_format . mFormatID = so_called_lib_cocoa_kAudioFormatLinearPCM ;
    output_format . mBytesPerPacket = shy_guts :: consts :: sound_bytes_per_channel * output_format . mChannelsPerFrame ;
    output_format . mFramesPerPacket = shy_guts :: consts :: sound_frames_per_packet ;
    output_format . mBytesPerFrame = shy_guts :: consts :: sound_bytes_per_channel * output_format . mChannelsPerFrame ;
    output_format . mBitsPerChannel = shy_guts :: consts :: sound_bits_per_channel ;
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

void shy_platform_sound_loader_cocoa :: init ( )
{
    shy_guts :: loader = [ [ shy_guts_platform_sound_loader_cocoa_type alloc ] init ] ;
    [ shy_guts :: loader thread_run ] ;
}

void shy_platform_sound_loader_cocoa :: done ( )
{
    [ shy_guts :: loader thread_stop ] ;
    shy_guts :: loader = nil ;
}

void shy_platform_sound_loader_cocoa :: create_stereo_resource_id 
    ( so_called_platform_sound_loader_cocoa_stereo_resource_id_type & result 
    , so_called_platform_math_num_whole_type resource_index
    )
{
    so_called_trace ( so_called_trace_platform_sound_loader :: check_args_create_stereo_resource_id ( resource_index ) ) ;
    so_called_lib_std_int32_t resource_index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( resource_index_int , resource_index ) ;
    result . _resource_id = resource_index_int ;
}

void shy_platform_sound_loader_cocoa :: loader_ready ( so_called_platform_math_num_whole_type & result )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , [ shy_guts :: loader loader_ready ] ) ;
}

void shy_platform_sound_loader_cocoa :: loaded_samples_count ( so_called_platform_math_num_whole_type & result )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , [ shy_guts :: loader loaded_samples_count ] ) ;
}

void shy_platform_sound_loader_cocoa :: _load_stereo_sample_data
    ( const so_called_platform_sound_sample_stereo_type * samples_ptr
    , so_called_lib_std_int32_t samples_count
    , const so_called_platform_sound_loader_cocoa_stereo_resource_id_type & resource_id 
    )
{
    [ shy_guts :: loader 
        load_16_bit_44100_khz_stereo_samples_from_resource : resource_id . _resource_id 
        to_buffer : ( void * ) samples_ptr
        with_max_samples_count_of : samples_count
    ] ;
}
