namespace shy_guts
{
    namespace logic_controls_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole primary_button_down ;
    }

    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole clicked ;
        static so_called_type_platform_math_num_fract time ;
    }

    namespace logic_main_menu_selection_animation_push_transform_state
    {
        static so_called_type_platform_math_num_fract time_begin ;
        static so_called_type_platform_math_num_fract time_middle ;
        static so_called_type_platform_math_num_fract time_end ;
        static so_called_type_platform_math_num_fract vertical_scale ;
        static so_called_type_platform_math_num_fract horizontal_scale ;
    }

    static void proceed_with_update ( ) ;
    static void obtain_controls_state ( ) ;
    static void controls_state_received ( ) ;
    static void calculate_time ( ) ;
    static void calculate_horizontal_scale ( ) ;
    static void calculate_vertical_scale ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_push > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_update ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: requested ) )
    {
        shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_controls_state ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_controls_state :: replied ) )
    {
        shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: controls_state_received ( ) ;
    }
}

void shy_guts :: obtain_controls_state ( )
{
}

void shy_guts :: controls_state_received ( )
{
}

void shy_guts :: calculate_time ( )
{
}

void shy_guts :: calculate_horizontal_scale ( )
{
}

void shy_guts :: calculate_vertical_scale ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_main_menu_update_state :: clicked = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_message_common_logic_controls_state_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_controls_state :: requested ) )
    {
        shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_controls_state :: primary_button_down = msg . primary_button_down ;
        shy_guts :: proceed_with_update ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_message_common_logic_main_menu_selection_animation_push_transform_request )
{
    shy_guts :: calculate_time ( ) ;
    shy_guts :: calculate_vertical_scale ( ) ;
    shy_guts :: calculate_horizontal_scale ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_message_common_logic_main_menu_update )
{
    shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_update ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_message_common_logic_main_menu_void_chosen )
{
    shy_guts :: logic_main_menu_update_state :: clicked = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}
