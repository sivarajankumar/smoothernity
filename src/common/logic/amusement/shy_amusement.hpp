typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_amusement > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_amusement :: receive ( so_called_common_logic_amusement_creation_permit_message )
{
    so_called_common_logic_blanket_creation_permit_sender :: send ( so_called_common_logic_blanket_creation_permit_message ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_common_logic_amusement_launch_permit_message )
{
    so_called_common_logic_room_launch_permit_sender :: send ( so_called_common_logic_room_launch_permit_message ( ) ) ;
    so_called_common_logic_blanket_animation_disappear_start_sender :: send ( so_called_common_logic_blanket_animation_disappear_start_message ( ) ) ;
    so_called_common_logic_blanket_place_sender :: send ( so_called_common_logic_blanket_place_message ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_common_logic_amusement_update_message )
{
    so_called_common_logic_blanket_update_sender :: send ( so_called_common_logic_blanket_update_message ( ) ) ;
    so_called_common_logic_door_update_sender :: send ( so_called_common_logic_door_update_message ( ) ) ;
    so_called_common_logic_observer_update_sender :: send ( so_called_common_logic_observer_update_message ( ) ) ;
    so_called_common_logic_room_update_sender :: send ( so_called_common_logic_room_update_message ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_common_logic_blanket_animation_appear_finished_message )
{
    so_called_common_logic_amusement_finished_sender :: send ( so_called_common_logic_amusement_finished_message ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_common_logic_blanket_animation_disappear_finished_message )
{
    so_called_common_logic_door_launch_permit_sender :: send ( so_called_common_logic_door_launch_permit_message ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_common_logic_blanket_creation_finished_message )
{
    so_called_common_logic_door_creation_permit_sender :: send ( so_called_common_logic_door_creation_permit_message ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_common_logic_door_creation_finished_message )
{
    so_called_common_logic_room_creation_permit_sender :: send ( so_called_common_logic_room_creation_permit_message ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_common_logic_room_creation_finished_message )
{
    so_called_common_logic_amusement_created_sender :: send ( so_called_common_logic_amusement_created_message ( ) ) ;
}

void _shy_common_logic_amusement :: receive ( so_called_common_logic_room_finished_message )
{
    so_called_common_logic_blanket_animation_appear_start_sender :: send ( so_called_common_logic_blanket_animation_appear_start_message ( ) ) ;
}

void _shy_common_logic_amusement :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
