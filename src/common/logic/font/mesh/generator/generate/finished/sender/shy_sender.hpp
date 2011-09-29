void shy_common_logic_font_mesh_generator_generate_finished_sender :: send ( so_called_common_logic_font_mesh_generator_generate_finished_message msg )
{
    so_called_common_logic_application_fsm :: receive ( msg ) ;
}
