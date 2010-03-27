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
    ( shy_iphone_platform :: sound_sample & sample 
    , shy_iphone_platform :: float_32 value 
    )
{
    sample . _value = ( ALubyte ) ( ( value * 127.0f ) + 127.0f ) ;
}

inline
shy_iphone_platform :: sound_buffer_id 
shy_iphone_platform :: sound_create_buffer 
    ( shy_iphone_platform :: sound_sample * samples 
    , shy_iphone_platform :: int_32 samples_count 
    )
{
    sound_buffer_id buffer_id ;
    alGenBuffers ( 1 , & buffer_id . _buffer_id ) ;
    alBufferData 
        ( buffer_id . _buffer_id 
        , AL_FORMAT_MONO8 
        , ( ALvoid * ) samples 
        , samples_count
        , sound_samples_per_second
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
