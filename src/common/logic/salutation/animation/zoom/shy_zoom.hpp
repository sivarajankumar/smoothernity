namespace shy_guts
{
    static so_called_type_platform_math_num_fract scale ;
    static so_called_type_platform_math_num_fract time ;
    static so_called_type_platform_math_num_whole enabled ;

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
    shy_guts :: enabled = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_common_logic_salutation_animation_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: enabled ) )
    {
        so_called_type_platform_math_num_fract time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: time , time_step ) ;
    }
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_common_logic_salutation_animation_zoom_play_message )
{
    shy_guts :: enabled = so_called_platform_math_consts :: whole_true ;
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_common_logic_salutation_animation_zoom_transform_request_message )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: send_transform ( ) ;
}

void _shy_common_logic_salutation_animation_zoom :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
