#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_door_consts :: value \
        )

void shy_loadable_consts_reflection_logic_door :: prepare ( )
{
    shy_bind_module_helper ( logic_door ) ;
    shy_bind_value_helper ( mesh_color_r ) ;
    shy_bind_value_helper ( mesh_color_g ) ;
    shy_bind_value_helper ( mesh_color_b ) ;
    shy_bind_value_helper ( mesh_color_a ) ;
    shy_bind_value_helper ( mesh_x_left ) ;
    shy_bind_value_helper ( mesh_x_right ) ;
    shy_bind_value_helper ( mesh_y_bottom ) ;
    shy_bind_value_helper ( mesh_y_top ) ;
    shy_bind_value_helper ( mesh_z ) ;
    shy_bind_value_helper ( mesh_u_top_left ) ;
    shy_bind_value_helper ( mesh_v_top_left ) ;
    shy_bind_value_helper ( mesh_u_top_right ) ;
    shy_bind_value_helper ( mesh_v_top_right ) ;
    shy_bind_value_helper ( mesh_u_bottom_left ) ;
    shy_bind_value_helper ( mesh_v_bottom_left ) ;
    shy_bind_value_helper ( mesh_u_bottom_right ) ;
    shy_bind_value_helper ( mesh_v_bottom_right ) ;
    shy_bind_value_helper ( texture_pen_r ) ;
    shy_bind_value_helper ( texture_pen_g ) ;
    shy_bind_value_helper ( texture_pen_b ) ;
    shy_bind_value_helper ( texture_pen_a ) ;
    shy_bind_value_helper ( texture_paper_r ) ;
    shy_bind_value_helper ( texture_paper_g ) ;
    shy_bind_value_helper ( texture_paper_b ) ;
    shy_bind_value_helper ( texture_paper_a ) ;
    shy_bind_value_helper ( texture_stripes ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
