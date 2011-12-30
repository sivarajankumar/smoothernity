namespace shy_guts
{
    namespace logic_main_menu_selection_animation_push_weight_state
    {
        static so_called_platform_math_num_fract_type weight ;
    }

    namespace logic_controls_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_whole_type primary_button_down ;
    }

    namespace logic_main_menu_update_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type clicked ;
        static so_called_platform_math_num_fract_type time ;
    }

    static void proceed_with_update ( ) ;
    static void obtain_controls_state ( ) ;
    static void controls_state_received ( ) ;
    static void compute_weight ( ) ;
    static void reply_weight ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_push_weight > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_update ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: requested ) )
    {
        shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_controls_state ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_controls_state :: replied ) )
    {
        shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: controls_state_received ( ) ;
    }
}

void shy_guts :: obtain_controls_state ( )
{
    shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_controls_state_request_sender :: send ( so_called_common_logic_controls_state_request_message ( ) ) ;
}

void shy_guts :: controls_state_received ( )
{
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type time_step ;
    so_called_platform_math_num_whole_type clicked ;
    so_called_platform_math_num_whole_type primary_button_down ;

    time = shy_guts :: logic_main_menu_update_state :: time ;
    clicked = shy_guts :: logic_main_menu_update_state :: clicked ;
    primary_button_down = shy_guts :: logic_controls_state :: primary_button_down ;
    so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;

    if ( so_called_platform_conditions :: whole_is_true ( primary_button_down ) )
        clicked = so_called_platform_math_consts :: whole_true ;

    if ( so_called_platform_conditions :: whole_is_true ( clicked ) )
        so_called_platform_math :: add_to_fract ( time , time_step ) ;

    shy_guts :: logic_main_menu_update_state :: time = time ;
    shy_guts :: logic_main_menu_update_state :: clicked = clicked ;
}

void shy_guts :: compute_weight ( )
{
    so_called_platform_math_num_fract_type time_to_begin ;
    so_called_platform_math_num_fract_type time_from_begin_to_end ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type weight ;
    so_called_platform_math_num_fract_type weight_min ;
    so_called_platform_math_num_fract_type weight_max ;
    
    time = shy_guts :: logic_main_menu_update_state :: time ;
    time_to_begin = so_called_common_logic_main_menu_selection_animation_consts :: push_weight_time_to_begin ;
    time_from_begin_to_end = so_called_common_logic_main_menu_selection_animation_consts :: push_weight_time_from_begin_to_end ;
    weight_min = so_called_common_logic_main_menu_selection_animation_consts :: push_weight_min ;
    weight_max = so_called_common_logic_main_menu_selection_animation_consts :: push_weight_max ;
    
    time_begin = time_to_begin ;
    so_called_platform_math :: add_fracts ( time_end , time_begin , time_from_begin_to_end ) ;

    so_called_common_engine_math_stateless :: easy_in_easy_out
        ( weight
        , time
        , weight_min
        , time_begin
        , weight_max
        , time_end
        ) ;
    
    shy_guts :: logic_main_menu_selection_animation_push_weight_state :: weight = weight ;
}

void shy_guts :: reply_weight ( )
{
    so_called_common_logic_main_menu_selection_animation_push_weight_reply_message msg ;
    msg . weight = shy_guts :: logic_main_menu_selection_animation_push_weight_state :: weight ;
    so_called_common_logic_main_menu_selection_animation_push_weight_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: clicked = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_common_logic_controls_state_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_controls_state :: requested ) )
    {
        shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_controls_state :: primary_button_down = msg . primary_button_down ;
        shy_guts :: proceed_with_update ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_common_logic_main_menu_row_chosen_message )
{
    shy_guts :: logic_main_menu_update_state :: clicked = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_common_logic_main_menu_selection_animation_push_weight_request_message )
{
    shy_guts :: compute_weight ( ) ;
    shy_guts :: reply_weight ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_common_logic_main_menu_update_message )
{
    shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_update ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: receive ( so_called_common_logic_main_menu_void_chosen_message )
{
    shy_guts :: logic_main_menu_update_state :: clicked = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_push_weight :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

