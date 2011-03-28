namespace shy_guts
{
    namespace logic_main_menu_letters_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole row ;
        static so_called_type_platform_math_num_whole col ;
        static so_called_type_platform_matrix_data transform ;
    }

    namespace logic_main_menu_letters_animation_appear_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    namespace logic_main_menu_letters_animation_disappear_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    namespace logic_main_menu_letters_animation_selection_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    namespace logic_main_menu_letters_animation_selection_push_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    namespace logic_main_menu_letters_animation_selection_weight_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract weight ;
    }
    
    namespace logic_main_menu_letters_animation_unselection_weight_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract weight ;
    }
    
    namespace logic_main_menu_letters_animation_idle_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_vector_data position ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    static void proceed_with_transform ( ) ;
    static void obtain_appear_transform ( ) ;
    static void obtain_disappear_transform ( ) ;
    static void obtain_selection_push_transform ( ) ;
    static void obtain_selection_transform ( ) ;
    static void obtain_selection_weight ( ) ;
    static void obtain_unselection_weight ( ) ;
    static void obtain_idle_transform ( ) ;
    static void all_transforms_received ( ) ;
    static void compute_transform ( ) ;
    static void reply_animated_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_appear_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_disappear_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_idle_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_selection_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_selection_push_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_selection_weight ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_unselection_weight ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: all_transforms_received ( ) ;
    }
}

void shy_guts :: obtain_appear_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_message_common_logic_main_menu_letters_animation_appear_transform_request msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_sender_common_logic_main_menu_letters_animation_appear_transform_request :: send ( msg ) ;
}

void shy_guts :: obtain_disappear_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_message_common_logic_main_menu_letters_animation_disappear_transform_request msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_sender_common_logic_main_menu_letters_animation_disappear_transform_request :: send ( msg ) ;
}

void shy_guts :: obtain_selection_push_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_message_common_logic_main_menu_letters_animation_selection_push_transform_request msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_sender_common_logic_main_menu_letters_animation_selection_push_transform_request :: send ( msg ) ;
}

void shy_guts :: obtain_selection_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_message_common_logic_main_menu_letters_animation_selection_transform_request msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_sender_common_logic_main_menu_letters_animation_selection_transform_request :: send ( msg ) ;
}

void shy_guts :: obtain_selection_weight ( )
{
}

void shy_guts :: obtain_unselection_weight ( )
{
}

void shy_guts :: obtain_idle_transform ( )
{
}

void shy_guts :: all_transforms_received ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_animated_transform ( )
{
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_message_common_logic_main_menu_letters_animation_appear_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_message_common_logic_main_menu_letters_animation_disappear_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_message_common_logic_main_menu_letters_animation_idle_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: position = msg . position ;
        shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_message_common_logic_main_menu_letters_animation_selection_push_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_message_common_logic_main_menu_letters_animation_selection_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_message_common_logic_main_menu_letters_animation_selection_weight_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: weight = msg . weight ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_message_common_logic_main_menu_letters_animation_transform_request msg )
{
    shy_guts :: logic_main_menu_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_transform_state :: row = msg . row ;
    shy_guts :: logic_main_menu_letters_animation_transform_state :: col = msg . col ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_message_common_logic_main_menu_letters_animation_unselection_weight_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: weight = msg . weight ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}
