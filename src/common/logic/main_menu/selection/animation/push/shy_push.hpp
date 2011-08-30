namespace shy_guts
{
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

    namespace logic_main_menu_selection_animation_push_transform_state
    {
        static so_called_platform_math_num_fract_type time_begin ;
        static so_called_platform_math_num_fract_type time_middle ;
        static so_called_platform_math_num_fract_type time_end ;
        static so_called_platform_math_num_fract_type vertical_scale ;
        static so_called_platform_math_num_fract_type horizontal_scale ;
    }

    static void proceed_with_update ( ) ;
    static void obtain_controls_state ( ) ;
    static void controls_state_received ( ) ;
    static void calculate_time ( ) ;
    static void calculate_horizontal_scale ( ) ;
    static void calculate_vertical_scale ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_push > _scheduled_context_type ;
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

void shy_guts :: calculate_time ( )
{
    so_called_platform_math_num_fract_type time_from_begin_to_middle ;
    so_called_platform_math_num_fract_type time_from_middle_to_end ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_middle ;
    so_called_platform_math_num_fract_type time_end ;
    
    time_from_begin_to_middle = so_called_common_logic_main_menu_selection_animation_consts :: push_time_from_begin_to_middle ;
    time_from_middle_to_end = so_called_common_logic_main_menu_selection_animation_consts :: push_time_from_middle_to_end ;

    time_begin = so_called_platform_math_consts :: fract_0 ;
    time_middle = time_from_begin_to_middle ;
    so_called_platform_math :: add_fracts ( time_end , time_middle , time_from_middle_to_end ) ;
    
    shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_begin = time_begin ;
    shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_middle = time_middle ;
    shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_end = time_end ;
}

void shy_guts :: calculate_horizontal_scale ( )
{
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_middle ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type horizontal_scale_begin ;
    so_called_platform_math_num_fract_type horizontal_scale_middle ;
    so_called_platform_math_num_fract_type horizontal_scale_end ;
    so_called_platform_math_num_fract_type horizontal_scale ;

    time_begin = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_begin ;
    time_middle = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_middle ;
    time_end = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_end ;
    time = shy_guts :: logic_main_menu_update_state :: time ;
    horizontal_scale_begin = so_called_common_logic_main_menu_selection_animation_consts :: push_horizontal_scale_begin ;
    horizontal_scale_middle = so_called_common_logic_main_menu_selection_animation_consts :: push_horizontal_scale_middle ;
    horizontal_scale_end = so_called_common_logic_main_menu_selection_animation_consts :: push_horizontal_scale_end ;

    so_called_common_engine_math_stateless :: hard_attack_easy_decay
        ( horizontal_scale
        , time
        , horizontal_scale_begin
        , time_begin
        , horizontal_scale_middle
        , time_middle
        , horizontal_scale_end
        , time_end
        ) ;

    shy_guts :: logic_main_menu_selection_animation_push_transform_state :: horizontal_scale = horizontal_scale ;
}

void shy_guts :: calculate_vertical_scale ( )
{
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_middle ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type vertical_scale_begin ;
    so_called_platform_math_num_fract_type vertical_scale_middle ;
    so_called_platform_math_num_fract_type vertical_scale_end ;
    so_called_platform_math_num_fract_type vertical_scale ;

    time_begin = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_begin ;
    time_middle = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_middle ;
    time_end = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: time_end ;
    time = shy_guts :: logic_main_menu_update_state :: time ;
    vertical_scale_begin = so_called_common_logic_main_menu_selection_animation_consts :: push_vertical_scale_begin ;
    vertical_scale_middle = so_called_common_logic_main_menu_selection_animation_consts :: push_vertical_scale_middle ;
    vertical_scale_end = so_called_common_logic_main_menu_selection_animation_consts :: push_vertical_scale_end ;

    so_called_common_engine_math_stateless :: hard_attack_easy_decay
        ( vertical_scale
        , time
        , vertical_scale_begin
        , time_begin
        , vertical_scale_middle
        , time_middle
        , vertical_scale_end
        , time_end
        ) ;

    shy_guts :: logic_main_menu_selection_animation_push_transform_state :: vertical_scale = vertical_scale ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_main_menu_selection_animation_push_transform_reply_message msg ;
    msg . scale_x = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: horizontal_scale ;
    msg . scale_y = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: vertical_scale ;
    so_called_common_logic_main_menu_selection_animation_push_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: clicked = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_common_logic_controls_state_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_controls_state :: requested ) )
    {
        shy_guts :: logic_controls_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_controls_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_controls_state :: primary_button_down = msg . primary_button_down ;
        shy_guts :: proceed_with_update ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_common_logic_main_menu_selection_animation_push_transform_request_message )
{
    shy_guts :: calculate_time ( ) ;
    shy_guts :: calculate_vertical_scale ( ) ;
    shy_guts :: calculate_horizontal_scale ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_common_logic_main_menu_update_message )
{
    shy_guts :: logic_main_menu_update_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_update ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_push :: receive ( so_called_common_logic_main_menu_void_chosen_message )
{
    shy_guts :: logic_main_menu_update_state :: clicked = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_push :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
