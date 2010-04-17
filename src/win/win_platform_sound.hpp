inline
void 
shy_win_platform :: sound_set_listener_position 
    ( shy_win_platform :: vector_data position 
    )
{
}

inline
void 
shy_win_platform :: sound_set_listener_velocity
    ( shy_win_platform :: vector_data velocity
    )
{
}

inline
void 
shy_win_platform :: sound_set_listener_orientation 
    ( shy_win_platform :: vector_data look_at 
    , shy_win_platform :: vector_data up 
    )
{
}

inline
void 
shy_win_platform :: sound_set_sample_value 
    ( shy_win_platform :: mono_sound_sample & sample 
    , shy_win_platform :: float_32 value 
    )
{
}

inline
shy_win_platform :: stereo_sound_resource_id
shy_win_platform :: sound_create_stereo_resource_id 
    ( int_32 resource_index 
    )
{
    stereo_sound_resource_id resource_id ;
    return resource_id ;
}

inline
void 
shy_win_platform :: sound_load_stereo_sample_data
    ( stereo_sound_sample * samples 
    , int_32 max_samples_count
    , int_32 & loaded_samples_count
    , const stereo_sound_resource_id & resource_id 
    )
{
}

inline
shy_win_platform :: int_32 
shy_win_platform :: sound_loader_ready ( )
{
    return 1 ;
}

inline
shy_win_platform :: sound_buffer_id 
shy_win_platform :: sound_create_mono_buffer 
    ( shy_win_platform :: mono_sound_sample * samples 
    , shy_win_platform :: int_32 samples_count 
    )
{
    sound_buffer_id buffer_id ;
    return buffer_id ;
}

inline
shy_win_platform :: sound_buffer_id 
shy_win_platform :: sound_create_stereo_buffer 
    ( stereo_sound_sample * samples 
    , int_32 samples_count 
    )
{
    sound_buffer_id buffer_id ;
    return buffer_id ;
}

inline
shy_win_platform :: sound_source_id
shy_win_platform :: sound_create_source 
    ( 
    )
{
    sound_source_id source_id ;
    return source_id ;
}

inline
void 
shy_win_platform :: sound_set_source_pitch 
    ( const shy_win_platform :: sound_source_id & source_id 
    , shy_win_platform :: float_32 pitch 
    )
{
}

inline
void 
shy_win_platform :: sound_set_source_gain 
    ( const shy_win_platform :: sound_source_id & source_id 
    , shy_win_platform :: float_32 gain 
    )
{
}

inline
void
shy_win_platform :: sound_set_source_position 
    ( const shy_win_platform :: sound_source_id & source_id 
    , shy_win_platform :: vector_data position 
    )
{
}

inline
void 
shy_win_platform :: sound_set_source_velocity 
    ( const shy_win_platform :: sound_source_id & source_id 
    , shy_win_platform :: vector_data velocity 
    )
{
}

inline
void 
shy_win_platform :: sound_set_source_buffer 
    ( const shy_win_platform :: sound_source_id & source_id 
    , shy_win_platform :: sound_buffer_id & buffer_id 
    )
{
}

inline
void 
shy_win_platform :: sound_set_source_playback_looping 
    ( const shy_win_platform :: sound_source_id & source_id 
    )
{
}

inline
void 
shy_win_platform :: sound_set_source_playback_once 
    ( const shy_win_platform :: sound_source_id & source_id 
    )
{
}

inline
void 
shy_win_platform :: sound_source_play 
    ( const shy_win_platform :: sound_source_id & source_id 
    )
{
}

inline
void 
shy_win_platform :: sound_source_stop 
    ( const shy_win_platform :: sound_source_id & source_id 
    )
{
}
