void shy_common_engine_render_mesh_create_reply_sender :: send ( so_called_common_engine_render_mesh_create_reply_message msg )
{
    so_called_common_logic_blanket_mesh :: receive ( msg ) ;
    so_called_common_logic_door_mesh :: receive ( msg ) ;
    so_called_common_logic_entities :: receive ( msg ) ;
    so_called_common_logic_fidget :: receive ( msg ) ;
    so_called_common_logic_image :: receive ( msg ) ;
    so_called_common_logic_land :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_mesh :: receive ( msg ) ;
    so_called_common_logic_room_mesh :: receive ( msg ) ;
    so_called_common_logic_text :: receive ( msg ) ;
    so_called_common_logic_text_letter_mesh :: receive ( msg ) ;
    so_called_common_logic_touch :: receive ( msg ) ;
}

