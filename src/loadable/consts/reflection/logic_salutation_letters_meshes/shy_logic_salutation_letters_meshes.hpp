#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_salutation_letters_meshes , value )

void shy_loadable_consts_reflection_logic_salutation_letters_meshes :: prepare ( )
{
    shy_guts_bind_module ( logic_salutation_letters_meshes ) ;
    shy_guts_bind_value ( color_a ) ;
    shy_guts_bind_value ( color_b ) ;
    shy_guts_bind_value ( color_g ) ;
    shy_guts_bind_value ( color_r ) ;
    shy_guts_bind_value ( mesh_size ) ;
    shy_guts_bind_value ( time_between_creation ) ;
}
