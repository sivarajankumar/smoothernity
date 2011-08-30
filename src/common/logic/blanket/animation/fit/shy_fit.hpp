namespace shy_guts
{
    namespace logic_blanket_animation_fit_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_fract_type scale ;
    }

    namespace engine_render_aspect_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type width ;
        static so_called_platform_math_num_fract_type height ;
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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_fit_transform_state :: requested ) )
    {
        shy_guts :: logic_blanket_animation_fit_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_aspect_ratio ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_aspect_state :: replied ) )
    {
        shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_computed_transform ( ) ;
    }
}

void shy_guts :: request_aspect_ratio ( )
{
    shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_render_aspect_request_sender :: send ( so_called_common_engine_render_aspect_request_message ( ) ) ;
}

void shy_guts :: reply_computed_transform ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_platform_math_num_fract_type width ;
    so_called_platform_math_num_fract_type height ;
    so_called_platform_math_num_fract_type scale ;

    width = shy_guts :: engine_render_aspect_state :: width ;
    height = shy_guts :: engine_render_aspect_state :: height ;

    so_called_platform_math :: add_fracts ( scale , width , height ) ;
    so_called_platform_math :: mul_fract_by ( scale , so_called_platform_math_consts :: fract_2 ) ;

    shy_guts :: logic_blanket_animation_fit_transform_state :: scale = scale ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_blanket_animation_fit_transform_reply_message msg ;
    msg . scale = shy_guts :: logic_blanket_animation_fit_transform_state :: scale ;
    so_called_common_logic_blanket_animation_fit_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_blanket_animation_fit :: receive ( so_called_common_engine_render_aspect_reply_message msg )
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

void _shy_common_logic_blanket_animation_fit :: receive ( so_called_common_init_message )
{
    shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_animation_fit_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_blanket_animation_fit :: receive ( so_called_common_logic_blanket_animation_fit_transform_request_message )
{
    shy_guts :: logic_blanket_animation_fit_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_blanket_animation_fit :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
