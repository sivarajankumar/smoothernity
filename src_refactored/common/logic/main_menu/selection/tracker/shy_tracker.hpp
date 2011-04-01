namespace shy_guts
{
    namespace logic_main_menu_selection_track_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole current_row ;
        static so_called_type_platform_math_num_whole cursor_in_selection_rect ;
        static so_called_type_platform_math_num_whole cursor_in_prev_selection_rect ;
        static so_called_type_platform_math_num_whole prev_row_is_selected ;
        static so_called_type_platform_math_num_whole prev_selected_row_index ;
        static so_called_type_common_engine_rect prev_selection_rect ;
        static so_called_type_common_engine_rect scaled_prev_selection_rect ;
        static so_called_type_platform_matrix_data transform ;
    }

    namespace logic_main_menu_letters_rows_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole rows ;
    }

    namespace logic_main_menu_letters_layout_row_rect_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_common_engine_rect row_rect ;
    }

    namespace logic_controls_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract cursor_x ;
        static so_called_type_platform_math_num_fract cursor_y ;
    }

    static void proceed_with_track ( ) ;
    static void obtain_controls_state ( ) ;
    static void controls_state_received ( ) ;
    static void obtain_rows_count ( ) ;
    static void obtain_first_row_rect ( ) ;
    static void obtain_current_row_rect ( ) ;
    static void received_row_rect ( ) ;
    static void determine_cursor_in_selection_rect ( ) ;
    static void determine_cursor_in_prev_selection_rect ( ) ;
    static void determine_cursor_in_rect ( so_called_type_platform_math_num_whole & result , so_called_type_common_engine_rect row_rect ) ;
    static void scale_prev_selection_rect ( ) ;
    static void send_row_selected ( ) ;
    static void send_void_selected ( ) ;
    static void send_reply ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_tracker > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_track ( )
{
}

void shy_guts :: obtain_controls_state ( )
{
}

void shy_guts :: controls_state_received ( )
{
}

void shy_guts :: obtain_rows_count ( )
{
}

void shy_guts :: obtain_first_row_rect ( )
{
}

void shy_guts :: obtain_current_row_rect ( )
{
}

void shy_guts :: received_row_rect ( )
{
}

void shy_guts :: determine_cursor_in_selection_rect ( )
{
}

void shy_guts :: determine_cursor_in_prev_selection_rect ( )
{
}

void shy_guts :: determine_cursor_in_rect ( so_called_type_platform_math_num_whole & result , so_called_type_common_engine_rect row_rect )
{
}

void shy_guts :: scale_prev_selection_rect ( )
{
}

void shy_guts :: send_row_selected ( )
{
}

void shy_guts :: send_void_selected ( )
{
}

void shy_guts :: send_reply ( )
{
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_message_common_logic_controls_state_reply )
{
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_message_common_logic_main_menu_letters_layout_row_rect_reply )
{
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_message_common_logic_main_menu_letters_rows_reply )
{
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_message_common_logic_main_menu_selection_track_request )
{
}
