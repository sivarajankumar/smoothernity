so_called_lib_std_bool shy_platform_conditions :: wholes_are_equal ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t a_int = 0 ;
    so_called_lib_std_int32_t b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int == b_int ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_is_true ( so_called_platform_math_num_whole_type num )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == so_called_lib_std_int32_t ( so_called_lib_std_true ) ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_is_false ( so_called_platform_math_num_whole_type num )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == so_called_lib_std_int32_t ( so_called_lib_std_false ) ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_greater_than_zero ( so_called_platform_math_num_whole_type num )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int > 0 ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_less_than_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t a_int = 0 ;
    so_called_lib_std_int32_t b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int < b_int ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_less_or_equal_to_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t a_int = 0 ;
    so_called_lib_std_int32_t b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int <= b_int ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_is_zero ( so_called_platform_math_num_whole_type num )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == 0 ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_is_even ( so_called_platform_math_num_whole_type num )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int % 2 == 0 ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_less_or_equal_to_zero ( so_called_platform_math_num_whole_type num )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int <= 0 ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_greater_or_equal_to_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t a_int = 0 ;
    so_called_lib_std_int32_t b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int >= b_int ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_less_than_zero ( so_called_platform_math_num_whole_type num )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int < 0 ;
}

so_called_lib_std_bool shy_platform_conditions :: whole_greater_than_whole ( so_called_platform_math_num_whole_type a , so_called_platform_math_num_whole_type b )
{
    so_called_profile ( so_called_profile_platform_conditions :: whole ( ) ) ;
    so_called_lib_std_int32_t a_int = 0 ;
    so_called_lib_std_int32_t b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int > b_int ;
}

so_called_lib_std_bool shy_platform_conditions :: fract_less_than_fract ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    so_called_profile ( so_called_profile_platform_conditions :: fract ( ) ) ;
    so_called_lib_std_float a_float = 0 ;
    so_called_lib_std_float b_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    return a_float < b_float ;
}

so_called_lib_std_bool shy_platform_conditions :: fract_greater_than_fract ( so_called_platform_math_num_fract_type a , so_called_platform_math_num_fract_type b )
{
    so_called_profile ( so_called_profile_platform_conditions :: fract ( ) ) ;
    so_called_lib_std_float a_float = 0 ;
    so_called_lib_std_float b_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    return a_float > b_float ;
}
