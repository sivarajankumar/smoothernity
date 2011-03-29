namespace shy_guts
{
    namespace logic_main_menu_letters_animation_appear_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole row ;
        static so_called_type_platform_math_num_whole col ;
        static so_called_type_platform_math_num_fract scale ;
        static so_called_type_platform_math_num_fract delay ;
        static so_called_type_platform_math_num_fract time_begin ;
        static so_called_type_platform_math_num_fract time_middle ;
        static so_called_type_platform_math_num_fract time_end ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_whole launch_permitted ;
        static so_called_type_platform_math_num_fract time ;
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
}

void shy_guts :: transform_request_received ( )
{
}

void shy_guts :: compute_delay ( )
{
}

void shy_guts :: compute_time ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_main_menu_letters_animation_appear :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_main_menu_letters_animation_appear :: receive ( so_called_message_common_logic_main_menu_launch_permit )
{
}

void _shy_common_logic_main_menu_letters_animation_appear :: receive ( so_called_message_common_logic_main_menu_letters_animation_appear_transform_request )
{
}

void _shy_common_logic_main_menu_letters_animation_appear :: receive ( so_called_message_common_logic_main_menu_update )
{
}
