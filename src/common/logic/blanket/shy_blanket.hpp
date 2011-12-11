namespace shy_guts
{
    static so_called_platform_math_num_whole_type created ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_blanket :: receive ( so_called_common_init_message )
{
    shy_guts :: created = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_blanket :: receive ( so_called_common_logic_blanket_creation_permit_message )
{
    so_called_common_logic_blanket_mesh_create_sender :: send ( so_called_common_logic_blanket_mesh_create_message ( ) ) ;
}

void _shy_common_logic_blanket :: receive ( so_called_common_logic_blanket_mesh_creation_finished_message )
{
    shy_guts :: created = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_blanket_creation_finished_sender :: send ( so_called_common_logic_blanket_creation_finished_message ( ) ) ;
}

void _shy_common_logic_blanket :: receive ( so_called_common_logic_blanket_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: created ) )
        so_called_common_logic_blanket_place_sender :: send ( so_called_common_logic_blanket_place_message ( ) ) ;
}

void _shy_common_logic_blanket :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
