typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_creation_permit )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_launch_permit )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_row_chosen )
{
}
