namespace shy_guts
{
    namespace logic_door_animation_appear_transform_state
    {
        static so_called_platform_math_num_fract_type scale ;
    }

    namespace logic_door_update_state
    {
        static so_called_platform_math_num_whole_type started ;
        static so_called_platform_math_num_fract_type time ;
    }

    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_animation_appear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_transform ( )
{
    so_called_platform_math_num_fract_type scale_begin ;
    so_called_platform_math_num_fract_type scale_end ;
    so_called_platform_math_num_fract_type scale ;
    so_called_platform_math_num_fract_type time_from_begin_to_end ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type time ;

    scale_begin = so_called_common_logic_door_animation_consts :: appear_scale_begin ;
    scale_end = so_called_common_logic_door_animation_consts :: appear_scale_end ;
    time_from_begin_to_end = so_called_common_logic_door_animation_consts :: appear_time_from_begin_to_end ;
    time = shy_guts :: logic_door_update_state :: time ;

    time_begin = so_called_platform_math_consts :: fract_0 ;
    time_end = time_from_begin_to_end ;
    
    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( scale
        , time
        , scale_begin
        , time_begin
        , scale_end
        , time_end
        ) ;

    shy_guts :: logic_door_animation_appear_transform_state :: scale = scale ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_door_animation_appear_transform_reply_message msg ;
    msg . scale = shy_guts :: logic_door_animation_appear_transform_state :: scale ;
    so_called_common_logic_door_animation_appear_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_door_update_state :: started = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_door_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_common_logic_door_animation_appear_start_message )
{
    shy_guts :: logic_door_update_state :: started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_door_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_common_logic_door_animation_appear_transform_request_message )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_common_logic_door_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_update_state :: started ) )
    {
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_door_update_state :: time , time_step ) ;
    }
}

void _shy_common_logic_door_animation_appear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

