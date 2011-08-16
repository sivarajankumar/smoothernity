void shy_platform_math_int_float_insider :: num_whole_value_get ( so_called_lib_std_int32_t & value , so_called_type_platform_math_int_float_num_whole num )
{
    value = num . _value ;
}

void shy_platform_math_int_float_insider :: num_whole_value_set ( so_called_type_platform_math_int_float_num_whole & num , so_called_lib_std_int32_t value )
{
    num . _value = value ;
}

void shy_platform_math_int_float_insider :: num_fract_value_get ( so_called_lib_std_float & value , so_called_type_platform_math_int_float_num_fract num )
{
    value = num . _value ;
}

void shy_platform_math_int_float_insider :: num_fract_value_set ( so_called_type_platform_math_int_float_num_fract & num , so_called_lib_std_float value )
{
    num . _value = value ;
}

so_called_type_platform_math_int_float_num_whole shy_platform_math_int_float_insider :: init_num_whole ( so_called_lib_std_int32_t value )
{
    so_called_type_platform_math_int_float_num_whole result ;
    result . _value = value ;
    return result ;
}

so_called_type_platform_math_int_float_num_fract shy_platform_math_int_float_insider :: init_num_fract ( so_called_lib_std_float value )
{
    so_called_type_platform_math_int_float_num_fract result ;
    result . _value = value ;
    return result ;
}
