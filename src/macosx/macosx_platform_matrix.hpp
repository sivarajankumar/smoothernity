inline
void
shy_macosx_platform :: matrix_set_axis_x 
    ( shy_macosx_platform :: matrix_data & matrix 
    , shy_macosx_platform :: float_32 x 
    , shy_macosx_platform :: float_32 y 
    , shy_macosx_platform :: float_32 z 
    )
{
    matrix . _elements [ 0 ] = x ;
    matrix . _elements [ 1 ] = y ;
    matrix . _elements [ 2 ] = z ;
    matrix . _elements [ 3 ] = 0 ;
}

inline
void 
shy_macosx_platform :: matrix_set_axis_y 
    ( shy_macosx_platform :: matrix_data & matrix 
    , shy_macosx_platform :: float_32 x 
    , shy_macosx_platform :: float_32 y 
    , shy_macosx_platform :: float_32 z 
    )
{
    matrix . _elements [ 4 ] = x ;
    matrix . _elements [ 5 ] = y ;
    matrix . _elements [ 6 ] = z ;
    matrix . _elements [ 7 ] = 0 ;
}

inline
void 
shy_macosx_platform :: matrix_set_axis_z 
    ( shy_macosx_platform :: matrix_data & matrix 
    , shy_macosx_platform :: float_32 x 
    , shy_macosx_platform :: float_32 y 
    , shy_macosx_platform :: float_32 z 
    )
{
    matrix . _elements [  8 ] = x ;
    matrix . _elements [  9 ] = y ;
    matrix . _elements [ 10 ] = z ;
    matrix . _elements [ 11 ] = 0 ;
}

inline
void 
shy_macosx_platform :: matrix_set_origin 
    ( shy_macosx_platform :: matrix_data & matrix 
    , shy_macosx_platform :: float_32 x 
    , shy_macosx_platform :: float_32 y 
    , shy_macosx_platform :: float_32 z 
    )
{
    matrix . _elements [ 12 ] = x ;
    matrix . _elements [ 13 ] = y ;
    matrix . _elements [ 14 ] = z ;
    matrix . _elements [ 15 ] = 1 ;
}

inline
void 
shy_macosx_platform :: matrix_set_axis_x 
    ( shy_macosx_platform :: matrix_data & matrix 
    , shy_macosx_platform :: vector_data v 
    )
{
    matrix_set_axis_x ( matrix , v . _x , v . _y , v . _z ) ;
}

inline
void 
shy_macosx_platform :: matrix_set_axis_y 
    ( shy_macosx_platform :: matrix_data & matrix 
    , shy_macosx_platform :: vector_data v 
    )
{
    matrix_set_axis_y ( matrix , v . _x , v . _y , v . _z ) ;
}

inline
void 
shy_macosx_platform :: matrix_set_axis_z 
    ( shy_macosx_platform :: matrix_data & matrix 
    , shy_macosx_platform :: vector_data v 
    )
{
    matrix_set_axis_z ( matrix , v . _x , v . _y , v . _z ) ;
}

inline
void 
shy_macosx_platform :: matrix_set_origin 
    ( shy_macosx_platform :: matrix_data & matrix 
    , shy_macosx_platform :: vector_data v 
    )
{
    matrix_set_origin ( matrix , v . _x , v . _y , v . _z ) ;
}

inline 
shy_macosx_platform :: vector_data 
shy_macosx_platform :: matrix_get_axis_x 
    ( const shy_macosx_platform :: matrix_data & matrix 
    )
{
    return vector_xyz ( matrix . _elements [ 0 ] , matrix . _elements [ 1 ] , matrix . _elements [ 2 ] ) ;
}

inline
shy_macosx_platform :: vector_data 
shy_macosx_platform :: matrix_get_axis_y 
    ( const shy_macosx_platform :: matrix_data & matrix 
    )
{
    return vector_xyz ( matrix . _elements [ 4 ] , matrix . _elements [ 5 ] , matrix . _elements [ 6 ] ) ;
}

inline
shy_macosx_platform :: vector_data 
shy_macosx_platform :: matrix_get_axis_z 
    ( const shy_macosx_platform :: matrix_data & matrix 
    )
{
    return vector_xyz ( matrix . _elements [ 8 ] , matrix . _elements [ 9 ] , matrix . _elements [ 10 ] ) ;
}

inline
shy_macosx_platform :: vector_data 
shy_macosx_platform :: matrix_get_origin 
    ( const shy_macosx_platform :: matrix_data & matrix 
    )
{
    return vector_xyz ( matrix . _elements [ 12 ] , matrix . _elements [ 13 ] , matrix . _elements [ 14 ] ) ;
}

inline
void 
shy_macosx_platform :: matrix_identity 
    ( shy_macosx_platform :: matrix_data & matrix 
    )
{
    for ( int i = 0 ; i < 16 ; i ++ )
    {
        if ( i == 0 || i == 5 || i == 10 || i == 15 )
            matrix . _elements [ i ] = 1 ;
        else
            matrix . _elements [ i ] = 0 ;
    }
}

inline
void 
shy_macosx_platform :: matrix_inverse_rotation_translation 
    ( shy_macosx_platform :: matrix_data & matrix 
    )
{
    matrix_set_origin ( matrix , vector_xyz
        ( - vector_dot_product ( matrix_get_origin ( matrix ) , matrix_get_axis_x ( matrix ) )
        , - vector_dot_product ( matrix_get_origin ( matrix ) , matrix_get_axis_y ( matrix ) )
        , - vector_dot_product ( matrix_get_origin ( matrix ) , matrix_get_axis_z ( matrix ) )
        ) ) ;
    swap_values ( matrix . _elements [ 1 ] , matrix . _elements [ 4 ] ) ;
    swap_values ( matrix . _elements [ 2 ] , matrix . _elements [ 8 ] ) ;
    swap_values ( matrix . _elements [ 6 ] , matrix . _elements [ 9 ] ) ;
}
