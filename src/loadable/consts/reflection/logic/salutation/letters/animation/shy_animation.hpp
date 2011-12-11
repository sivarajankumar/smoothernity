#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_salutation_letters_animation , value )
#define shy_guts_bind_value_min so_called_loadable_consts_binder :: bind_value_min
#define shy_guts_bind_value_max so_called_loadable_consts_binder :: bind_value_max

void shy_loadable_consts_reflection_logic_salutation_letters_animation :: prepare ( )
{
    shy_guts_bind_module ( logic_salutation_letters_animation ) ;

    shy_guts_bind_value ( appear_scale_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_scale_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_time ) ;
    shy_guts_bind_value_min ( 1 , 10 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( appear_time_shift_per_letter ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_scale_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_scale_cut_off ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_scale_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_time ) ;
    shy_guts_bind_value_min ( 1 , 10 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( disappear_time_shift_per_letter ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( layout_border_height ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( layout_border_width ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( layout_step ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( roll_in_position_radius_begin ) ;
    shy_guts_bind_value_min ( - 10 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( roll_in_position_radius_end ) ;
    shy_guts_bind_value_min ( - 10 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( roll_in_position_spin_periods_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( roll_in_position_spin_periods_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( roll_in_rotation_periods_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( roll_in_rotation_periods_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( roll_in_time ) ;
    shy_guts_bind_value_min ( 1 , 10 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( roll_in_time_shift_per_letter ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( roll_out_position_radius_begin ) ;
    shy_guts_bind_value_min ( - 10 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( roll_out_position_radius_end ) ;
    shy_guts_bind_value_min ( - 10 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( roll_out_position_spin_periods_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( roll_out_position_spin_periods_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( roll_out_rotation_periods_begin ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( roll_out_rotation_periods_end ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 100 , 1 ) ;

    shy_guts_bind_value ( roll_out_time ) ;
    shy_guts_bind_value_min ( 1 , 10 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;

    shy_guts_bind_value ( roll_out_time_shift_per_letter ) ;
    shy_guts_bind_value_min ( 0 , 1 ) ;
    shy_guts_bind_value_max ( 10 , 1 ) ;
}
