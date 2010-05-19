inline void shy_macosx_platform :: math_sin ( float_32 & result , num_fract a )
{
    result = sinf ( a . _value ) ;
}

inline void shy_macosx_platform :: math_cos ( float_32 & result , num_fract a )
{
    result = cosf ( a . _value ) ;
}

inline void shy_macosx_platform :: math_sub_wholes ( num_whole & result , num_whole from , num_whole what )
{
    result . _value = from . _value - what . _value ;
}

inline void shy_macosx_platform :: math_add_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value + b . _value ;
}

inline void shy_macosx_platform :: math_make_num_whole ( num_whole & result , const_int_32 value )
{
    result . _value = int ( value ) ;
}

inline void shy_macosx_platform :: math_make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator )
{
    result . _value = float ( numerator ) / float ( denominator ) ;
}
