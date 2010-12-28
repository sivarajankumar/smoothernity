#include "shy_math_int_float.h"
#include <math.h>

shy_platform_math_int_float :: num_whole :: num_whole ( )
: _value ( so_called_platform_consts_insider :: uninitialized_value )
{
}

shy_platform_math_int_float :: num_whole :: num_whole ( int arg_value )
: _value ( arg_value )
{
}

shy_platform_math_int_float :: num_fract :: num_fract ( )
: _value ( ( float ) so_called_platform_consts_insider :: uninitialized_value )
{
}

shy_platform_math_int_float :: num_fract :: num_fract ( float arg_value )
: _value ( arg_value )
{
}

void shy_platform_math_int_float :: sin ( num_fract & result , num_fract a )
{
    result . _value = sinf ( a . _value ) ;
}

void shy_platform_math_int_float :: cos ( num_fract & result , num_fract a )
{
    result . _value = cosf ( a . _value ) ;
}

void shy_platform_math_int_float :: add_to_whole ( num_whole & a , num_whole b )
{
    a . _value += b . _value ;
}

void shy_platform_math_int_float :: sub_wholes ( num_whole & result , num_whole from , num_whole what )
{
    result . _value = from . _value - what . _value ;
}

void shy_platform_math_int_float :: add_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value + b . _value ;
}

void shy_platform_math_int_float :: mul_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value * b . _value ;
}

void shy_platform_math_int_float :: mul_fract_by ( num_fract & a , num_fract b )
{
    a . _value *= b . _value ;
}
    
void shy_platform_math_int_float :: make_num_whole ( num_whole & result , const_int_32 value )
{
    result . _value = int ( value ) ;
}

void shy_platform_math_int_float :: make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator )
{
    result . _value = float ( numerator ) / float ( denominator ) ;
}

void shy_platform_math_int_float :: make_whole_from_fract ( num_whole & result , num_fract fract )
{
    result . _value = int ( fract . _value ) ;
}

void shy_platform_math_int_float :: sub_from_whole ( num_whole & a , num_whole b )
{
    a . _value -= b . _value ;
}

void shy_platform_math_int_float :: mod_wholes ( num_whole & result , num_whole value , num_whole modulator )
{
    result . _value = value . _value % modulator . _value ;
}

void shy_platform_math_int_float :: div_fract_by ( num_fract & a , num_fract b )
{
    a . _value /= b . _value ;
}

void shy_platform_math_int_float :: neg_fract ( num_fract & result , num_fract a )
{
    result . _value = - a . _value ;
}
    
void shy_platform_math_int_float :: make_fract_from_whole ( num_fract & result , num_whole whole )
{
    result . _value = float ( whole . _value ) ;
}

void shy_platform_math_int_float :: sub_fracts ( num_fract & result , num_fract from , num_fract what )
{
    result . _value = from . _value - what . _value ;
}

void shy_platform_math_int_float :: add_to_fract ( num_fract & a , num_fract b )
{
    a . _value += b . _value ;
}

void shy_platform_math_int_float :: inc_whole ( num_whole & a )
{
    ++ a . _value ;
}

void shy_platform_math_int_float :: mul_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value * b . _value ;
}

void shy_platform_math_int_float :: div_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value / b . _value ;
}

void shy_platform_math_int_float :: mod_whole_by ( num_whole & a , num_whole b )
{
    a . _value %= b . _value ;
}

void shy_platform_math_int_float :: div_whole_by ( num_whole & a , num_whole b )
{
    a . _value /= b . _value ;
}

void shy_platform_math_int_float :: add_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value + b . _value ;
}

void shy_platform_math_int_float :: sub_from_fract ( num_fract & from , num_fract what )
{
    from . _value -= what . _value ;
}

void shy_platform_math_int_float :: xor_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value ^ b . _value ;
}

void shy_platform_math_int_float :: mul_whole_by ( num_whole & a , num_whole b )
{
    a . _value *= b . _value ;
}

void shy_platform_math_int_float :: div_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value / b . _value ;
}

void shy_platform_math_int_float :: dec_whole ( num_whole & a )
{
    -- a . _value ;
}

void shy_platform_math_int_float :: neg_fract ( num_fract & a )
{
    a . _value = - a . _value ;
}

void shy_platform_math_int_float :: neg_whole ( num_whole & result , num_whole a )
{
    result . _value = - a . _value ;
}

