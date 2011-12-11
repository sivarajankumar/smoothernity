namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_conditions" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_conditions :: check_args_wholes_are_equal ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_conditions :: check_args_whole_is_true ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_conditions :: check_args_whole_is_false ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_conditions :: check_args_whole_greater_than_zero ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_conditions :: check_args_whole_less_than_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_conditions :: check_args_whole_less_or_equal_to_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_conditions :: check_args_whole_is_zero ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_conditions :: check_args_whole_is_even ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_conditions :: check_args_whole_less_or_equal_to_zero ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_conditions :: check_args_whole_greater_or_equal_to_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_conditions :: check_args_whole_less_than_zero ( so_called_platform_math_num_whole_type a )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
}

void shy_trace_platform_conditions :: check_args_whole_greater_than_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ;
    }
}

void shy_trace_platform_conditions :: check_args_fract_less_than_fract ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ;
    }
}

void shy_trace_platform_conditions :: check_args_fract_greater_than_fract ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ;
    }
}
