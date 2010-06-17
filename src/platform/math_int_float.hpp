template < typename platform_insider >
class shy_platform_math_int_float_insider ;

template < typename platform_insider >
class shy_platform_math_int_float
{
public :
    typedef const int const_int_32 ;
    
    class num_whole
    {
        friend class shy_platform_math_int_float ;
        friend class shy_platform_math_int_float_insider < platform_insider > ;
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
        friend class shy_platform_math_int_float_insider < platform_insider > ;
    public :
        num_fract ( ) ;
    private :
        num_fract ( float arg_value ) ;
    private :
        float _value ;
    } ;
    
public :
    static void add_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void add_to_whole ( num_whole & a , num_whole b ) ;
    static void sub_wholes ( num_whole & result , num_whole from , num_whole what ) ;
    static void sub_from_whole ( num_whole & a , num_whole b ) ;
    static void mul_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void mul_whole_by ( num_whole & a , num_whole b ) ;
    static void mod_wholes ( num_whole & result , num_whole value , num_whole modulator ) ;
    static void mod_whole_by ( num_whole & a , num_whole b ) ;
    static void div_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void div_whole_by ( num_whole & a , num_whole b ) ;
    static void inc_whole ( num_whole & a ) ;
    static void dec_whole ( num_whole & a ) ;
    static void xor_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void neg_whole ( num_whole & result , num_whole a ) ;

    static void sin ( num_fract & result , num_fract a ) ;
    static void cos ( num_fract & result , num_fract a ) ;    
    static void sub_fracts ( num_fract & result , num_fract from , num_fract what ) ;
    static void sub_from_fract ( num_fract & from , num_fract what ) ;
    static void add_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void add_to_fract ( num_fract & a , num_fract b ) ;
    static void mul_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void mul_fract_by ( num_fract & a , num_fract b ) ;
    static void div_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void div_fract_by ( num_fract & a , num_fract b ) ;
    static void neg_fract ( num_fract & a ) ;
    static void neg_fract ( num_fract & result , num_fract a ) ;
    
    static void make_whole_from_fract ( num_whole & result , num_fract fract ) ;
    static void make_fract_from_whole ( num_fract & result , num_whole whole ) ;
    
    static void make_num_whole ( num_whole & result , const_int_32 value ) ;
    static void make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator ) ;
} ;

template < typename platform_insider >
shy_platform_math_int_float < platform_insider > :: num_whole :: num_whole ( )
: _value ( platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
shy_platform_math_int_float < platform_insider > :: num_whole :: num_whole ( int arg_value )
: _value ( arg_value )
{
}

template < typename platform_insider >
shy_platform_math_int_float < platform_insider > :: num_fract :: num_fract ( )
: _value ( platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
shy_platform_math_int_float < platform_insider > :: num_fract :: num_fract ( float arg_value )
: _value ( arg_value )
{
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: sin ( num_fract & result , num_fract a )
{
    result . _value = sinf ( a . _value ) ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: cos ( num_fract & result , num_fract a )
{
    result . _value = cosf ( a . _value ) ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: add_to_whole ( num_whole & a , num_whole b )
{
    a . _value += b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: sub_wholes ( num_whole & result , num_whole from , num_whole what )
{
    result . _value = from . _value - what . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: add_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value + b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: mul_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value * b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: mul_fract_by ( num_fract & a , num_fract b )
{
    a . _value *= b . _value ;
}
    
template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: make_num_whole ( num_whole & result , const_int_32 value )
{
    result . _value = int ( value ) ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator )
{
    result . _value = float ( numerator ) / float ( denominator ) ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: make_whole_from_fract ( num_whole & result , num_fract fract )
{
    result . _value = int ( fract . _value ) ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: sub_from_whole ( num_whole & a , num_whole b )
{
    a . _value -= b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: mod_wholes ( num_whole & result , num_whole value , num_whole modulator )
{
    result . _value = value . _value % modulator . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: div_fract_by ( num_fract & a , num_fract b )
{
    a . _value /= b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: neg_fract ( num_fract & result , num_fract a )
{
    result . _value = - a . _value ;
}
    
template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: make_fract_from_whole ( num_fract & result , num_whole whole )
{
    result . _value = float ( whole . _value ) ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: sub_fracts ( num_fract & result , num_fract from , num_fract what )
{
    result . _value = from . _value - what . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: add_to_fract ( num_fract & a , num_fract b )
{
    a . _value += b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: inc_whole ( num_whole & a )
{
    ++ a . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: mul_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value * b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: div_fracts ( num_fract & result , num_fract a , num_fract b )
{
    result . _value = a . _value / b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: mod_whole_by ( num_whole & a , num_whole b )
{
    a . _value %= b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: div_whole_by ( num_whole & a , num_whole b )
{
    a . _value /= b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: add_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value + b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: sub_from_fract ( num_fract & from , num_fract what )
{
    from . _value -= what . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: xor_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value ^ b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: mul_whole_by ( num_whole & a , num_whole b )
{
    a . _value *= b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: div_wholes ( num_whole & result , num_whole a , num_whole b )
{
    result . _value = a . _value / b . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: dec_whole ( num_whole & a )
{
    -- a . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: neg_fract ( num_fract & a )
{
    a . _value = - a . _value ;
}

template < typename platform_insider >
inline void shy_platform_math_int_float < platform_insider > :: neg_whole ( num_whole & result , num_whole a )
{
    result . _value = - a . _value ;
}
