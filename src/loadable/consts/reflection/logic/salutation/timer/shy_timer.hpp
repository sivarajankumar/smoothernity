#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_salutation_timer , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_salutation_timer :: prepare ( )
{
    shy_guts_bind_module ( logic_salutation_timer ) ;

    shy_guts_bind_value ( time_appear ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( time_disappear ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;
}
