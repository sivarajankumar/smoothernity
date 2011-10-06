namespace shy_guts
{
    namespace logic_main_menu_selection_track_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type current_row ;
        static so_called_platform_math_num_whole_type cursor_in_selection_rect ;
        static so_called_platform_math_num_whole_type cursor_in_prev_selection_rect ;
        static so_called_platform_math_num_whole_type prev_row_is_selected ;
        static so_called_platform_math_num_whole_type prev_selected_row_index ;
        static so_called_common_engine_rect_type prev_selection_rect ;
        static so_called_common_engine_rect_type scaled_prev_selection_rect ;
        static so_called_platform_matrix_data_type transform ;
    }

    namespace logic_main_menu_letters_rows_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_whole_type rows ;
    }

    namespace logic_main_menu_letters_layout_row_rect_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_common_engine_rect_type row_rect ;
    }

    namespace logic_controls_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type cursor_x ;
        static so_called_platform_math_num_fract_type cursor_y ;
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
    static void determine_cursor_in_rect ( so_called_platform_math_num_whole_type & result , so_called_common_engine_rect_type row_rect ) ;
    static void scale_prev_selection_rect ( ) ;
    static void send_row_selected ( ) ;
    static void send_void_selected ( ) ;
    static void send_reply ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_tracker > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_track ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_track_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_track_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_controls_state ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_controls_state :: replied ) )
    {
        shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: controls_state_received ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_rows_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_rows_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_first_row_rect ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: received_row_rect ( ) ;
    }
}

void shy_guts :: obtain_controls_state ( )
{
    shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_controls_state_request_sender :: send ( so_called_common_logic_controls_state_request_message ( ) ) ;
}

void shy_guts :: controls_state_received ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_track_state :: prev_row_is_selected ) )
    {
        shy_guts :: determine_cursor_in_prev_selection_rect ( ) ;
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_track_state :: cursor_in_prev_selection_rect ) )
            shy_guts :: send_reply ( ) ;
        else
            shy_guts :: obtain_rows_count ( ) ;
    }
    else
        shy_guts :: obtain_rows_count ( ) ;
}

void shy_guts :: obtain_rows_count ( )
{
    shy_guts :: logic_main_menu_letters_rows_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_letters_rows_request_sender :: send ( so_called_common_logic_main_menu_letters_rows_request_message ( ) ) ;
}

void shy_guts :: obtain_first_row_rect ( )
{
    shy_guts :: logic_main_menu_selection_track_state :: current_row = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: obtain_current_row_rect ( ) ;
}

void shy_guts :: obtain_current_row_rect ( )
{
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row = shy_guts :: logic_main_menu_selection_track_state :: current_row ;

    so_called_common_logic_main_menu_letters_layout_row_rect_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row ;
    so_called_common_logic_main_menu_letters_layout_row_rect_request_sender :: send ( msg ) ;
}

void shy_guts :: received_row_rect ( )
{
    so_called_platform_math_num_whole_type cursor_in_selection_rect ;
    so_called_platform_math_num_whole_type current_row ;
    so_called_platform_math_num_whole_type rows_count ;
    
    shy_guts :: determine_cursor_in_selection_rect ( ) ;
    
    cursor_in_selection_rect = shy_guts :: logic_main_menu_selection_track_state :: cursor_in_selection_rect ;
    current_row = shy_guts :: logic_main_menu_selection_track_state :: current_row ;
    rows_count = shy_guts :: logic_main_menu_letters_rows_state :: rows ;
    
    if ( so_called_platform_conditions :: whole_is_true ( cursor_in_selection_rect ) )
    {
        shy_guts :: send_row_selected ( ) ;
        shy_guts :: send_reply ( ) ;
    }
    else
    {
        so_called_platform_math :: inc_whole ( current_row ) ;
        if ( so_called_platform_conditions :: whole_less_than_whole ( current_row , rows_count ) )
        {
            shy_guts :: logic_main_menu_selection_track_state :: current_row = current_row ;
            shy_guts :: obtain_current_row_rect ( ) ;
        }
        else
        {
            shy_guts :: send_void_selected ( ) ;
            shy_guts :: send_reply ( ) ;
        }
    }
}

void shy_guts :: determine_cursor_in_selection_rect ( )
{
    shy_guts :: determine_cursor_in_rect
        ( shy_guts :: logic_main_menu_selection_track_state :: cursor_in_selection_rect
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect
        ) ;
}

void shy_guts :: determine_cursor_in_prev_selection_rect ( )
{
    shy_guts :: scale_prev_selection_rect ( ) ;
    shy_guts :: determine_cursor_in_rect
        ( shy_guts :: logic_main_menu_selection_track_state :: cursor_in_prev_selection_rect
        , shy_guts :: logic_main_menu_selection_track_state :: scaled_prev_selection_rect
        ) ;
}

void shy_guts :: determine_cursor_in_rect ( so_called_platform_math_num_whole_type & result , so_called_common_engine_rect_type row_rect )
{
    so_called_platform_math_num_fract_type cursor_x ;
    so_called_platform_math_num_fract_type cursor_y ;
    
    cursor_x = shy_guts :: logic_controls_state :: cursor_x ;
    cursor_y = shy_guts :: logic_controls_state :: cursor_y ;
    
    if ( so_called_platform_conditions :: fract_less_than_fract ( cursor_x , row_rect . left ) 
      || so_called_platform_conditions :: fract_less_than_fract ( cursor_y , row_rect . bottom ) 
      || so_called_platform_conditions :: fract_greater_than_fract ( cursor_x , row_rect . right ) 
      || so_called_platform_conditions :: fract_greater_than_fract ( cursor_y , row_rect . top ) 
       )
    {
        result = so_called_platform_math_consts :: whole_false ;
    }
    else
        result = so_called_platform_math_consts :: whole_true ;
}

