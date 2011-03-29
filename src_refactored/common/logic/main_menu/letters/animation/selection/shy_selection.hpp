namespace shy_guts
{
    namespace logic_main_menu_letters_animation_selection_transform_state
    {
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_fract scale ;
        static so_called_type_platform_math_num_fract weight ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_type_platform_math_num_whole launch_permitted ;
        static so_called_type_platform_math_num_fract time ;
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
}

void shy_guts :: compute_weight ( )
{
}

void shy_guts :: invert_even_weight ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_message_common_logic_main_menu_launch_permit )
{
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_message_common_logic_main_menu_letters_animation_selection_transform_request )
{
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_message_common_logic_main_menu_update )
{
}
