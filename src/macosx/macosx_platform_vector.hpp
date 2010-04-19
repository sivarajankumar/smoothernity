inline
shy_macosx_platform :: vector_data
shy_macosx_platform :: vector_xyz 
    ( shy_macosx_platform :: float_32 x 
    , shy_macosx_platform :: float_32 y 
    , shy_macosx_platform :: float_32 z
    )
{
    shy_macosx_platform :: vector_data vector ;
    vector . _x = x ;
    vector . _y = y ;
    vector . _z = z ;
    return vector ;
}

inline
shy_macosx_platform :: float_32
shy_macosx_platform :: vector_dot_product 
    ( shy_macosx_platform :: vector_data v1 
    , shy_macosx_platform :: vector_data v2
    )
{
    return v1 . _x * v2 . _x
         + v1 . _y * v2 . _y
         + v1 . _z * v2 . _z ;
}

inline
shy_macosx_platform :: vector_data 
shy_macosx_platform :: vector_cross_product 
    ( shy_macosx_platform :: vector_data v1 
    , shy_macosx_platform :: vector_data v2 
    )
{
    shy_macosx_platform :: vector_data result ;
    result . _x = v1 . _y * v2 . _z - v2 . _y * v1 . _z ;
    result . _y = v1 . _z * v2 . _x - v2 . _z * v1 . _x ;
    result . _z = v1 . _x * v2 . _y - v2 . _x * v1 . _y ;
    return result ;
}

inline
shy_macosx_platform :: vector_data 
shy_macosx_platform :: vector_add 
    ( shy_macosx_platform :: vector_data v1 
    , shy_macosx_platform :: vector_data v2 
    )
{
    shy_macosx_platform :: vector_data result ;
    result . _x = v1 . _x + v2 . _x ;
    result . _y = v1 . _y + v2 . _y ;
    result . _z = v1 . _z + v2 . _z ;
    return result ;
}

inline
shy_macosx_platform :: vector_data 
shy_macosx_platform :: vector_sub 
    ( shy_macosx_platform :: vector_data v1 
    , shy_macosx_platform :: vector_data v2 
    )
{
    vector_data result ;
    result . _x = v1 . _x - v2 . _x ;
    result . _y = v1 . _y - v2 . _y ;
    result . _z = v1 . _z - v2 . _z ;
    return result ;
}

inline
shy_macosx_platform :: vector_data 
shy_macosx_platform :: vector_mul 
    ( shy_macosx_platform :: vector_data v 
    , shy_macosx_platform :: float_32 f 
    )
{
    vector_data result ;
    result . _x = f * v . _x ;
    result . _y = f * v . _y ;
    result . _z = f * v . _z ;
    return result ;
}

inline
shy_macosx_platform :: float_32 
shy_macosx_platform :: vector_length 
    ( shy_macosx_platform :: vector_data v 
    )
{
    return ( float_32 ) sqrt ( vector_dot_product ( v , v ) ) ;
}

inline
shy_macosx_platform :: vector_data 
shy_macosx_platform :: vector_normalize 
    ( shy_macosx_platform :: vector_data v 
    )
{
    return vector_mul ( v , 1.0f / vector_length ( v ) ) ;
}
