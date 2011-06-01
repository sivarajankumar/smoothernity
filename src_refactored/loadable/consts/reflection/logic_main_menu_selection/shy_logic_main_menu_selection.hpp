#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_main_menu_selection_consts :: value \
        )

void shy_loadable_consts_reflection_logic_main_menu_selection :: prepare ( )
{
    shy_bind_module_helper ( logic_main_menu_selection ) ;
    shy_bind_value_helper ( mesh_size ) ;
    shy_bind_value_helper ( mesh_color_r ) ;
    shy_bind_value_helper ( mesh_color_g ) ;
    shy_bind_value_helper ( mesh_color_b ) ;
    shy_bind_value_helper ( mesh_color_a ) ;
    shy_bind_value_helper ( selected_rect_vertical_scale ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
