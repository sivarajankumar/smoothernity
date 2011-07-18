namespace shy_guts
{
    static so_called_type_platform_math_num_fract time ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_timer_appear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_timer_appear :: receive ( so_called_message_common_init )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_timer_appear :: receive ( so_called_message_common_logic_salutation_timer_appear_run )
{
    so_called_sender_common_logic_salutation_timer_appear_run_finished :: send ( so_called_message_common_logic_salutation_timer_appear_run_finished ( ) ) ;
}

void _shy_common_logic_salutation_timer_appear :: receive ( so_called_message_common_logic_salutation_timer_update )
{
}

void _shy_common_logic_salutation_timer_appear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

