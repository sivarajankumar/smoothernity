namespace shy_guts
{
    namespace logic_main_menu_letters_animation_appear_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type row ;
        static so_called_platform_math_num_whole_type col ;
        static so_called_platform_math_num_fract_type scale ;
        static so_called_platform_math_num_fract_type delay ;
        static so_called_platform_math_num_fract_type time_begin ;
        static so_called_platform_math_num_fract_type time_middle ;
        static so_called_platform_math_num_fract_type time_end ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_platform_math_num_whole_type launch_permitted ;
        static so_called_platform_math_num_fract_type time ;
    }

    static void proceed_with_transform ( ) ;
    static void transform_request_received ( ) ;
    static void compute_delay ( ) ;
    static void compute_time ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_appear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: transform_request_received ( ) ;
    }
}

void shy_guts :: transform_request_received ( )
{
    shy_guts :: compute_delay ( ) ;
    shy_guts :: compute_time ( ) ;
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void shy_guts :: compute_delay ( )
{
    so_called_platform_math_num_fract_type delay_for_row ;
    so_called_platform_math_num_fract_type delay_for_col ;
    so_called_platform_math_num_fract_type delay_per_row ;
    so_called_platform_math_num_fract_type delay_per_col ;
    so_called_platform_math_num_fract_type delay ;
    so_called_platform_math_num_fract_type row ;
    so_called_platform_math_num_fract_type col ;
    
    so_called_platform_math :: make_fract_from_whole ( row , shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: row ) ;
    so_called_platform_math :: make_fract_from_whole ( col , shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: col ) ;
    delay_per_row = so_called_common_logic_main_menu_letters_animation_consts :: appear_delay_per_row_in_seconds ;
    delay_per_col = so_called_common_logic_main_menu_letters_animation_consts :: appear_delay_per_col_in_seconds ;
    so_called_platform_math :: mul_fracts ( delay_for_row , delay_per_row , row ) ;
    so_called_platform_math :: mul_fracts ( delay_for_col , delay_per_col , col ) ;
    so_called_platform_math :: add_fracts ( delay , delay_for_row , delay_for_col ) ;
    
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: delay = delay ;
}

void shy_guts :: compute_time ( )
{
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_middle ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type delay ;
    so_called_platform_math_num_fract_type time_from_begin_to_middle ;
    so_called_platform_math_num_fract_type time_from_middle_to_end ;
    
    delay = shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: delay ;
    time_from_begin_to_middle = so_called_common_logic_main_menu_letters_animation_consts :: appear_time_from_begin_to_middle_in_seconds ;
    time_from_middle_to_end = so_called_common_logic_main_menu_letters_animation_consts :: appear_time_from_middle_to_end_in_seconds ;
    time_begin = delay ;
    so_called_platform_math :: add_fracts ( time_middle , time_begin , time_from_begin_to_middle ) ;
    so_called_platform_math :: add_fracts ( time_end , time_middle , time_from_middle_to_end ) ;
    
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: time_begin = time_begin ;
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: time_middle = time_middle ;
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: time_end = time_end ;
}

void shy_guts :: compute_transform ( )
{
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_middle ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type scale_begin ;
    so_called_platform_math_num_fract_type scale_middle ;
    so_called_platform_math_num_fract_type scale_end ;
    so_called_platform_math_num_fract_type scale ;
    
    time_begin = shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: time_begin ;
    time_middle = shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: time_middle ;
    time_end = shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: time_end ;
    time = shy_guts :: logic_main_menu_update_state :: time ;
    scale_begin = so_called_common_logic_main_menu_letters_animation_consts :: appear_scale_begin ;
    scale_middle = so_called_common_logic_main_menu_letters_animation_consts :: appear_scale_middle ;
    scale_end = so_called_common_logic_main_menu_letters_animation_consts :: appear_scale_end ;
    
    so_called_common_engine_math_stateless :: hard_attack_easy_decay
        ( scale
        , time
        , scale_begin
        , time_begin
        , scale_middle
        , time_middle
        , scale_end
        , time_end
        ) ;
        
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: scale = scale ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_main_menu_letters_animation_appear_transform_reply_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: col ;
    msg . scale = shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: scale ;
    so_called_common_logic_main_menu_letters_animation_appear_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_letters_animation_appear :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_appear :: receive ( so_called_common_logic_main_menu_launch_permit_message )
{
    shy_guts :: logic_main_menu_update_state :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_appear :: receive ( so_called_common_logic_main_menu_letters_animation_appear_transform_request_message msg )
{
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: row = msg . row ;
    shy_guts :: logic_main_menu_letters_animation_appear_transform_state :: col = msg . col ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_letters_animation_appear :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: launch_permitted ) )
    {
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation_appear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
