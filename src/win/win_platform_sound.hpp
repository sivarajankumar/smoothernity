inline void shy_win_platform :: sound_set_listener_position ( vector_data position )
{
}

inline void shy_win_platform :: sound_set_listener_velocity ( vector_data velocity )
{
}

inline void shy_win_platform :: sound_set_listener_orientation ( vector_data look_at , vector_data up )
{
}

inline void shy_win_platform :: sound_set_sample_value ( mono_sound_sample & sample , num_fract value )
{
}

inline void shy_win_platform :: sound_create_stereo_resource_id 
    ( stereo_sound_resource_id & result 
    , num_whole resource_index
    )
{
}

template < shy_win_platform :: const_int_32 samples_array_size >
inline void shy_win_platform :: sound_load_stereo_sample_data
    ( const static_array < stereo_sound_sample , samples_array_size > & samples 
    , const stereo_sound_resource_id & resource_id 
    )
{
}

inline void shy_win_platform :: sound_loader_ready ( num_whole & result )
{
    result . _value = true ;
}

inline void shy_win_platform :: sound_loaded_samples_count ( num_whole & result )
{
}

template < shy_win_platform :: const_int_32 samples_array_size >
inline void shy_win_platform :: sound_create_mono_buffer 
    ( sound_buffer_id & result
    , const static_array < mono_sound_sample , samples_array_size > & samples 
    , num_whole samples_count 
    )
{
}

template < shy_win_platform :: const_int_32 samples_array_size >
inline void shy_win_platform :: sound_create_stereo_buffer 
    ( sound_buffer_id & result
    , const static_array < stereo_sound_sample , samples_array_size > & samples 
    , num_whole samples_count 
    )
{
}

inline void shy_win_platform :: sound_create_source ( sound_source_id & result )
{
}

inline void shy_win_platform :: sound_set_source_pitch ( const sound_source_id & source_id , num_fract pitch )
{
}

inline void shy_win_platform :: sound_set_source_gain ( const sound_source_id & source_id , num_fract gain )
{
}

inline void shy_win_platform :: sound_set_source_position ( const sound_source_id & source_id , vector_data position )
{
}

inline void shy_win_platform :: sound_set_source_velocity ( const sound_source_id & source_id , vector_data velocity )
{
}

inline void shy_win_platform :: sound_set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id )
{
}

inline void shy_win_platform :: sound_set_source_playback_looping ( const sound_source_id & source_id )
{
}

inline void shy_win_platform :: sound_set_source_playback_once ( const sound_source_id & source_id )
{
}

inline void shy_win_platform :: sound_source_play ( const sound_source_id & source_id )
{
}

inline void shy_win_platform :: sound_source_stop ( const sound_source_id & source_id )
{
}
