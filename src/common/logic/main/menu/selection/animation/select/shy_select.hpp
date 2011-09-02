namespace shy_guts
{
    namespace logic_main_menu_selection_animation_select_transform_state
    {
        static so_called_platform_math_num_fract_type horizontal_scale ;
        static so_called_platform_math_num_fract_type vertical_scale ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_platform_math_num_whole_type select_started ;
        static so_called_platform_math_num_fract_type time ;
    }

    static void compute_horizontal_scale ( ) ;
    static void compute_vertical_scale ( ) ;
    static void compute_identity_scale ( ) ;
    static void reply_computed_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_select > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_horizontal_scale ( )
{
    so_called_platform_math_num_fract_type horizontal_scale_time_to_begin ;
    so_called_platform_math_num_fract_type horizontal_scale_time_from_begin_to_end ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_end ;
    
    horizontal_scale_time_to_begin = so_called_common_logic_main_menu_selection_animation_consts :: select_horizontal_scale_time_to_begin ;
    horizontal_scale_time_from_begin_to_end = so_called_common_logic_main_menu_selection_animation_consts :: select_horizontal_scale_time_from_begin_to_end ;
    
    time_begin = horizontal_scale_time_to_begin ;
    so_called_platform_math :: add_fracts ( time_end , time_begin , horizontal_scale_time_from_begin_to_end ) ;
    
    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( shy_guts :: logic_main_menu_selection_animation_select_transform_state :: horizontal_scale
        , shy_guts :: logic_main_menu_update_state :: time
        , so_called_common_logic_main_menu_selection_animation_consts :: select_horizontal_scale_value_begin
        , time_begin
        , so_called_common_logic_main_menu_selection_animation_consts :: select_horizontal_scale_value_end
        , time_end
        ) ;
}

void shy_guts :: compute_vertical_scale ( )
{
    so_called_platform_math_num_fract_type vertical_scale_time_to_begin ;
    so_called_platform_math_num_fract_type vertical_scale_time_from_begin_to_end ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_end ;
    
    vertical_scale_time_to_begin = so_called_common_logic_main_menu_selection_animation_consts :: select_vertical_scale_time_to_begin ;
    vertical_scale_time_from_begin_to_end = so_called_common_logic_main_menu_selection_animation_consts :: select_vertical_scale_time_from_begin_to_end ;
    
    time_begin = vertical_scale_time_to_begin ;
    so_called_platform_math :: add_fracts ( time_end , time_begin , vertical_scale_time_from_begin_to_end ) ;
    
    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( shy_guts :: logic_main_menu_selection_animation_select_transform_state :: vertical_scale
        , shy_guts :: logic_main_menu_update_state :: time
        , so_called_common_logic_main_menu_selection_animation_consts :: select_vertical_scale_value_begin
        , time_begin
        , so_called_common_logic_main_menu_selection_animation_consts :: select_vertical_scale_value_end
        , time_end
        ) ;
}

void shy_guts :: compute_identity_scale ( )
{
    shy_guts :: logic_main_menu_selection_animation_select_transform_state :: vertical_scale = so_called_platform_math_consts :: fract_1 ;
    shy_guts :: logic_main_menu_selection_animation_select_transform_state :: horizontal_scale = so_called_platform_math_consts :: fract_1 ;
}

void shy_guts :: reply_computed_transform ( )
{
    so_called_common_logic_main_menu_selection_animation_select_transform_reply_message msg ;
    msg . scale_x = shy_guts :: logic_main_menu_selection_animation_select_transform_state :: horizontal_scale ;
    msg . scale_y = shy_guts :: logic_main_menu_selection_animation_select_transform_state :: vertical_scale ;
    so_called_common_logic_main_menu_selection_animation_select_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_selection_animation_select :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_update_state :: select_started = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_select :: receive ( so_called_common_logic_main_menu_selection_animation_select_start_message )
{
    shy_guts :: logic_main_menu_update_state :: select_started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_select :: receive ( so_called_common_logic_main_menu_selection_animation_select_transform_request_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: select_started ) )
    {
        shy_guts :: compute_horizontal_scale ( ) ;
        shy_guts :: compute_vertical_scale ( ) ;
    }
    else
        shy_guts :: compute_identity_scale ( ) ;
    shy_guts :: reply_computed_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_select :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: select_started ) )
    {
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math_num_fract_type time ;
        so_called_platform_math_num_fract_type total_animation_time ;
        
        time = shy_guts :: logic_main_menu_update_state :: time ;
        total_animation_time = so_called_common_logic_main_menu_selection_animation_consts :: select_total_animation_time ;
        
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( time , time_step ) ;
        
        if ( so_called_platform_conditions :: fract_greater_than_fract ( time , total_animation_time ) )
        {
            shy_guts :: logic_main_menu_update_state :: select_started = so_called_platform_math_consts :: whole_false ;
            so_called_common_logic_main_menu_selection_animation_select_finished_sender :: send ( so_called_common_logic_main_menu_selection_animation_select_finished_message ( ) ) ;
        }

        shy_guts :: logic_main_menu_update_state :: time = time ;
    }
}

void _shy_common_logic_main_menu_selection_animation_select :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

