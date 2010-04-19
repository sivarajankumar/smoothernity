inline
void 
shy_macosx_platform :: sound_set_listener_position 
    ( shy_macosx_platform :: vector_data position 
    )
{/*
    ALfloat al_position [ ] = { position . _x , position . _y , position . _z } ;
    alListenerfv ( AL_POSITION , al_position ) ;
*/}

inline
void 
shy_macosx_platform :: sound_set_listener_velocity
    ( shy_macosx_platform :: vector_data velocity
    )
{/*
    ALfloat al_velocity [ ] = { velocity . _x , velocity . _y , velocity . _z } ;
    alListenerfv ( AL_VELOCITY , al_velocity ) ;
*/}

inline
void 
shy_macosx_platform :: sound_set_listener_orientation 
    ( shy_macosx_platform :: vector_data look_at 
    , shy_macosx_platform :: vector_data up 
    )
{/*
    ALfloat al_orientation [ ] = 
        { look_at . _x 
        , look_at . _y 
        , look_at . _z 
        , up . _x 
        , up . _y 
        , up . _z 
        } ;
    alListenerfv ( AL_ORIENTATION , al_orientation ) ;
*/}

inline
void 
shy_macosx_platform :: sound_set_sample_value 
    ( shy_macosx_platform :: mono_sound_sample & sample 
    , shy_macosx_platform :: float_32 value 
    )
{/*
    sample . _value = ( ALubyte ) ( ( value * 127.0f ) + 127.0f ) ;
*/}

inline
shy_macosx_platform :: stereo_sound_resource_id
shy_macosx_platform :: sound_create_stereo_resource_id 
    ( int_32 resource_index 
    )
{
    stereo_sound_resource_id resource_id ;
//    resource_id . _resource_id = resource_index ;
    return resource_id ;
}

inline
void 
shy_macosx_platform :: sound_load_stereo_sample_data
    ( stereo_sound_sample * samples 
    , int_32 max_samples_count
    , int_32 & loaded_samples_count
    , const stereo_sound_resource_id & resource_id 
    )
{/*
    [ _sound_loader 
        load_16_bit_44100_khz_stereo_samples_from_resource : resource_id . _resource_id 
        to_buffer : ( void * ) samples
        with_max_samples_count_of : max_samples_count
        put_loaded_samples_count_to : & loaded_samples_count
    ] ;
*/}

inline
shy_macosx_platform :: int_32 
shy_macosx_platform :: sound_loader_ready ( )
{
//    return [ _sound_loader loader_ready ] ;
	return true ;
}

inline
shy_macosx_platform :: sound_buffer_id 
shy_macosx_platform :: sound_create_mono_buffer 
    ( shy_macosx_platform :: mono_sound_sample * samples 
    , shy_macosx_platform :: int_32 samples_count 
    )
{
//    alBufferDataStaticProcPtr al_buffer_data_static_proc = 
//        ( alBufferDataStaticProcPtr ) alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    sound_buffer_id buffer_id ;
//    alGenBuffers ( 1 , & buffer_id . _buffer_id ) ;
//    al_buffer_data_static_proc
//        ( buffer_id . _buffer_id 
//        , AL_FORMAT_MONO8 
//        , ( ALvoid * ) samples
//        , samples_count * sizeof ( mono_sound_sample )
//        , mono_sound_samples_per_second
//        ) ;
    return buffer_id ;
}

inline
shy_macosx_platform :: sound_buffer_id 
shy_macosx_platform :: sound_create_stereo_buffer 
    ( stereo_sound_sample * samples 
    , int_32 samples_count 
    )
{
//    alBufferDataStaticProcPtr al_buffer_data_static_proc = 
//        ( alBufferDataStaticProcPtr ) alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    sound_buffer_id buffer_id ;
//    alGenBuffers ( 1 , & buffer_id . _buffer_id ) ;
//    al_buffer_data_static_proc
//        ( buffer_id . _buffer_id 
//        , AL_FORMAT_STEREO16 
//        , ( ALvoid * ) samples 
//        , samples_count * sizeof ( stereo_sound_sample )
//        , stereo_sound_samples_per_second
//        ) ;
    return buffer_id ;
}

inline
shy_macosx_platform :: sound_source_id
shy_macosx_platform :: sound_create_source 
    ( 
    )
{
    sound_source_id source_id ;
//    alGenSources ( 1 , & source_id . _source_id ) ;
    return source_id ;
}

inline
void 
shy_macosx_platform :: sound_set_source_pitch 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    , shy_macosx_platform :: float_32 pitch 
    )
{
//    alSourcef ( source_id . _source_id , AL_PITCH , pitch ) ;
}

inline
void 
shy_macosx_platform :: sound_set_source_gain 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    , shy_macosx_platform :: float_32 gain 
    )
{
//    alSourcef ( source_id . _source_id , AL_GAIN , gain ) ;
}

inline
void
shy_macosx_platform :: sound_set_source_position 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    , shy_macosx_platform :: vector_data position 
    )
{/*
    ALfloat al_position [ ] = { position . _x , position . _y , position . _z } ;
    alSourcefv ( source_id . _source_id , AL_POSITION , al_position ) ;
*/}

inline
void 
shy_macosx_platform :: sound_set_source_velocity 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    , shy_macosx_platform :: vector_data velocity 
    )
{/*
    ALfloat al_velocity [ ] = { velocity . _x , velocity . _y , velocity . _z } ;
    alSourcefv ( source_id . _source_id , AL_VELOCITY , al_velocity ) ;
*/}

inline
void 
shy_macosx_platform :: sound_set_source_buffer 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    , shy_macosx_platform :: sound_buffer_id & buffer_id 
    )
{/*
    alSourcei ( source_id . _source_id , AL_BUFFER , buffer_id . _buffer_id ) ;
*/}

inline
void 
shy_macosx_platform :: sound_set_source_playback_looping 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    )
{/*
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_TRUE ) ;
*/}

inline
void 
shy_macosx_platform :: sound_set_source_playback_once 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    )
{/*
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_FALSE ) ;
*/}

inline
void 
shy_macosx_platform :: sound_source_play 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    )
{/*
    alSourcePlay ( source_id . _source_id ) ;
*/}

inline
void 
shy_macosx_platform :: sound_source_stop 
    ( const shy_macosx_platform :: sound_source_id & source_id 
    )
{/*
    alSourceStop ( source_id . _source_id ) ;
*/}
