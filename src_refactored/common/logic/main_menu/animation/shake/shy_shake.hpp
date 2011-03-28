namespace shy_guts
{
    namespace logic_main_menu_animation_shake_transform_state
    {
        so_called_type_platform_math_num_fract shift_x ;
    }

    namespace logic_main_menu_update_state
    {
        so_called_type_platform_math_num_whole started ;
        so_called_type_platform_math_num_fract time ;
    }

    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_animation_shake > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_main_menu_animation_shake :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_main_menu_update_state :: started = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_animation_shake :: receive ( so_called_message_common_logic_main_menu_animation_shake_transform_request )
{
}

void _shy_common_logic_main_menu_animation_shake :: receive ( so_called_message_common_logic_main_menu_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: started ) )
    {
        so_called_type_platform_math_num_fract time ;
        so_called_type_platform_math_num_fract time_step ;
        so_called_type_platform_math_num_fract time_total ;
        so_called_type_platform_math_num_fract time_to_begin ;
        so_called_type_platform_math_num_fract time_from_begin_to_end ;

        time = shy_guts :: logic_main_menu_update_state :: time ;
        time_to_begin = so_called_common_logic_main_menu_animation_consts :: shake_time_to_begin ;
        time_from_begin_to_end = so_called_common_logic_main_menu_animation_consts :: shake_time_from_begin_to_end ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;

        so_called_platform_math :: add_fracts ( time_total , time_to_begin , time_from_begin_to_end ) ;
        so_called_platform_math :: add_to_fract ( time , time_step ) ;
        if ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_total ) )
            shy_guts :: logic_main_menu_update_state :: started = so_called_platform_math_consts :: whole_false ;

        shy_guts :: logic_main_menu_update_state :: time = time ;
    }
}

void _shy_common_logic_main_menu_animation_shake :: receive ( so_called_message_common_logic_main_menu_void_chosen )
{
}
