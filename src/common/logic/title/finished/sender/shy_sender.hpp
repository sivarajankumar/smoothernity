void shy_common_logic_title_finished_sender :: send ( so_called_common_logic_title_finished_message msg )
{
    so_called_common_logic_application_fsm :: receive ( msg ) ;
}
