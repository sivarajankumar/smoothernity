namespace shy_guts
{
    static void swap_values ( so_called_lib_std_float & , so_called_lib_std_float & ) ;
}

void shy_guts :: swap_values ( so_called_lib_std_float & a , so_called_lib_std_float & b )
{
    so_called_lib_std_float c = b ;
    b = a ;
    a = c ;
}

void shy_platform_matrix_float :: set_axis_x 
    ( so_called_platform_matrix_float_data_type & matrix 
    , so_called_platform_math_num_fract_type x 
    , so_called_platform_math_num_fract_type y 
    , so_called_platform_math_num_fract_type z 
    )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_set ( ) ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 0 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 1 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 2 ] , z ) ;
    matrix . _elements [ 3 ] = 0 ;
}

void shy_platform_matrix_float :: set_axis_y 
    ( so_called_platform_matrix_float_data_type & matrix 
    , so_called_platform_math_num_fract_type x 
    , so_called_platform_math_num_fract_type y 
    , so_called_platform_math_num_fract_type z 
    )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_set ( ) ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 4 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 5 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 6 ] , z ) ;
    matrix . _elements [ 7 ] = 0 ;
}

void shy_platform_matrix_float :: set_axis_z 
    ( so_called_platform_matrix_float_data_type & matrix 
    , so_called_platform_math_num_fract_type x 
    , so_called_platform_math_num_fract_type y 
    , so_called_platform_math_num_fract_type z 
    )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_set ( ) ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 8 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 9 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 10 ] , z ) ;
    matrix . _elements [ 11 ] = 0 ;
}

void shy_platform_matrix_float :: set_origin 
    ( so_called_platform_matrix_float_data_type & matrix 
    , so_called_platform_math_num_fract_type x 
    , so_called_platform_math_num_fract_type y 
    , so_called_platform_math_num_fract_type z 
    )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_set ( ) ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 12 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 13 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( matrix . _elements [ 14 ] , z ) ;
    matrix . _elements [ 15 ] = 1 ;
}

void shy_platform_matrix_float :: set_axis_x ( so_called_platform_matrix_float_data_type & matrix , so_called_platform_vector_data_type v )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_set ( ) ) ;
    so_called_platform_vector_insider :: x_get ( matrix . _elements [ 0 ] , v ) ;
    so_called_platform_vector_insider :: y_get ( matrix . _elements [ 1 ] , v ) ;
    so_called_platform_vector_insider :: z_get ( matrix . _elements [ 2 ] , v ) ;
    matrix . _elements [ 3 ] = 0 ;
}

void shy_platform_matrix_float :: set_axis_y ( so_called_platform_matrix_float_data_type & matrix , so_called_platform_vector_data_type v )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_set ( ) ) ;
    so_called_platform_vector_insider :: x_get ( matrix . _elements [ 4 ] , v ) ;
    so_called_platform_vector_insider :: y_get ( matrix . _elements [ 5 ] , v ) ;
    so_called_platform_vector_insider :: z_get ( matrix . _elements [ 6 ] , v ) ;
    matrix . _elements [ 7 ] = 0 ;
}

void shy_platform_matrix_float :: set_axis_z ( so_called_platform_matrix_float_data_type & matrix , so_called_platform_vector_data_type v )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_set ( ) ) ;
    so_called_platform_vector_insider :: x_get ( matrix . _elements [  8 ] , v ) ;
    so_called_platform_vector_insider :: y_get ( matrix . _elements [  9 ] , v ) ;
    so_called_platform_vector_insider :: z_get ( matrix . _elements [ 10 ] , v ) ;
    matrix . _elements [ 11 ] = 0 ;
}

void shy_platform_matrix_float :: set_origin ( so_called_platform_matrix_float_data_type & matrix , so_called_platform_vector_data_type v )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_set ( ) ) ;
    so_called_platform_vector_insider :: x_get ( matrix . _elements [ 12 ] , v ) ;
    so_called_platform_vector_insider :: y_get ( matrix . _elements [ 13 ] , v ) ;
    so_called_platform_vector_insider :: z_get ( matrix . _elements [ 14 ] , v ) ;
    matrix . _elements [ 15 ] = 1 ;
}

void shy_platform_matrix_float :: get_axis_x ( so_called_platform_vector_data_type & result , const so_called_platform_matrix_float_data_type & matrix )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_get ( ) ) ;
    so_called_platform_vector_insider :: x_set ( result , matrix . _elements [ 0 ] ) ;
    so_called_platform_vector_insider :: y_set ( result , matrix . _elements [ 1 ] ) ;
    so_called_platform_vector_insider :: z_set ( result , matrix . _elements [ 2 ] ) ;
}

