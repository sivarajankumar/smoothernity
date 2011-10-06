namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_math" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_math :: check_num_fract_uninitialized ( so_called_platform_math_num_fract_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = false ;
        so_called_platform_math_insider :: num_fract_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized fractional value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_num_whole_uninitialized ( so_called_platform_math_num_whole_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = false ;
        so_called_platform_math_insider :: num_whole_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized whole value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_division_num_fract_by_zero ( so_called_platform_math_num_fract_type numerator , so_called_platform_math_num_fract_type denominator )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_float denominator_float = 0 ;
        so_called_platform_math_insider :: num_fract_value_get ( denominator_float , denominator ) ;
        if ( denominator_float == so_called_lib_std_float ( 0 ) )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Division by zero with numerator of " ) ;
            so_called_platform_trace :: trace_num_fract_error ( numerator ) ;
            so_called_platform_trace :: trace_string_error ( "." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_division_num_whole_by_zero ( so_called_platform_math_num_whole_type numerator , so_called_platform_math_num_whole_type denominator )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_int32_t denominator_int = 0 ;
        so_called_platform_math_insider :: num_whole_value_get ( denominator_int , denominator ) ;
        if ( denominator_int == 0 )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Division by zero with numerator of " ) ;
            so_called_platform_trace :: trace_num_whole_error ( numerator ) ;
            so_called_platform_trace :: trace_string_error ( "." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_division_const_int_32_by_zero ( so_called_platform_math_const_int_32_type numerator , so_called_platform_math_const_int_32_type denominator )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        if ( denominator == 0 )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Division by zero with numerator of " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( numerator ) ;
            so_called_platform_trace :: trace_string_error ( "." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}
