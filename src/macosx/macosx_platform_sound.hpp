inline void shy_macosx_platform :: sound_set_listener_position ( vector_data position )
{
    ALfloat al_position [ ] = { position . _x , position . _y , position . _z } ;
    alListenerfv ( AL_POSITION , al_position ) ;
}

inline void shy_macosx_platform :: sound_set_listener_velocity ( vector_data velocity )
{
    ALfloat al_velocity [ ] = { velocity . _x , velocity . _y , velocity . _z } ;
    alListenerfv ( AL_VELOCITY , al_velocity ) ;
}

inline void shy_macosx_platform :: sound_set_listener_orientation ( vector_data look_at , vector_data up )
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

inline void shy_macosx_platform :: sound_set_sample_value ( mono_sound_sample & sample , num_fract value )
{
    sample . _value = ( ALubyte ) ( ( value . _value * 127.0f ) + 127.0f ) ;
}

inline void shy_macosx_platform :: sound_create_stereo_resource_id 
    ( stereo_sound_resource_id & result 
    , num_whole resource_index
    )
{
    result . _resource_id = resource_index . _value ;
}

template < typename samples_array >
inline void shy_macosx_platform :: sound_load_stereo_sample_data
    ( const samples_array & samples 
    , const stereo_sound_resource_id & resource_id 
    )
{
    [ shy_macosx_platform_utility :: _sound_loader 
        load_16_bit_44100_khz_stereo_samples_from_resource : resource_id . _resource_id 
        to_buffer : ( void * ) _platform_static_array_insider :: array_elements_unsafe_ptr ( samples )
        with_max_samples_count_of : _platform_static_array_insider :: array_elements_count < samples_array > ( )
    ] ;
}

inline void shy_macosx_platform :: sound_loader_ready ( num_whole & result )
{
    result . _value = [ shy_macosx_platform_utility :: _sound_loader loader_ready ] ;
}

inline void shy_macosx_platform :: sound_loaded_samples_count ( num_whole & result )
{
    result . _value = [ shy_macosx_platform_utility :: _sound_loader loaded_samples_count ] ;
}

template < typename samples_array >
inline void shy_macosx_platform :: sound_create_mono_buffer 
    ( sound_buffer_id & result
    , const samples_array & samples 
    , num_whole samples_count 
    )
{
    alBufferDataStaticProcPtr al_buffer_data_static_proc = 
        ( alBufferDataStaticProcPtr ) alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    alGenBuffers ( 1 , & result . _buffer_id ) ;
    al_buffer_data_static_proc
        ( result . _buffer_id 
        , AL_FORMAT_MONO8 
        , ( ALvoid * ) _platform_static_array_insider :: array_elements_unsafe_ptr ( samples )
        , samples_count . _value * sizeof ( mono_sound_sample )
        , mono_sound_samples_per_second
        ) ;
}

template < typename samples_array >
inline void shy_macosx_platform :: sound_create_stereo_buffer 
    ( sound_buffer_id & result
    , const samples_array & samples 
    , num_whole samples_count 
    )
{
    alBufferDataStaticProcPtr al_buffer_data_static_proc = 
        ( alBufferDataStaticProcPtr ) alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    alGenBuffers ( 1 , & result . _buffer_id ) ;
    al_buffer_data_static_proc
        ( result . _buffer_id 
        , AL_FORMAT_STEREO16 
        , ( ALvoid * ) _platform_static_array_insider :: array_elements_unsafe_ptr ( samples )
        , samples_count . _value * sizeof ( stereo_sound_sample )
        , stereo_sound_samples_per_second
        ) ;
}

inline void shy_macosx_platform :: sound_create_source ( sound_source_id & result )
{
    alGenSources ( 1 , & result . _source_id ) ;
}

inline void shy_macosx_platform :: sound_set_source_pitch ( const sound_source_id & source_id , num_fract pitch )
{
    alSourcef ( source_id . _source_id , AL_PITCH , pitch . _value ) ;
}

inline void shy_macosx_platform :: sound_set_source_gain ( const sound_source_id & source_id , num_fract gain )
{
    alSourcef ( source_id . _source_id , AL_GAIN , gain . _value ) ;
}

inline void shy_macosx_platform :: sound_set_source_position ( const sound_source_id & source_id , vector_data position )
{
    ALfloat al_position [ ] = { position . _x , position . _y , position . _z } ;
    alSourcefv ( source_id . _source_id , AL_POSITION , al_position ) ;
}

inline void shy_macosx_platform :: sound_set_source_velocity ( const sound_source_id & source_id , vector_data velocity )
{
    ALfloat al_velocity [ ] = { velocity . _x , velocity . _y , velocity . _z } ;
    alSourcefv ( source_id . _source_id , AL_VELOCITY , al_velocity ) ;
}

inline void shy_macosx_platform :: sound_set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id )
{
    alSourcei ( source_id . _source_id , AL_BUFFER , buffer_id . _buffer_id ) ;
}

inline void shy_macosx_platform :: sound_set_source_playback_looping ( const sound_source_id & source_id )
{
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_TRUE ) ;
}

inline void shy_macosx_platform :: sound_set_source_playback_once ( const sound_source_id & source_id )
{
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_FALSE ) ;
}

inline void shy_macosx_platform :: sound_source_play ( const sound_source_id & source_id )
{
    alSourcePlay ( source_id . _source_id ) ;
}

inline void shy_macosx_platform :: sound_source_stop ( const sound_source_id & source_id )
{
    alSourceStop ( source_id . _source_id ) ;
}
