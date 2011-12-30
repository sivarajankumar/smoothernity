namespace shy_guts
{
    namespace logic_main_menu_letters_animation_selection_weight_state
    {
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type row_selected ;
        static so_called_platform_math_num_whole_type selected_row_index ;
        static so_called_platform_math_num_fract_type weight ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_platform_math_num_fract_type time ;
    }

    static void proceed_with_weight ( ) ;
    static void compute_weight ( ) ;
    static void compute_identity_weight ( ) ;
    static void reply_weight ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_selection_weight > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_weight ( )
{
    so_called_platform_math_num_whole_type row_selected ;
    so_called_platform_math_num_whole_type selected_row_index ;
    so_called_platform_math_num_whole_type requested_row ;
    
    row_selected = shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: row_selected ;
    selected_row_index = shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: selected_row_index ;
    requested_row = shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_row ;
    
    if ( so_called_platform_conditions :: whole_is_true ( row_selected ) )
    {
        if ( so_called_platform_conditions :: wholes_are_equal ( selected_row_index , requested_row ) )
            shy_guts :: compute_weight ( ) ;
        else
            shy_guts :: compute_identity_weight ( ) ;
    }
    else
        shy_guts :: compute_identity_weight ( ) ;

    shy_guts :: reply_weight ( ) ;
}

void shy_guts :: compute_weight ( )
{
    so_called_platform_math_num_fract_type time_to_begin ;
    so_called_platform_math_num_fract_type time_from_begin_to_end ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type weight_begin ;
    so_called_platform_math_num_fract_type weight_end ;
    so_called_platform_math_num_fract_type weight ;
    
    time_to_begin = so_called_common_logic_main_menu_letters_animation_consts :: selection_weight_time_to_begin ;
    time_from_begin_to_end = so_called_common_logic_main_menu_letters_animation_consts :: selection_weight_time_from_begin_to_end ;
    time = shy_guts :: logic_main_menu_update_state :: time ;
    weight_begin = so_called_platform_math_consts :: fract_0 ;
    weight_end = so_called_platform_math_consts :: fract_1 ;
    
    time_begin = time_to_begin ;
    so_called_platform_math :: add_fracts ( time_end , time_begin , time_from_begin_to_end ) ;
    
    so_called_common_engine_math_stateless :: easy_in_easy_out 
        ( weight
        , time
        , weight_begin
        , time_begin
        , weight_end
        , time_end
        ) ;
        
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: weight = weight ;
}

void shy_guts :: compute_identity_weight ( )
{
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: weight = so_called_platform_math_consts :: fract_0 ;
}

void shy_guts :: reply_weight ( )
{
    so_called_common_logic_main_menu_letters_animation_selection_weight_reply_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_col ;
    msg . weight = shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: weight ;
    so_called_common_logic_main_menu_letters_animation_selection_weight_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_letters_animation_selection_weight :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: row_selected = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_selection_weight :: receive ( so_called_common_logic_main_menu_letters_animation_selection_weight_request_message msg )
{
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_row = msg . row ;
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_col = msg . col ;
    shy_guts :: proceed_with_weight ( ) ;
}

void _shy_common_logic_main_menu_letters_animation_selection_weight :: receive ( so_called_common_logic_main_menu_letters_animation_selection_weight_select_row_message msg )
{
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: row_selected = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: selected_row_index = msg . row ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_selection_weight :: receive ( so_called_common_logic_main_menu_letters_animation_selection_weight_unselect_row_message msg )
{
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: row_selected = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: selected_row_index = msg . row ;
}

void _shy_common_logic_main_menu_letters_animation_selection_weight :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: row_selected ) )
    {
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation_selection_weight :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

