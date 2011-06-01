#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_main_menu_selection_animation_consts :: value \
        )

void shy_loadable_consts_reflection_logic_main_menu_selection_animation :: prepare ( )
{
    shy_bind_module_helper ( logic_main_menu_selection_animation ) ;
    shy_bind_value_helper ( appear_horizontal_scale_time_to_begin ) ;
    shy_bind_value_helper ( appear_horizontal_scale_time_from_begin_to_end ) ;
    shy_bind_value_helper ( appear_horizontal_scale_value_begin ) ;
    shy_bind_value_helper ( appear_horizontal_scale_value_end ) ;
    shy_bind_value_helper ( appear_vertical_scale_time_to_begin ) ;
    shy_bind_value_helper ( appear_vertical_scale_time_from_begin_to_middle ) ;
    shy_bind_value_helper ( appear_vertical_scale_time_from_middle_to_end ) ;
    shy_bind_value_helper ( appear_vertical_scale_value_begin ) ;
    shy_bind_value_helper ( appear_vertical_scale_value_middle ) ;
    shy_bind_value_helper ( appear_vertical_scale_value_end ) ;
    shy_bind_value_helper ( appear_total_animation_time ) ;
    shy_bind_value_helper ( disappear_horizontal_scale_time_to_begin ) ;
    shy_bind_value_helper ( disappear_horizontal_scale_time_from_begin_to_end ) ;
    shy_bind_value_helper ( disappear_horizontal_scale_value_begin ) ;
    shy_bind_value_helper ( disappear_horizontal_scale_value_end ) ;
    shy_bind_value_helper ( disappear_vertical_scale_time_to_begin ) ;
    shy_bind_value_helper ( disappear_vertical_scale_time_from_begin_to_end ) ;
    shy_bind_value_helper ( disappear_vertical_scale_value_begin ) ;
    shy_bind_value_helper ( disappear_vertical_scale_value_end ) ;
    shy_bind_value_helper ( idle_position_z ) ;
    shy_bind_value_helper ( idle_attention_horizontal_scale_min ) ;
    shy_bind_value_helper ( idle_attention_horizontal_scale_max ) ;
    shy_bind_value_helper ( idle_attention_horizontal_scale_period_in_seconds ) ;
    shy_bind_value_helper ( idle_attention_vertical_scale_min ) ;
    shy_bind_value_helper ( idle_attention_vertical_scale_max ) ;
    shy_bind_value_helper ( idle_attention_vertical_scale_period_in_seconds ) ;
    shy_bind_value_helper ( push_time_from_begin_to_middle ) ;
    shy_bind_value_helper ( push_time_from_middle_to_end ) ;
    shy_bind_value_helper ( push_horizontal_scale_begin ) ;
    shy_bind_value_helper ( push_horizontal_scale_middle ) ;
    shy_bind_value_helper ( push_horizontal_scale_end ) ;
    shy_bind_value_helper ( push_vertical_scale_begin ) ;
    shy_bind_value_helper ( push_vertical_scale_middle ) ;
    shy_bind_value_helper ( push_vertical_scale_end ) ;
    shy_bind_value_helper ( push_attention_horizontal_scale_min ) ;
    shy_bind_value_helper ( push_attention_horizontal_scale_max ) ;
    shy_bind_value_helper ( push_attention_vertical_scale_min ) ;
    shy_bind_value_helper ( push_attention_vertical_scale_max ) ;
    shy_bind_value_helper ( push_attention_period_in_seconds ) ;
    shy_bind_value_helper ( push_weight_time_to_begin ) ;
    shy_bind_value_helper ( push_weight_time_from_begin_to_end ) ;
    shy_bind_value_helper ( push_weight_min ) ;
    shy_bind_value_helper ( push_weight_max ) ;
    shy_bind_value_helper ( select_horizontal_scale_time_to_begin ) ;
    shy_bind_value_helper ( select_horizontal_scale_time_from_begin_to_end ) ;
    shy_bind_value_helper ( select_horizontal_scale_value_begin ) ;
    shy_bind_value_helper ( select_horizontal_scale_value_end ) ;
    shy_bind_value_helper ( select_vertical_scale_time_to_begin ) ;
    shy_bind_value_helper ( select_vertical_scale_time_from_begin_to_end ) ;
    shy_bind_value_helper ( select_vertical_scale_value_begin ) ;
    shy_bind_value_helper ( select_vertical_scale_value_end ) ;
    shy_bind_value_helper ( select_total_animation_time ) ;
    shy_bind_value_helper ( unselect_horizontal_scale_time_to_begin ) ;
    shy_bind_value_helper ( unselect_horizontal_scale_time_from_begin_to_end ) ;
    shy_bind_value_helper ( unselect_horizontal_scale_value_begin ) ;
    shy_bind_value_helper ( unselect_horizontal_scale_value_end ) ;
    shy_bind_value_helper ( unselect_vertical_scale_time_to_begin ) ;
    shy_bind_value_helper ( unselect_vertical_scale_time_from_begin_to_end ) ;
    shy_bind_value_helper ( unselect_vertical_scale_value_begin ) ;
    shy_bind_value_helper ( unselect_vertical_scale_value_end ) ;
    shy_bind_value_helper ( unselect_total_animation_time ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
