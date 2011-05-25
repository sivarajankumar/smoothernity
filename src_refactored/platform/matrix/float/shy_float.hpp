class shy_platform_matrix_float_guts
{
public :
    static void swap_values ( so_called_lib_std_float & , so_called_lib_std_float & ) ;
} ;

void shy_platform_matrix_float_guts :: swap_values ( so_called_lib_std_float & a , so_called_lib_std_float & b )
{
    so_called_lib_std_float c = b ;
    b = a ;
    a = c ;
}

void shy_platform_matrix_float :: set_axis_x 
    ( so_called_type_platform_matrix_data & matrix 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 0 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 1 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 2 ] , z ) ;
    matrix . _elements [ 3 ] = 0 ;
}

void shy_platform_matrix_float :: set_axis_y 
    ( so_called_type_platform_matrix_data & matrix 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 4 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 5 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 6 ] , z ) ;
    matrix . _elements [ 7 ] = 0 ;
}

void shy_platform_matrix_float :: set_axis_z 
    ( so_called_type_platform_matrix_data & matrix 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 8 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 9 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 10 ] , z ) ;
    matrix . _elements [ 11 ] = 0 ;
}

void shy_platform_matrix_float :: set_origin 
    ( so_called_type_platform_matrix_data & matrix 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 12 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 13 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 14 ] , z ) ;
    matrix . _elements [ 15 ] = 1 ;
}

void shy_platform_matrix_float :: set_axis_x ( so_called_type_platform_matrix_data & matrix , so_called_type_platform_vector_data v )
{
    so_called_platform_vector_insider :: x_get ( matrix . _elements [ 0 ] , v ) ;
    so_called_platform_vector_insider :: y_get ( matrix . _elements [ 1 ] , v ) ;
    so_called_platform_vector_insider :: z_get ( matrix . _elements [ 2 ] , v ) ;
    matrix . _elements [ 3 ] = 0 ;
}

void shy_platform_matrix_float :: set_axis_y ( so_called_type_platform_matrix_data & matrix , so_called_type_platform_vector_data v )
{
    so_called_platform_vector_insider :: x_get ( matrix . _elements [ 4 ] , v ) ;
    so_called_platform_vector_insider :: y_get ( matrix . _elements [ 5 ] , v ) ;
    so_called_platform_vector_insider :: z_get ( matrix . _elements [ 6 ] , v ) ;
    matrix . _elements [ 7 ] = 0 ;
}

void shy_platform_matrix_float :: set_axis_z ( so_called_type_platform_matrix_data & matrix , so_called_type_platform_vector_data v )
{
    so_called_platform_vector_insider :: x_get ( matrix . _elements [  8 ] , v ) ;
    so_called_platform_vector_insider :: y_get ( matrix . _elements [  9 ] , v ) ;
    so_called_platform_vector_insider :: z_get ( matrix . _elements [ 10 ] , v ) ;
    matrix . _elements [ 11 ] = 0 ;
}

void shy_platform_matrix_float :: set_origin ( so_called_type_platform_matrix_data & matrix , so_called_type_platform_vector_data v )
{
    so_called_platform_vector_insider :: x_get ( matrix . _elements [ 12 ] , v ) ;
    so_called_platform_vector_insider :: y_get ( matrix . _elements [ 13 ] , v ) ;
    so_called_platform_vector_insider :: z_get ( matrix . _elements [ 14 ] , v ) ;
    matrix . _elements [ 15 ] = 1 ;
}

void shy_platform_matrix_float :: get_axis_x ( so_called_type_platform_vector_data & result , const so_called_type_platform_matrix_data & matrix )
{
    so_called_platform_vector_insider :: x_set ( result , matrix . _elements [ 0 ] ) ;
    so_called_platform_vector_insider :: y_set ( result , matrix . _elements [ 1 ] ) ;
    so_called_platform_vector_insider :: z_set ( result , matrix . _elements [ 2 ] ) ;
}

