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
}

void shy_guts :: compute_horizontal_scale ( )
{
}

void shy_guts :: compute_vertical_scale ( )
{
}

void shy_guts :: compute_animation_scale
    ( so_called_type_platform_math_num_fract & scale
    , so_called_type_platform_math_num_fract scale_min
    , so_called_type_platform_math_num_fract scale_max
    , so_called_type_platform_math_num_fract period_in_seconds
    )
{
}

void _shy_common_logic_main_menu_selection_animation_push_attention :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_main_menu_selection_animation_push_attention :: receive ( so_called_message_common_logic_main_menu_launch_permit )
{
}

void _shy_common_logic_main_menu_selection_animation_push_attention :: receive ( so_called_message_common_logic_main_menu_selection_animation_push_attention_transform_request )
{
}

void _shy_common_logic_main_menu_selection_animation_push_attention :: receive ( so_called_message_common_logic_main_menu_update )
{
}
