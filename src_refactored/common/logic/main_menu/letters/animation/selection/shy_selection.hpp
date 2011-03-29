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
    shy_guts :: logic_main_menu_update_state :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_message_common_logic_main_menu_letters_animation_selection_transform_request )
{
}

void _shy_common_logic_main_menu_letters_animation_selection :: receive ( so_called_message_common_logic_main_menu_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: launch_permitted ) )
    {
        so_called_type_platform_math_num_fract time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}
