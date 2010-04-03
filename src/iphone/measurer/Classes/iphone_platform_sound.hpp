inline
void 
shy_iphone_platform :: sound_set_listener_position 
    ( shy_iphone_platform :: vector_data position 
    )
{
    ALfloat al_position [ ] = { position . _x , position . _y , position . _z } ;
    alListenerfv ( AL_POSITION , al_position ) ;
}

inline
void 
shy_iphone_platform :: sound_set_listener_velocity
    ( shy_iphone_platform :: vector_data velocity
    )
{
    ALfloat al_velocity [ ] = { velocity . _x , velocity . _y , velocity . _z } ;
    alListenerfv ( AL_VELOCITY , al_velocity ) ;
}

inline
void 
shy_iphone_platform :: sound_set_listener_orientation 
    ( shy_iphone_platform :: vector_data look_at 
    , shy_iphone_platform :: vector_data up 
    )
{
    ALfloat al_orientation [ ] = 
        { look_at . _x 
        , look_at . _y 
        , look_at . _z 
        , up . _x 
        , up . _y 
        , up . _z 
        } ;
    alListenerfv ( AL_ORIENTATION , al_orientation ) ;
}

inline
void 
shy_iphone_platform :: sound_set_sample_value 
    ( shy_iphone_platform :: mono_sound_sample & sample 
    , shy_iphone_platform :: float_32 value 
    )
{
    sample . _value = ( ALubyte ) ( ( value * 127.0f ) + 127.0f ) ;
}

inline
shy_iphone_platform :: stereo_sound_resource_id
shy_iphone_platform :: sound_create_stereo_resource_id 
    ( int_32 resource_index 
    )
{
    stereo_sound_resource_id resource_id ;
    resource_id . _resource_id = resource_index ;
    return resource_id ;
}

inline
void 
shy_iphone_platform :: sound_load_stereo_sample_data
    ( stereo_sound_sample * samples 
    , int_32 max_samples_count
    , int_32 & loaded_samples_count
    , const stereo_sound_resource_id & resource_id 
    )
{
    NSBundle * bundle = [ NSBundle mainBundle ] ;
    CFURLRef file_url = ( CFURLRef ) [ [ NSURL fileURLWithPath : [ bundle 
        pathForResource : [ NSString stringWithFormat : @"stereo_sound_resource_%i" , resource_id . _resource_id ] 
        ofType : @"mp3" 
        ] ] retain ] ;
        
    SInt64 file_length_in_frames = 0 ;
    AudioStreamBasicDescription file_format ;
    UInt32 property_size = sizeof ( file_format ) ;
    ExtAudioFileRef ext_ref = 0 ;
    AudioStreamBasicDescription output_format ;
                 
    ExtAudioFileOpenURL ( file_url , & ext_ref ) ;
    ExtAudioFileGetProperty ( ext_ref , kExtAudioFileProperty_FileDataFormat , & property_size , & file_format ) ;
                    
    output_format . mSampleRate = stereo_sound_samples_per_second ;
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
    data_buffer . mBuffers [ 0 ] . mData = ( void * ) samples ;
    
    ExtAudioFileRead ( ext_ref , ( UInt32 * ) & file_length_in_frames , & data_buffer ) ;
    loaded_samples_count = file_length_in_frames ;
    ExtAudioFileDispose ( ext_ref ) ;
    CFRelease ( file_url ) ;
}

inline
shy_iphone_platform :: sound_buffer_id 
shy_iphone_platform :: sound_create_mono_buffer 
    ( shy_iphone_platform :: mono_sound_sample * samples 
    , shy_iphone_platform :: int_32 samples_count 
    )
{
    sound_buffer_id buffer_id ;
    alGenBuffers ( 1 , & buffer_id . _buffer_id ) ;
    alBufferData 
        ( buffer_id . _buffer_id 
        , AL_FORMAT_MONO8 
        , ( ALvoid * ) samples
        , samples_count * sizeof ( mono_sound_sample )
        , mono_sound_samples_per_second
        ) ;
    return buffer_id ;
}

inline
shy_iphone_platform :: sound_buffer_id 
shy_iphone_platform :: sound_create_stereo_buffer 
    ( stereo_sound_sample * samples 
    , int_32 samples_count 
    )
{
    sound_buffer_id buffer_id ;
    alGenBuffers ( 1 , & buffer_id . _buffer_id ) ;
    alBufferData 
        ( buffer_id . _buffer_id 
        , AL_FORMAT_STEREO16 
        , ( ALvoid * ) samples 
        , samples_count * sizeof ( stereo_sound_sample )
        , stereo_sound_samples_per_second
        ) ;
    return buffer_id ;
}

inline
shy_iphone_platform :: sound_source_id
shy_iphone_platform :: sound_create_source 
    ( 
    )
{
    sound_source_id source_id ;
    alGenSources ( 1 , & source_id . _source_id ) ;
    return source_id ;
}

inline
void 
shy_iphone_platform :: sound_set_source_pitch 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    , shy_iphone_platform :: float_32 pitch 
    )
{
    alSourcef ( source_id . _source_id , AL_PITCH , pitch ) ;
}

inline
void 
shy_iphone_platform :: sound_set_source_gain 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    , shy_iphone_platform :: float_32 gain 
    )
{
    alSourcef ( source_id . _source_id , AL_GAIN , gain ) ;
}

inline
void
shy_iphone_platform :: sound_set_source_position 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    , shy_iphone_platform :: vector_data position 
    )
{
    ALfloat al_position [ ] = { position . _x , position . _y , position . _z } ;
    alSourcefv ( source_id . _source_id , AL_POSITION , al_position ) ;
}

inline
void 
shy_iphone_platform :: sound_set_source_velocity 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    , shy_iphone_platform :: vector_data velocity 
    )
{
    ALfloat al_velocity [ ] = { velocity . _x , velocity . _y , velocity . _z } ;
    alSourcefv ( source_id . _source_id , AL_VELOCITY , al_velocity ) ;
}

inline
void 
shy_iphone_platform :: sound_set_source_buffer 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    , shy_iphone_platform :: sound_buffer_id & buffer_id 
    )
{
    alSourcei ( source_id . _source_id , AL_BUFFER , buffer_id . _buffer_id ) ;
}

inline
void 
shy_iphone_platform :: sound_set_source_playback_looping 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    )
{
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_TRUE ) ;
}

inline
void 
shy_iphone_platform :: sound_set_source_playback_once 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    )
{
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_FALSE ) ;
}

inline
void 
shy_iphone_platform :: sound_source_play 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    )
{
    alSourcePlay ( source_id . _source_id ) ;
}

inline
void 
shy_iphone_platform :: sound_source_stop 
    ( const shy_iphone_platform :: sound_source_id & source_id 
    )
{
    alSourceStop ( source_id . _source_id ) ;
}
