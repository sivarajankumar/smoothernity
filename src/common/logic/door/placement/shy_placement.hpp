typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_placement > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_door_placement :: receive ( so_called_message_common_logic_door_animation_transform_reply msg )
{
    so_called_message_common_logic_door_mesh_set_transform set_transform_msg ;
    set_transform_msg . transform = msg . transform ;
    so_called_sender_common_logic_door_mesh_set_transform :: send ( set_transform_msg ) ;
}

void _shy_common_logic_door_placement :: receive ( so_called_message_common_logic_door_place )
{
    so_called_sender_common_logic_door_animation_transform_request :: send ( so_called_message_common_logic_door_animation_transform_request ( ) ) ;
}

void _shy_common_logic_door_placement :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
