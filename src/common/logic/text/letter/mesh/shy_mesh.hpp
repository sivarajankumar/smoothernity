typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_text_letter_mesh > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_text_letter_mesh :: receive ( so_called_message_common_logic_text_letter_mesh_create_request )
{
    so_called_sender_common_logic_text_letter_mesh_create_reply :: send ( so_called_message_common_logic_text_letter_mesh_create_reply ( ) ) ;
}

void _shy_common_logic_text_letter_mesh :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

