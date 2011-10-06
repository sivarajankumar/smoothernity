namespace shy_guts
{
    namespace logic_main_menu_letters_animation_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type row ;
        static so_called_platform_math_num_whole_type col ;
        static so_called_platform_matrix_data_type transform ;
    }

    namespace logic_main_menu_letters_animation_appear_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale ;
    }
    
    namespace logic_main_menu_letters_animation_disappear_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale ;
    }
    
    namespace logic_main_menu_letters_animation_selection_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale ;
    }
    
    namespace logic_main_menu_letters_animation_selection_push_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale ;
    }
    
    namespace logic_main_menu_letters_animation_selection_weight_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type weight ;
    }
    
    namespace logic_main_menu_letters_animation_unselection_weight_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type weight ;
    }
    
    namespace logic_main_menu_letters_animation_idle_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_vector_data_type position ;
        static so_called_platform_math_num_fract_type scale ;
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

    so_called_common_logic_main_menu_letters_animation_appear_transform_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_common_logic_main_menu_letters_animation_appear_transform_request_sender :: send ( msg ) ;
}

void shy_guts :: obtain_disappear_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_common_logic_main_menu_letters_animation_disappear_transform_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_common_logic_main_menu_letters_animation_disappear_transform_request_sender :: send ( msg ) ;
}

void shy_guts :: obtain_selection_push_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_common_logic_main_menu_letters_animation_selection_push_transform_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_common_logic_main_menu_letters_animation_selection_push_transform_request_sender :: send ( msg ) ;
}

void shy_guts :: obtain_selection_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_common_logic_main_menu_letters_animation_selection_transform_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_common_logic_main_menu_letters_animation_selection_transform_request_sender :: send ( msg ) ;
}

void shy_guts :: obtain_selection_weight ( )
{
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_common_logic_main_menu_letters_animation_selection_weight_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_common_logic_main_menu_letters_animation_selection_weight_request_sender :: send ( msg ) ;
}

void shy_guts :: obtain_unselection_weight ( )
{
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_common_logic_main_menu_letters_animation_unselection_weight_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_common_logic_main_menu_letters_animation_unselection_weight_request_sender :: send ( msg ) ;
}

void shy_guts :: obtain_idle_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;

    so_called_common_logic_main_menu_letters_animation_idle_transform_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    so_called_common_logic_main_menu_letters_animation_idle_transform_request_sender :: send ( msg ) ;
}

void shy_guts :: all_transforms_received ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_animated_transform ( ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_platform_matrix_data_type transform ;
    so_called_platform_vector_data_type position ;
    so_called_platform_math_num_fract_type scale_appear ;
    so_called_platform_math_num_fract_type scale_disappear ;
    so_called_platform_math_num_fract_type scale_selection ;
    so_called_platform_math_num_fract_type scale_selection_push ;
    so_called_platform_math_num_fract_type scale_selection_weighted ;
    so_called_platform_math_num_fract_type scale_idle ;
    so_called_platform_math_num_fract_type scale ;
    so_called_platform_math_num_fract_type weight_selection ;
    so_called_platform_math_num_fract_type weight_unselection ;
    so_called_platform_math_num_fract_type weight ;
    so_called_platform_math_num_fract_type zero ;
    so_called_platform_math_num_fract_type final_selection_scale ;
    
    position = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: position ;
    scale_appear = shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: scale ;
    scale_disappear = shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: scale ;
    scale_idle = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: scale ;
    scale_selection = shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: scale ;
    scale_selection_push = shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: scale ;
    weight_selection = shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: weight ;
    weight_unselection = shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: weight ;
    zero = so_called_platform_math_consts :: fract_0 ;
    
    so_called_platform_math :: mul_fracts ( weight , weight_selection , weight_unselection ) ;
    so_called_platform_math :: mul_fracts ( final_selection_scale , scale_selection , scale_selection_push ) ;
    
    so_called_common_engine_math_stateless :: lerp
        ( scale_selection_weighted
        , weight
        , so_called_platform_math_consts :: fract_1
        , so_called_platform_math_consts :: fract_0
        , final_selection_scale
        , so_called_platform_math_consts :: fract_1
        ) ;
    
    so_called_platform_math :: mul_fracts ( scale , scale_idle , scale_appear ) ;
    so_called_platform_math :: mul_fract_by ( scale , scale_disappear ) ;
    so_called_platform_math :: mul_fract_by ( scale , scale_selection_weighted ) ;
    
    so_called_platform_matrix :: set_origin ( transform , position ) ;
    so_called_platform_matrix :: set_axis_x ( transform , scale , zero , zero ) ;
    so_called_platform_matrix :: set_axis_y ( transform , zero , scale , zero ) ;
    so_called_platform_matrix :: set_axis_z ( transform , zero , zero , scale ) ;
    
    shy_guts :: logic_main_menu_letters_animation_transform_state :: transform = transform ;
}

void shy_guts :: reply_animated_transform ( )
{
    so_called_common_logic_main_menu_letters_animation_transform_reply_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_transform_state :: col ;
    msg . transform = shy_guts :: logic_main_menu_letters_animation_transform_state :: transform ;
    so_called_common_logic_main_menu_letters_animation_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_selection_push_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_selection_weight_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_animation_unselection_weight_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_logic_main_menu_letters_animation_appear_transform_reply_message msg )
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

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_logic_main_menu_letters_animation_disappear_transform_reply_message msg )
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

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_logic_main_menu_letters_animation_idle_transform_reply_message msg )
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

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_logic_main_menu_letters_animation_selection_push_transform_reply_message msg )
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

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_logic_main_menu_letters_animation_selection_transform_reply_message msg )
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

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_logic_main_menu_letters_animation_selection_weight_reply_message msg )
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

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_logic_main_menu_letters_animation_transform_request_message msg )
{
    shy_guts :: logic_main_menu_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_transform_state :: row = msg . row ;
    shy_guts :: logic_main_menu_letters_animation_transform_state :: col = msg . col ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_letters_animation :: receive ( so_called_common_logic_main_menu_letters_animation_unselection_weight_reply_message msg )
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

void _shy_common_logic_main_menu_letters_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
