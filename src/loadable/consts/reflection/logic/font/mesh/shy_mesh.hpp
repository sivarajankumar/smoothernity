#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_font_mesh , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_font_mesh :: prepare ( )
{
    shy_guts_bind_module ( logic_font_mesh ) ;

    shy_guts_bind_value ( color_a ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( color_b ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( color_g ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( color_r ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( mesh_size ) ;
    shy_guts_bind_value_min ( 1 , 10 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( time_between_letters_creation ) ;
    shy_guts_bind_value_min ( 1 , 1000 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;
}
