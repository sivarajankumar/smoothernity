template < typename platform >
class shy_platform_math_int_float_insider
{
    typedef typename platform :: platform_math :: num_fract num_fract ;
    typedef typename platform :: platform_math :: num_whole num_whole ;
public :
    static void num_whole_value_ptr ( int * & value , num_whole & num ) ;
    static void num_fract_value_ptr ( float * & value , num_fract & num ) ;
    static void num_whole_value_set ( num_whole & num , int value ) ;
    static float num_fract_value_get ( num_fract num ) ;
    static void num_fract_value_set ( num_fract & num , float value ) ;
} ;

template < typename platform >
inline void shy_platform_math_int_float_insider < platform > :: num_whole_value_ptr ( int * & value , num_whole & num )
{
    value = & num . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float_insider < platform > :: num_fract_value_ptr ( float * & value , num_fract & num )
{
    value = & num . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float_insider < platform > :: num_whole_value_set ( num_whole & num , int value )
{
    num . _value = value ;
}

template < typename platform >
inline float shy_platform_math_int_float_insider < platform > :: num_fract_value_get ( num_fract num )
{
    return num . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float_insider < platform > :: num_fract_value_set ( num_fract & num , float value )
{
    num . _value = value ;
}
