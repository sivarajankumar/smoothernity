namespace shy_guts
{
    namespace logic_main_menu_selection_animation_push_attention_transform_state
    {
        static so_called_type_platform_math_num_fract horizontal_scale ;
        static so_called_type_platform_math_num_fract vertical_scale ;
    }

    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_whole update_permitted ;
        static so_called_type_platform_math_num_fract time ;
    }

    static void reply_transform ( ) ;
    static void compute_horizontal_scale ( ) ;
    static void compute_vertical_scale ( ) ;
    static void compute_animation_scale
        ( so_called_type_platform_math_num_fract & scale
        , so_called_type_platform_math_num_fract scale_min
        , so_called_type_platform_math_num_fract scale_max
        , so_called_type_platform_math_num_fract period_in_seconds
        ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_push_attention > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: reply_transform ( )
{
    so_called_message_common_logic_main_menu_selection_animation_push_attention_transform_reply msg ;
    msg . scale_x = shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: horizontal_scale ;
    msg . scale_y = shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: vertical_scale ;
    so_called_sender_common_logic_main_menu_selection_animation_push_attention_transform_reply :: send ( msg ) ;
}

void shy_guts :: compute_horizontal_scale ( )
{
    shy_guts :: compute_animation_scale
        ( shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: horizontal_scale
        , so_called_common_logic_main_menu_selection_animation_consts :: push_attention_horizontal_scale_min
        , so_called_common_logic_main_menu_selection_animation_consts :: push_attention_horizontal_scale_max
        , so_called_common_logic_main_menu_selection_animation_consts :: push_attention_period_in_seconds
        ) ;
}

void shy_guts :: compute_vertical_scale ( )
{
    shy_guts :: compute_animation_scale
        ( shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: vertical_scale
        , so_called_common_logic_main_menu_selection_animation_consts :: push_attention_vertical_scale_min
        , so_called_common_logic_main_menu_selection_animation_consts :: push_attention_vertical_scale_max
        , so_called_common_logic_main_menu_selection_animation_consts :: push_attention_period_in_seconds
        ) ;
}

void shy_guts :: compute_animation_scale
    ( so_called_type_platform_math_num_fract & scale
    , so_called_type_platform_math_num_fract scale_min
    , so_called_type_platform_math_num_fract scale_max
    , so_called_type_platform_math_num_fract period_in_seconds
    )
{
    so_called_type_platform_math_num_fract time ;
    so_called_type_platform_math_num_fract phase ;
    so_called_type_platform_math_num_fract amplitude ;
    so_called_type_platform_math_num_fract offset ;
    
    time = shy_guts :: logic_main_menu_update_state :: time ;
    
    so_called_platform_math :: div_fracts ( phase , time , period_in_seconds ) ;
    so_called_platform_math :: mul_fract_by ( phase , so_called_platform_math_consts :: fract_2pi ) ;
    
    so_called_platform_math :: sub_fracts ( amplitude , scale_max , scale_min ) ;
    so_called_platform_math :: div_fract_by ( amplitude , so_called_platform_math_consts :: fract_2 ) ;
    
    so_called_platform_math :: add_fracts ( offset , scale_max , scale_min ) ;
    so_called_platform_math :: div_fract_by ( offset , so_called_platform_math_consts :: fract_2 ) ;
    
    so_called_platform_math :: sin ( scale , phase ) ;
    so_called_platform_math :: mul_fract_by ( scale , amplitude ) ;
    so_called_platform_math :: add_to_fract ( scale , offset ) ;        
}

void _shy_common_logic_main_menu_selection_animation_push_attention :: receive ( so_called_message_common_logic_main_menu_launch_permit )
{
    shy_guts :: logic_main_menu_update_state :: update_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_push_attention :: receive ( so_called_message_common_logic_main_menu_selection_animation_push_attention_transform_request )
{
    shy_guts :: compute_horizontal_scale ( ) ;
    shy_guts :: compute_vertical_scale ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_push_attention :: receive ( so_called_message_common_logic_main_menu_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: update_permitted ) )
    {
        so_called_type_platform_math_num_fract time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation_push_attention :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

