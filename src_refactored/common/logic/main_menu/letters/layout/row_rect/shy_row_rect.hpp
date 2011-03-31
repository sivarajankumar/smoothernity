namespace shy_guts
{
    namespace logic_main_menu_letters_layout_row_rect_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        
        static so_called_type_platform_math_num_fract unscaled_menu_width ;
        static so_called_type_platform_math_num_fract unscaled_menu_height ;
        static so_called_type_platform_math_num_fract menu_scale ;

        static so_called_type_common_engine_rect menu_rect ;
        static so_called_type_common_engine_rect row_rect ;
    }
    
    namespace logic_main_menu_letters_boundaries_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole rows ;
        static so_called_type_platform_math_num_whole cols ;
    }

    namespace engine_render_aspect_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract width ;
        static so_called_type_platform_math_num_fract height ;
    }

    static void proceed_with_row_rect ( ) ;
    static void obtain_boundaries ( ) ;
    static void obtain_aspect_ratio ( ) ;
    static void received_aspect_ratio ( ) ;
    static void compute_row_rect ( ) ;
    static void decorate_row_rect ( ) ;
    static void reply_row_rect ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_layout_row_rect > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_row_rect ( )
{
}

void shy_guts :: obtain_boundaries ( )
{
}

void shy_guts :: obtain_aspect_ratio ( )
{
}

void shy_guts :: received_aspect_ratio ( )
{
}

void shy_guts :: compute_row_rect ( )
{
}

void shy_guts :: decorate_row_rect ( )
{
}

void shy_guts :: reply_row_rect ( )
{
}

void _shy_common_logic_main_menu_letters_layout_row_rect :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_main_menu_letters_layout_row_rect :: receive ( so_called_message_common_logic_main_menu_letters_boundaries_reply )
{
}

void _shy_common_logic_main_menu_letters_layout_row_rect :: receive ( so_called_message_common_logic_main_menu_letters_layout_row_rect_request )
{
}
