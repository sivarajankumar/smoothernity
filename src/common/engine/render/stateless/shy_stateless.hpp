so_called_common_engine_render_mesh_id_type shy_common_engine_render_stateless :: init_mesh_id
    ( so_called_platform_math_const_int_32_type arg_mesh_id 
    )
{
    so_called_common_engine_render_mesh_id_type mesh ;
    so_called_platform_math :: make_num_whole ( mesh . _mesh_id , arg_mesh_id ) ;
    return mesh ;
}

void shy_common_engine_render_stateless :: create_texture_resource_id
    ( so_called_platform_render_texture_loader_resource_id_type & resource_id
    , so_called_platform_math_num_whole_type resource_index
    )
{
    so_called_platform_render_texture_loader :: create_resource_id ( resource_id , resource_index ) ;
}

void shy_common_engine_render_stateless :: set_texel_color
    ( so_called_platform_render_texel_data_type & texel
    , so_called_platform_math_num_fract_type r
    , so_called_platform_math_num_fract_type g
    , so_called_platform_math_num_fract_type b
    , so_called_platform_math_num_fract_type a
    )
{
    so_called_platform_render :: set_texel_color ( texel , r , g , b , a ) ;
}
