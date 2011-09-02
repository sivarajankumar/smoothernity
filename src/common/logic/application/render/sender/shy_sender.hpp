void shy_common_logic_application_render_sender :: send ( so_called_common_logic_application_render_message msg )
{
    so_called_common_logic_application_fsm :: receive ( msg ) ;
}
