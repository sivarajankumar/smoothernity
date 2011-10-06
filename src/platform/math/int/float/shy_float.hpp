void shy_platform_math_int_float :: sin ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_sin_cos ( ) ) ;
    result . _value = so_called_lib_std_sinf ( a . _value ) ;
}

void shy_platform_math_int_float :: cos ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_sin_cos ( ) ) ;
    result . _value = so_called_lib_std_cosf ( a . _value ) ;
}

void shy_platform_math_int_float :: add_to_whole ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_add_sub ( ) ) ;
    a . _value += b . _value ;
}

void shy_platform_math_int_float :: sub_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type from 
    , so_called_platform_math_int_float_num_whole_type what
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( from ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( what ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_add_sub ( ) ) ;
    result . _value = from . _value - what . _value ;
}

void shy_platform_math_int_float :: add_fracts 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_num_fract_type a 
    , so_called_platform_math_int_float_num_fract_type b 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_add_sub ( ) ) ;
    result . _value = a . _value + b . _value ;
}

void shy_platform_math_int_float :: mul_fracts 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_num_fract_type a 
    , so_called_platform_math_int_float_num_fract_type b 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_mul ( ) ) ;
    result . _value = a . _value * b . _value ;
}

void shy_platform_math_int_float :: mul_fract_by ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_mul ( ) ) ;
    a . _value *= b . _value ;
}
    
void shy_platform_math_int_float :: make_num_whole ( so_called_platform_math_int_float_num_whole_type & result , so_called_platform_math_int_float_const_int_32_type value )
{
    so_called_profile ( so_called_profile_platform_math :: whole_make ( ) ) ;
    result . _value = so_called_lib_std_int32_t ( value ) ;
}

void shy_platform_math_int_float :: make_num_fract 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_const_int_32_type numerator 
    , so_called_platform_math_int_float_const_int_32_type denominator 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_division_const_int_32_by_zero ( numerator , denominator ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_make ( ) ) ;
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
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( fract ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_make_from_fract ( ) ) ;
    result . _value = so_called_lib_std_int32_t ( fract . _value ) ;
}

void shy_platform_math_int_float :: sub_from_whole ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_add_sub ( ) ) ;
    a . _value -= b . _value ;
}

void shy_platform_math_int_float :: mod_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type value 
    , so_called_platform_math_int_float_num_whole_type modulator 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( value ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( modulator ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_division_num_whole_by_zero ( value , modulator ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_div_mod ( ) ) ;
    result . _value = value . _value % modulator . _value ;
}

void shy_platform_math_int_float :: div_fract_by ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_division_num_fract_by_zero ( a , b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_div ( ) ) ;
    a . _value /= b . _value ;
}

void shy_platform_math_int_float :: neg_fract ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_add_sub ( ) ) ;
    result . _value = - a . _value ;
}
    
void shy_platform_math_int_float :: make_fract_from_whole ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_whole_type whole )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( whole ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_make_from_whole ( ) ) ;
    result . _value = so_called_lib_std_float ( whole . _value ) ;
}

void shy_platform_math_int_float :: sub_fracts 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_num_fract_type from 
    , so_called_platform_math_int_float_num_fract_type what 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( from ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( what ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_add_sub ( ) ) ;
    result . _value = from . _value - what . _value ;
}

void shy_platform_math_int_float :: add_to_fract ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_add_sub ( ) ) ;
    a . _value += b . _value ;
}

void shy_platform_math_int_float :: inc_whole ( so_called_platform_math_int_float_num_whole_type & a )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_add_sub ( ) ) ;
    ++ a . _value ;
}

void shy_platform_math_int_float :: mul_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type a 
    , so_called_platform_math_int_float_num_whole_type b 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_mul ( ) ) ;
    result . _value = a . _value * b . _value ;
}

void shy_platform_math_int_float :: div_fracts 
    ( so_called_platform_math_int_float_num_fract_type & result 
    , so_called_platform_math_int_float_num_fract_type a 
    , so_called_platform_math_int_float_num_fract_type b 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_division_num_fract_by_zero ( a , b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_div ( ) ) ;
    result . _value = a . _value / b . _value ;
}

void shy_platform_math_int_float :: mod_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_division_num_whole_by_zero ( a , b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_div_mod ( ) ) ;
    a . _value %= b . _value ;
}

void shy_platform_math_int_float :: div_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_division_num_whole_by_zero ( a , b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_div_mod ( ) ) ;
    a . _value /= b . _value ;
}

void shy_platform_math_int_float :: add_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type a 
    , so_called_platform_math_int_float_num_whole_type b
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_add_sub ( ) ) ;
    result . _value = a . _value + b . _value ;
}

void shy_platform_math_int_float :: sub_from_fract ( so_called_platform_math_int_float_num_fract_type & from , so_called_platform_math_int_float_num_fract_type what )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( from ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( what ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_add_sub ( ) ) ;
    from . _value -= what . _value ;
}

void shy_platform_math_int_float :: xor_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type a 
    , so_called_platform_math_int_float_num_whole_type b 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_bitwise ( ) ) ;
    result . _value = a . _value ^ b . _value ;
}

void shy_platform_math_int_float :: mul_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_mul ( ) ) ;
    a . _value *= b . _value ;
}

void shy_platform_math_int_float :: div_wholes 
    ( so_called_platform_math_int_float_num_whole_type & result 
    , so_called_platform_math_int_float_num_whole_type a 
    , so_called_platform_math_int_float_num_whole_type b 
    )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( b ) ) ;
    so_called_trace ( so_called_trace_platform_math :: check_division_num_whole_by_zero ( a , b ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_div_mod ( ) ) ;
    result . _value = a . _value / b . _value ;
}

void shy_platform_math_int_float :: dec_whole ( so_called_platform_math_int_float_num_whole_type & a )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_add_sub ( ) ) ;
    -- a . _value ;
}

void shy_platform_math_int_float :: neg_fract ( so_called_platform_math_int_float_num_fract_type & a )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ) ;
    so_called_profile ( so_called_profile_platform_math :: fract_add_sub ( ) ) ;
    a . _value = - a . _value ;
}

void shy_platform_math_int_float :: neg_whole ( so_called_platform_math_int_float_num_whole_type & result , so_called_platform_math_int_float_num_whole_type a )
{
    so_called_trace ( so_called_trace_platform_math :: check_num_whole_uninitialized ( a ) ) ;
    so_called_profile ( so_called_profile_platform_math :: whole_add_sub ( ) ) ;
    result . _value = - a . _value ;
}

