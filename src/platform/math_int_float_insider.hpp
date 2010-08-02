template < typename platform >
class shy_platform_math_int_float_insider
{
    typedef typename platform :: platform_math :: num_fract num_fract ;
    typedef typename platform :: platform_math :: num_whole num_whole ;
public :
    static void num_whole_value_get ( int & , num_whole ) ;
    static void num_whole_value_set ( num_whole & , int ) ;
    static void num_fract_value_get ( float & , num_fract ) ;
    static void num_fract_value_set ( num_fract & , float ) ;
} ;

template < typename platform >
inline void shy_platform_math_int_float_insider < platform > :: num_whole_value_get ( int & value , num_whole num )
{
    value = num . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float_insider < platform > :: num_whole_value_set ( num_whole & num , int value )
{
    num . _value = value ;
}

template < typename platform >
inline void shy_platform_math_int_float_insider < platform > :: num_fract_value_get ( float & value , num_fract num )
{
    value = num . _value ;
}

template < typename platform >
inline void shy_platform_math_int_float_insider < platform > :: num_fract_value_set ( num_fract & num , float value )
{
    num . _value = value ;
}
