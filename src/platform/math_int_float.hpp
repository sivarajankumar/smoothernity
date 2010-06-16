template < typename platform >
class shy_platform_math_int_float
{
    typedef typename platform :: const_int_32 const_int_32 ;
public :
    class num_whole
    {
        friend class shy_platform_math_int_float ;
    public :
        num_whole ( ) ;
    private :
        num_whole ( int arg_value ) ;
    private :
        int _value ;
    } ;
    
    class num_fract
    {
        friend class shy_platform_math_int_float ;
    public :
        num_fract ( ) ;
    private :
        num_fract ( float arg_value ) ;
    private :
        float _value ;
    } ;
    
    static void math_add_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void math_add_to_whole ( num_whole & a , num_whole b ) ;
    static void math_sub_wholes ( num_whole & result , num_whole from , num_whole what ) ;
    static void math_sub_from_whole ( num_whole & a , num_whole b ) ;
    static void math_mul_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void math_mul_whole_by ( num_whole & a , num_whole b ) ;
    static void math_mod_wholes ( num_whole & result , num_whole value , num_whole modulator ) ;
    static void math_mod_whole_by ( num_whole & a , num_whole b ) ;
    static void math_div_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void math_div_whole_by ( num_whole & a , num_whole b ) ;
    static void math_inc_whole ( num_whole & a ) ;
    static void math_dec_whole ( num_whole & a ) ;
    static void math_xor_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void math_neg_whole ( num_whole & result , num_whole a ) ;

    static void math_sin ( num_fract & result , num_fract a ) ;
    static void math_cos ( num_fract & result , num_fract a ) ;    
    static void math_sub_fracts ( num_fract & result , num_fract from , num_fract what ) ;
    static void math_sub_from_fract ( num_fract & from , num_fract what ) ;
    static void math_add_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void math_add_to_fract ( num_fract & a , num_fract b ) ;
    static void math_mul_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void math_mul_fract_by ( num_fract & a , num_fract b ) ;
    static void math_div_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void math_div_fract_by ( num_fract & a , num_fract b ) ;
    static void math_neg_fract ( num_fract & a ) ;
    static void math_neg_fract ( num_fract & result , num_fract a ) ;
    
    static void math_make_whole_from_fract ( num_whole & result , num_fract fract ) ;
    static void math_make_fract_from_whole ( num_fract & result , num_whole whole ) ;
    
    static void math_make_num_whole ( num_whole & result , const_int_32 value ) ;
    static void math_make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator ) ;
} ;

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_sin ( num_fract & result , num_fract a )
{
    result . _value = sinf ( a . _value ) ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_cos ( num_fract & result , num_fract a )
{
    result . _value = cosf ( a . _value ) ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_add_to_whole ( num_whole & a , num_whole b )
{
    a . _value += b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_sub_wholes ( num_whole & result , num_whole from , num_whole what )
{
    result . _value = from . _value - what . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_add_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value + b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_mul_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value * b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_mul_fract_by ( num_fract & a , num_fract b )
{
    a . _value *= b . _value ;
}
    
template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_make_num_whole ( num_whole & result , const_int_32 value )
{
    result . _value = int ( value ) ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator )
{
    result . _value = float ( numerator ) / float ( denominator ) ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_make_whole_from_fract ( num_whole & result , num_fract fract )
{
    result . _value = int ( fract . _value ) ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_sub_from_whole ( num_whole & a , num_whole b )
{
    a . _value -= b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_mod_wholes ( num_whole & result , num_whole value , num_whole modulator )
{
    result . _value = value . _value % modulator . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_div_fract_by ( num_fract & a , num_fract b )
{
    a . _value /= b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_neg_fract ( num_fract & result , num_fract a )
{
    result . _value = - a . _value ;
}
    
template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_make_fract_from_whole ( num_fract & result , num_whole whole )
{
    result . _value = float ( whole . _value ) ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_sub_fracts ( num_fract & result , num_fract from , num_fract what )
{
    result . _value = from . _value - what . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_add_to_fract ( num_fract & a , num_fract b )
{
    a . _value += b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_inc_whole ( num_whole & a )
{
    ++ a . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_mul_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value * b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_div_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value / b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_mod_whole_by ( num_whole & a , num_whole b )
{
    a . _value %= b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_div_whole_by ( num_whole & a , num_whole b )
{
    a . _value /= b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_add_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value + b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_sub_from_fract ( num_fract & from , num_fract what )
{
    from . _value -= what . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_xor_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value ^ b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_mul_whole_by ( num_whole & a , num_whole b )
{
    a . _value *= b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_div_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value / b . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_dec_whole ( num_whole & a )
{
    -- a . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_neg_fract ( num_fract & a )
{
    a . _value = - a . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float < platform > :: math_neg_whole ( num_whole & result , num_whole a )
{
    result . _value = - a . _value ;
}
