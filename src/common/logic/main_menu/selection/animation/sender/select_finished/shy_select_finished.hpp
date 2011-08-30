void shy_common_logic_main_menu_selection_animation_select_finished_sender :: send ( so_called_common_logic_main_menu_selection_animation_select_finished_message msg )
{
    so_called_common_logic_main_menu_selection_tracking_director :: receive ( msg ) ;
}
