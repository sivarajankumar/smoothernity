namespace shy_guts
{
    namespace logic_main_menu_letters_animation_idle_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole row ;
        static so_called_type_platform_math_num_whole col ;
        static so_called_type_platform_vector_data vertical_position_delta ;
        static so_called_type_platform_vector_data horizontal_position_delta ;
        static so_called_type_platform_vector_data position ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    namespace logic_main_menu_letters_layout_position_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_vector_data position ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_whole launch_permitted ;
        static so_called_type_platform_math_num_fract time ;
    }

    static void proceed_with_transform ( ) ;
    static void obtain_layout_position ( ) ;
    static void layout_position_received ( ) ;
    static void compute_horizontal_position_delta ( ) ;
    static void compute_vertical_position_delta ( ) ;
    static void compute_transform ( ) ;
    static void reply_animated_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_idle > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_layout_position ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_position_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_layout_position_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: layout_position_received ( ) ;
    }
}

void shy_guts :: obtain_layout_position ( )
{
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: col ;

    so_called_message_common_logic_main_menu_letters_layout_position_request msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: col ;
    so_called_sender_common_logic_main_menu_letters_layout_position_request :: send ( msg ) ;
}

void shy_guts :: layout_position_received ( )
{
}

void shy_guts :: compute_horizontal_position_delta ( )
{
}

void shy_guts :: compute_vertical_position_delta ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_animated_transform ( )
{
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_message_common_logic_main_menu_launch_permit )
{
    shy_guts :: logic_main_menu_update_state :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_message_common_logic_main_menu_letters_animation_idle_transform_request msg )
{
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row = msg . row ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: col = msg . col ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_message_common_logic_main_menu_letters_layout_position_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_position_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_layout_position_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_layout_position_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_layout_position_state :: position = msg . position ;
        shy_guts :: logic_main_menu_letters_layout_position_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_message_common_logic_main_menu_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: launch_permitted ) )
    {
        so_called_type_platform_math_num_fract time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}
