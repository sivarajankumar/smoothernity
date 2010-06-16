template < typename platform >
class shy_platform_vector_float_insider ;

template < typename platform >
class shy_platform_vector_float
{
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: num_fract num_fract ;
public :
    class vector_data
    {
        friend class shy_platform_vector_float ;
        friend class shy_platform_vector_float_insider < platform > ;
    public :
        vector_data ( ) ;
    private :
        float _x ;
        float _y ;
        float _z ;
    } ;
public :
    static void vector_xyz ( vector_data & result , num_fract x , num_fract y , num_fract z ) ;
    static void vector_dot_product ( num_fract & result , vector_data v1 , vector_data v2 ) ;
    static void vector_cross_product ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_add ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_sub ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_mul ( vector_data & result , vector_data v , num_fract f ) ;
    static void vector_mul_by ( vector_data & v , num_fract f ) ;
    static void vector_length ( num_fract & result , vector_data v ) ;
    static void vector_normalize ( vector_data & result , vector_data v ) ;
private :
    static int _uninitialized_value ( ) ;
} ;

template < typename platform >
int shy_platform_vector_float < platform > :: _uninitialized_value ( )
{
    return platform :: _uninitialized_value ;
}

template < typename platform >
shy_platform_vector_float < platform > :: vector_data :: vector_data ( )
: _x ( shy_platform_vector_float < platform > :: _uninitialized_value ( ) )
, _y ( shy_platform_vector_float < platform > :: _uninitialized_value ( ) )
, _z ( shy_platform_vector_float < platform > :: _uninitialized_value ( ) )
{
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_xyz ( vector_data & result , num_fract x , num_fract y , num_fract z )
{
    result . _x = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    result . _y = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    result . _z = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_dot_product ( num_fract & result , vector_data v1 , vector_data v2 )
{
    _platform_math_insider :: num_fract_unsafe_value_set 
        ( result
        , v1 . _x * v2 . _x
        + v1 . _y * v2 . _y
        + v1 . _z * v2 . _z
        ) ;
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_cross_product ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _y * v2 . _z - v2 . _y * v1 . _z ;
    result . _y = v1 . _z * v2 . _x - v2 . _z * v1 . _x ;
    result . _z = v1 . _x * v2 . _y - v2 . _x * v1 . _y ;
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_add ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _x + v2 . _x ;
    result . _y = v1 . _y + v2 . _y ;
    result . _z = v1 . _z + v2 . _z ;
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_sub ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _x - v2 . _x ;
    result . _y = v1 . _y - v2 . _y ;
    result . _z = v1 . _z - v2 . _z ;
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_mul ( vector_data & result , vector_data v , num_fract f )
{
    result . _x = _platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _x ;
    result . _y = _platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _y ;
    result . _z = _platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _z ;
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_mul_by ( vector_data & v , num_fract f )
{
    v . _x *= _platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
    v . _y *= _platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
    v . _z *= _platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_length ( num_fract & result , vector_data v )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ) ;
}

template < typename platform >
inline void shy_platform_vector_float < platform > :: vector_normalize ( vector_data & result , vector_data v )
{
    float inv_length = 1.0f / float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ;
    result . _x = inv_length * v . _x ;
    result . _y = inv_length * v . _y ;
    result . _z = inv_length * v . _z ;
}
