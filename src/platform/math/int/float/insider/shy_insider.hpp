void shy_platform_math_int_float_insider :: num_whole_value_get ( so_called_lib_std_int32_t & value , so_called_platform_math_int_float_num_whole_type num )
{
    value = num . _value ;
}

void shy_platform_math_int_float_insider :: num_whole_value_set ( so_called_platform_math_int_float_num_whole_type & num , so_called_lib_std_int32_t value )
{
    num . _value = value ;
}

void shy_platform_math_int_float_insider :: num_whole_uninitialized ( so_called_lib_std_bool & result , so_called_platform_math_int_float_num_whole_type value )
{
    so_called_platform_math_int_float_num_whole_type uninitialized_value ;
    result = value . _value == uninitialized_value . _value ;
}

void shy_platform_math_int_float_insider :: num_fract_value_get ( so_called_lib_std_float & value , so_called_platform_math_int_float_num_fract_type num )
{
    value = num . _value ;
}

void shy_platform_math_int_float_insider :: num_fract_value_set ( so_called_platform_math_int_float_num_fract_type & num , so_called_lib_std_float value )
{
    num . _value = value ;
}

void shy_platform_math_int_float_insider :: num_fract_uninitialized ( so_called_lib_std_bool & result , so_called_platform_math_int_float_num_fract_type value )
{
    so_called_platform_math_int_float_num_fract_type uninitialized_value ;
    result = value . _value == uninitialized_value . _value ;
}

so_called_platform_math_int_float_num_whole_type shy_platform_math_int_float_insider :: init_num_whole ( so_called_lib_std_int32_t value )
{
    so_called_platform_math_int_float_num_whole_type result ;
    result . _value = value ;
    return result ;
}

so_called_platform_math_int_float_num_fract_type shy_platform_math_int_float_insider :: init_num_fract ( so_called_lib_std_float value )
{
    so_called_platform_math_int_float_num_fract_type result ;
    result . _value = value ;
    return result ;
}
