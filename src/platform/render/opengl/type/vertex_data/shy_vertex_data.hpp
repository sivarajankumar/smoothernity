shy_platform_render_opengl_vertex_data_type :: shy_platform_render_opengl_vertex_data_type ( )
{
    for ( so_called_lib_std_int32_t i = 0 ; i < 3 ; i ++ )
        _position [ i ] = so_called_platform_consts_insider :: uninitialized_value ;
    for ( so_called_lib_std_int32_t i = 0 ; i < 2 ; i ++ )
        _tex_coord [ i ] = so_called_platform_consts_insider :: uninitialized_value ;
    for ( so_called_lib_std_int32_t i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( so_called_lib_opengl_GLubyte ) so_called_platform_consts_insider :: uninitialized_value ;
}
