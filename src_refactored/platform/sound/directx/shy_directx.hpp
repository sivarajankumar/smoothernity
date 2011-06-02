void shy_platform_sound_directx :: set_listener_position ( so_called_type_platform_vector_data position )
{
}

void shy_platform_sound_directx :: set_listener_velocity ( so_called_type_platform_vector_data velocity )
{
}

void shy_platform_sound_directx :: set_listener_orientation ( so_called_type_platform_vector_data look_at , so_called_type_platform_vector_data up )
{
}

void shy_platform_sound_directx :: set_sample_value ( so_called_type_platform_sound_sample_mono & sample , so_called_type_platform_math_num_fract value )
{
}

void shy_platform_sound_directx :: create_source ( so_called_type_platform_sound_source_id & result )
{
}

void shy_platform_sound_directx :: set_source_pitch ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_math_num_fract pitch )
{
}

void shy_platform_sound_directx :: set_source_gain ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_math_num_fract gain )
{
}

void shy_platform_sound_directx :: set_source_position ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_vector_data position )
{
}

void shy_platform_sound_directx :: set_source_velocity ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_vector_data velocity )
{
}

void shy_platform_sound_directx :: set_source_buffer ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_sound_buffer_id & buffer_id )
{
}

void shy_platform_sound_directx :: set_source_playback_looping ( const so_called_type_platform_sound_source_id & source_id )
{
}

void shy_platform_sound_directx :: set_source_playback_once ( const so_called_type_platform_sound_source_id & source_id )
{
}

void shy_platform_sound_directx :: source_play ( const so_called_type_platform_sound_source_id & source_id )
{
}

void shy_platform_sound_directx :: source_stop ( const so_called_type_platform_sound_source_id & source_id )
{
}

void shy_platform_sound_directx :: _create_mono_buffer 
    ( so_called_type_platform_sound_buffer_id & result
    , const so_called_type_platform_sound_sample_mono * samples_ptr
    , so_called_type_platform_math_num_whole samples_count 
    )
{
}

void shy_platform_sound_directx :: _create_stereo_buffer 
    ( so_called_type_platform_sound_buffer_id & result
    , const so_called_type_platform_sound_sample_stereo * samples_ptr 
    , so_called_type_platform_math_num_whole samples_count 
    )
{
}
