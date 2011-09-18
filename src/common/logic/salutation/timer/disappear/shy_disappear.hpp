namespace shy_guts
{
    static so_called_platform_math_num_fract_type time ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_timer_disappear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_timer_disappear :: receive ( so_called_common_init_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_timer_disappear :: receive ( so_called_common_logic_salutation_timer_disappear_start_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_timer_disappear :: receive ( so_called_common_logic_salutation_timer_disappear_tick_message )
{
    so_called_common_engine_math_stateless :: add_frame_to_time ( shy_guts :: time ) ;
    if ( so_called_platform_conditions :: fract_greater_than_fract ( shy_guts :: time , so_called_common_logic_salutation_timer_consts :: time_disappear ) )
        so_called_common_logic_salutation_timer_disappear_finished_sender :: send ( so_called_common_logic_salutation_timer_disappear_finished_message ( ) ) ;
}

void _shy_common_logic_salutation_timer_disappear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
