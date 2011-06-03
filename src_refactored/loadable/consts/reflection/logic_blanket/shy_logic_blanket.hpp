#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_blanket , value )

void shy_loadable_consts_reflection_logic_blanket :: prepare ( )
{
    shy_guts_bind_module ( logic_blanket ) ;
    shy_guts_bind_value ( mesh_vertex_x_left ) ;
    shy_guts_bind_value ( mesh_vertex_x_right ) ;
    shy_guts_bind_value ( mesh_vertex_y_bottom ) ;
    shy_guts_bind_value ( mesh_vertex_y_top ) ;
    shy_guts_bind_value ( mesh_vertex_z ) ;
    shy_guts_bind_value ( mesh_color_r ) ;
    shy_guts_bind_value ( mesh_color_g ) ;
    shy_guts_bind_value ( mesh_color_b ) ;
    shy_guts_bind_value ( mesh_color_a ) ;
}
