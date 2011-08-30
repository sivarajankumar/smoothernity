namespace shy_guts
{
    namespace logic_main_menu_selection_animation_disappear_transform_state
    {
        static so_called_type_platform_math_num_fract horizontal_scale ;
        static so_called_type_platform_math_num_fract vertical_scale ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_whole disappear_started ;
        static so_called_type_platform_math_num_fract time ;
    }

    static void compute_horizontal_scale ( ) ;
    static void compute_vertical_scale ( ) ;
    static void reply_computed_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_disappear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_horizontal_scale ( )
{
    so_called_type_platform_math_num_fract horizontal_scale_time_to_begin ;
    so_called_type_platform_math_num_fract horizontal_scale_time_from_begin_to_end ;
    so_called_type_platform_math_num_fract time_begin ;
    so_called_type_platform_math_num_fract time_end ;
    
    horizontal_scale_time_to_begin = so_called_common_logic_main_menu_selection_animation_consts :: disappear_horizontal_scale_time_to_begin ;
    horizontal_scale_time_from_begin_to_end = so_called_common_logic_main_menu_selection_animation_consts :: disappear_horizontal_scale_time_from_begin_to_end ;
    
    time_begin = horizontal_scale_time_to_begin ;
    so_called_platform_math :: add_fracts ( time_end , time_begin , horizontal_scale_time_from_begin_to_end ) ;
    
    so_called_common_engine_math_stateless :: easy_in_hard_out
        ( shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: horizontal_scale
        , shy_guts :: logic_main_menu_update_state :: time
        , so_called_common_logic_main_menu_selection_animation_consts :: disappear_horizontal_scale_value_begin
        , time_begin
        , so_called_common_logic_main_menu_selection_animation_consts :: disappear_horizontal_scale_value_end
        , time_end
        ) ;
}

void shy_guts :: compute_vertical_scale ( )
{
    so_called_type_platform_math_num_fract vertical_scale_time_to_begin ;
    so_called_type_platform_math_num_fract vertical_scale_time_from_begin_to_end ;
    so_called_type_platform_math_num_fract time_begin ;
    so_called_type_platform_math_num_fract time_end ;
    
    vertical_scale_time_to_begin = so_called_common_logic_main_menu_selection_animation_consts :: disappear_vertical_scale_time_to_begin ;
    vertical_scale_time_from_begin_to_end = so_called_common_logic_main_menu_selection_animation_consts :: disappear_vertical_scale_time_from_begin_to_end ;
    
    time_begin = vertical_scale_time_to_begin ;
    so_called_platform_math :: add_fracts ( time_end , time_begin , vertical_scale_time_from_begin_to_end ) ;
    
    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: vertical_scale
        , shy_guts :: logic_main_menu_update_state :: time
        , so_called_common_logic_main_menu_selection_animation_consts :: disappear_vertical_scale_value_begin
        , time_begin
        , so_called_common_logic_main_menu_selection_animation_consts :: disappear_vertical_scale_value_end
        , time_end
        ) ;
}

void shy_guts :: reply_computed_transform ( )
{
    so_called_common_logic_main_menu_selection_animation_disappear_transform_reply_message msg ;
    msg . scale_x = shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: horizontal_scale ;
    msg . scale_y = shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: vertical_scale ;
    so_called_common_logic_main_menu_selection_animation_disappear_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_selection_animation_disappear :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_update_state :: disappear_started = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_disappear :: receive ( so_called_common_logic_main_menu_selection_animation_disappear_start_message )
{
    shy_guts :: logic_main_menu_update_state :: disappear_started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_disappear :: receive ( so_called_common_logic_main_menu_selection_animation_disappear_transform_request_message )
{
    shy_guts :: compute_horizontal_scale ( ) ;
    shy_guts :: compute_vertical_scale ( ) ;
    shy_guts :: reply_computed_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_disappear :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: disappear_started ) )
    {
        so_called_type_platform_math_num_fract time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation_disappear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

