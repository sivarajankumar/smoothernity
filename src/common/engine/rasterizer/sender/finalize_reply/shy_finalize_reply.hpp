void shy_common_engine_rasterizer_finalize_reply_sender :: send ( so_called_common_engine_rasterizer_finalize_reply_message msg )
{
    so_called_common_logic_door_texture :: receive ( msg ) ;
    so_called_common_logic_room_texture :: receive ( msg ) ;
    so_called_common_logic_text :: receive ( msg ) ;
}
