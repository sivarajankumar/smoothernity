#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_amusement , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_amusement :: prepare ( )
{
    shy_guts_bind_module ( logic_amusement ) ;

    shy_guts_bind_value ( renderer_clear_color_r ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( renderer_clear_color_g ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( renderer_clear_color_b ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;
}
