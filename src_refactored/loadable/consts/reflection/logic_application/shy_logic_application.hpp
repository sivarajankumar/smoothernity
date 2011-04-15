void shy_loadable_consts_reflection_logic_application :: prepare ( )
{
    so_called_loadable_consts_binder :: module ( "logic_application" ) ;
    so_called_loadable_consts_binder :: bind ( "skip_title" , so_called_common_logic_application_consts :: skip_title ) ;
    so_called_loadable_consts_binder :: bind ( "skip_main_menu" , so_called_common_logic_application_consts :: skip_main_menu ) ;
    so_called_loadable_consts_binder :: bind ( "skip_amusement" , so_called_common_logic_application_consts :: skip_amusement ) ;
}
