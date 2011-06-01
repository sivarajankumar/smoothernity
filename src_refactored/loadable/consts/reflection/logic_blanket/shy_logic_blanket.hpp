#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_blanket_consts :: value \
        )

void shy_loadable_consts_reflection_logic_blanket :: prepare ( )
{
    shy_bind_module_helper ( logic_blanket ) ;
    shy_bind_value_helper ( mesh_vertex_x_left ) ;
    shy_bind_value_helper ( mesh_vertex_x_right ) ;
    shy_bind_value_helper ( mesh_vertex_y_bottom ) ;
    shy_bind_value_helper ( mesh_vertex_y_top ) ;
    shy_bind_value_helper ( mesh_vertex_z ) ;
    shy_bind_value_helper ( mesh_color_r ) ;
    shy_bind_value_helper ( mesh_color_g ) ;
    shy_bind_value_helper ( mesh_color_b ) ;
    shy_bind_value_helper ( mesh_color_a ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
