void shy_common_logic_main_menu_letters_rows_reply_sender :: send ( so_called_common_logic_main_menu_letters_rows_reply_message msg )
{
    so_called_common_logic_main_menu_letters_meshes_creator :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_tracker :: receive ( msg ) ;
}