void shy_common_logic_door_update_sender :: send ( so_called_message_common_logic_door_update msg )
{
    so_called_common_logic_door :: receive ( msg ) ;
    so_called_common_logic_door_animation_appear :: receive ( msg ) ;
}
