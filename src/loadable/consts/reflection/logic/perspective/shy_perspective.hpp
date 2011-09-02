#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_perspective , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_perspective :: prepare ( )
{
    shy_guts_bind_module ( logic_perspective ) ;

    shy_guts_bind_value ( z_far_unscaled ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;
}
