namespace shy_guts
{
    namespace logic_main_menu_letters_layout_position_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        
        static so_called_type_platform_math_num_fract unscaled_menu_width ;
        static so_called_type_platform_math_num_fract unscaled_menu_height ;
        static so_called_type_platform_math_num_fract menu_scale ;
        static so_called_type_common_engine_rect menu_rect ;
        static so_called_type_common_engine_rect row_rect ;
        static so_called_type_common_engine_rect decorated_row_rect ;
        static so_called_type_common_engine_rect letter_rect ;
        static so_called_type_platform_vector_data letter_position ;
    }
    
    namespace logic_main_menu_letters_boundaries_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole rows ;
        static so_called_type_platform_math_num_whole cols ;
    }
    
    namespace logic_main_menu_letters_cols_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole cols ;
    }

    namespace engine_render_aspect_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract width ;
        static so_called_type_platform_math_num_fract height ;
    }

    static void proceed_with_layout ( ) ;
    static void obtain_boundaries ( ) ;
    static void obtain_cols_count ( ) ;
    static void obtain_aspect_ratio ( ) ;
    static void reply_layout ( ) ;
    static void reply_computed_layout ( ) ;
    static void compute_layout ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_layout_position > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_layout ( )
{
}

void shy_guts :: obtain_boundaries ( )
{
}

void shy_guts :: obtain_cols_count ( )
{
}

void shy_guts :: obtain_aspect_ratio ( )
{
}

void shy_guts :: reply_layout ( )
{
}

void shy_guts :: reply_computed_layout ( )
{
}

void shy_guts :: compute_layout ( )
{
}

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_message_common_logic_main_menu_letters_boundaries_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_boundaries_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_boundaries_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_boundaries_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_boundaries_state :: rows = msg . rows ;
        shy_guts :: logic_main_menu_letters_boundaries_state :: cols = msg . cols ;
        shy_guts :: proceed_with_layout ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_message_common_logic_main_menu_letters_cols_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_cols_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_cols_state :: requested_row , msg . row )
       )
    {
        shy_guts :: logic_main_menu_letters_cols_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_cols_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_cols_state :: cols = msg . cols ;
        shy_guts :: proceed_with_layout ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_message_common_logic_main_menu_letters_layout_position_request msg )
{
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested_col = msg . col ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row = msg . row ;
    shy_guts :: proceed_with_layout ( ) ;
}
