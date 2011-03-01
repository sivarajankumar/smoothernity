namespace shy_guts
{
    namespace logic_door_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace logic_door_mesh_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    namespace logic_door_texture_select_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static void proceed_with_render ( ) ;
    static void render_requested ( ) ;
    static void prepare_render_state ( ) ;
    static void request_mesh_render ( ) ;
    static void request_texture_select ( ) ;
    static void reply_door_render ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_render ( )
{
}

void shy_guts :: render_requested ( )
{
}

void shy_guts :: prepare_render_state ( )
{
}

void shy_guts :: request_mesh_render ( )
{
}

void shy_guts :: request_texture_select ( )
{
}

void shy_guts :: reply_door_render ( )
{
}

void _shy_common_logic_door_renderer :: receive ( so_called_message_common_logic_door_mesh_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_mesh_render_state :: requested ) )
    {
        shy_guts :: logic_door_mesh_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_door_mesh_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_door_renderer :: receive ( so_called_message_common_logic_door_render_request )
{
    shy_guts :: logic_door_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_render ( ) ;
}

void _shy_common_logic_door_renderer :: receive ( so_called_message_common_logic_door_texture_select_reply )
{
}
