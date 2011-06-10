namespace shy_guts
{
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_vacuum > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_vacuum :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_vacuum :: receive ( so_called_message_common_logic_vacuum_render )
{
    so_called_message_common_engine_render_clear_screen msg ;
    msg . r = so_called_common_logic_vacuum_consts :: color_r ;
    msg . g = so_called_common_logic_vacuum_consts :: color_g ;
    msg . b = so_called_common_logic_vacuum_consts :: color_b ;
    so_called_sender_common_engine_render_clear_screen :: send ( msg ) ;
}

void _shy_common_logic_vacuum :: receive ( so_called_message_common_logic_vacuum_update )
{
}

void _shy_common_logic_vacuum :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

