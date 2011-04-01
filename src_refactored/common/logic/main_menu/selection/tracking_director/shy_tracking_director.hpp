namespace shy_guts
{
    namespace logic_main_menu_selection_tracking_director_update_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole row_selected ;
        static so_called_type_platform_math_num_whole selected_row_index ;
        static so_called_type_platform_math_num_whole first_selection ;
        static so_called_type_platform_math_num_whole appear_animation_in_progress ;
        static so_called_type_platform_math_num_whole selection_animation_in_progress ;
        static so_called_type_platform_math_num_whole unselection_animation_in_progress ;
    }
    
    namespace logic_main_menu_selection_track_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static void proceed_with_tracking ( ) ;
    static void update_received ( ) ;
    static void request_track ( ) ;
    static void place_mesh ( ) ;
    static void first_selection ( ) ;
    static void start_selection ( ) ;
    static void continue_selection ( ) ;
    static void letters_selection ( ) ;
    static void start_unselection ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_tracking_director > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_tracking ( )
{
}

void shy_guts :: update_received ( )
{
}

void shy_guts :: request_track ( )
{
}

void shy_guts :: place_mesh ( )
{
}

void shy_guts :: first_selection ( )
{
}

void shy_guts :: start_selection ( )
{
}

void shy_guts :: continue_selection ( )
{
}

void shy_guts :: letters_selection ( )
{
}

void shy_guts :: start_unselection ( )
{
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_animation_appear_finished )
{
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_animation_select_finished )
{
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_animation_unselect_finished )
{
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_track_reply )
{
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_track_row_selected )
{
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_track_void_selected )
{
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_tracking_director_update )
{
}
