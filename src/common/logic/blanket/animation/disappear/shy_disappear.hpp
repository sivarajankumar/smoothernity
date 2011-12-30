namespace shy_guts
{
    namespace logic_blanket_animation_disappear_transform_state
    {
        static so_called_platform_math_num_fract_type scale ;
        static so_called_platform_math_num_fract_type rotation ;
    }

    namespace logic_blanket_update_state
    {
        static so_called_platform_math_num_whole_type started ;
        static so_called_platform_math_num_fract_type time ;
    }

    static void compute_scale ( ) ;
    static void compute_rotation ( ) ;
    static void reply_transform ( ) ; 
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_animation_disappear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_scale ( )
{
    so_called_platform_math_num_fract_type scale ;
    so_called_platform_math_num_fract_type scale_begin ;
    so_called_platform_math_num_fract_type scale_end ;
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type time_from_begin_to_end ;

    scale_begin = so_called_common_logic_blanket_animation_consts :: disappear_scale_begin ;
    scale_end = so_called_common_logic_blanket_animation_consts :: disappear_scale_end ;
    time_from_begin_to_end = so_called_common_logic_blanket_animation_consts :: disappear_time_from_begin_to_end ;
    time = shy_guts :: logic_blanket_update_state :: time ;

    time_begin = so_called_platform_math_consts :: fract_0 ;
    time_end = time_from_begin_to_end ;

    so_called_common_engine_math_stateless :: lerp ( scale , time , scale_begin , time_begin , scale_end , time_end ) ;

    shy_guts :: logic_blanket_animation_disappear_transform_state :: scale = scale ;
}

void shy_guts :: compute_rotation ( )
{
    so_called_platform_math_num_fract_type rotation ;
    so_called_platform_math_num_fract_type rotation_begin ;
    so_called_platform_math_num_fract_type rotation_end ;
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type time_from_begin_to_end ;

    rotation_begin = so_called_common_logic_blanket_animation_consts :: disappear_rotation_begin ;
    rotation_end = so_called_common_logic_blanket_animation_consts :: disappear_rotation_end ;
    time_from_begin_to_end = so_called_common_logic_blanket_animation_consts :: disappear_time_from_begin_to_end ;
    time = shy_guts :: logic_blanket_update_state :: time ;

    time_begin = so_called_platform_math_consts :: fract_0 ;
    time_end = time_from_begin_to_end ;

    so_called_common_engine_math_stateless :: lerp ( rotation , time , rotation_begin , time_begin , rotation_end , time_end ) ;

    shy_guts :: logic_blanket_animation_disappear_transform_state :: rotation = rotation ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_blanket_animation_disappear_transform_reply_message msg ;
    msg . scale = shy_guts :: logic_blanket_animation_disappear_transform_state :: scale ;
    msg . rotation = shy_guts :: logic_blanket_animation_disappear_transform_state :: rotation ;
    so_called_common_logic_blanket_animation_disappear_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_blanket_animation_disappear :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_blanket_update_state :: started = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_blanket_animation_disappear :: receive ( so_called_common_logic_blanket_animation_disappear_start_message )
{
    shy_guts :: logic_blanket_update_state :: started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_blanket_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_blanket_animation_disappear :: receive ( so_called_common_logic_blanket_animation_disappear_transform_request_message )
{
    shy_guts :: compute_scale ( ) ;
    shy_guts :: compute_rotation ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void _shy_common_logic_blanket_animation_disappear :: receive ( so_called_common_logic_blanket_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_update_state :: started ) )
    {
        so_called_platform_math_num_fract_type time ;
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math_num_fract_type time_from_begin_to_end ;
        so_called_platform_math_num_whole_type started ;

        time = shy_guts :: logic_blanket_update_state :: time ;
        started = shy_guts :: logic_blanket_update_state :: started ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        time_from_begin_to_end = so_called_common_logic_blanket_animation_consts :: disappear_time_from_begin_to_end ;

        so_called_platform_math :: add_to_fract ( time , time_step ) ;

        if ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_from_begin_to_end ) )
        {
            started = so_called_platform_math_consts :: whole_false ;
            so_called_common_logic_blanket_animation_disappear_finished_sender :: send ( so_called_common_logic_blanket_animation_disappear_finished_message ( ) ) ;
        }

        shy_guts :: logic_blanket_update_state :: time = time ;
        shy_guts :: logic_blanket_update_state :: started = started ;
    }
}

void _shy_common_logic_blanket_animation_disappear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
