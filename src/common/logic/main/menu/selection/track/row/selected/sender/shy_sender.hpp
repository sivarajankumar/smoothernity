void shy_common_logic_main_menu_selection_track_row_selected_sender :: send ( so_called_common_logic_main_menu_selection_track_row_selected_message msg )
{
    so_called_common_logic_main_menu_selection_tracking_director :: receive ( msg ) ;
}