namespace shy_guts
{
    namespace logic_room_texture_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace engine_render_texture_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_common_engine_render_texture_id texture ;
    }

    namespace engine_rasterizer_finalize_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static void proceed_with_creation ( ) ;
    static void request_texture_create ( ) ;
    static void texture_received ( ) ;
    static void rasterizer_finalized ( ) ;
    static void use_texel 
        ( so_called_type_platform_render_texel_data 
        ) ;
    static void draw_cell 
        ( so_called_type_platform_math_num_whole x_left
        , so_called_type_platform_math_num_whole y_bottom
        , so_called_type_platform_math_num_whole x_right
        , so_called_type_platform_math_num_whole y_top
        ) ;
    static void draw_rect 
        ( so_called_type_platform_math_num_whole x1
        , so_called_type_platform_math_num_whole y1
        , so_called_type_platform_math_num_whole x2
        , so_called_type_platform_math_num_whole y2
        ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room_texture > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_texture_create_state :: requested ) )
    {
        shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_texture_create ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_texture_create_state :: replied ) )
    {
        shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_received ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_rasterizer_finalize_state :: replied ) )
    {
        shy_guts :: engine_rasterizer_finalize_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: rasterizer_finalized ( ) ;
    }
}

void shy_guts :: request_texture_create ( )
{
    shy_guts :: engine_render_texture_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_engine_render_texture_create_request :: send ( so_called_message_common_engine_render_texture_create_request ( ) ) ;
}

void shy_guts :: texture_received ( )
{
}

void shy_guts :: rasterizer_finalized ( )
{
}

void shy_guts :: use_texel ( so_called_type_platform_render_texel_data )
{
}

void shy_guts :: draw_cell 
    ( so_called_type_platform_math_num_whole x_left
    , so_called_type_platform_math_num_whole y_bottom
    , so_called_type_platform_math_num_whole x_right
    , so_called_type_platform_math_num_whole y_top
    )
{
}

void shy_guts :: draw_rect 
    ( so_called_type_platform_math_num_whole x1
    , so_called_type_platform_math_num_whole y1
    , so_called_type_platform_math_num_whole x2
    , so_called_type_platform_math_num_whole y2
    )
{
}

void _shy_common_logic_room_texture :: receive ( so_called_message_common_engine_rasterizer_finalize_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_rasterizer_finalize_state :: requested ) )
    {
        shy_guts :: engine_rasterizer_finalize_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_rasterizer_finalize_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room_texture :: receive ( so_called_message_common_engine_render_texture_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_texture_create_state :: requested ) )
    {
        shy_guts :: engine_render_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_texture_create_state :: texture = msg . texture ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room_texture :: receive ( so_called_message_common_logic_room_texture_create )
{
    shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_room_texture :: receive ( so_called_message_common_logic_room_texture_select_request )
{
    so_called_message_common_engine_render_texture_select msg ;
    msg . texture = shy_guts :: engine_render_texture_create_state :: texture ;
    so_called_sender_common_engine_render_texture_select :: send ( msg ) ;

    so_called_sender_common_logic_room_texture_select_reply :: send ( so_called_message_common_logic_room_texture_select_reply ( ) ) ;
}
