namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_conditions" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_conditions :: check_uninitialized ( so_called_platform_math_num_fract_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_float value_float = 0 ;
        so_called_lib_std_float uninitialized_float = 0 ;
        so_called_platform_math_insider :: num_fract_value_get ( value_float , value ) ;
        so_called_platform_math_insider :: num_fract_value_get ( uninitialized_float , so_called_platform_math_num_fract_type ( ) ) ;
        if ( value_float == uninitialized_float )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized fractional value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_conditions :: check_uninitialized ( so_called_platform_math_num_whole_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_int32_t value_int = 0 ;
        so_called_lib_std_int32_t uninitialized_int = 0 ;
        so_called_platform_math_insider :: num_whole_value_get ( value_int , value ) ;
        so_called_platform_math_insider :: num_whole_value_get ( uninitialized_int , so_called_platform_math_num_whole_type ( ) ) ;
        if ( value_int == uninitialized_int )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized whole value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}
