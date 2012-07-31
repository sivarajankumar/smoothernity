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

void shy_trace_platform_math :: check_num_whole_non_positive ( so_called_platform_math_num_whole_type value_whole )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_int32_t value = 0 ;
        so_called_platform_math_insider :: num_whole_value_get ( value , value_whole ) ;
        if ( value <= 0 )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Whole value " ) ;
            so_called_platform_trace :: trace_num_whole_error ( value_whole ) ;
            so_called_platform_trace :: trace_string_error ( " is not positive." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_math :: check_num_whole_negative ( so_called_platform_math_num_whole_type value_whole )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_int32_t value = 0 ;
        so_called_platform_math_insider :: num_whole_value_get ( value , value_whole ) ;
        if ( value < 0 )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Whole value " ) ;
            so_called_platform_trace :: trace_num_whole_error ( value_whole ) ;
            so_called_platform_trace :: trace_string_error ( " is negative." ) ;
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

void shy_trace_platform_math :: check_args_sin ( so_called_platform_math_num_fract_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_num_fract_uninitialized ( a ) ;
}

void shy_trace_platform_math :: check_args_cos ( so_called_platform_math_num_fract_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_num_fract_uninitialized ( a ) ;
}

void shy_trace_platform_math :: check_args_add_to_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_sub_from_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_sub_wholes ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_add_fracts ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_fract_uninitialized ( a ) ;
        check_num_fract_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_mul_fracts ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_fract_uninitialized ( a ) ;
        check_num_fract_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_mul_fract_by ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_fract_uninitialized ( a ) ;
        check_num_fract_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_make_num_fract
    ( so_called_platform_math_const_int_32_type numerator 
    , so_called_platform_math_const_int_32_type denominator 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_division_const_int_32_by_zero ( numerator , denominator ) ;
}

void shy_trace_platform_math :: check_args_make_whole_from_fract ( so_called_platform_math_num_fract_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_num_fract_uninitialized ( a ) ;
}

void shy_trace_platform_math :: check_args_make_fract_from_whole ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_math :: check_args_mod_wholes ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
        check_division_num_whole_by_zero ( a , b ) ;
    }
}

void shy_trace_platform_math :: check_args_mod_whole_by ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
        check_division_num_whole_by_zero ( a , b ) ;
    }
}

void shy_trace_platform_math :: check_args_div_wholes ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
        check_division_num_whole_by_zero ( a , b ) ;
    }
}

void shy_trace_platform_math :: check_args_div_whole_by ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
        check_division_num_whole_by_zero ( a , b ) ;
    }
}

void shy_trace_platform_math :: check_args_div_fract_by ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_fract_uninitialized ( a ) ;
        check_num_fract_uninitialized ( b ) ;
        check_division_num_fract_by_zero ( a , b ) ;
    }
}

void shy_trace_platform_math :: check_args_neg_fract ( so_called_platform_math_num_fract_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_num_fract_uninitialized ( a ) ;
}

void shy_trace_platform_math :: check_args_sub_fracts ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_fract_uninitialized ( a ) ;
        check_num_fract_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_add_to_fract ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_fract_uninitialized ( a ) ;
        check_num_fract_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_sub_from_fract ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_fract_uninitialized ( a ) ;
        check_num_fract_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_inc_whole ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_math :: check_args_dec_whole ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_math :: check_args_neg_whole ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_math :: check_args_mul_wholes ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_mul_whole_by ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_add_wholes ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_xor_wholes ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_whole_uninitialized ( a ) ;
        check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_math :: check_args_div_fracts ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_num_fract_uninitialized ( a ) ;
        check_num_fract_uninitialized ( b ) ;
        check_division_num_fract_by_zero ( a , b ) ;
    }
}