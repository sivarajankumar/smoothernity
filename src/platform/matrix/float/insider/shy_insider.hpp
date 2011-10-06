void shy_platform_matrix_float_insider :: data_uninitialized ( so_called_lib_std_bool & result , so_called_platform_matrix_float_data_type matrix )
{
    so_called_platform_matrix_float_data_type uninitialized_matrix ;
    result = so_called_lib_std_false ;
    for ( so_called_lib_std_int32_t i = 0 ; i < 16 ; i ++ )
        result |= ( matrix . _elements [ i ] == uninitialized_matrix . _elements [ i ] ) ;
}

void shy_platform_matrix_float_insider :: elements_ptr ( so_called_lib_std_float * & result , so_called_platform_matrix_float_data_type & matrix )
{
    result = matrix . _elements ;
}

void shy_platform_matrix_float_insider :: elements_ptr ( const so_called_lib_std_float * & result , const so_called_platform_matrix_float_data_type & matrix )
{
    result = matrix . _elements ;
}

