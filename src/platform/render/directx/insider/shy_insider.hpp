namespace shy_guts
{
    so_called_lib_std_float aspect_width = 1 ;
    so_called_lib_std_float aspect_height = 1 ;
    so_called_lib_std_bool frame_loss = so_called_lib_std_false ;
}

void shy_platform_render_directx_insider :: set_aspect_width ( so_called_lib_std_float aspect_width )
{
    shy_guts :: aspect_width = aspect_width ;
}

void shy_platform_render_directx_insider :: get_aspect_width ( so_called_lib_std_float & aspect_width )
{
    aspect_width = shy_guts :: aspect_width ;
}

void shy_platform_render_directx_insider :: set_aspect_height ( so_called_lib_std_float aspect_height )
{
    shy_guts :: aspect_height = aspect_height ;
}

void shy_platform_render_directx_insider :: get_aspect_height ( so_called_lib_std_float & aspect_height )
{
    aspect_height = shy_guts :: aspect_height ;
}

void shy_platform_render_directx_insider :: set_frame_loss ( so_called_lib_std_bool frame_loss )
{
    shy_guts :: frame_loss = frame_loss ;
}

void shy_platform_render_directx_insider :: get_frame_loss ( so_called_lib_std_bool & frame_loss )
{
    frame_loss = shy_guts :: frame_loss ;
}

void shy_platform_render_directx_insider :: get_texture_size ( so_called_lib_std_int32_t & width , so_called_lib_std_int32_t & height , so_called_platform_render_directx_texture_id_type texture_id )
{
    width = texture_id . _width ;
    height = texture_id . _height ;
}

void shy_platform_render_directx_insider :: get_mapped_vertices_count ( so_called_lib_std_int32_t & elements , so_called_platform_render_directx_vertex_buffer_mapped_data_type data )
{
    elements = data . _elements ;
}

void shy_platform_render_directx_insider :: get_mapped_indices_count ( so_called_lib_std_int32_t & elements , so_called_platform_render_directx_index_buffer_mapped_data_type data )
{
    elements = data . _elements ;
}

void shy_platform_render_directx_insider :: get_indices_count ( so_called_lib_std_int32_t & elements , so_called_platform_render_directx_index_buffer_id_type data )
{
    elements = data . _elements ;
}

void shy_platform_render_directx_insider :: index_buffer_id_uninitialized ( so_called_lib_std_bool & result , so_called_platform_render_directx_index_buffer_id_type value )
{
    so_called_platform_render_directx_index_buffer_id_type uninitialized_value ;
    result = value . _buffer_id == uninitialized_value . _buffer_id ;
}

void shy_platform_render_directx_insider :: index_buffer_mapped_data_uninitialized ( so_called_lib_std_bool & result , so_called_platform_render_directx_index_buffer_mapped_data_type value )
{
    so_called_platform_render_directx_index_buffer_mapped_data_type uninitialized_value ;
    result = value . _data == uninitialized_value . _data ;
}

void shy_platform_render_directx_insider :: texture_id_uninitialized ( so_called_lib_std_bool & result , so_called_platform_render_directx_texture_id_type value )
{
    so_called_platform_render_directx_texture_id_type uninitialized_value ;
    result = value . _texture_id == uninitialized_value . _texture_id ;
}

void shy_platform_render_directx_insider :: vertex_buffer_id_uninitialized ( so_called_lib_std_bool & result , so_called_platform_render_directx_vertex_buffer_id_type value )
{
    so_called_platform_render_directx_vertex_buffer_id_type uninitialized_value ;
    result = value . _buffer_id == uninitialized_value . _buffer_id ;
}

void shy_platform_render_directx_insider :: vertex_buffer_mapped_data_uninitialized ( so_called_lib_std_bool & result , so_called_platform_render_directx_vertex_buffer_mapped_data_type value )
{
    so_called_platform_render_directx_vertex_buffer_mapped_data_type uninitialized_value ;
    result = value . _data == uninitialized_value . _data ;
}
