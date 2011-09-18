void shy_common_engine_render_aspect_reply_sender :: send ( so_called_common_engine_render_aspect_reply_message msg )
{
    so_called_common_logic_blanket_animation_fit :: receive ( msg ) ;
    so_called_common_logic_core :: receive ( msg ) ;
    so_called_common_logic_camera :: receive ( msg ) ;
    so_called_common_logic_fidget :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_layout_position :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_layout_row_rect :: receive ( msg ) ;
    so_called_common_logic_ortho :: receive ( msg ) ;
    so_called_common_logic_perspective :: receive ( msg ) ;
    so_called_common_logic_salutation_letters_animation_layout :: receive ( msg ) ;
}

