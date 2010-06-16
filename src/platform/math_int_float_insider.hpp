template < typename platform >
class shy_platform_math_int_float_insider
{
    typedef typename platform :: platform_math :: num_fract num_fract ;
    typedef typename platform :: platform_math :: num_whole num_whole ;
public :
    static int & num_whole_unsafe_value ( num_whole num ) ;
    static float & num_fract_unsafe_value ( num_fract num ) ;
} ;

template < typename platform >
inline int & shy_platform_math_int_float_insider < platform > :: num_whole_unsafe_value ( num_whole num )
{
    return num . _value ;
}

template < typename platform >
inline float & shy_platform_math_int_float_insider < platform > :: num_fract_unsafe_value ( num_fract num )
{
    return num . _value ;
}
