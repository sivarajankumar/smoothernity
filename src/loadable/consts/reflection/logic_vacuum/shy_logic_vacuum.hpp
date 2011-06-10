#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_vacuum , value )

void shy_loadable_consts_reflection_logic_vacuum :: prepare ( )
{
    shy_guts_bind_module ( logic_vacuum ) ;
    shy_guts_bind_value ( color_r ) ;
    shy_guts_bind_value ( color_g ) ;
    shy_guts_bind_value ( color_b ) ;
}
