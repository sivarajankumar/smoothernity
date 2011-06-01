#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_room_consts :: value \
        )

void shy_loadable_consts_reflection_logic_room :: prepare ( )
{
    shy_bind_module_helper ( logic_room ) ;
    shy_bind_value_helper ( mesh_color_right_r ) ;
    shy_bind_value_helper ( mesh_color_right_g ) ;
    shy_bind_value_helper ( mesh_color_right_b ) ;
    shy_bind_value_helper ( mesh_color_right_a ) ;
    shy_bind_value_helper ( mesh_color_left_r ) ;
    shy_bind_value_helper ( mesh_color_left_g ) ;
    shy_bind_value_helper ( mesh_color_left_b ) ;
    shy_bind_value_helper ( mesh_color_left_a ) ;
    shy_bind_value_helper ( mesh_color_near_r ) ;
    shy_bind_value_helper ( mesh_color_near_g ) ;
    shy_bind_value_helper ( mesh_color_near_b ) ;
    shy_bind_value_helper ( mesh_color_near_a ) ;
    shy_bind_value_helper ( mesh_color_far_r ) ;
    shy_bind_value_helper ( mesh_color_far_g ) ;
    shy_bind_value_helper ( mesh_color_far_b ) ;
    shy_bind_value_helper ( mesh_color_far_a ) ;
    shy_bind_value_helper ( mesh_color_top_r ) ;
    shy_bind_value_helper ( mesh_color_top_g ) ;
    shy_bind_value_helper ( mesh_color_top_b ) ;
    shy_bind_value_helper ( mesh_color_top_a ) ;
    shy_bind_value_helper ( mesh_color_bottom_r ) ;
    shy_bind_value_helper ( mesh_color_bottom_g ) ;
    shy_bind_value_helper ( mesh_color_bottom_b ) ;
    shy_bind_value_helper ( mesh_color_bottom_a ) ;
    shy_bind_value_helper ( mesh_position_x ) ;
    shy_bind_value_helper ( mesh_position_y ) ;
    shy_bind_value_helper ( mesh_position_z ) ;
    shy_bind_value_helper ( mesh_x_left ) ;
    shy_bind_value_helper ( mesh_x_right ) ;
    shy_bind_value_helper ( mesh_y_top ) ;
    shy_bind_value_helper ( mesh_y_bottom ) ;
    shy_bind_value_helper ( mesh_z_near ) ;
    shy_bind_value_helper ( mesh_z_far ) ;
    shy_bind_value_helper ( mesh_right_side_u_left ) ;
    shy_bind_value_helper ( mesh_right_side_u_right ) ;
    shy_bind_value_helper ( mesh_right_side_v_top ) ;
    shy_bind_value_helper ( mesh_right_side_v_bottom ) ;
    shy_bind_value_helper ( mesh_left_side_u_left ) ;
    shy_bind_value_helper ( mesh_left_side_u_right ) ;
    shy_bind_value_helper ( mesh_left_side_v_top ) ;
    shy_bind_value_helper ( mesh_left_side_v_bottom ) ;
    shy_bind_value_helper ( mesh_near_side_u_left ) ;
    shy_bind_value_helper ( mesh_near_side_u_right ) ;
    shy_bind_value_helper ( mesh_near_side_v_top ) ;
    shy_bind_value_helper ( mesh_near_side_v_bottom ) ;
    shy_bind_value_helper ( mesh_far_side_u_left ) ;
    shy_bind_value_helper ( mesh_far_side_u_right ) ;
    shy_bind_value_helper ( mesh_far_side_v_top ) ;
    shy_bind_value_helper ( mesh_far_side_v_bottom ) ;
    shy_bind_value_helper ( mesh_top_side_u_left ) ;
    shy_bind_value_helper ( mesh_top_side_u_right ) ;
    shy_bind_value_helper ( mesh_top_side_v_top ) ;
    shy_bind_value_helper ( mesh_top_side_v_bottom ) ;
    shy_bind_value_helper ( mesh_bottom_side_u_left ) ;
    shy_bind_value_helper ( mesh_bottom_side_u_right ) ;
    shy_bind_value_helper ( mesh_bottom_side_v_top ) ;
    shy_bind_value_helper ( mesh_bottom_side_v_bottom ) ;
    shy_bind_value_helper ( room_show_time ) ;
    shy_bind_value_helper ( texture_pen_intensity ) ;
    shy_bind_value_helper ( texture_paper_intensity ) ;
    shy_bind_value_helper ( texture_alpha ) ;
    shy_bind_value_helper ( texture_grid_size ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
