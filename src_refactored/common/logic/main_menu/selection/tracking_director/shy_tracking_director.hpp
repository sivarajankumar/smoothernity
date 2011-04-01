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
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: appear_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selection_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: unselection_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: first_selection = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_animation_appear_finished )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: appear_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: letters_selection ( ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_animation_select_finished )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selection_animation_in_progress = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_animation_unselect_finished )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: unselection_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected ) )
        shy_guts :: start_selection ( ) ;
    else
        so_called_sender_common_logic_main_menu_selection_animation_idle_void_selected :: send ( so_called_message_common_logic_main_menu_selection_animation_idle_void_selected ( ) ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_track_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_track_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_track_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_track_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_tracking ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_track_row_selected msg )
{
    so_called_type_platform_math_num_whole first_selection ;
    so_called_type_platform_math_num_whole prev_row_selected ;
    
    first_selection = shy_guts :: logic_main_menu_selection_tracking_director_update_state :: first_selection ;
    prev_row_selected = shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selected_row_index = msg . row ;
    
    if ( so_called_platform_conditions :: whole_is_true ( first_selection ) )
        shy_guts :: first_selection ( ) ;
    else if ( so_called_platform_conditions :: whole_is_true ( prev_row_selected ) )
        shy_guts :: start_unselection ( ) ;
    else
        shy_guts :: start_selection ( ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_track_void_selected )
{
    so_called_type_platform_math_num_whole prev_row_selected ;
    
    prev_row_selected = shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected = so_called_platform_math_consts :: whole_false ;
    
    if ( so_called_platform_conditions :: whole_is_true ( prev_row_selected ) )
        shy_guts :: start_unselection ( ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_message_common_logic_main_menu_selection_tracking_director_update )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_tracking ( ) ;
}