void shy_guts :: scale_prev_selection_rect ( )
{
    so_called_platform_math_num_fract_type selected_rect_vertical_scale ;
    so_called_platform_math_num_fract_type rect_height ;
    so_called_platform_math_num_fract_type scaled_rect_height ;
    so_called_platform_math_num_fract_type half_scaled_rect_height ;
    so_called_platform_math_num_fract_type y_center ;
    so_called_common_engine_rect_type prev_selection_rect ;
    so_called_common_engine_rect_type scaled_prev_selection_rect ;
    
    selected_rect_vertical_scale = so_called_common_logic_main_menu_selection_consts :: selected_rect_vertical_scale ;
    prev_selection_rect = shy_guts :: logic_main_menu_selection_track_state :: prev_selection_rect ;
    
    so_called_platform_math :: add_fracts ( y_center , prev_selection_rect . top , prev_selection_rect . bottom ) ;
    so_called_platform_math :: div_fract_by ( y_center , so_called_platform_math_consts :: fract_2 ) ;
    
    so_called_platform_math :: sub_fracts ( rect_height , prev_selection_rect . top , prev_selection_rect . bottom ) ;
    so_called_platform_math :: mul_fracts ( scaled_rect_height , rect_height , selected_rect_vertical_scale ) ;
    so_called_platform_math :: div_fracts ( half_scaled_rect_height , scaled_rect_height , so_called_platform_math_consts :: fract_2 ) ;
    
    scaled_prev_selection_rect = prev_selection_rect ;
    so_called_platform_math :: add_fracts ( scaled_prev_selection_rect . top , y_center , half_scaled_rect_height ) ;
    so_called_platform_math :: sub_fracts ( scaled_prev_selection_rect . bottom , y_center , half_scaled_rect_height ) ;
    
    shy_guts :: logic_main_menu_selection_track_state :: scaled_prev_selection_rect = scaled_prev_selection_rect ;
}

void shy_guts :: send_row_selected ( )
{
    so_called_platform_math_num_whole_type prev_row_is_selected ;
    so_called_platform_math_num_whole_type prev_selected_row_index ;
    so_called_platform_math_num_whole_type current_row ;
    so_called_common_engine_rect_type row_rect ;
    
    prev_row_is_selected = shy_guts :: logic_main_menu_selection_track_state :: prev_row_is_selected ;
    prev_selected_row_index = shy_guts :: logic_main_menu_selection_track_state :: prev_selected_row_index ;
    current_row = shy_guts :: logic_main_menu_selection_track_state :: current_row ;
    row_rect = shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect ;
    
    if ( ! so_called_platform_conditions :: whole_is_true ( prev_row_is_selected ) 
      || ! so_called_platform_conditions :: wholes_are_equal ( prev_selected_row_index , current_row )
       )
    {
        prev_row_is_selected = so_called_platform_math_consts :: whole_true ;
        prev_selected_row_index = current_row ;
        
        shy_guts :: logic_main_menu_selection_track_state :: prev_row_is_selected = prev_row_is_selected ;
        shy_guts :: logic_main_menu_selection_track_state :: prev_selected_row_index = prev_selected_row_index ;
        shy_guts :: logic_main_menu_selection_track_state :: prev_selection_rect = row_rect ;

        so_called_common_logic_main_menu_selection_track_row_selected_message msg ;
        msg . row = shy_guts :: logic_main_menu_selection_track_state :: current_row ;
        so_called_common_logic_main_menu_selection_track_row_selected_sender :: send ( msg ) ;        
    }
}

void shy_guts :: send_void_selected ( )
{
    if ( ! so_called_platform_conditions :: whole_is_false ( shy_guts :: logic_main_menu_selection_track_state :: prev_row_is_selected ) )
    {
        shy_guts :: logic_main_menu_selection_track_state :: prev_row_is_selected = so_called_platform_math_consts :: whole_false ;
        so_called_common_logic_main_menu_selection_track_void_selected_sender :: send ( so_called_common_logic_main_menu_selection_track_void_selected_message ( ) ) ;
    }
}

void shy_guts :: send_reply ( )
{
    so_called_common_logic_main_menu_selection_track_reply_sender :: send ( so_called_common_logic_main_menu_selection_track_reply_message ( ) ) ;
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_rows_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_rows_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_track_state :: prev_row_is_selected = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_track_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_common_logic_controls_state_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_controls_state :: requested ) )
    {
        shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_controls_state :: cursor_x = msg . cursor_x ;
        shy_guts :: logic_controls_state :: cursor_y = msg . cursor_y ;
        shy_guts :: proceed_with_track ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_common_logic_main_menu_letters_layout_row_rect_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row , msg . row )
       )
    {
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect = msg . row_rect ;
        shy_guts :: proceed_with_track ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_common_logic_main_menu_letters_rows_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_rows_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_rows_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_rows_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_rows_state :: rows = msg . rows ;
        shy_guts :: proceed_with_track ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_tracker :: receive ( so_called_common_logic_main_menu_selection_track_request_message )
{
    shy_guts :: logic_main_menu_selection_track_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_track ( ) ;
}

void _shy_common_logic_main_menu_selection_tracker :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

