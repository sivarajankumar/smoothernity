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
}

void shy_guts :: compute_vertical_scale ( )
{
}

void shy_guts :: reply_computed_transform ( )
{
}

void _shy_common_logic_main_menu_selection_animation_disappear :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_disappear :: receive ( so_called_message_common_logic_main_menu_selection_animation_disappear_start )
{
    shy_guts :: logic_main_menu_update_state :: disappear_started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_selection_animation_disappear :: receive ( so_called_message_common_logic_main_menu_selection_animation_disappear_transform_request )
{
}

void _shy_common_logic_main_menu_selection_animation_disappear :: receive ( so_called_message_common_logic_main_menu_update )
{
}
