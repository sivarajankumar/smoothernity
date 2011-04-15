void shy_loadable_consts_reflection_logic_main_menu_animation :: prepare ( )
{
    so_called_loadable_consts_binder :: module ( "logic_main_menu_animation" ) ;
    so_called_loadable_consts_binder :: bind ( "shake_time_to_begin" , so_called_common_logic_main_menu_animation_consts :: shake_time_to_begin ) ;
    so_called_loadable_consts_binder :: bind ( "shake_time_from_begin_to_end" , so_called_common_logic_main_menu_animation_consts :: shake_time_from_begin_to_end ) ;
    so_called_loadable_consts_binder :: bind ( "shake_shift_x_amplitude_begin" , so_called_common_logic_main_menu_animation_consts :: shake_shift_x_amplitude_begin ) ;
    so_called_loadable_consts_binder :: bind ( "shake_shift_x_amplitude_end" , so_called_common_logic_main_menu_animation_consts :: shake_shift_x_amplitude_end ) ;
    so_called_loadable_consts_binder :: bind ( "shake_shift_x_period_in_seconds" , so_called_common_logic_main_menu_animation_consts :: shake_shift_x_period_in_seconds ) ;
}
