namespace shy_guts
{
    namespace logic_main_menu_letters_animation_selection_transform_state
    {
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_fract_type scale ;
        static so_called_platform_math_num_fract_type weight ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_platform_math_num_whole_type launch_permitted ;
        static so_called_platform_math_num_fract_type time ;
    }

    static void proceed_with_transform ( ) ;
    static void compute_weight ( ) ;
    static void invert_even_weight ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_selection > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    shy_guts :: compute_weight ( ) ;
    shy_guts :: invert_even_weight ( ) ;
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void shy_guts :: compute_weight ( )
{
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type time_stable ;
    so_called_platform_math_num_fract_type time_transition ;
    so_called_platform_math_num_fract_type time_raise_begin ;
    so_called_platform_math_num_fract_type time_raise_end ;
    so_called_platform_math_num_fract_type time_fall_begin ;
    so_called_platform_math_num_fract_type time_fall_end ;
    so_called_platform_math_num_fract_type weight_low ;
    so_called_platform_math_num_fract_type weight_high ;
    so_called_platform_math_num_fract_type weight ;
    
    time = shy_guts :: logic_main_menu_update_state :: time ;
    time_stable = so_called_common_logic_main_menu_letters_animation_consts :: selection_time_stable ;
    time_transition = so_called_common_logic_main_menu_letters_animation_consts :: selection_time_transition ;
    weight_low = so_called_platform_math_consts :: fract_0 ;
    weight_high = so_called_platform_math_consts :: fract_1 ;

    time_raise_begin = time_stable ;
    so_called_platform_math :: add_fracts ( time_raise_end , time_raise_begin , time_transition ) ;
    so_called_platform_math :: add_fracts ( time_fall_begin , time_raise_end , time_stable ) ;
    so_called_platform_math :: add_fracts ( time_fall_end , time_fall_begin , time_transition ) ;
    
    while ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_fall_end ) )
        so_called_platform_math :: sub_from_fract ( time , time_fall_end ) ;

    if ( so_called_platform_conditions :: fract_less_than_fract ( time , time_raise_end ) )
    {
        so_called_common_engine_math_stateless :: easy_in_easy_out
            ( weight
            , time
            , weight_low
            , time_raise_begin
            , weight_high
            , time_raise_end
            ) ;
    }
    else
    {
        so_called_common_engine_math_stateless :: easy_in_easy_out
            ( weight
            , time
            , weight_high
            , time_fall_begin
            , weight_low
            , time_fall_end
            ) ;
    }

    shy_guts :: logic_main_menu_update_state :: time = time ;
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: weight = weight ;
}

void shy_guts :: invert_even_weight ( )
{
    so_called_platform_math_num_whole_type requested_row ;
    so_called_platform_math_num_whole_type requested_col ;
    so_called_platform_math_num_whole_type index ;
    so_called_platform_math_num_fract_type weight ;
    
    requested_row = shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_row ;
    requested_col = shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_col ;
    weight = shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: weight ;
    
    so_called_platform_math :: add_wholes ( index , requested_row , requested_col ) ;
    so_called_platform_math :: mod_whole_by ( index , so_called_platform_math_consts :: whole_2 ) ;
    
    if ( so_called_platform_conditions :: whole_is_zero ( index ) )
    {
        so_called_platform_math :: sub_fracts ( weight , so_called_platform_math_consts :: fract_1 , weight ) ;
        shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: weight = weight ;
    }
}

void shy_guts :: compute_transform ( )
{
    so_called_platform_math_num_fract_type scale_min ;
    so_called_platform_math_num_fract_type scale_max ;
    so_called_platform_math_num_fract_type scale ;
    so_called_platform_math_num_fract_type weight_min ;
    so_called_platform_math_num_fract_type weight_max ;
    so_called_platform_math_num_fract_type weight ;
    
    scale_min = so_called_common_logic_main_menu_letters_animation_consts :: selection_scale_min ;
    scale_max = so_called_common_logic_main_menu_letters_animation_consts :: selection_scale_max ;
    weight_min = so_called_platform_math_consts :: fract_0 ;
    weight_max = so_called_platform_math_consts :: fract_1 ;
    weight = shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: weight ;
    
    so_called_common_engine_math_stateless :: lerp
        ( scale
        , weight
        , scale_min
        , weight_min
        , scale_max
        , weight_max
        ) ;
    
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: scale = scale ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_main_menu_letters_animation_selection_transform_reply_message reply_msg ;
    reply_msg . row = shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_row ;
    reply_msg . col = shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_col ;
    reply_msg . scale = shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: scale ;
    so_called_common_logic_main_menu_letters_animation_selection_transform_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_update_state :: launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_common_logic_main_menu_launch_permit_message )
{
    shy_guts :: logic_main_menu_update_state :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_common_logic_main_menu_letters_animation_selection_transform_request_message msg )
{
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_row = msg . row ;
    shy_guts :: logic_main_menu_letters_animation_selection_transform_state :: requested_col = msg . col ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: launch_permitted ) )
    {
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation_selection :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

