template < typename platform_insider >
class shy_platform_conditions
{
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
    
public :
    static int fract_less_than_fract ( num_fract , num_fract ) ;
    static int whole_greater_or_equal_to_whole ( num_whole , num_whole ) ;
    static int fract_greater_than_fract ( num_fract , num_fract ) ;
    static int whole_greater_than_whole ( num_whole , num_whole ) ;
    static int whole_greater_than_zero ( num_whole ) ;
    static int whole_is_even ( num_whole ) ;
    static int whole_is_false ( num_whole ) ;
    static int whole_is_true ( num_whole ) ;
    static int whole_is_zero ( num_whole ) ;
    static int whole_less_or_equal_to_whole ( num_whole , num_whole ) ;
    static int whole_less_or_equal_to_zero ( num_whole ) ;
    static int whole_less_than_whole ( num_whole , num_whole ) ;
    static int whole_less_than_zero ( num_whole ) ;
    static int wholes_are_equal ( num_whole , num_whole ) ;
} ;

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: wholes_are_equal ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int == b_int ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_is_true ( num_whole num )
{
    int num_int = 0 ;
    platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == int ( true ) ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_is_false ( num_whole num )
{
    int num_int = 0 ;
    platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == false ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_greater_than_zero ( num_whole num )
{
    int num_int = 0 ;
    platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int > 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_less_than_whole ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int < b_int ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_less_or_equal_to_whole ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int <= b_int ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_is_zero ( num_whole num )
{
    int num_int = 0 ;
    platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_is_even ( num_whole num )
{
    int num_int = 0 ;
    platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int % 2 == 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_less_or_equal_to_zero ( num_whole num )
{
    int num_int = 0 ;
    platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int <= 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_greater_or_equal_to_whole ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int >= b_int ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_less_than_zero ( num_whole num )
{
    int num_int = 0 ;
    platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int < 0 ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: whole_greater_than_whole ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int > b_int ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: fract_less_than_fract ( num_fract a , num_fract b )
{
    float a_float = 0 ;
    float b_float = 0 ;
    platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    return a_float < b_float ;
}

template < typename platform_insider >
inline int shy_platform_conditions < platform_insider > :: fract_greater_than_fract ( num_fract a , num_fract b )
{
    float a_float = 0 ;
    float b_float = 0 ;
    platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    return a_float > b_float ;
}
