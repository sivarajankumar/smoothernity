namespace shy_guts
{
    namespace logic_door_animation_appear_transform_state
    {
        static so_called_type_platform_math_num_fract scale ;
    }

    namespace logic_door_update_state
    {
        static so_called_type_platform_math_num_whole started ;
        static so_called_type_platform_math_num_fract time ;
    }

    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_animation_appear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_door_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_message_common_logic_door_animation_appear_start )
{
    shy_guts :: logic_door_update_state :: started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_door_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_message_common_logic_door_animation_appear_transform_request )
{
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_message_common_logic_door_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_update_state :: started ) )
    {
        so_called_type_platform_math_num_fract time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_door_update_state :: time , time_step ) ;
    }
}
