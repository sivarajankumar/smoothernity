namespace shy_guts
{
    namespace logic_main_menu_selection_animation_idle_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole row_is_selected ;
        static so_called_type_platform_math_num_whole selected_row_index ;
        static so_called_type_platform_vector_data position ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_letters_layout_row_rect_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_common_engine_rect row_rect ;
    }

    static void proceed_with_transform ( ) ;
    static void obtain_row_rect ( ) ;
    static void received_row_rect ( ) ;
    static void reply_transform ( ) ;
    static void compute_row_rect_mesh_transform ( ) ;
    static void compute_empty_mesh_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_idle > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
}

void shy_guts :: obtain_row_rect ( )
{
}

void shy_guts :: received_row_rect ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void shy_guts :: compute_row_rect_mesh_transform ( )
{
}

void shy_guts :: compute_empty_mesh_transform ( )
{
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_message_common_logic_main_menu_letters_layout_row_rect_reply )
{
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_message_common_logic_main_menu_selection_animation_idle_row_selected msg )
{
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: row_is_selected = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: selected_row_index = msg . row ;
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_message_common_logic_main_menu_selection_animation_idle_transform_request )
{
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_message_common_logic_main_menu_selection_animation_idle_void_selected )
{
}
