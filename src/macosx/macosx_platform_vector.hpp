inline void shy_macosx_platform :: vector_xyz ( vector_data & result , num_fract x , num_fract y , num_fract z )
{
    result . _x = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    result . _y = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    result . _z = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
}

inline void shy_macosx_platform :: vector_dot_product ( num_fract & result , vector_data v1 , vector_data v2 )
{
    _platform_math_insider :: num_fract_unsafe_value_set 
        ( result
        , v1 . _x * v2 . _x
        + v1 . _y * v2 . _y
        + v1 . _z * v2 . _z
        ) ;
}

inline void shy_macosx_platform :: vector_cross_product ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _y * v2 . _z - v2 . _y * v1 . _z ;
    result . _y = v1 . _z * v2 . _x - v2 . _z * v1 . _x ;
    result . _z = v1 . _x * v2 . _y - v2 . _x * v1 . _y ;
}

inline void shy_macosx_platform :: vector_add ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _x + v2 . _x ;
    result . _y = v1 . _y + v2 . _y ;
    result . _z = v1 . _z + v2 . _z ;
}

inline void shy_macosx_platform :: vector_sub ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _x - v2 . _x ;
    result . _y = v1 . _y - v2 . _y ;
    result . _z = v1 . _z - v2 . _z ;
}

inline void shy_macosx_platform :: vector_mul ( vector_data & result , vector_data v , num_fract f )
{
    result . _x = _platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _x ;
    result . _y = _platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _y ;
    result . _z = _platform_math_insider :: num_fract_unsafe_value_get ( f ) * v . _z ;
}

inline void shy_macosx_platform :: vector_mul_by ( vector_data & v , num_fract f )
{
    v . _x *= _platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
    v . _y *= _platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
    v . _z *= _platform_math_insider :: num_fract_unsafe_value_get ( f ) ;
}

inline void shy_macosx_platform :: vector_length ( num_fract & result , vector_data v )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ) ;
}

inline void shy_macosx_platform :: vector_normalize ( vector_data & result , vector_data v )
{
    float inv_length = 1.0f / float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ;
    result . _x = inv_length * v . _x ;
    result . _y = inv_length * v . _y ;
    result . _z = inv_length * v . _z ;
}
