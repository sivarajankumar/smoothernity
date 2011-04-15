void shy_loadable_consts_reflection_logic_door_animation :: prepare ( )
{
    so_called_loadable_consts_binder :: module ( "logic_door_animation" ) ;
    so_called_loadable_consts_binder :: bind ( "animation_origin_x" , so_called_common_logic_door_animation_consts :: animation_origin_x ) ;
    so_called_loadable_consts_binder :: bind ( "animation_origin_y" , so_called_common_logic_door_animation_consts :: animation_origin_y ) ;
    so_called_loadable_consts_binder :: bind ( "animation_origin_z" , so_called_common_logic_door_animation_consts :: animation_origin_z ) ;
    so_called_loadable_consts_binder :: bind ( "appear_scale_begin" , so_called_common_logic_door_animation_consts :: appear_scale_begin ) ;
    so_called_loadable_consts_binder :: bind ( "appear_scale_end" , so_called_common_logic_door_animation_consts :: appear_scale_end ) ;
    so_called_loadable_consts_binder :: bind ( "appear_time_from_begin_to_end" , so_called_common_logic_door_animation_consts :: appear_time_from_begin_to_end ) ;
}
