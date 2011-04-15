void shy_loadable_consts_reflection_logic_ortho :: prepare ( )
{
    so_called_loadable_consts_binder :: module ( "logic_ortho" ) ;
    so_called_loadable_consts_binder :: bind ( "z_near" , so_called_common_logic_ortho_consts :: z_near ) ;
    so_called_loadable_consts_binder :: bind ( "z_far" , so_called_common_logic_ortho_consts :: z_far ) ;
}
