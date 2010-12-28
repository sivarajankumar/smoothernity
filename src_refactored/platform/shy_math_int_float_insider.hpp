#include "shy_math_int_float_insider.h"

void shy_platform_math_int_float_insider :: num_whole_value_get ( int & value , num_whole num )
{
    value = num . _value ;
}

void shy_platform_math_int_float_insider :: num_whole_value_set ( num_whole & num , int value )
{
    num . _value = value ;
}

void shy_platform_math_int_float_insider :: num_fract_value_get ( float & value , num_fract num )
{
    value = num . _value ;
}

void shy_platform_math_int_float_insider :: num_fract_value_set ( num_fract & num , float value )
{
    num . _value = value ;
}