void shy_platform_matrix_float :: get_axis_y ( so_called_type_platform_vector_data & result , const so_called_type_platform_matrix_data & matrix )
{
    so_called_platform_vector_insider :: x_set ( result , matrix . _elements [ 4 ] ) ;
    so_called_platform_vector_insider :: y_set ( result , matrix . _elements [ 5 ] ) ;
    so_called_platform_vector_insider :: z_set ( result , matrix . _elements [ 6 ] ) ;
}

void shy_platform_matrix_float :: get_axis_z ( so_called_type_platform_vector_data & result , const so_called_type_platform_matrix_data & matrix )
{
    so_called_platform_vector_insider :: x_set ( result , matrix . _elements [ 8 ] ) ;
    so_called_platform_vector_insider :: y_set ( result , matrix . _elements [ 9 ] ) ;
    so_called_platform_vector_insider :: z_set ( result , matrix . _elements [ 10 ] ) ;
}

void shy_platform_matrix_float :: get_origin ( so_called_type_platform_vector_data & result , const so_called_type_platform_matrix_data & matrix )
{
    so_called_platform_vector_insider :: x_set ( result , matrix . _elements [ 12 ] ) ;
    so_called_platform_vector_insider :: y_set ( result , matrix . _elements [ 13 ] ) ;
    so_called_platform_vector_insider :: z_set ( result , matrix . _elements [ 14 ] ) ;
}

void shy_platform_matrix_float :: identity ( so_called_type_platform_matrix_data & matrix )
{
    for ( so_called_lib_std_int32_t i = 0 ; i < 16 ; i ++ )
    {
        if ( i == 0 || i == 5 || i == 10 || i == 15 )
            matrix . _elements [ i ] = 1 ;
        else
            matrix . _elements [ i ] = 0 ;
    }
}

void shy_platform_matrix_float :: inverse_rotation_translation ( so_called_type_platform_matrix_data & matrix )
{
    so_called_type_platform_vector_data axis_x ;
    so_called_type_platform_vector_data axis_y ;
    so_called_type_platform_vector_data axis_z ;
    so_called_type_platform_vector_data origin ;
    get_axis_x ( axis_x , matrix ) ;
    get_axis_y ( axis_y , matrix ) ;
    get_axis_z ( axis_z , matrix ) ;
    get_origin ( origin , matrix ) ;
    
    so_called_type_platform_math_num_fract dot_x ;
    so_called_type_platform_math_num_fract dot_y ;
    so_called_type_platform_math_num_fract dot_z ;
    so_called_platform_vector :: dot_product ( dot_x , origin , axis_x ) ;
    so_called_platform_vector :: dot_product ( dot_y , origin , axis_y ) ;
    so_called_platform_vector :: dot_product ( dot_z , origin , axis_z ) ;
    
    so_called_lib_std_float dot_x_float = 0 ;
    so_called_lib_std_float dot_y_float = 0 ;
    so_called_lib_std_float dot_z_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( dot_x_float , dot_x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( dot_y_float , dot_y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( dot_z_float , dot_z ) ;
    
    so_called_type_platform_vector_data new_origin ;
    so_called_platform_vector_insider :: x_set ( new_origin , - dot_x_float ) ;
    so_called_platform_vector_insider :: y_set ( new_origin , - dot_y_float ) ;
    so_called_platform_vector_insider :: z_set ( new_origin , - dot_z_float ) ;
    
    set_origin ( matrix , new_origin ) ;
    shy_platform_matrix_float_guts :: swap_values ( matrix . _elements [ 1 ] , matrix . _elements [ 4 ] ) ;
    shy_platform_matrix_float_guts :: swap_values ( matrix . _elements [ 2 ] , matrix . _elements [ 8 ] ) ;
    shy_platform_matrix_float_guts :: swap_values ( matrix . _elements [ 6 ] , matrix . _elements [ 9 ] ) ;
}
