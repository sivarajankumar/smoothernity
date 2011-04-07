typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_application_fsm > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_application_fsm :: reset_input_events ( )
{
}

void _shy_common_logic_application_fsm :: recalc_current_inputs ( )
{
}

void _shy_common_logic_application_fsm :: determine_inputs_change ( so_called_type_platform_math_num_whole & )
{
}

void _shy_common_logic_application_fsm :: update_fixed_inputs ( )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_amusement_created )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_amusement_finished )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_application_render )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_application_update )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_main_menu_created )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_main_menu_finished )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_text_prepared )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_title_created )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_title_finished )
{
}
