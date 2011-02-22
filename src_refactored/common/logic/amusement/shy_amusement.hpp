typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_amusement > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_amusement :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_amusement_creation_permit )
{
    so_called_sender_common_logic_blanket_creation_permit :: send ( so_called_message_common_logic_blanket_creation_permit ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_amusement_launch_permit )
{
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_amusement_update )
{
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_blanket_animation_appear_finished )
{
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_blanket_animation_disappear_finished )
{
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_blanket_creation_finished )
{
    so_called_sender_common_logic_door_creation_permit :: send ( so_called_message_common_logic_door_creation_permit ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_door_creation_finished )
{
    so_called_sender_common_logic_room_creation_permit :: send ( so_called_message_common_logic_room_creation_permit ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_room_creation_finished )
{
    so_called_sender_common_logic_amusement_created :: send ( so_called_message_common_logic_amusement_created ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_message_common_logic_room_finished )
{
}
