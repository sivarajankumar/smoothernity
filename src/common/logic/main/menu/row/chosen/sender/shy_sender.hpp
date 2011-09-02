void shy_common_logic_main_menu_row_chosen_sender :: send ( so_called_common_logic_main_menu_row_chosen_message msg )
{
    so_called_common_logic_main_menu :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push_weight :: receive ( msg ) ;
}
