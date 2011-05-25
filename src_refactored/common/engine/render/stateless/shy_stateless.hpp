void shy_common_engine_render_stateless :: set_texel_color
    ( so_called_type_platform_render_texel_data & texel
    , so_called_type_platform_math_num_fract r
    , so_called_type_platform_math_num_fract g
    , so_called_type_platform_math_num_fract b
    , so_called_type_platform_math_num_fract a
    )
{
    so_called_platform_render :: set_texel_color ( texel , r , g , b , a ) ;
}

void shy_common_engine_render_stateless :: create_texture_resource_id
    ( so_called_type_platform_render_texture_loader_resource_id & resource_id
    , so_called_type_platform_math_num_whole resource_index
    )
{
    so_called_platform_render_texture_loader :: create_resource_id ( resource_id , resource_index ) ;
}

