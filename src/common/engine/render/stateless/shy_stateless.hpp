so_called_type_common_engine_render_mesh_id shy_common_engine_render_stateless :: init_mesh_id
    ( so_called_type_platform_math_const_int_32 arg_mesh_id 
    )
{
    so_called_type_common_engine_render_mesh_id mesh ;
    so_called_platform_math :: make_num_whole ( mesh . _mesh_id , arg_mesh_id ) ;
    return mesh ;
}

void shy_common_engine_render_stateless :: create_texture_resource_id
    ( so_called_type_platform_render_texture_loader_resource_id & resource_id
    , so_called_type_platform_math_num_whole resource_index
    )
{
    so_called_platform_render_texture_loader :: create_resource_id ( resource_id , resource_index ) ;
}

void shy_common_engine_render_stateless :: mesh_set_vertex_position 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_common_engine_render_mesh_set_vertex_position_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    so_called_common_engine_render_mesh_set_vertex_position_sender :: send ( msg ) ;
}

void shy_common_engine_render_stateless :: mesh_set_vertex_tex_coord 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract u
    , so_called_type_platform_math_num_fract v 
    )
{
    so_called_common_engine_render_mesh_set_vertex_tex_coord_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_common_engine_render_mesh_set_vertex_tex_coord_sender :: send ( msg ) ;
}

void shy_common_engine_render_stateless :: mesh_set_vertex_color 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract r
    , so_called_type_platform_math_num_fract g
    , so_called_type_platform_math_num_fract b
    , so_called_type_platform_math_num_fract a 
    )
{
    so_called_common_engine_render_mesh_set_vertex_color_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    so_called_common_engine_render_mesh_set_vertex_color_sender :: send ( msg ) ;
}

void shy_common_engine_render_stateless :: mesh_set_triangle_strip_index_value
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_whole index 
    )
{
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_sender :: send ( msg ) ;
}

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
