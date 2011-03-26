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
        static so_called_type_platform_math_num_whole prev_primary_button_down ;
        static so_called_type_platform_math_num_whole row_selected ;
    }

    static void proceed_with_update ( ) ;
    static void obtain_controls_state ( ) ;
    static void controls_state_received ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_choice > _scheduled_context_type ;
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

void _shy_common_logic_main_menu_choice :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_main_menu_update_state :: prev_primary_button_down = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_choice :: receive ( so_called_message_common_logic_controls_state_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_controls_state :: requested ) )
    {
        shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_controls_state :: primary_button_down = msg . primary_button_down ;
        shy_guts :: proceed_with_update ( ) ;
    }
}

void _shy_common_logic_main_menu_choice :: receive ( so_called_message_common_logic_main_menu_choice_row_selected )
{
    shy_guts :: logic_main_menu_update_state :: row_selected = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_main_menu_choice :: receive ( so_called_message_common_logic_main_menu_choice_void_selected )
{
    shy_guts :: logic_main_menu_update_state :: row_selected = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_choice :: receive ( so_called_message_common_logic_main_menu_update )
{
    shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_update ( ) ;
}
