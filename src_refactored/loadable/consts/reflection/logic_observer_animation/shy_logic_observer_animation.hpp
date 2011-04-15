void shy_loadable_consts_reflection_logic_observer_animation :: prepare ( )
{
    so_called_loadable_consts_binder :: module ( "logic_observer_animation" ) ;
    so_called_loadable_consts_binder :: bind ( "flight_target_z" , so_called_common_logic_observer_animation_consts :: flight_target_z ) ;
    so_called_loadable_consts_binder :: bind ( "flight_horizontal_offset_period" , so_called_common_logic_observer_animation_consts :: flight_horizontal_offset_period ) ;
    so_called_loadable_consts_binder :: bind ( "flight_horizontal_offset_amplitude" , so_called_common_logic_observer_animation_consts :: flight_horizontal_offset_amplitude ) ;
    so_called_loadable_consts_binder :: bind ( "flight_vertical_offset_period" , so_called_common_logic_observer_animation_consts :: flight_vertical_offset_period ) ;
    so_called_loadable_consts_binder :: bind ( "flight_vertical_offset_amplitude" , so_called_common_logic_observer_animation_consts :: flight_vertical_offset_amplitude ) ;
}
