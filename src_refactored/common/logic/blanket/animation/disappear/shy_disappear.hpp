namespace shy_guts
{
    namespace logic_blanket_animation_disappear_transform_state
    {
        static so_called_type_platform_math_num_fract scale ;
        static so_called_type_platform_math_num_fract rotation ;
    }

    namespace logic_blanket_update_state
    {
        static so_called_type_platform_math_num_whole started ;
        static so_called_type_platform_math_num_fract time ;
    }

    static void compute_scale ( ) ;
    static void compute_rotation ( ) ;
    static void reply_transform ( ) ; 
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_animation_disappear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_blanket_animation_disappear :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_blanket_animation_disappear :: receive ( so_called_message_common_logic_blanket_animation_disappear_start )
{
}

void _shy_common_logic_blanket_animation_disappear :: receive ( so_called_message_common_logic_blanket_animation_disappear_transform_request )
{
}

void _shy_common_logic_blanket_animation_disappear :: receive ( so_called_message_common_logic_blanket_update )
{
}
