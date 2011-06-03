#define shy_bind_module_helper(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_bind_value_helper(value) so_called_loadable_consts_binder_helper_value ( logic_amusement , value )

void shy_loadable_consts_reflection_logic_amusement :: prepare ( )
{
    shy_bind_module_helper ( logic_amusement ) ;
    shy_bind_value_helper ( renderer_clear_color_r ) ;
    shy_bind_value_helper ( renderer_clear_color_g ) ;
    shy_bind_value_helper ( renderer_clear_color_b ) ;
}
