template < typename platform_insider >
class shy_platform_conditions
{
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
    
public :
    static int fract_less_than_fract ( num_fract a , num_fract b ) ;
    static int whole_greater_or_equal_to_whole ( num_whole a , num_whole b ) ;
    static int fract_greater_than_fract ( num_fract a , num_fract b ) ;
    static int whole_greater_than_whole ( num_whole a , num_whole b ) ;
    static int whole_greater_than_zero ( num_whole num ) ;
    static int whole_is_even ( num_whole num ) ;
    static int whole_is_false ( num_whole num ) ;
    static int whole_is_true ( num_whole num ) ;
    static int whole_is_zero ( num_whole num ) ;
    static int whole_less_or_equal_to_whole ( num_whole a , num_whole b ) ;
    static int whole_less_or_equal_to_zero ( num_whole a ) ;
    static int whole_less_than_whole ( num_whole a , num_whole b ) ;
    static int whole_less_than_zero ( num_whole a ) ;
    static int wholes_are_equal ( num_whole a , num_whole b ) ;
} ;

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: wholes_are_equal ( num_whole a , num_whole b )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( a ) 
        == platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_is_true ( num_whole num )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( num ) == true ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_is_false ( num_whole num )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( num ) == false ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_greater_than_zero ( num_whole num )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( num ) > 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_less_than_whole ( num_whole a , num_whole b )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( a )
         < platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_less_or_equal_to_whole ( num_whole a , num_whole b )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( a ) 
        <= platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_is_zero ( num_whole num )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( num ) == 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_is_even ( num_whole num )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( num ) % 2 == 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_less_or_equal_to_zero ( num_whole a )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( a ) <= 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_greater_or_equal_to_whole ( num_whole a , num_whole b )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( a )
        >= platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_less_than_zero ( num_whole a )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( a ) < 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_greater_than_whole ( num_whole a , num_whole b )
{
    return platform_math_insider :: num_whole_unsafe_value_get ( a ) 
         > platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: fract_less_than_fract ( num_fract a , num_fract b )
{
    return platform_math_insider :: num_fract_unsafe_value_get ( a )
         < platform_math_insider :: num_fract_unsafe_value_get ( b ) ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: fract_greater_than_fract ( num_fract a , num_fract b )
{
    return platform_math_insider :: num_fract_unsafe_value_get ( a ) 
         > platform_math_insider :: num_fract_unsafe_value_get ( b ) ;
}
