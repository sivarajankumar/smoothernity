namespace shy_guts
{
    namespace logic_door_texture_create_state
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
    static void texture_created ( ) ;
    static void fill_texture_contents ( ) ;
    static void finalize_texture ( ) ;
    static void reply_door_texture_created ( ) ;
    static void request_rasterizer_finalize ( ) ;
    static void rasterizer_finalized ( ) ;
    static void use_texel 
        ( so_called_type_platform_render_texel_data 
        ) ;
    static void draw_rect 
        ( so_called_type_platform_math_num_whole x1 
        , so_called_type_platform_math_num_whole y1 
        , so_called_type_platform_math_num_whole x2 
        , so_called_type_platform_math_num_whole y2 
        ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_texture > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
}

void shy_guts :: request_texture_create ( )
{
}

void shy_guts :: texture_created ( )
{
}

void shy_guts :: fill_texture_contents ( )
{
}

void shy_guts :: finalize_texture ( )
{
}

void shy_guts :: reply_door_texture_created ( )
{
}

void shy_guts :: request_rasterizer_finalize ( )
{
}

void shy_guts :: rasterizer_finalized ( )
{
}

void shy_guts :: use_texel ( so_called_type_platform_render_texel_data )
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

void _shy_common_logic_door_texture :: receive ( so_called_message_common_engine_rasterizer_finalize_reply )
{
}

void _shy_common_logic_door_texture :: receive ( so_called_message_common_engine_render_texture_create_reply )
{
}

void _shy_common_logic_door_texture :: receive ( so_called_message_common_logic_door_texture_create )
{
}

void _shy_common_logic_door_texture :: receive ( so_called_message_common_logic_door_texture_select_request )
{
}
