#define shy_bind_module_helper(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_bind_value_helper(value) so_called_loadable_consts_binder_helper_value ( logic_application , value )

void shy_loadable_consts_reflection_logic_application :: prepare ( )
{
    shy_bind_module_helper ( logic_application ) ;
    shy_bind_value_helper ( skip_amusement ) ;
    shy_bind_value_helper ( skip_main_menu ) ;
    shy_bind_value_helper ( skip_salutation ) ;
    shy_bind_value_helper ( skip_title ) ;
}
