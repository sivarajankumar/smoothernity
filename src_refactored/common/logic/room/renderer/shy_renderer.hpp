namespace shy_guts
{
    namespace logic_room_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole render_permitted ;
    }

    namespace logic_room_mesh_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    namespace logic_room_texture_select_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static void proceed_with_render ( ) ;
    static void render_requested ( ) ;
    static void request_texture_select ( ) ;
    static void request_mesh_render ( ) ;
    static void prepare_render_state ( ) ;
    static void reply_room_render ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_render ( )
{
}

void shy_guts :: render_requested ( )
{
}

void shy_guts :: request_texture_select ( )
{
}

void shy_guts :: request_mesh_render ( )
{
}

void shy_guts :: prepare_render_state ( )
{
}

void shy_guts :: reply_room_render ( )
{
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_logic_room_mesh_render_reply )
{
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_logic_room_render_permit )
{
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_logic_room_render_request )
{
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_logic_room_texture_select_reply )
{
}
