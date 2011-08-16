#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_main_menu_animation , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_main_menu_animation :: prepare ( )
{
    shy_guts_bind_module ( logic_main_menu_animation ) ;

    shy_guts_bind_value ( shake_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( shake_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( shake_shift_x_amplitude_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( shake_shift_x_amplitude_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( shake_shift_x_period_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;
}
