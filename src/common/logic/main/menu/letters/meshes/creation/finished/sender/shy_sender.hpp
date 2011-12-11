void shy_common_logic_main_menu_letters_meshes_creation_finished_sender :: send ( so_called_common_logic_main_menu_letters_meshes_creation_finished_message msg )
{
    so_called_common_logic_main_menu :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_meshes_creation_director :: receive ( msg ) ;
}
