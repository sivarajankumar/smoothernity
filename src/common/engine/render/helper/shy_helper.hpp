void shy_common_engine_render_helper :: mesh_set_vertex_position 
    ( so_called_common_engine_render_mesh_id_type mesh
    , so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_fract_type x
    , so_called_platform_math_num_fract_type y
    , so_called_platform_math_num_fract_type z 
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

void shy_common_engine_render_helper :: mesh_set_vertex_tex_coord 
    ( so_called_common_engine_render_mesh_id_type mesh
    , so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_fract_type u
    , so_called_platform_math_num_fract_type v 
    )
{
    so_called_common_engine_render_mesh_set_vertex_tex_coord_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_common_engine_render_mesh_set_vertex_tex_coord_sender :: send ( msg ) ;
}

void shy_common_engine_render_helper :: mesh_set_vertex_color 
    ( so_called_common_engine_render_mesh_id_type mesh
    , so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_fract_type r
    , so_called_platform_math_num_fract_type g
    , so_called_platform_math_num_fract_type b
    , so_called_platform_math_num_fract_type a 
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

void shy_common_engine_render_helper :: mesh_set_triangle_strip_index_value
    ( so_called_common_engine_render_mesh_id_type mesh
    , so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_whole_type index 
    )
{
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_sender :: send ( msg ) ;
}
