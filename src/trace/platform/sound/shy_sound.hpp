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
