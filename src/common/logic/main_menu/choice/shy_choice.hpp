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
    shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_controls_state_request :: send ( so_called_message_common_logic_controls_state_request ( ) ) ;
}

void shy_guts :: controls_state_received ( )
{
    so_called_type_platform_math_num_whole row_selected ;
    so_called_type_platform_math_num_whole primary_button_down ;
    so_called_type_platform_math_num_whole prev_primary_button_down ;

    row_selected = shy_guts :: logic_main_menu_update_state :: row_selected ;
    primary_button_down = shy_guts :: logic_controls_state :: primary_button_down ;
    prev_primary_button_down = shy_guts :: logic_main_menu_update_state :: prev_primary_button_down ;    

    if ( so_called_platform_conditions :: whole_is_false ( primary_button_down ) 
      && so_called_platform_conditions :: whole_is_true ( prev_primary_button_down )
       )
    {
        if ( so_called_platform_conditions :: whole_is_true ( row_selected ) )
            so_called_sender_common_logic_main_menu_row_chosen :: send ( so_called_message_common_logic_main_menu_row_chosen ( ) ) ;
        else
            so_called_sender_common_logic_main_menu_void_chosen :: send ( so_called_message_common_logic_main_menu_void_chosen ( ) ) ;
    }

    prev_primary_button_down = primary_button_down ;
    shy_guts :: logic_main_menu_update_state :: prev_primary_button_down = prev_primary_button_down ;
}

void _shy_common_logic_main_menu_choice :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: prev_primary_button_down = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_false ;
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

void _shy_common_logic_main_menu_choice :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
