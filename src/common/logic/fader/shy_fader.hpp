namespace shy_guts
{
    static so_called_platform_math_num_fract_type time ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_fader > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_fader :: receive ( so_called_common_init_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_fader :: receive ( so_called_common_logic_fader_render_message )
{
    so_called_platform_math_num_fract_type color_r ;
    so_called_platform_math_num_fract_type color_g ;
    so_called_platform_math_num_fract_type color_b ;

    so_called_common_engine_math_stateless :: lerp
        ( color_r
        , shy_guts :: time
        , so_called_common_logic_fader_consts :: color_begin_r
        , so_called_platform_math_consts :: fract_0
        , so_called_common_logic_fader_consts :: color_end_r
        , so_called_common_logic_fader_consts :: fade_time
        ) ;

    so_called_common_engine_math_stateless :: lerp
        ( color_g
        , shy_guts :: time
        , so_called_common_logic_fader_consts :: color_begin_g
        , so_called_platform_math_consts :: fract_0
        , so_called_common_logic_fader_consts :: color_end_g
        , so_called_common_logic_fader_consts :: fade_time
        ) ;

    so_called_common_engine_math_stateless :: lerp
        ( color_b
        , shy_guts :: time
        , so_called_common_logic_fader_consts :: color_begin_b
        , so_called_platform_math_consts :: fract_0
        , so_called_common_logic_fader_consts :: color_end_b
        , so_called_common_logic_fader_consts :: fade_time
        ) ;

    so_called_common_engine_render_clear_screen_message msg ;
    msg . r = color_r ;
    msg . g = color_g ;
    msg . b = color_b ;
    so_called_common_engine_render_clear_screen_sender :: send ( msg ) ;
}

void _shy_common_logic_fader :: receive ( so_called_common_logic_fader_start_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_fader :: receive ( so_called_common_logic_fader_update_message )
{
    so_called_platform_math_num_fract_type fade_time ;
    fade_time = so_called_common_logic_fader_consts :: fade_time ;
    so_called_common_engine_math_stateless :: add_frame_to_time ( shy_guts :: time ) ;
    if ( so_called_platform_conditions :: fract_greater_than_fract ( shy_guts :: time , fade_time ) )
        so_called_common_logic_fader_finished_sender :: send ( so_called_common_logic_fader_finished_message ( ) ) ;
}

void _shy_common_logic_fader :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
