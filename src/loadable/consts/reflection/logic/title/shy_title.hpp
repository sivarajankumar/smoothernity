#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_title , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_title :: prepare ( )
{
    shy_guts_bind_module ( logic_title ) ;

    shy_guts_bind_value ( appear_pos_angle_periods ) ;
    shy_guts_bind_value_min ( 1 , 1000 ) ;
    shy_guts_bind_value_max ( 1000 , 1 ) ;

    shy_guts_bind_value ( appear_rubber_first ) ;
    shy_guts_bind_value_min ( 1 , 1000 ) ;
    shy_guts_bind_value_max ( 1000 , 1 ) ;

    shy_guts_bind_value ( appear_rubber_last ) ;
    shy_guts_bind_value_min ( 1 , 1000 ) ;
    shy_guts_bind_value_max ( 1000 , 1 ) ;

    shy_guts_bind_value ( appear_duration_in_frames ) ;
    shy_guts_bind_value_min ( 1 ) ;
    shy_guts_bind_value_max ( 1000 ) ;

    shy_guts_bind_value ( disappear_pos_angle_periods ) ;
    shy_guts_bind_value_min ( 1 , 1000 ) ;
    shy_guts_bind_value_max ( 1000 , 1 ) ;

    shy_guts_bind_value ( disappear_rubber_first ) ;
    shy_guts_bind_value_min ( 1 , 1000 ) ;
    shy_guts_bind_value_max ( 1000 , 1 ) ;

    shy_guts_bind_value ( disappear_rubber_last ) ;
    shy_guts_bind_value_min ( 1 , 1000 ) ;
    shy_guts_bind_value_max ( 1000 , 1 ) ;

    shy_guts_bind_value ( disappear_duration_in_frames ) ;
    shy_guts_bind_value_min ( 1 ) ;
    shy_guts_bind_value_max ( 1000 ) ;

    shy_guts_bind_value ( scene_scale_min ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( scene_scale_max ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( spin_radius_in_letters ) ;
    shy_guts_bind_value_min ( 1 , 10 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( frames_between_letters ) ;
    shy_guts_bind_value_min ( 1 ) ;
    shy_guts_bind_value_max ( 100 ) ;
}
