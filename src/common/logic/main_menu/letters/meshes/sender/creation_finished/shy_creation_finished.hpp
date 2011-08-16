void shy_sender_common_logic_main_menu_letters_meshes_creation_finished :: send ( so_called_message_common_logic_main_menu_letters_meshes_creation_finished msg )
{
    so_called_common_logic_main_menu :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_meshes_creation_director :: receive ( msg ) ;
}
