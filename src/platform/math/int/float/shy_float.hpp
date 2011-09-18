void shy_platform_math_int_float :: sin ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a )
{
    result . _value = so_called_lib_std_sinf ( a . _value ) ;
}

void shy_platform_math_int_float :: cos ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a )
{
    result . _value = so_called_lib_std_cosf ( a . _value ) ;
}

void shy_platform_math_int_float :: add_to_whole ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    a . _value += b . _value ;
}

void shy_platform_math_int_float :: sub_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type from 
    , so_called_platform_math_int_float_num_whole_type what
    )
{
    result . _value = from . _value - what . _value ;
}

void shy_platform_math_int_float :: add_fracts 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_num_fract_type a 
    , so_called_platform_math_int_float_num_fract_type b 
    )
{
    result . _value = a . _value + b . _value ;
}

void shy_platform_math_int_float :: mul_fracts 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_num_fract_type a 
    , so_called_platform_math_int_float_num_fract_type b 
    )
{
    result . _value = a . _value * b . _value ;
}

void shy_platform_math_int_float :: mul_fract_by ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b )
{
    a . _value *= b . _value ;
}
    
void shy_platform_math_int_float :: make_num_whole ( so_called_platform_math_int_float_num_whole_type & result , so_called_platform_math_int_float_const_int_32_type value )
{
    result . _value = so_called_lib_std_int32_t ( value ) ;
}

void shy_platform_math_int_float :: make_num_fract 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_const_int_32_type numerator 
    , so_called_platform_math_int_float_const_int_32_type denominator 
    )
{
    result . _value = so_called_lib_std_float ( numerator ) / so_called_lib_std_float ( denominator ) ;
}

so_called_platform_math_int_float_num_whole_type shy_platform_math_int_float :: init_num_whole ( so_called_platform_math_int_float_const_int_32_type value )
{
    so_called_platform_math_int_float_num_whole_type result ;
    result . _value = so_called_lib_std_int32_t ( value ) ;
    return result ;
}

so_called_platform_math_int_float_num_fract_type shy_platform_math_int_float :: init_num_fract 
    ( so_called_platform_math_int_float_const_int_32_type numerator 
    , so_called_platform_math_int_float_const_int_32_type denominator 
    )
{
    so_called_platform_math_int_float_num_fract_type result ;
    result . _value = so_called_lib_std_float ( numerator ) / so_called_lib_std_float ( denominator ) ;
    return result ;
}

void shy_platform_math_int_float :: make_whole_from_fract ( so_called_platform_math_int_float_num_whole_type & result , so_called_platform_math_int_float_num_fract_type fract )
{
    result . _value = so_called_lib_std_int32_t ( fract . _value ) ;
}

void shy_platform_math_int_float :: sub_from_whole ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    a . _value -= b . _value ;
}

void shy_platform_math_int_float :: mod_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type value 
    , so_called_platform_math_int_float_num_whole_type modulator 
    )
{
    result . _value = value . _value % modulator . _value ;
}

void shy_platform_math_int_float :: div_fract_by ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b )
{
    a . _value /= b . _value ;
}

void shy_platform_math_int_float :: neg_fract ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a )
{
    result . _value = - a . _value ;
}
    
void shy_platform_math_int_float :: make_fract_from_whole ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_whole_type whole )
{
    result . _value = so_called_lib_std_float ( whole . _value ) ;
}

void shy_platform_math_int_float :: sub_fracts 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_num_fract_type from 
    , so_called_platform_math_int_float_num_fract_type what 
    )
{
    result . _value = from . _value - what . _value ;
}

void shy_platform_math_int_float :: add_to_fract ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b )
{
    a . _value += b . _value ;
}

void shy_platform_math_int_float :: inc_whole ( so_called_platform_math_int_float_num_whole_type & a )
{
    ++ a . _value ;
}

void shy_platform_math_int_float :: mul_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type a 
    , so_called_platform_math_int_float_num_whole_type b 
    )
{
    result . _value = a . _value * b . _value ;
}

void shy_platform_math_int_float :: div_fracts 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_num_fract_type a 
    , so_called_platform_math_int_float_num_fract_type b 
    )
{
    result . _value = a . _value / b . _value ;
}

void shy_platform_math_int_float :: mod_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    a . _value %= b . _value ;
}

void shy_platform_math_int_float :: div_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    a . _value /= b . _value ;
}

void shy_platform_math_int_float :: add_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type a 
    , so_called_platform_math_int_float_num_whole_type b
    )
{
    result . _value = a . _value + b . _value ;
}

void shy_platform_math_int_float :: sub_from_fract ( so_called_platform_math_int_float_num_fract_type & from , so_called_platform_math_int_float_num_fract_type what )
{
    from . _value -= what . _value ;
}

void shy_platform_math_int_float :: xor_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type a 
    , so_called_platform_math_int_float_num_whole_type b 
    )
{
    result . _value = a . _value ^ b . _value ;
}

void shy_platform_math_int_float :: mul_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    a . _value *= b . _value ;
}

void shy_platform_math_int_float :: div_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type a 
    , so_called_platform_math_int_float_num_whole_type b 
    )
{
    result . _value = a . _value / b . _value ;
}

void shy_platform_math_int_float :: dec_whole ( so_called_platform_math_int_float_num_whole_type & a )
{
    -- a . _value ;
}

void shy_platform_math_int_float :: neg_fract ( so_called_platform_math_int_float_num_fract_type & a )
{
    a . _value = - a . _value ;
}

void shy_platform_math_int_float :: neg_whole ( so_called_platform_math_int_float_num_whole_type & result , so_called_platform_math_int_float_num_whole_type a )
{
    result . _value = - a . _value ;
}

