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
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
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
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_math_insider :: num_whole_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized whole value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_num_whole_exceeds_range_int
    ( so_called_platform_math_num_whole_type value_whole
    , so_called_platform_math_const_int_32_type value_min
    , so_called_platform_math_const_int_32_type value_max
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_int32_t value = 0 ;
        so_called_platform_math_insider :: num_whole_value_get ( value , value_whole ) ;
        if ( value < value_min || value > value_max )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Whole value " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( value ) ;
            so_called_platform_trace :: trace_string_error ( " exceeds range from " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( value_min ) ;
            so_called_platform_trace :: trace_string_error ( " to " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( value_max ) ;
            so_called_platform_trace :: trace_string_error ( "." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_num_fract_exceeds_range_int
    ( so_called_platform_math_num_fract_type value_fract
    , so_called_platform_math_const_int_32_type value_min
    , so_called_platform_math_const_int_32_type value_max
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_float value = 0 ;
        so_called_platform_math_insider :: num_fract_value_get ( value , value_fract ) ;
        if ( value < so_called_lib_std_float ( value_min ) || value > so_called_lib_std_float ( value_max ) )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Fract value " ) ;
            so_called_platform_trace :: trace_num_fract_error ( value_fract ) ;
            so_called_platform_trace :: trace_string_error ( " exceeds range from " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( value_min ) ;
            so_called_platform_trace :: trace_string_error ( " to " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( value_max ) ;
            so_called_platform_trace :: trace_string_error ( "." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_num_fract_non_positive ( so_called_platform_math_num_fract_type value_fract )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_float value = 0 ;
        so_called_platform_math_insider :: num_fract_value_get ( value , value_fract ) ;
        if ( value <= so_called_lib_std_float ( 0 ) )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Fract value " ) ;
            so_called_platform_trace :: trace_num_fract_error ( value_fract ) ;
            so_called_platform_trace :: trace_string_error ( " is not positive." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_num_fract_not_less_than_fract ( so_called_platform_math_num_fract_type value1_fract , so_called_platform_math_num_fract_type value2_fract )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_float value1 = 0 ;
        so_called_lib_std_float value2 = 0 ;
        so_called_platform_math_insider :: num_fract_value_get ( value1 , value1_fract ) ;
        so_called_platform_math_insider :: num_fract_value_get ( value2 , value2_fract ) ;
        if ( value1 >= value2 )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Fract value " ) ;
            so_called_platform_trace :: trace_num_fract_error ( value1_fract ) ;
            so_called_platform_trace :: trace_string_error ( " is not less than " ) ;
            so_called_platform_trace :: trace_num_fract_error ( value2_fract ) ;
            so_called_platform_trace :: trace_string_error ( "." ) ;
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
