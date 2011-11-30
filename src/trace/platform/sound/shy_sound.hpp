namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_sound" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_sound :: check_source_id_uninitialized ( so_called_platform_sound_source_id_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_sound_insider :: source_id_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized source id." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_sound :: check_buffer_id_uninitialized ( so_called_platform_sound_buffer_id_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_sound_insider :: buffer_id_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized buffer id." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_sound :: check_args_set_listener_position ( so_called_platform_vector_data_type position )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_vector :: check_data_uninitialized ( position ) ;
}

void shy_trace_platform_sound :: check_args_set_listener_velocity ( so_called_platform_vector_data_type velocity )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_vector :: check_data_uninitialized ( velocity ) ;
}

void shy_trace_platform_sound :: check_args_set_listener_orientation 
    ( so_called_platform_vector_data_type look_at
    , so_called_platform_vector_data_type up
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_vector :: check_zero_length ( look_at ) ;
        so_called_trace_platform_vector :: check_zero_length ( up ) ;
        so_called_trace_platform_vector :: check_data_uninitialized ( look_at ) ;
        so_called_trace_platform_vector :: check_data_uninitialized ( up ) ;
    }
}

void shy_trace_platform_sound :: check_args_set_sample_value ( so_called_platform_math_num_fract_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( value , - 1 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( value ) ;
    }
}

void shy_trace_platform_sound :: check_args_set_source_pitch
    ( so_called_platform_sound_source_id_type source_id
    , so_called_platform_math_num_fract_type pitch
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_source_id_uninitialized ( source_id ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( pitch ) ;
        so_called_trace_platform_math :: check_num_fract_non_positive ( pitch ) ;
    }
}

void shy_trace_platform_sound :: check_args_set_source_gain
    ( so_called_platform_sound_source_id_type source_id
    , so_called_platform_math_num_fract_type gain
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_source_id_uninitialized ( source_id ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( gain ) ;
        so_called_trace_platform_math :: check_num_fract_non_positive ( gain ) ;
    }
}

void shy_trace_platform_sound :: check_args_set_source_position
    ( so_called_platform_sound_source_id_type source_id
    , so_called_platform_vector_data_type position
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_source_id_uninitialized ( source_id ) ;
        so_called_trace_platform_vector :: check_data_uninitialized ( position ) ;
    }
}

void shy_trace_platform_sound :: check_args_set_source_velocity
    ( so_called_platform_sound_source_id_type source_id
    , so_called_platform_vector_data_type velocity
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_source_id_uninitialized ( source_id ) ;
        so_called_trace_platform_vector :: check_data_uninitialized ( velocity ) ;
    }
}

void shy_trace_platform_sound :: check_args_set_source_buffer
    ( so_called_platform_sound_source_id_type source_id
    , so_called_platform_sound_buffer_id_type buffer_id
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_source_id_uninitialized ( source_id ) ;
        check_buffer_id_uninitialized ( buffer_id ) ;
    }
}

void shy_trace_platform_sound :: check_args_set_source_playback_looping ( so_called_platform_sound_source_id_type source_id )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_source_id_uninitialized ( source_id ) ;
}

void shy_trace_platform_sound :: check_args_set_source_playback_once ( so_called_platform_sound_source_id_type source_id )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_source_id_uninitialized ( source_id ) ;
}

void shy_trace_platform_sound :: check_args_source_play ( so_called_platform_sound_source_id_type source_id )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_source_id_uninitialized ( source_id ) ;
}

void shy_trace_platform_sound :: check_args_source_stop ( so_called_platform_sound_source_id_type source_id )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_source_id_uninitialized ( source_id ) ;
}

void shy_trace_platform_sound :: _check_args_create_buffer 
    ( so_called_lib_std_int32_t array_size
    , so_called_platform_math_num_whole_type samples_count 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( samples_count ) ;
        so_called_trace_platform_math :: check_num_whole_non_positive ( samples_count ) ;
        so_called_lib_std_int32_t samples_count_int = 0 ;
        so_called_platform_math_insider :: num_whole_value_get ( samples_count_int , samples_count ) ;
        if ( array_size <= 0 )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Supplied array of " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( array_size ) ;
            so_called_platform_trace :: trace_string_error ( " samples." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( samples_count , 1 , array_size ) ;
    }
}
