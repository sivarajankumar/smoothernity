#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_door_animation , value )

void shy_loadable_consts_reflection_logic_door_animation :: prepare ( )
{
    shy_guts_bind_module ( logic_door_animation ) ;
    shy_guts_bind_value ( animation_origin_x ) ;
    shy_guts_bind_value ( animation_origin_y ) ;
    shy_guts_bind_value ( animation_origin_z ) ;
    shy_guts_bind_value ( appear_scale_begin ) ;
    shy_guts_bind_value ( appear_scale_end ) ;
    shy_guts_bind_value ( appear_time_from_begin_to_end ) ;
}
