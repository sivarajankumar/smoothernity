void shy_sender_common_engine_render_texture_create_reply :: send ( so_called_message_common_engine_render_texture_create_reply msg )
{
    so_called_common_logic_door_texture :: receive ( msg ) ;
    so_called_common_logic_image :: receive ( msg ) ;
    so_called_common_logic_land :: receive ( msg ) ;
    so_called_common_logic_room_texture :: receive ( msg ) ;
    so_called_common_logic_text :: receive ( msg ) ;
}

