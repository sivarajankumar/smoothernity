namespace shy_guts
{
    namespace logic_main_menu_letters_animation_idle_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole row ;
        static so_called_type_platform_math_num_whole col ;
        static so_called_type_platform_vector_data vertical_position_delta ;
        static so_called_type_platform_vector_data horizontal_position_delta ;
        static so_called_type_platform_vector_data position ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    namespace logic_main_menu_letters_layout_position_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_vector_data position ;
        static so_called_type_platform_math_num_fract scale ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_whole launch_permitted ;
        static so_called_type_platform_math_num_fract time ;
    }

    static void proceed_with_transform ( ) ;
    static void obtain_layout_position ( ) ;
    static void layout_position_received ( ) ;
    static void compute_horizontal_position_delta ( ) ;
    static void compute_vertical_position_delta ( ) ;
    static void compute_transform ( ) ;
    static void reply_animated_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_idle > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
}

void shy_guts :: obtain_layout_position ( )
{
}

void shy_guts :: layout_position_received ( )
{
}

void shy_guts :: compute_horizontal_position_delta ( )
{
}

void shy_guts :: compute_vertical_position_delta ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_animated_transform ( )
{
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_message_common_logic_main_menu_launch_permit )
{
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_message_common_logic_main_menu_letters_animation_idle_transform_request )
{
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_message_common_logic_main_menu_letters_layout_position_reply )
{
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_message_common_logic_main_menu_update )
{
}
