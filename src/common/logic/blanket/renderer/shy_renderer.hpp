namespace shy_guts
{
    namespace logic_blanket_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace logic_blanket_mesh_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static void proceed_with_render ( ) ;
    static void render_requested ( ) ;
    static void prepare_render_state ( ) ;
    static void request_blanket_render ( ) ;
    static void reply_render ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_render ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_render_state :: requested ) )
    {
        shy_guts :: logic_blanket_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_mesh_render_state :: replied ) )
    {
        shy_guts :: logic_blanket_mesh_render_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_render ( ) ;
    }
}

void shy_guts :: render_requested ( )
{
    shy_guts :: prepare_render_state ( ) ;
    shy_guts :: request_blanket_render ( ) ;
}

void shy_guts :: prepare_render_state ( )
{
    so_called_sender_common_engine_render_blend_disable :: send ( so_called_message_common_engine_render_blend_disable ( ) ) ;
    so_called_sender_common_engine_render_texture_unselect :: send ( so_called_message_common_engine_render_texture_unselect ( ) ) ;
}

void shy_guts :: request_blanket_render ( )
{
    shy_guts :: logic_blanket_mesh_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_blanket_mesh_render_request :: send ( so_called_message_common_logic_blanket_mesh_render_request ( ) ) ;
}

void shy_guts :: reply_render ( )
{
    so_called_sender_common_logic_blanket_render_reply :: send ( so_called_message_common_logic_blanket_render_reply ( ) ) ;
}

void _shy_common_logic_blanket_renderer :: receive ( so_called_message_common_logic_blanket_mesh_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_mesh_render_state :: requested ) )
    {
        shy_guts :: logic_blanket_mesh_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_blanket_mesh_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_blanket_renderer :: receive ( so_called_message_common_logic_blanket_render_request )
{
    shy_guts :: logic_blanket_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_render ( ) ;
}

void _shy_common_logic_blanket_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

