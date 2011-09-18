void shy_common_logic_core_near_plane_distance_reply_sender :: send ( so_called_common_logic_core_near_plane_distance_reply_message msg )
{
    so_called_common_logic_camera :: receive ( msg ) ;
    so_called_common_logic_game :: receive ( msg ) ;
}
