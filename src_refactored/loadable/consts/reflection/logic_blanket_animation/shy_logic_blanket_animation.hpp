#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_blanket_animation , value )

void shy_loadable_consts_reflection_logic_blanket_animation :: prepare ( )
{
    shy_guts_bind_module ( logic_blanket_animation ) ;
    shy_guts_bind_value ( animation_origin_x ) ;
    shy_guts_bind_value ( animation_origin_y ) ;
    shy_guts_bind_value ( animation_origin_z ) ;
    shy_guts_bind_value ( appear_scale_begin ) ;
    shy_guts_bind_value ( appear_scale_end ) ;
    shy_guts_bind_value ( appear_rotation_begin ) ;
    shy_guts_bind_value ( appear_rotation_end ) ;
    shy_guts_bind_value ( appear_time_from_begin_to_end ) ;
    shy_guts_bind_value ( disappear_scale_begin ) ;
    shy_guts_bind_value ( disappear_scale_end ) ;
    shy_guts_bind_value ( disappear_rotation_begin ) ;
    shy_guts_bind_value ( disappear_rotation_end ) ;
    shy_guts_bind_value ( disappear_time_from_begin_to_end ) ;
}
