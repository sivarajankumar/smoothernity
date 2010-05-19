inline void shy_macosx_platform :: math_sin ( num_fract & result , num_fract a )
{
    result . _value = sinf ( a . _value ) ;
}

inline void shy_macosx_platform :: math_cos ( num_fract & result , num_fract a )
{
    result . _value = cosf ( a . _value ) ;
}

inline void shy_macosx_platform :: math_add_to_whole ( num_whole & a , num_whole b )
{
    a . _value += b . _value ;
}

inline void shy_macosx_platform :: math_sub_wholes ( num_whole & result , num_whole from , num_whole what )
{
    result . _value = from . _value - what . _value ;
}

inline void shy_macosx_platform :: math_add_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value + b . _value ;
}

inline void shy_macosx_platform :: math_mul_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value * b . _value ;
}

inline void shy_macosx_platform :: math_mul_fract_by ( num_fract & a , num_fract b )
{
    a . _value *= b . _value ;
}
    
inline void shy_macosx_platform :: math_make_num_whole ( num_whole & result , const_int_32 value )
{
    result . _value = int ( value ) ;
}

inline void shy_macosx_platform :: math_make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator )
{
    result . _value = float ( numerator ) / float ( denominator ) ;
}

inline void shy_macosx_platform :: math_make_whole_from_fract ( num_whole & result , num_fract fract )
{
    result . _value = int ( fract . _value ) ;
}

inline void shy_macosx_platform :: math_sub_from_whole ( num_whole & a , num_whole b )
{
    a . _value -= b . _value ;
}

inline void shy_macosx_platform :: math_mod_wholes ( num_whole & result , num_whole value , num_whole modulator )
{
    result . _value = value . _value % modulator . _value ;
}

inline void shy_macosx_platform :: math_div_fract_by ( num_fract & a , num_fract b )
{
    a . _value /= b . _value ;
}

inline void shy_macosx_platform :: math_neg_fract ( num_fract & result , num_fract a )
{
    result . _value = - a . _value ;
}
    
inline void shy_macosx_platform :: math_make_fract_from_whole ( num_fract & result , num_whole whole )
{
    result . _value = float ( whole . _value ) ;
}
