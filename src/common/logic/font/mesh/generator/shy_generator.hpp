typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_font_mesh_generator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_font_mesh_generator :: receive ( so_called_common_init_message )
{
}

void _shy_common_logic_font_mesh_generator :: receive ( so_called_common_logic_font_mesh_generator_generate_message )
{
}

void _shy_common_logic_font_mesh_generator :: receive ( so_called_common_logic_font_mesh_generator_update_message )
{
    so_called_common_logic_font_mesh_generator_generate_finished_sender :: send ( so_called_common_logic_font_mesh_generator_generate_finished_message ( ) ) ;
}

void _shy_common_logic_font_mesh_generator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
