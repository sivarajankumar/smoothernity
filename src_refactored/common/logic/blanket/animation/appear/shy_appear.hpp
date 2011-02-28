namespace shy_guts
{
    namespace logic_blanket_animation_appear_transform_state
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

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_animation_appear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_scale ( )
{
}

void shy_guts :: compute_rotation ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_blanket_animation_appear :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_blanket_update_state :: started = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_blanket_animation_appear :: receive ( so_called_message_common_logic_blanket_animation_appear_start )
{
    shy_guts :: logic_blanket_update_state :: started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_blanket_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_blanket_animation_appear :: receive ( so_called_message_common_logic_blanket_animation_appear_transform_request )
{
}

void _shy_common_logic_blanket_animation_appear :: receive ( so_called_message_common_logic_blanket_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_update_state :: started ) )
    {
        so_called_type_platform_math_num_fract time ;
        so_called_type_platform_math_num_fract time_step ;
        so_called_type_platform_math_num_fract time_from_begin_to_end ;
        so_called_type_platform_math_num_whole started ;

        time = shy_guts :: logic_blanket_update_state :: time ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        time_from_begin_to_end = so_called_common_logic_blanket_animation_consts :: appear_time_from_begin_to_end ;
        started = shy_guts :: logic_blanket_update_state :: started ;

        so_called_platform_math :: add_to_fract ( time , time_step ) ;
        if ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_from_begin_to_end ) )
        {
            started = so_called_platform_math_consts :: whole_false ;
            so_called_sender_common_logic_blanket_animation_appear_finished :: send ( so_called_message_common_logic_blanket_animation_appear_finished ( ) ) ;
        }

        shy_guts :: logic_blanket_update_state :: started = started ;
        shy_guts :: logic_blanket_update_state :: time = time ;
    }
}
