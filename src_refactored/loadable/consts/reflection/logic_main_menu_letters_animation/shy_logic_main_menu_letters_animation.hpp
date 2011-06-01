#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_main_menu_letters_animation_consts :: value \
        )

void shy_loadable_consts_reflection_logic_main_menu_letters_animation :: prepare ( )
{
    shy_bind_module_helper ( logic_main_menu_letters_animation ) ;
    shy_bind_value_helper ( appear_time_from_begin_to_middle_in_seconds ) ;
    shy_bind_value_helper ( appear_time_from_middle_to_end_in_seconds ) ;
    shy_bind_value_helper ( appear_delay_per_col_in_seconds ) ;
    shy_bind_value_helper ( appear_delay_per_row_in_seconds ) ;
    shy_bind_value_helper ( appear_scale_begin ) ;
    shy_bind_value_helper ( appear_scale_middle ) ;
    shy_bind_value_helper ( appear_scale_end ) ;
    shy_bind_value_helper ( disappear_animation_time_in_seconds ) ;
    shy_bind_value_helper ( disappear_time_from_begin_to_end_in_seconds ) ;
    shy_bind_value_helper ( disappear_delay_per_row_in_seconds ) ;
    shy_bind_value_helper ( disappear_delay_per_col_in_seconds ) ;
    shy_bind_value_helper ( disappear_scale_begin ) ;
    shy_bind_value_helper ( disappear_scale_end ) ;
    shy_bind_value_helper ( idle_vertical_shift_period_in_seconds ) ;
    shy_bind_value_helper ( idle_vertical_shift_phase_per_col ) ;
    shy_bind_value_helper ( idle_vertical_shift_phase_per_row ) ;
    shy_bind_value_helper ( idle_vertical_shift_amplitude ) ;
    shy_bind_value_helper ( idle_horizontal_shift_period_in_seconds ) ;
    shy_bind_value_helper ( idle_horizontal_shift_phase_per_row ) ;
    shy_bind_value_helper ( idle_horizontal_shift_amplitude ) ;
    shy_bind_value_helper ( selection_time_stable ) ;
    shy_bind_value_helper ( selection_time_transition ) ;
    shy_bind_value_helper ( selection_scale_min ) ;
    shy_bind_value_helper ( selection_scale_max ) ;
    shy_bind_value_helper ( selection_push_time_from_begin_to_middle ) ;
    shy_bind_value_helper ( selection_push_time_from_middle_to_end ) ;
    shy_bind_value_helper ( selection_push_scale_begin ) ;
    shy_bind_value_helper ( selection_push_scale_middle ) ;
    shy_bind_value_helper ( selection_push_scale_end ) ;
    shy_bind_value_helper ( selection_weight_time_to_begin ) ;
    shy_bind_value_helper ( selection_weight_time_from_begin_to_end ) ;
    shy_bind_value_helper ( unselection_weight_time_to_begin ) ;
    shy_bind_value_helper ( unselection_weight_time_from_begin_to_end ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
