#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_main_menu_letters_layout , value )

void shy_loadable_consts_reflection_logic_main_menu_letters_layout :: prepare ( )
{
    shy_guts_bind_module ( logic_main_menu_letters_layout ) ;
    shy_guts_bind_value ( letter_size_fract_horizontal_spacing ) ;
    shy_guts_bind_value ( letter_size_fract_vertical_spacing ) ;
    shy_guts_bind_value ( letter_size_fract_horizontal_border ) ;
    shy_guts_bind_value ( letter_size_fract_vertical_border ) ;
    shy_guts_bind_value ( menu_position_z ) ;
}
