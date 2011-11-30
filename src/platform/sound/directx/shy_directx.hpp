void shy_platform_sound_directx :: set_listener_position ( so_called_platform_vector_data_type )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_listener_position ( position ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: listener_state ( ) ) ;
}

void shy_platform_sound_directx :: set_listener_velocity ( so_called_platform_vector_data_type )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_listener_velocity ( position ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: listener_state ( ) ) ;
}

void shy_platform_sound_directx :: set_listener_orientation ( so_called_platform_vector_data_type , so_called_platform_vector_data_type )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_listener_orientation ( look_at , up ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: listener_state ( ) ) ;
}

void shy_platform_sound_directx :: set_sample_value ( so_called_platform_sound_sample_mono_type & , so_called_platform_math_num_fract_type )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_sample_value ( value ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: buffer_set ( ) ) ;
}

void shy_platform_sound_directx :: create_source ( so_called_platform_sound_source_id_type & )
{
    so_called_profile ( so_called_profile_platform_sound :: source_create ( ) ) ;
}

void shy_platform_sound_directx :: set_source_pitch ( const so_called_platform_sound_source_id_type & source_id , so_called_platform_math_num_fract_type pitch )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_source_pitch ( source_id , pitch ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_state ( ) ) ;
}

void shy_platform_sound_directx :: set_source_gain ( const so_called_platform_sound_source_id_type & source_id , so_called_platform_math_num_fract_type gain )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_source_gain ( source_id , gain ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_state ( ) ) ;
}

void shy_platform_sound_directx :: set_source_position ( const so_called_platform_sound_source_id_type & source_id , so_called_platform_vector_data_type position )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_source_position ( source_id , position ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_state ( ) ) ;
}

void shy_platform_sound_directx :: set_source_velocity ( const so_called_platform_sound_source_id_type & source_id , so_called_platform_vector_data_type velocity )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_source_velocity ( source_id , velocity ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_state ( ) ) ;
}

void shy_platform_sound_directx :: set_source_buffer ( const so_called_platform_sound_source_id_type & source_id , so_called_platform_sound_buffer_id_type & buffer_id )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_source_buffer ( source_id , buffer_id ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_state ( ) ) ;
}

void shy_platform_sound_directx :: set_source_playback_looping ( const so_called_platform_sound_source_id_type & source_id )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_source_playback_looping ( source_id ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_state ( ) ) ;
}

void shy_platform_sound_directx :: set_source_playback_once ( const so_called_platform_sound_source_id_type & )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_set_source_playback_once ( source_id ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_state ( ) ) ;
}

void shy_platform_sound_directx :: source_play ( const so_called_platform_sound_source_id_type & )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_source_play ( source_id ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_play ( ) ) ;
}

void shy_platform_sound_directx :: source_stop ( const so_called_platform_sound_source_id_type & )
{
    so_called_trace ( so_called_trace_platform_sound :: check_args_source_stop ( source_id ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: source_stop ( ) ) ;
}

void shy_platform_sound_directx :: _create_mono_buffer 
    ( so_called_platform_sound_buffer_id_type & 
    , const so_called_platform_sound_sample_mono_type *
    , so_called_platform_math_num_whole_type
    )
{
}

void shy_platform_sound_directx :: _create_stereo_buffer 
    ( so_called_platform_sound_buffer_id_type &
    , const so_called_platform_sound_sample_stereo_type *
    , so_called_platform_math_num_whole_type
    )
{
}
