void shy_common_logic_salutation_timer_disappear_run_finished_sender :: send ( so_called_common_logic_salutation_timer_disappear_run_finished_message msg )
{
    so_called_common_logic_application_fsm :: receive ( msg ) ;
}
