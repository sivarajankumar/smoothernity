typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_application_fsm > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_application_render )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_application_update )
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
