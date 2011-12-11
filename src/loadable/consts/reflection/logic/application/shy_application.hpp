#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_application , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_application :: prepare ( )
{
    shy_guts_bind_module ( logic_application ) ;

    shy_guts_bind_value ( skip_amusement ) ;
    shy_guts_bind_value_min ( 0 ) ;
    shy_guts_bind_value_max ( 1 ) ;

    shy_guts_bind_value ( skip_fader ) ;
    shy_guts_bind_value_min ( 0 ) ;
    shy_guts_bind_value_max ( 1 ) ;

    shy_guts_bind_value ( skip_main_menu ) ;
    shy_guts_bind_value_min ( 0 ) ;
    shy_guts_bind_value_max ( 1 ) ;

    shy_guts_bind_value ( skip_salutation ) ;
    shy_guts_bind_value_min ( 0 ) ;
    shy_guts_bind_value_max ( 1 ) ;
}
