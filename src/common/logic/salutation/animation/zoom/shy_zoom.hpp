namespace shy_guts
{
    static so_called_platform_math_num_fract_type scale ;
    static so_called_platform_math_num_fract_type time ;

    static void compute_transform ( ) ;
    static void send_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_animation_zoom > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_transform ( )
{
    so_called_common_engine_math_stateless :: lerp
        ( shy_guts :: scale
        , shy_guts :: time
        , so_called_common_logic_salutation_animation_consts :: zoom_scale_from
        , so_called_platform_math_consts :: fract_0
        , so_called_common_logic_salutation_animation_consts :: zoom_scale_to
        , so_called_common_logic_salutation_animation_consts :: zoom_time
        ) ;
}

void shy_guts :: send_transform ( )
{
    so_called_common_logic_salutation_animation_zoom_transform_reply_message msg ;
    msg . scale = shy_guts :: scale ;
    so_called_common_logic_salutation_animation_zoom_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_common_init_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_common_logic_salutation_animation_zoom_rewind_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_common_logic_salutation_animation_zoom_transform_request_message )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: send_transform ( ) ;
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_common_logic_salutation_animation_zoom_step_message )
{
    so_called_common_engine_math_stateless :: add_frame_to_time ( shy_guts :: time ) ;
}

void _shy_common_logic_salutation_animation_zoom :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
