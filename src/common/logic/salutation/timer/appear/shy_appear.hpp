namespace shy_guts
{
    static so_called_platform_math_num_fract_type time ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_timer_appear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_timer_appear :: receive ( so_called_common_init_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_timer_appear :: receive ( so_called_common_logic_salutation_timer_appear_run_message )
{
    shy_guts :: time = so_called_common_logic_salutation_timer_consts :: time_appear ;
}

void _shy_common_logic_salutation_timer_appear :: receive ( so_called_common_logic_salutation_timer_update_message )
{
    if ( so_called_platform_conditions :: fract_greater_than_fract ( shy_guts :: time , so_called_platform_math_consts :: fract_0 ) )
    {
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        if ( so_called_platform_conditions :: fract_greater_than_fract ( shy_guts :: time , time_step ) )
            so_called_platform_math :: sub_from_fract ( shy_guts :: time , time_step ) ;
        else
        {
            shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
            so_called_common_logic_salutation_timer_appear_run_finished_sender :: send ( so_called_common_logic_salutation_timer_appear_run_finished_message ( ) ) ;
        }
    }
}

void _shy_common_logic_salutation_timer_appear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
