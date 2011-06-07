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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_render_state :: requested ) )
    {
        shy_guts :: logic_room_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_texture_select_state :: replied ) )
    {
        shy_guts :: logic_room_texture_select_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_mesh_render ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_mesh_render_state :: replied ) )
    {
        shy_guts :: logic_room_mesh_render_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_room_render ( ) ;
    }
}

void shy_guts :: render_requested ( )
{
    shy_guts :: prepare_render_state ( ) ;
    shy_guts :: request_texture_select ( ) ;
}

void shy_guts :: request_texture_select ( )
{
    shy_guts :: logic_room_texture_select_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_room_texture_select_request :: send ( so_called_message_common_logic_room_texture_select_request ( ) ) ;
}

void shy_guts :: request_mesh_render ( )
{
    shy_guts :: logic_room_mesh_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_room_mesh_render_request :: send ( so_called_message_common_logic_room_mesh_render_request ( ) ) ;
}

void shy_guts :: prepare_render_state ( )
{
    so_called_sender_common_engine_render_texture_unselect :: send ( so_called_message_common_engine_render_texture_unselect ( ) ) ;
    so_called_sender_common_engine_render_blend_disable :: send ( so_called_message_common_engine_render_blend_disable ( ) ) ;
    so_called_sender_common_engine_render_disable_depth_test :: send ( so_called_message_common_engine_render_disable_depth_test ( ) ) ;
}

void shy_guts :: reply_room_render ( )
{
    so_called_sender_common_logic_room_render_reply :: send ( so_called_message_common_logic_room_render_reply ( ) ) ;
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_logic_room_mesh_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_mesh_render_state :: requested ) )
    {
        shy_guts :: logic_room_mesh_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_room_mesh_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_logic_room_render_permit )
{
    shy_guts :: logic_room_render_state :: render_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_logic_room_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_render_state :: render_permitted ) )
    {        
        shy_guts :: logic_room_render_state :: requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_room_renderer :: receive ( so_called_message_common_logic_room_texture_select_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_texture_select_state :: requested ) )
    {
        shy_guts :: logic_room_texture_select_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_room_texture_select_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_room_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
