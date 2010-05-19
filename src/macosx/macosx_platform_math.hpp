inline void shy_macosx_platform :: math_sin ( float_32 & result , float_32 a )
{
    result = sinf ( a ) ;
}

inline void shy_macosx_platform :: math_cos ( float_32 & result , float_32 a )
{
    result = cosf ( a ) ;
}

inline void shy_macosx_platform :: math_make_num_whole ( num_whole & result , const_int_32 value )
{
    result . _value = int ( value ) ;
}

inline void shy_macosx_platform :: math_make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator )
{
    result . _value = float ( numerator ) / float ( denominator ) ;
}
