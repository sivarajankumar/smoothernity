void shy_common_logic_salutation_timer_update_sender :: send ( so_called_common_logic_salutation_timer_update_message msg )
{
    so_called_common_logic_salutation_timer_appear :: receive ( msg ) ;
    so_called_common_logic_salutation_timer_disappear :: receive ( msg ) ;
}
