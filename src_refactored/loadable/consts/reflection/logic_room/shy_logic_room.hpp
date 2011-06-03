#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_room , value )

void shy_loadable_consts_reflection_logic_room :: prepare ( )
{
    shy_guts_bind_module ( logic_room ) ;
    shy_guts_bind_value ( mesh_color_right_r ) ;
    shy_guts_bind_value ( mesh_color_right_g ) ;
    shy_guts_bind_value ( mesh_color_right_b ) ;
    shy_guts_bind_value ( mesh_color_right_a ) ;
    shy_guts_bind_value ( mesh_color_left_r ) ;
    shy_guts_bind_value ( mesh_color_left_g ) ;
    shy_guts_bind_value ( mesh_color_left_b ) ;
    shy_guts_bind_value ( mesh_color_left_a ) ;
    shy_guts_bind_value ( mesh_color_near_r ) ;
    shy_guts_bind_value ( mesh_color_near_g ) ;
    shy_guts_bind_value ( mesh_color_near_b ) ;
    shy_guts_bind_value ( mesh_color_near_a ) ;
    shy_guts_bind_value ( mesh_color_far_r ) ;
    shy_guts_bind_value ( mesh_color_far_g ) ;
    shy_guts_bind_value ( mesh_color_far_b ) ;
    shy_guts_bind_value ( mesh_color_far_a ) ;
    shy_guts_bind_value ( mesh_color_top_r ) ;
    shy_guts_bind_value ( mesh_color_top_g ) ;
    shy_guts_bind_value ( mesh_color_top_b ) ;
    shy_guts_bind_value ( mesh_color_top_a ) ;
    shy_guts_bind_value ( mesh_color_bottom_r ) ;
    shy_guts_bind_value ( mesh_color_bottom_g ) ;
    shy_guts_bind_value ( mesh_color_bottom_b ) ;
    shy_guts_bind_value ( mesh_color_bottom_a ) ;
    shy_guts_bind_value ( mesh_position_x ) ;
    shy_guts_bind_value ( mesh_position_y ) ;
    shy_guts_bind_value ( mesh_position_z ) ;
    shy_guts_bind_value ( mesh_x_left ) ;
    shy_guts_bind_value ( mesh_x_right ) ;
    shy_guts_bind_value ( mesh_y_top ) ;
    shy_guts_bind_value ( mesh_y_bottom ) ;
    shy_guts_bind_value ( mesh_z_near ) ;
    shy_guts_bind_value ( mesh_z_far ) ;
    shy_guts_bind_value ( mesh_right_side_u_left ) ;
    shy_guts_bind_value ( mesh_right_side_u_right ) ;
    shy_guts_bind_value ( mesh_right_side_v_top ) ;
    shy_guts_bind_value ( mesh_right_side_v_bottom ) ;
    shy_guts_bind_value ( mesh_left_side_u_left ) ;
    shy_guts_bind_value ( mesh_left_side_u_right ) ;
    shy_guts_bind_value ( mesh_left_side_v_top ) ;
    shy_guts_bind_value ( mesh_left_side_v_bottom ) ;
    shy_guts_bind_value ( mesh_near_side_u_left ) ;
    shy_guts_bind_value ( mesh_near_side_u_right ) ;
    shy_guts_bind_value ( mesh_near_side_v_top ) ;
    shy_guts_bind_value ( mesh_near_side_v_bottom ) ;
    shy_guts_bind_value ( mesh_far_side_u_left ) ;
    shy_guts_bind_value ( mesh_far_side_u_right ) ;
    shy_guts_bind_value ( mesh_far_side_v_top ) ;
    shy_guts_bind_value ( mesh_far_side_v_bottom ) ;
    shy_guts_bind_value ( mesh_top_side_u_left ) ;
    shy_guts_bind_value ( mesh_top_side_u_right ) ;
    shy_guts_bind_value ( mesh_top_side_v_top ) ;
    shy_guts_bind_value ( mesh_top_side_v_bottom ) ;
    shy_guts_bind_value ( mesh_bottom_side_u_left ) ;
    shy_guts_bind_value ( mesh_bottom_side_u_right ) ;
    shy_guts_bind_value ( mesh_bottom_side_v_top ) ;
    shy_guts_bind_value ( mesh_bottom_side_v_bottom ) ;
    shy_guts_bind_value ( room_show_time ) ;
    shy_guts_bind_value ( texture_pen_intensity ) ;
    shy_guts_bind_value ( texture_paper_intensity ) ;
    shy_guts_bind_value ( texture_alpha ) ;
    shy_guts_bind_value ( texture_grid_size ) ;
}
