namespace shy_guts
{
    namespace logic_blanket_animation_fit_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_fract scale ;
    }

    namespace engine_render_aspect_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract width ;
        static so_called_type_platform_math_num_fract height ;
    }

    static void proceed_with_transform ( ) ;
    static void request_aspect_ratio ( ) ;
    static void reply_computed_transform ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_animation_fit > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
}

void shy_guts :: request_aspect_ratio ( )
{
}

void shy_guts :: reply_computed_transform ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_blanket_animation_fit :: receive ( so_called_message_common_engine_render_aspect_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_aspect_state :: requested ) )
    {
        shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_aspect_state :: width = msg . width ;
        shy_guts :: engine_render_aspect_state :: height = msg . height ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_blanket_animation_fit :: receive ( so_called_message_common_logic_blanket_animation_fit_transform_request )
{
    shy_guts :: logic_blanket_animation_fit_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}
