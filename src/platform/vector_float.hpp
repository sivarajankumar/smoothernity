template < typename platform_insider >
class shy_platform_vector_float_insider ;

template < typename platform_insider >
class shy_platform_vector_float
{
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
    class vector_data
    {
        friend class shy_platform_vector_float ;
        friend class shy_platform_vector_float_insider < platform_insider > ;
    public :
        vector_data ( ) ;
    private :
        float _x ;
        float _y ;
        float _z ;
    } ;
public :
    static void xyz ( vector_data & result , num_fract x , num_fract y , num_fract z ) ;
    static void dot_product ( num_fract & result , vector_data v1 , vector_data v2 ) ;
    static void cross_product ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void add ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void sub ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void mul ( vector_data & result , vector_data v , num_fract f ) ;
    static void mul_by ( vector_data & v , num_fract f ) ;
    static void length ( num_fract & result , vector_data v ) ;
    static void normalize ( vector_data & result , vector_data v ) ;
} ;

template < typename platform_insider >
shy_platform_vector_float < platform_insider > :: vector_data :: vector_data ( )
: _x ( platform_insider :: uninitialized_value )
, _y ( platform_insider :: uninitialized_value )
, _z ( platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: xyz ( vector_data & result , num_fract x , num_fract y , num_fract z )
{
    result . _x = platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    result . _y = platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    result . _z = platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: dot_product ( num_fract & result , vector_data v1 , vector_data v2 )
{
    platform_math_insider :: num_fract_unsafe_value_set 
        ( result
        , v1 . _x * v2 . _x
        + v1 . _y * v2 . _y
        + v1 . _z * v2 . _z
        ) ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: cross_product ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _y * v2 . _z - v2 . _y * v1 . _z ;
    result . _y = v1 . _z * v2 . _x - v2 . _z * v1 . _x ;
    result . _z = v1 . _x * v2 . _y - v2 . _x * v1 . _y ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: add ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _x + v2 . _x ;
    result . _y = v1 . _y + v2 . _y ;
    result . _z = v1 . _z + v2 . _z ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: sub ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _x - v2 . _x ;
    result . _y = v1 . _y - v2 . _y ;
    result . _z = v1 . _z - v2 . _z ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: mul ( vector_data & result , vector_data v , num_fract f )
{
    result . _x = platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _x ;
    result . _y = platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _y ;
    result . _z = platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _z ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: mul_by ( vector_data & v , num_fract f )
{
    v . _x *= platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
    v . _y *= platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
    v . _z *= platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: length ( num_fract & result , vector_data v )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ) ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: normalize ( vector_data & result , vector_data v )
{
    float inv_length = 1.0f / float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ;
    result . _x = inv_length * v . _x ;
    result . _y = inv_length * v . _y ;
    result . _z = inv_length * v . _z ;
}
