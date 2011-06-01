#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_main_menu_letters_layout_consts :: value \
        )

void shy_loadable_consts_reflection_logic_main_menu_letters_layout :: prepare ( )
{
    shy_bind_module_helper ( logic_main_menu_letters_layout ) ;
    shy_bind_value_helper ( letter_size_fract_horizontal_spacing ) ;
    shy_bind_value_helper ( letter_size_fract_vertical_spacing ) ;
    shy_bind_value_helper ( letter_size_fract_horizontal_border ) ;
    shy_bind_value_helper ( letter_size_fract_vertical_border ) ;
    shy_bind_value_helper ( menu_position_z ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
