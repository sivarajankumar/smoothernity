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
    static void xyz ( vector_data & , num_fract , num_fract , num_fract ) ;
    static void dot_product ( num_fract & , vector_data , vector_data ) ;
    static void cross_product ( vector_data & , vector_data , vector_data ) ;
    static void add ( vector_data & , vector_data , vector_data ) ;
    static void add_to ( vector_data & , vector_data ) ;
    static void sub ( vector_data & , vector_data , vector_data ) ;
    static void mul ( vector_data & , vector_data , num_fract ) ;
    static void mul_by ( vector_data & , num_fract ) ;
    static void length ( num_fract & , vector_data ) ;
    static void normalize ( vector_data & , vector_data ) ;
} ;

template < typename platform_insider >
shy_platform_vector_float < platform_insider > :: vector_data :: vector_data ( )
: _x ( ( float ) platform_insider :: uninitialized_value )
, _y ( ( float ) platform_insider :: uninitialized_value )
, _z ( ( float ) platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: xyz ( vector_data & result , num_fract x , num_fract y , num_fract z )
{
    platform_math_insider :: num_fract_value_get ( result . _x , x ) ;
    platform_math_insider :: num_fract_value_get ( result . _y , y ) ;
    platform_math_insider :: num_fract_value_get ( result . _z , z ) ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: dot_product ( num_fract & result , vector_data v1 , vector_data v2 )
{
    platform_math_insider :: num_fract_value_set 
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
inline void shy_platform_vector_float < platform_insider > :: add_to ( vector_data & result , vector_data v )
{
    result . _x += v . _x ;
    result . _y += v . _y ;
    result . _z += v . _z ;
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
    float f_float = 0 ;
    platform_math_insider :: num_fract_value_get ( f_float , f ) ;
    result . _x = f_float * v . _x ;
    result . _y = f_float * v . _y ;
    result . _z = f_float * v . _z ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: mul_by ( vector_data & v , num_fract f )
{
    float f_float = 0 ;
    platform_math_insider :: num_fract_value_get ( f_float , f ) ;
    v . _x *= f_float ;
    v . _y *= f_float ;
    v . _z *= f_float ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: length ( num_fract & result , vector_data v )
{
    platform_math_insider :: num_fract_value_set ( result , float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ) ;
}

template < typename platform_insider >
inline void shy_platform_vector_float < platform_insider > :: normalize ( vector_data & result , vector_data v )
{
    float inv_length = 1.0f / float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ;
    result . _x = inv_length * v . _x ;
    result . _y = inv_length * v . _y ;
    result . _z = inv_length * v . _z ;
}
