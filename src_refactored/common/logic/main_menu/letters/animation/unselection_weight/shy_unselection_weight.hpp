namespace shy_guts
{
    namespace logic_main_menu_letters_animation_unselection_weight_state
    {
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole row_unselected ;
        static so_called_type_platform_math_num_whole unselected_row_index ;
        static so_called_type_platform_math_num_fract weight ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_fract time ;
    }

    static void proceed_with_weight ( ) ;
    static void compute_weight ( ) ;
    static void compute_identity_weight ( ) ;
    static void reply_weight ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_unselection_weight > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_weight ( )
{
}

void shy_guts :: compute_weight ( )
{
}

void shy_guts :: compute_identity_weight ( )
{
}

void shy_guts :: reply_weight ( )
{
}

void _shy_common_logic_main_menu_letters_animation_unselection_weight :: receive ( so_called_message_common_logic_main_menu_letters_animation_unselection_weight_request )
{
}

void _shy_common_logic_main_menu_letters_animation_unselection_weight :: receive ( so_called_message_common_logic_main_menu_letters_animation_unselection_weight_select_row )
{
}

void _shy_common_logic_main_menu_letters_animation_unselection_weight :: receive ( so_called_message_common_logic_main_menu_letters_animation_unselection_weight_unselect_row )
{
}

void _shy_common_logic_main_menu_letters_animation_unselection_weight :: receive ( so_called_message_common_logic_main_menu_update )
{
}
