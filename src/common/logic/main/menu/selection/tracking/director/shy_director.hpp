namespace shy_guts
{
    namespace logic_main_menu_selection_tracking_director_update_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type row_selected ;
        static so_called_platform_math_num_whole_type selected_row_index ;
        static so_called_platform_math_num_whole_type first_selection ;
        static so_called_platform_math_num_whole_type appear_animation_in_progress ;
        static so_called_platform_math_num_whole_type selection_animation_in_progress ;
        static so_called_platform_math_num_whole_type unselection_animation_in_progress ;
    }
    
    namespace logic_main_menu_selection_track_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_tracking_director_update_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_tracking_director_update_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: update_received ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_track_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_track_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: place_mesh ( ) ;
    }
}

void shy_guts :: update_received ( )
{
    if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: logic_main_menu_selection_tracking_director_update_state :: appear_animation_in_progress ) 
      && so_called_platform_conditions :: whole_is_false ( shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selection_animation_in_progress ) 
      && so_called_platform_conditions :: whole_is_false ( shy_guts :: logic_main_menu_selection_tracking_director_update_state :: unselection_animation_in_progress )
       )
    {
        shy_guts :: request_track ( ) ;
    }
    else
        shy_guts :: place_mesh ( ) ;
}

void shy_guts :: request_track ( )
{
    shy_guts :: logic_main_menu_selection_track_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_track_request_sender :: send ( so_called_common_logic_main_menu_selection_track_request_message ( ) ) ;
}

void shy_guts :: place_mesh ( )
{
    so_called_common_logic_main_menu_selection_mesh_place_sender :: send ( so_called_common_logic_main_menu_selection_mesh_place_message ( ) ) ;
}

void shy_guts :: first_selection ( )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: first_selection = so_called_platform_math_consts :: whole_false ;
    
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: appear_animation_in_progress = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_appear_start_sender :: send ( so_called_common_logic_main_menu_selection_animation_appear_start_message ( ) ) ;

    shy_guts :: continue_selection ( ) ;
}

void shy_guts :: start_selection ( )
{
    shy_guts :: letters_selection ( ) ;
    shy_guts :: continue_selection ( ) ;
}

void shy_guts :: continue_selection ( )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selection_animation_in_progress = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_select_start_sender :: send ( so_called_common_logic_main_menu_selection_animation_select_start_message ( ) ) ;
    
    so_called_platform_math_num_whole_type selected_row_index ;    
    selected_row_index = shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selected_row_index ;

    so_called_common_logic_main_menu_selection_animation_idle_row_selected_message idle_row_selected_msg ;
    idle_row_selected_msg . row = selected_row_index ;
    so_called_common_logic_main_menu_selection_animation_idle_row_selected_sender :: send ( idle_row_selected_msg ) ;
    
    so_called_common_logic_main_menu_choice_row_selected_sender :: send ( so_called_common_logic_main_menu_choice_row_selected_message ( ) ) ;
}

void shy_guts :: letters_selection ( )
{
    so_called_platform_math_num_whole_type selected_row_index ;    
    selected_row_index = shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selected_row_index ;

    so_called_common_logic_main_menu_letters_animation_selection_weight_select_row_message letter_selection_row_select_msg ;
    letter_selection_row_select_msg . row = selected_row_index ;
    so_called_common_logic_main_menu_letters_animation_selection_weight_select_row_sender :: send ( letter_selection_row_select_msg ) ;

    so_called_common_logic_main_menu_letters_animation_unselection_weight_select_row_message letter_unselection_row_select_msg ;
    letter_unselection_row_select_msg . row = selected_row_index ;
    so_called_common_logic_main_menu_letters_animation_unselection_weight_select_row_sender :: send ( letter_unselection_row_select_msg ) ;
}

void shy_guts :: start_unselection ( )
{
    so_called_platform_math_num_whole_type selected_row_index ;    
    selected_row_index = shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selected_row_index ;

    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: unselection_animation_in_progress = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_unselect_start_sender :: send ( so_called_common_logic_main_menu_selection_animation_unselect_start_message ( ) ) ;

    so_called_common_logic_main_menu_letters_animation_selection_weight_unselect_row_message letter_selection_row_unselect_msg ;
    letter_selection_row_unselect_msg . row = selected_row_index ;
    so_called_common_logic_main_menu_letters_animation_selection_weight_unselect_row_sender :: send ( letter_selection_row_unselect_msg ) ;

    so_called_common_logic_main_menu_letters_animation_unselection_weight_unselect_row_message letter_unselection_row_unselect_msg ;
    letter_unselection_row_unselect_msg . row = selected_row_index ;
    so_called_common_logic_main_menu_letters_animation_unselection_weight_unselect_row_sender :: send ( letter_unselection_row_unselect_msg ) ;

    so_called_common_logic_main_menu_choice_void_selected_sender :: send ( so_called_common_logic_main_menu_choice_void_selected_message ( ) ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_selection_track_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_track_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: appear_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: first_selection = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selection_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: unselection_animation_in_progress = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_common_logic_main_menu_selection_animation_appear_finished_message )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: appear_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: letters_selection ( ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_common_logic_main_menu_selection_animation_select_finished_message )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: selection_animation_in_progress = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_common_logic_main_menu_selection_animation_unselect_finished_message )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: unselection_animation_in_progress = so_called_platform_math_consts :: whole_false ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected ) )
        shy_guts :: start_selection ( ) ;
    else
        so_called_common_logic_main_menu_selection_animation_idle_void_selected_sender :: send ( so_called_common_logic_main_menu_selection_animation_idle_void_selected_message ( ) ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_common_logic_main_menu_selection_track_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_track_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_track_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_track_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_tracking ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_common_logic_main_menu_selection_track_row_selected_message msg )
{
    so_called_platform_math_num_whole_type first_selection ;
    so_called_platform_math_num_whole_type prev_row_selected ;
    
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

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_common_logic_main_menu_selection_track_void_selected_message )
{
    so_called_platform_math_num_whole_type prev_row_selected ;
    
    prev_row_selected = shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected ;
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: row_selected = so_called_platform_math_consts :: whole_false ;
    
    if ( so_called_platform_conditions :: whole_is_true ( prev_row_selected ) )
        shy_guts :: start_unselection ( ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: receive ( so_called_common_logic_main_menu_selection_tracking_director_update_message )
{
    shy_guts :: logic_main_menu_selection_tracking_director_update_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_tracking ( ) ;
}

void _shy_common_logic_main_menu_selection_tracking_director :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

