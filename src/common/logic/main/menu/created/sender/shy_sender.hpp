void shy_common_logic_main_menu_created_sender :: send ( so_called_common_logic_main_menu_created_message msg )
{
    so_called_common_logic_application_fsm :: receive ( msg ) ;
}