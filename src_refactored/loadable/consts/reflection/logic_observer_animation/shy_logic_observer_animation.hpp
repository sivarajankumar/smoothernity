#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_observer_animation , value )

void shy_loadable_consts_reflection_logic_observer_animation :: prepare ( )
{
    shy_guts_bind_module ( logic_observer_animation ) ;
    shy_guts_bind_value ( flight_target_z ) ;
    shy_guts_bind_value ( flight_horizontal_offset_period ) ;
    shy_guts_bind_value ( flight_horizontal_offset_amplitude ) ;
    shy_guts_bind_value ( flight_vertical_offset_period ) ;
    shy_guts_bind_value ( flight_vertical_offset_amplitude ) ;
}
