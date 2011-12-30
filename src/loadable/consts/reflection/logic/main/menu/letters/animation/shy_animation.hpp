#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_main_menu_letters_animation , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_main_menu_letters_animation :: prepare ( )
{
    shy_guts_bind_module ( logic_main_menu_letters_animation ) ;

    shy_guts_bind_value ( appear_time_from_begin_to_middle_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( appear_time_from_middle_to_end_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( appear_delay_per_col_in_seconds ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( appear_delay_per_row_in_seconds ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( appear_scale_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_scale_middle ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_scale_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_animation_time_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_time_from_begin_to_end_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_delay_per_row_in_seconds ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( disappear_delay_per_col_in_seconds ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 1 , 1 ) ;

    shy_guts_bind_value ( disappear_scale_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_scale_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_vertical_shift_period_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_vertical_shift_phase_per_col ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_vertical_shift_phase_per_row ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_vertical_shift_amplitude ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_horizontal_shift_period_in_seconds ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_horizontal_shift_phase_per_row ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( idle_horizontal_shift_amplitude ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_time_stable ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_time_transition ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_scale_min ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_scale_max ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_push_time_from_begin_to_middle ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_push_time_from_middle_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_push_scale_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_push_scale_middle ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_push_scale_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_weight_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( selection_weight_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselection_weight_time_to_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( unselection_weight_time_from_begin_to_end ) ;
    shy_guts_bind_value_min ( 1 , 100 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;
}
