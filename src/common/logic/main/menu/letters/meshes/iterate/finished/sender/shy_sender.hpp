void shy_common_logic_main_menu_letters_meshes_iterate_finished_sender :: send ( so_called_common_logic_main_menu_letters_meshes_iterate_finished_message msg )
{
    so_called_common_logic_main_menu_letters_meshes_renderer :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_meshes_destroyer :: receive ( msg ) ;
}
