#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_main_menu_animation_consts :: value \
        )

void shy_loadable_consts_reflection_logic_main_menu_animation :: prepare ( )
{
    shy_bind_module_helper ( logic_main_menu_animation ) ;
    shy_bind_value_helper ( shake_time_to_begin ) ;
    shy_bind_value_helper ( shake_time_from_begin_to_end ) ;
    shy_bind_value_helper ( shake_shift_x_amplitude_begin ) ;
    shy_bind_value_helper ( shake_shift_x_amplitude_end ) ;
    shy_bind_value_helper ( shake_shift_x_period_in_seconds ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
