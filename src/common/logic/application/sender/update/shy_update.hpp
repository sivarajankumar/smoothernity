void shy_common_logic_application_update_sender :: send ( so_called_common_logic_application_update_message msg )
{
    so_called_common_logic_application_fsm :: receive ( msg ) ;
}
