namespace shy_guts
{
    namespace logic_main_menu_letters_animation_selection_push_transform_state
    {
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_fract scale ;
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

    static void proceed_with_transform ( ) ;
    static void proceed_with_update ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
    static void obtain_controls_state ( ) ;
    static void controls_state_received ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_selection_push > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
}

void shy_guts :: proceed_with_update ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void shy_guts :: obtain_controls_state ( )
{
}

void shy_guts :: controls_state_received ( )
{
}

void _shy_common_logic_main_menu_letters_animation_selection_push :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_main_menu_update_state :: clicked = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_selection_push :: receive ( so_called_message_common_logic_controls_state_reply )
{
}

void _shy_common_logic_main_menu_letters_animation_selection_push :: receive ( so_called_message_common_logic_main_menu_letters_animation_selection_push_transform_request )
{
}

void _shy_common_logic_main_menu_letters_animation_selection_push :: receive ( so_called_message_common_logic_main_menu_update )
{
}

void _shy_common_logic_main_menu_letters_animation_selection_push :: receive ( so_called_message_common_logic_main_menu_void_chosen )
{
}
