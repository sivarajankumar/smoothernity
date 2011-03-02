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
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_message_common_logic_door_animation_appear_start )
{
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_message_common_logic_door_animation_appear_transform_request )
{
}

void _shy_common_logic_door_animation_appear :: receive ( so_called_message_common_logic_door_update )
{
}
