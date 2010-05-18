inline void shy_macosx_platform :: matrix_set_axis_x ( matrix_data & matrix , float_32 x , float_32 y , float_32 z )
{
    matrix . _elements [ 0 ] = x ;
    matrix . _elements [ 1 ] = y ;
    matrix . _elements [ 2 ] = z ;
    matrix . _elements [ 3 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_axis_y ( matrix_data & matrix , float_32 x , float_32 y , float_32 z )
{
    matrix . _elements [ 4 ] = x ;
    matrix . _elements [ 5 ] = y ;
    matrix . _elements [ 6 ] = z ;
    matrix . _elements [ 7 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_axis_z ( matrix_data & matrix , float_32 x , float_32 y , float_32 z )
{
    matrix . _elements [  8 ] = x ;
    matrix . _elements [  9 ] = y ;
    matrix . _elements [ 10 ] = z ;
    matrix . _elements [ 11 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_origin ( matrix_data & matrix , float_32 x , float_32 y , float_32 z )
{
    matrix . _elements [ 12 ] = x ;
    matrix . _elements [ 13 ] = y ;
    matrix . _elements [ 14 ] = z ;
    matrix . _elements [ 15 ] = 1 ;
}

inline void shy_macosx_platform :: matrix_set_axis_x ( matrix_data & matrix , vector_data v )
{
    matrix_set_axis_x ( matrix , v . _x , v . _y , v . _z ) ;
}

inline void shy_macosx_platform :: matrix_set_axis_y ( matrix_data & matrix , vector_data v )
{
    matrix_set_axis_y ( matrix , v . _x , v . _y , v . _z ) ;
}

inline void shy_macosx_platform :: matrix_set_axis_z ( matrix_data & matrix , vector_data v )
{
    matrix_set_axis_z ( matrix , v . _x , v . _y , v . _z ) ;
}

inline void shy_macosx_platform :: matrix_set_origin ( matrix_data & matrix , vector_data v )
{
    matrix_set_origin ( matrix , v . _x , v . _y , v . _z ) ;
}

inline void shy_macosx_platform :: matrix_get_axis_x ( vector_data & result , const matrix_data & matrix )
{
    vector_xyz ( result , matrix . _elements [ 0 ] , matrix . _elements [ 1 ] , matrix . _elements [ 2 ] ) ;
}

inline void shy_macosx_platform :: matrix_get_axis_y ( vector_data & result , const matrix_data & matrix )
{
    vector_xyz ( result , matrix . _elements [ 4 ] , matrix . _elements [ 5 ] , matrix . _elements [ 6 ] ) ;
}

inline void shy_macosx_platform :: matrix_get_axis_z ( vector_data & result , const matrix_data & matrix )
{
    vector_xyz ( result , matrix . _elements [ 8 ] , matrix . _elements [ 9 ] , matrix . _elements [ 10 ] ) ;
}

inline void shy_macosx_platform :: matrix_get_origin ( vector_data & result , const matrix_data & matrix )
{
    vector_xyz ( result , matrix . _elements [ 12 ] , matrix . _elements [ 13 ] , matrix . _elements [ 14 ] ) ;
}

inline void shy_macosx_platform :: matrix_identity ( matrix_data & matrix )
{
    for ( int i = 0 ; i < 16 ; i ++ )
    {
        if ( i == 0 || i == 5 || i == 10 || i == 15 )
            matrix . _elements [ i ] = 1 ;
        else
            matrix . _elements [ i ] = 0 ;
    }
}

inline void shy_macosx_platform :: matrix_inverse_rotation_translation ( matrix_data & matrix )
{
    vector_data axis_x ;
    vector_data axis_y ;
    vector_data axis_z ;
    vector_data origin ;
    matrix_get_axis_x ( axis_x , matrix ) ;
    matrix_get_axis_y ( axis_y , matrix ) ;
    matrix_get_axis_z ( axis_z , matrix ) ;
    matrix_get_origin ( origin , matrix ) ;
    
    float_32 dot_x ;
    float_32 dot_y ;
    float_32 dot_z ;
    vector_dot_product ( dot_x , origin , axis_x ) ;
    vector_dot_product ( dot_y , origin , axis_y ) ;
    vector_dot_product ( dot_z , origin , axis_z ) ;
    
    vector_data new_origin ;
    vector_xyz ( new_origin , - dot_x , - dot_y , - dot_z ) ;
    
    matrix_set_origin ( matrix , new_origin ) ;
    swap_values ( matrix . _elements [ 1 ] , matrix . _elements [ 4 ] ) ;
    swap_values ( matrix . _elements [ 2 ] , matrix . _elements [ 8 ] ) ;
    swap_values ( matrix . _elements [ 6 ] , matrix . _elements [ 9 ] ) ;
}
