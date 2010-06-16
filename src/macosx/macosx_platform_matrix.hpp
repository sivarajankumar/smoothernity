inline void shy_macosx_platform :: matrix_set_axis_x ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 0 ] = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 1 ] = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 2 ] = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 3 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_axis_y ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 4 ] = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 5 ] = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 6 ] = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 7 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_axis_z ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [  8 ] = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [  9 ] = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 10 ] = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 11 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_origin ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 12 ] = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 13 ] = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 14 ] = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 15 ] = 1 ;
}

inline void shy_macosx_platform :: matrix_set_axis_x ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 0 ] = v . _x ;
    matrix . _elements [ 1 ] = v . _y ;
    matrix . _elements [ 2 ] = v . _z ;
    matrix . _elements [ 3 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_axis_y ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 4 ] = v . _x ;
    matrix . _elements [ 5 ] = v . _y ;
    matrix . _elements [ 6 ] = v . _z ;
    matrix . _elements [ 7 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_axis_z ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [  8 ] = v . _x ;
    matrix . _elements [  9 ] = v . _y ;
    matrix . _elements [ 10 ] = v . _z ;
    matrix . _elements [ 11 ] = 0 ;
}

inline void shy_macosx_platform :: matrix_set_origin ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 12 ] = v . _x ;
    matrix . _elements [ 13 ] = v . _y ;
    matrix . _elements [ 14 ] = v . _z ;
    matrix . _elements [ 15 ] = 1 ;
}

inline void shy_macosx_platform :: matrix_get_axis_x ( vector_data & result , const matrix_data & matrix )
{
    result . _x = matrix . _elements [ 0 ] ;
    result . _y = matrix . _elements [ 1 ] ;
    result . _z = matrix . _elements [ 2 ] ;
}

inline void shy_macosx_platform :: matrix_get_axis_y ( vector_data & result , const matrix_data & matrix )
{
    result . _x = matrix . _elements [ 4 ] ;
    result . _y = matrix . _elements [ 5 ] ;
    result . _z = matrix . _elements [ 6 ] ;
}

inline void shy_macosx_platform :: matrix_get_axis_z ( vector_data & result , const matrix_data & matrix )
{
    result . _x = matrix . _elements [ 8 ] ;
    result . _y = matrix . _elements [ 9 ] ;
    result . _z = matrix . _elements [ 10 ] ;
}

inline void shy_macosx_platform :: matrix_get_origin ( vector_data & result , const matrix_data & matrix )
{
    result . _x = matrix . _elements [ 12 ] ;
    result . _y = matrix . _elements [ 13 ] ;
    result . _z = matrix . _elements [ 14 ] ;
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
    
    num_fract dot_x ;
    num_fract dot_y ;
    num_fract dot_z ;
    vector_dot_product ( dot_x , origin , axis_x ) ;
    vector_dot_product ( dot_y , origin , axis_y ) ;
    vector_dot_product ( dot_z , origin , axis_z ) ;
    
    vector_data new_origin ;
    new_origin . _x = - _platform_math_insider :: num_fract_unsafe_value_get ( dot_x ) ;
    new_origin . _y = - _platform_math_insider :: num_fract_unsafe_value_get ( dot_y ) ;
    new_origin . _z = - _platform_math_insider :: num_fract_unsafe_value_get ( dot_z ) ;
    
    matrix_set_origin ( matrix , new_origin ) ;
    swap_values ( matrix . _elements [ 1 ] , matrix . _elements [ 4 ] ) ;
    swap_values ( matrix . _elements [ 2 ] , matrix . _elements [ 8 ] ) ;
    swap_values ( matrix . _elements [ 6 ] , matrix . _elements [ 9 ] ) ;
}
