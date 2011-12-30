void shy_platform_vector_float_insider :: data_uninitialized ( so_called_lib_std_bool & result , so_called_platform_vector_float_data_type vector )
{
    so_called_platform_vector_float_data_type uninitialized_vector ;
    result = so_called_lib_std_false ;
    result |= ( vector . _x == uninitialized_vector . _x ) ;
    result |= ( vector . _y == uninitialized_vector . _y ) ;
    result |= ( vector . _z == uninitialized_vector . _z ) ;
}

void shy_platform_vector_float_insider :: x_get ( so_called_lib_std_float & x , so_called_platform_vector_float_data_type v )
{
    x = v . _x ;
}

void shy_platform_vector_float_insider :: y_get ( so_called_lib_std_float & y , so_called_platform_vector_float_data_type v )
{
    y = v . _y ;
}

void shy_platform_vector_float_insider :: z_get ( so_called_lib_std_float & z , so_called_platform_vector_float_data_type v )
{
    z = v . _z ;
}

void shy_platform_vector_float_insider :: x_set ( so_called_platform_vector_float_data_type & v , so_called_lib_std_float x )
{
    v . _x = x ;
}

void shy_platform_vector_float_insider :: y_set ( so_called_platform_vector_float_data_type & v , so_called_lib_std_float y )
{
    v . _y = y ;
}

void shy_platform_vector_float_insider :: z_set ( so_called_platform_vector_float_data_type & v , so_called_lib_std_float z )
{
    v . _z = z ;
}

