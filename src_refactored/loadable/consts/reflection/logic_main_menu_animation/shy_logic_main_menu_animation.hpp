#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_main_menu_animation , value )

void shy_loadable_consts_reflection_logic_main_menu_animation :: prepare ( )
{
    shy_guts_bind_module ( logic_main_menu_animation ) ;
    shy_guts_bind_value ( shake_time_to_begin ) ;
    shy_guts_bind_value ( shake_time_from_begin_to_end ) ;
    shy_guts_bind_value ( shake_shift_x_amplitude_begin ) ;
    shy_guts_bind_value ( shake_shift_x_amplitude_end ) ;
    shy_guts_bind_value ( shake_shift_x_period_in_seconds ) ;
}
