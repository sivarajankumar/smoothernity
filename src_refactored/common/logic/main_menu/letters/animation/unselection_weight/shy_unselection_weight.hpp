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

void _shy_common_logic_main_menu_letters_animation_unselection_weight :: receive ( so_called_message_common_logic_main_menu_letters_animation_unselection_weight_request msg )
{
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested_row = msg . row ;
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested_col = msg . col ;
    shy_guts :: proceed_with_weight ( ) ;
}

void _shy_common_logic_main_menu_letters_animation_unselection_weight :: receive ( so_called_message_common_logic_main_menu_letters_animation_unselection_weight_select_row msg )
{
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: row_unselected = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: unselected_row_index = msg . row ;
}

void _shy_common_logic_main_menu_letters_animation_unselection_weight :: receive ( so_called_message_common_logic_main_menu_letters_animation_unselection_weight_unselect_row msg )
{
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: row_unselected = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: unselected_row_index = msg . row ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_unselection_weight :: receive ( so_called_message_common_logic_main_menu_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: row_unselected ) )
    {
        so_called_type_platform_math_num_fract time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}
