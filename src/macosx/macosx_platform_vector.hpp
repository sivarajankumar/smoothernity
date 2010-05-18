inline void shy_macosx_platform :: vector_xyz ( vector_data & result , float_32 x , float_32 y , float_32 z )
{
    result . _x = x ;
    result . _y = y ;
    result . _z = z ;
}

inline void shy_macosx_platform :: vector_dot_product ( float_32 & result , vector_data v1 , vector_data v2 )
{
    result = v1 . _x * v2 . _x
           + v1 . _y * v2 . _y
           + v1 . _z * v2 . _z ;
}

inline void shy_macosx_platform :: vector_cross_product ( vector_data & result , vector_data v1 , vector_data v2 )
{
    vector_xyz 
        ( result
        , v1 . _y * v2 . _z - v2 . _y * v1 . _z
        , v1 . _z * v2 . _x - v2 . _z * v1 . _x
        , v1 . _x * v2 . _y - v2 . _x * v1 . _y
        ) ;
}

inline void shy_macosx_platform :: vector_add ( vector_data & result , vector_data v1 , vector_data v2 )
{
    vector_xyz
        ( result
        , v1 . _x + v2 . _x
        , v1 . _y + v2 . _y
        , v1 . _z + v2 . _z
        ) ;
}

inline void shy_macosx_platform :: vector_sub ( vector_data & result , vector_data v1 , vector_data v2 )
{
    vector_xyz
        ( result
        , v1 . _x - v2 . _x
        , v1 . _y - v2 . _y
        , v1 . _z - v2 . _z
        ) ;
}

inline void shy_macosx_platform :: vector_mul ( vector_data & result , vector_data v , float_32 f )
{
    vector_xyz
        ( result
        , f * v . _x
        , f * v . _y
        , f * v . _z
        ) ;
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
