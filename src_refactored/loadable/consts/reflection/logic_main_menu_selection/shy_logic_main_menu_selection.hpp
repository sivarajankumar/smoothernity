#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_main_menu_selection , value )

void shy_loadable_consts_reflection_logic_main_menu_selection :: prepare ( )
{
    shy_guts_bind_module ( logic_main_menu_selection ) ;
    shy_guts_bind_value ( mesh_size ) ;
    shy_guts_bind_value ( mesh_color_r ) ;
    shy_guts_bind_value ( mesh_color_g ) ;
    shy_guts_bind_value ( mesh_color_b ) ;
    shy_guts_bind_value ( mesh_color_a ) ;
    shy_guts_bind_value ( selected_rect_vertical_scale ) ;
}
