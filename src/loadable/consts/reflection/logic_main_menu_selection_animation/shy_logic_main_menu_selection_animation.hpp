#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_main_menu_selection_animation , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_main_menu_selection_animation :: prepare ( )
{
    shy_guts_bind_module ( logic_main_menu_selection_animation ) ;

    shy_guts_bind_value ( appear_horizontal_scale_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_horizontal_scale_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_horizontal_scale_value_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_horizontal_scale_value_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_vertical_scale_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_vertical_scale_time_from_begin_to_middle ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_vertical_scale_time_from_middle_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_vertical_scale_value_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_vertical_scale_value_middle ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_vertical_scale_value_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_total_animation_time ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_horizontal_scale_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_horizontal_scale_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_horizontal_scale_value_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_horizontal_scale_value_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_vertical_scale_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_vertical_scale_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_vertical_scale_value_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_vertical_scale_value_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_position_z ) ;
    shy_guts_bind_value_min ( - 10 , 1 ) ;
    shy_guts_bind_value_max ( - 1 , 1 ) ;

    shy_guts_bind_value ( idle_attention_horizontal_scale_min ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_attention_horizontal_scale_max ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_attention_horizontal_scale_period_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_attention_vertical_scale_min ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_attention_vertical_scale_max ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_attention_vertical_scale_period_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_time_from_begin_to_middle ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_time_from_middle_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_horizontal_scale_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_horizontal_scale_middle ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_horizontal_scale_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_vertical_scale_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_vertical_scale_middle ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_vertical_scale_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_attention_horizontal_scale_min ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_attention_horizontal_scale_max ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_attention_vertical_scale_min ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_attention_vertical_scale_max ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_attention_period_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_weight_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_weight_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( push_weight_min ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( push_weight_max ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( select_horizontal_scale_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( select_horizontal_scale_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( select_horizontal_scale_value_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( select_horizontal_scale_value_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( select_vertical_scale_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( select_vertical_scale_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( select_vertical_scale_value_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( select_vertical_scale_value_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( select_total_animation_time ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_horizontal_scale_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_horizontal_scale_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_horizontal_scale_value_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_horizontal_scale_value_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_vertical_scale_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_vertical_scale_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_vertical_scale_value_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_vertical_scale_value_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselect_total_animation_time ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;
}
