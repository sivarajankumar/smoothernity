void shy_common_logic_controls_state_reply_sender :: send ( so_called_common_logic_controls_state_reply_message msg )
{
    so_called_common_logic_main_menu_choice :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_selection_push :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push_weight :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_tracker :: receive ( msg ) ;
}
