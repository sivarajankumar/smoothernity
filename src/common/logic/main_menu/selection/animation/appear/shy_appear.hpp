namespace shy_guts
{
    namespace logic_main_menu_selection_animation_appear_transform_state
    {
        static so_called_type_platform_math_num_fract horizontal_scale ;
        static so_called_type_platform_math_num_fract vertical_scale ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_whole started ;
        static so_called_type_platform_math_num_fract time ;
    }

    static void compute_horizontal_scale ( ) ;
    static void compute_vertical_scale ( ) ;
    static void reply_computed_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_appear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_horizontal_scale ( )
{
    so_called_type_platform_math_num_fract horizontal_scale_time_to_begin ;
    so_called_type_platform_math_num_fract horizontal_scale_time_from_begin_to_end ;
    so_called_type_platform_math_num_fract time_begin ;
    so_called_type_platform_math_num_fract time_end ;
    
    horizontal_scale_time_to_begin = so_called_common_logic_main_menu_selection_animation_consts :: appear_horizontal_scale_time_to_begin ;
    horizontal_scale_time_from_begin_to_end = so_called_common_logic_main_menu_selection_animation_consts :: appear_horizontal_scale_time_from_begin_to_end ;
    
    time_begin = horizontal_scale_time_to_begin ;
    so_called_platform_math :: add_fracts ( time_end , time_begin , horizontal_scale_time_from_begin_to_end ) ;
    
    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: horizontal_scale
        , shy_guts :: logic_main_menu_update_state :: time
        , so_called_common_logic_main_menu_selection_animation_consts :: appear_horizontal_scale_value_begin
        , time_begin
        , so_called_common_logic_main_menu_selection_animation_consts :: appear_horizontal_scale_value_end
        , time_end
        ) ;
}

void shy_guts :: compute_vertical_scale ( )
{
    so_called_type_platform_math_num_fract vertical_scale_time_to_begin ;
    so_called_type_platform_math_num_fract vertical_scale_time_from_begin_to_middle ;
    so_called_type_platform_math_num_fract vertical_scale_time_from_middle_to_end ;
    so_called_type_platform_math_num_fract time_begin ;
    so_called_type_platform_math_num_fract time_middle ;
    so_called_type_platform_math_num_fract time_end ;
    
    vertical_scale_time_to_begin = so_called_common_logic_main_menu_selection_animation_consts :: appear_vertical_scale_time_to_begin ;
    vertical_scale_time_from_begin_to_middle = so_called_common_logic_main_menu_selection_animation_consts :: appear_vertical_scale_time_from_begin_to_middle ;
    vertical_scale_time_from_middle_to_end = so_called_common_logic_main_menu_selection_animation_consts :: appear_vertical_scale_time_from_middle_to_end ;
    
    time_begin = vertical_scale_time_to_begin ;
    so_called_platform_math :: add_fracts ( time_middle , time_begin , vertical_scale_time_from_begin_to_middle ) ;
    so_called_platform_math :: add_fracts ( time_end , time_middle , vertical_scale_time_from_middle_to_end ) ;
    
    so_called_common_engine_math_stateless :: hard_attack_easy_decay
        ( shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: vertical_scale
        , shy_guts :: logic_main_menu_update_state :: time
        , so_called_common_logic_main_menu_selection_animation_consts :: appear_vertical_scale_value_begin
        , time_begin
        , so_called_common_logic_main_menu_selection_animation_consts :: appear_vertical_scale_value_middle
        , time_middle
        , so_called_common_logic_main_menu_selection_animation_consts :: appear_vertical_scale_value_end
        , time_end
        ) ;
}

void shy_guts :: reply_computed_transform ( )
{
    so_called_message_common_logic_main_menu_selection_animation_appear_transform_reply msg ;
    msg . scale_x = shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: horizontal_scale ;
    msg . scale_y = shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: vertical_scale ;
    so_called_sender_common_logic_main_menu_selection_animation_appear_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_main_menu_selection_animation_appear :: receive ( so_called_message_common_logic_main_menu_selection_animation_appear_start )
{
    shy_guts :: logic_main_menu_update_state :: started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_appear :: receive ( so_called_message_common_logic_main_menu_selection_animation_appear_transform_request )
{
    shy_guts :: compute_horizontal_scale ( ) ;
    shy_guts :: compute_vertical_scale ( ) ;
    shy_guts :: reply_computed_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_appear :: receive ( so_called_message_common_logic_main_menu_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: started ) )
    {
        so_called_type_platform_math_num_fract time ;
        so_called_type_platform_math_num_fract time_step ;
        so_called_type_platform_math_num_fract total_animation_time ;
        
        time = shy_guts :: logic_main_menu_update_state :: time ;
        total_animation_time = so_called_common_logic_main_menu_selection_animation_consts :: appear_total_animation_time ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        
        so_called_platform_math :: add_to_fract ( time , time_step ) ;
        
        if ( so_called_platform_conditions :: fract_greater_than_fract ( time , total_animation_time ) )
        {
            shy_guts :: logic_main_menu_update_state :: started = so_called_platform_math_consts :: whole_false ;
            so_called_sender_common_logic_main_menu_selection_animation_appear_finished :: send ( so_called_message_common_logic_main_menu_selection_animation_appear_finished ( ) ) ;
        }

        shy_guts :: logic_main_menu_update_state :: time = time ;
    }
}

void _shy_common_logic_main_menu_selection_animation_appear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