void shy_platform_matrix_float :: get_axis_y ( so_called_platform_vector_data_type & result , const so_called_platform_matrix_float_data_type & matrix )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_get ( ) ) ;
    so_called_platform_vector_insider :: x_set ( result , matrix . _elements [ 4 ] ) ;
    so_called_platform_vector_insider :: y_set ( result , matrix . _elements [ 5 ] ) ;
    so_called_platform_vector_insider :: z_set ( result , matrix . _elements [ 6 ] ) ;
}

void shy_platform_matrix_float :: get_axis_z ( so_called_platform_vector_data_type & result , const so_called_platform_matrix_float_data_type & matrix )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_get ( ) ) ;
    so_called_platform_vector_insider :: x_set ( result , matrix . _elements [ 8 ] ) ;
    so_called_platform_vector_insider :: y_set ( result , matrix . _elements [ 9 ] ) ;
    so_called_platform_vector_insider :: z_set ( result , matrix . _elements [ 10 ] ) ;
}

void shy_platform_matrix_float :: get_origin ( so_called_platform_vector_data_type & result , const so_called_platform_matrix_float_data_type & matrix )
{
    so_called_profile ( so_called_profile_platform_matrix :: row_get ( ) ) ;
    so_called_platform_vector_insider :: x_set ( result , matrix . _elements [ 12 ] ) ;
    so_called_platform_vector_insider :: y_set ( result , matrix . _elements [ 13 ] ) ;
    so_called_platform_vector_insider :: z_set ( result , matrix . _elements [ 14 ] ) ;
}

void shy_platform_matrix_float :: identity ( so_called_platform_matrix_float_data_type & matrix )
{
    so_called_profile ( so_called_profile_platform_matrix :: identity ( ) ) ;
    for ( so_called_lib_std_int32_t i = 0 ; i < 16 ; i ++ )
    {
        if ( i == 0 || i == 5 || i == 10 || i == 15 )
            matrix . _elements [ i ] = 1 ;
        else
            matrix . _elements [ i ] = 0 ;
    }
}

void shy_platform_matrix_float :: inverse_rotation_translation ( so_called_platform_matrix_float_data_type & matrix )
{
    so_called_profile ( so_called_profile_platform_matrix :: inverse ( ) ) ;

    so_called_platform_vector_data_type axis_x ;
    so_called_platform_vector_data_type axis_y ;
    so_called_platform_vector_data_type axis_z ;
    so_called_platform_vector_data_type origin ;
    so_called_platform_matrix_float :: get_axis_x ( axis_x , matrix ) ;
    so_called_platform_matrix_float :: get_axis_y ( axis_y , matrix ) ;
    so_called_platform_matrix_float :: get_axis_z ( axis_z , matrix ) ;
    so_called_platform_matrix_float :: get_origin ( origin , matrix ) ;
    
    so_called_platform_math_num_fract_type dot_x ;
    so_called_platform_math_num_fract_type dot_y ;
    so_called_platform_math_num_fract_type dot_z ;
    so_called_platform_vector :: dot_product ( dot_x , origin , axis_x ) ;
    so_called_platform_vector :: dot_product ( dot_y , origin , axis_y ) ;
    so_called_platform_vector :: dot_product ( dot_z , origin , axis_z ) ;
    
    so_called_lib_std_float dot_x_float = 0 ;
    so_called_lib_std_float dot_y_float = 0 ;
    so_called_lib_std_float dot_z_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( dot_x_float , dot_x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( dot_y_float , dot_y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( dot_z_float , dot_z ) ;
    
    so_called_platform_vector_data_type new_origin ;
    so_called_platform_vector_insider :: x_set ( new_origin , - dot_x_float ) ;
    so_called_platform_vector_insider :: y_set ( new_origin , - dot_y_float ) ;
    so_called_platform_vector_insider :: z_set ( new_origin , - dot_z_float ) ;
    
    so_called_platform_matrix_float :: set_origin ( matrix , new_origin ) ;
    shy_guts :: swap_values ( matrix . _elements [ 1 ] , matrix . _elements [ 4 ] ) ;
    shy_guts :: swap_values ( matrix . _elements [ 2 ] , matrix . _elements [ 8 ] ) ;
    shy_guts :: swap_values ( matrix . _elements [ 6 ] , matrix . _elements [ 9 ] ) ;
}
