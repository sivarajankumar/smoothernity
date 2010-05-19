inline void shy_macosx_platform :: vector_xyz ( vector_data & result , num_fract x , num_fract y , num_fract z )
{
    result . _x = x . _value ;
    result . _y = y . _value ;
    result . _z = z . _value ;
}

inline void shy_macosx_platform :: vector_dot_product ( float_32 & result , vector_data v1 , vector_data v2 )
{
    result = v1 . _x * v2 . _x
           + v1 . _y * v2 . _y
           + v1 . _z * v2 . _z ;
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

inline void shy_macosx_platform :: vector_mul ( vector_data & result , vector_data v , float_32 f )
{
    result . _x = f * v . _x ;
    result . _y = f * v . _y ;
    result . _z = f * v . _z ;
}

inline void shy_macosx_platform :: vector_length ( float_32 & result , vector_data v )
{
    vector_dot_product ( result , v , v ) ;
    result = ( float_32 ) sqrt ( result ) ;
}

inline void shy_macosx_platform :: vector_normalize ( vector_data & result , vector_data v )
{
    float length ;
    vector_length ( length , v ) ;
    vector_mul ( result , v , 1.0f / length ) ;
}
