namespace shy_guts
{
    namespace logic_main_menu_selection_animation_push_weight_state
    {
        static so_called_type_platform_math_num_fract weight ;
    }

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

    static void proceed_with_update ( ) ;
    static void obtain_controls_state ( ) ;
    static void controls_state_received ( ) ;
    static void compute_weight ( ) ;
    static void reply_weight ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_push_weight > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_update ( )
{
}

void shy_guts :: obtain_controls_state ( )
{
}

void shy_guts :: controls_state_received ( )
{
}

void shy_guts :: compute_weight ( )
{
}

void shy_guts :: reply_weight ( )
{
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_message_common_logic_controls_state_reply )
{
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_message_common_logic_main_menu_row_chosen )
{
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_message_common_logic_main_menu_selection_animation_push_weight_request )
{
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_message_common_logic_main_menu_update )
{
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_message_common_logic_main_menu_void_chosen )
{
}
