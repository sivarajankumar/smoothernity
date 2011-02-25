namespace shy_guts
{
    namespace logic_blanket_mesh_consts
    {
        static const so_called_type_platform_math_num_whole vertices = so_called_platform_math :: init_num_whole ( 4 ) ;
        static const so_called_type_platform_math_num_whole triangle_strip_indices = so_called_platform_math :: init_num_whole ( 4 ) ;
        static const so_called_type_platform_math_num_whole triangle_fan_indices = so_called_platform_math :: init_num_whole ( 0 ) ;
    }

    namespace logic_blanket_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace engine_render_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole finalized ;
        static so_called_type_common_engine_render_mesh_id mesh ;
    }
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_mesh > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_logic_blanket_mesh_create )
{
}

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_logic_blanket_mesh_render_request )
{
}

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_logic_blanket_mesh_set_transform )
{
}
