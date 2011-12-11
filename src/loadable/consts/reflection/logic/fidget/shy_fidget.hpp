#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_fidget , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_fidget :: prepare ( )
{
    shy_guts_bind_module ( logic_fidget ) ;

    shy_guts_bind_value ( fidget_size ) ;
    shy_guts_bind_value_min ( 1 , 20 ) ;
    shy_guts_bind_value_max ( 1 , 2 ) ;

    shy_guts_bind_value ( fidget_r ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( fidget_g ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( fidget_b ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( mesh_x ) ;
    shy_guts_bind_value_min ( - 1 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( mesh_y_from_top ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 2 , 1 ) ;

    shy_guts_bind_value ( mesh_z ) ;
    shy_guts_bind_value_min ( - 10 , 1 ) ;
    shy_guts_bind_value_max ( - 1 , 1 ) ;

    shy_guts_bind_value ( angle_delta ) ;
    shy_guts_bind_value_min ( 1 , 1000 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( fidget_edges ) ;
    shy_guts_bind_value_min ( 3 ) ;
    shy_guts_bind_value_max ( 10 ) ;

    shy_guts_bind_value ( scale_in_frames ) ;
    shy_guts_bind_value_min ( 1 ) ;
    shy_guts_bind_value_max ( 1000 ) ;

    shy_guts_bind_value ( should_render_fidget ) ;
    shy_guts_bind_value_min ( 0 ) ;
    shy_guts_bind_value_max ( 1 ) ;
}
