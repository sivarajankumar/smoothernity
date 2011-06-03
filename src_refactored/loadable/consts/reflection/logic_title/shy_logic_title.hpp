#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_title , value )

void shy_loadable_consts_reflection_logic_title :: prepare ( )
{
    shy_guts_bind_module ( logic_title ) ;
    shy_guts_bind_value ( appear_pos_angle_periods ) ;
    shy_guts_bind_value ( appear_rubber_first ) ;
    shy_guts_bind_value ( appear_rubber_last ) ;
    shy_guts_bind_value ( appear_duration_in_frames ) ;
    shy_guts_bind_value ( disappear_pos_angle_periods ) ;
    shy_guts_bind_value ( disappear_rubber_first ) ;
    shy_guts_bind_value ( disappear_rubber_last ) ;
    shy_guts_bind_value ( disappear_duration_in_frames ) ;
    shy_guts_bind_value ( scene_scale_min ) ;
    shy_guts_bind_value ( scene_scale_max ) ;
    shy_guts_bind_value ( spin_radius_in_letters ) ;
    shy_guts_bind_value ( frames_between_letters ) ;
}
