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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_position_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_boundaries ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_boundaries_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_boundaries_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_cols_count ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_cols_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_cols_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_aspect_ratio ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_aspect_state :: replied ) )
    {
        shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_layout ( ) ;
    }
}

void shy_guts :: obtain_boundaries ( )
{
    shy_guts :: logic_main_menu_letters_boundaries_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_letters_boundaries_request_sender :: send ( so_called_common_logic_main_menu_letters_boundaries_request_message ( ) ) ;
}

void shy_guts :: obtain_cols_count ( )
{
    shy_guts :: logic_main_menu_letters_cols_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_cols_state :: requested_row = shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row ;

    so_called_common_logic_main_menu_letters_cols_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row ;
    so_called_common_logic_main_menu_letters_cols_request_sender :: send ( msg ) ;
}

void shy_guts :: obtain_aspect_ratio ( )
{
    shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_render_aspect_request_sender :: send ( so_called_common_engine_render_aspect_request_message ( ) ) ;
}

void shy_guts :: reply_layout ( )
{
    shy_guts :: compute_layout ( ) ;
    shy_guts :: reply_computed_layout ( ) ;
}

void shy_guts :: reply_computed_layout ( )
{
    so_called_common_logic_main_menu_letters_layout_position_reply_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row ;
    msg . col = shy_guts :: logic_main_menu_letters_layout_position_state :: requested_col ;
    msg . position = shy_guts :: logic_main_menu_letters_layout_position_state :: letter_position ;
    msg . scale = shy_guts :: logic_main_menu_letters_layout_position_state :: menu_scale ;
    so_called_common_logic_main_menu_letters_layout_position_reply_sender :: send ( msg ) ;
}

void shy_guts :: compute_layout ( )
{
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_unscaled_menu_size 
        ( shy_guts :: logic_main_menu_letters_layout_position_state :: unscaled_menu_width
        , shy_guts :: logic_main_menu_letters_layout_position_state :: unscaled_menu_height
        , shy_guts :: logic_main_menu_letters_boundaries_state :: cols
        , shy_guts :: logic_main_menu_letters_boundaries_state :: rows
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_horizontal_spacing
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_vertical_spacing
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_horizontal_border
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_vertical_border
        , so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size
        ) ;
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_menu_scale 
        ( shy_guts :: logic_main_menu_letters_layout_position_state :: menu_scale
        , shy_guts :: engine_render_aspect_state :: width
        , shy_guts :: engine_render_aspect_state :: height
        , shy_guts :: logic_main_menu_letters_layout_position_state :: unscaled_menu_width
        , shy_guts :: logic_main_menu_letters_layout_position_state :: unscaled_menu_height
        ) ;
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_menu_rect 
        ( shy_guts :: logic_main_menu_letters_layout_position_state :: menu_rect
        , shy_guts :: logic_main_menu_letters_layout_position_state :: menu_scale
        , shy_guts :: logic_main_menu_letters_layout_position_state :: unscaled_menu_width
        , shy_guts :: logic_main_menu_letters_layout_position_state :: unscaled_menu_height
        ) ;
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_row_rect 
        ( shy_guts :: logic_main_menu_letters_layout_position_state :: row_rect
        , shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row
        , shy_guts :: logic_main_menu_letters_cols_state :: cols
        , shy_guts :: logic_main_menu_letters_layout_position_state :: menu_scale
        , shy_guts :: logic_main_menu_letters_layout_position_state :: menu_rect
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_vertical_border
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_horizontal_spacing
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_vertical_spacing
        , so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size
        ) ;
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_letter_rect 
        ( shy_guts :: logic_main_menu_letters_layout_position_state :: letter_rect
        , shy_guts :: logic_main_menu_letters_layout_position_state :: requested_col
        , shy_guts :: logic_main_menu_letters_layout_position_state :: menu_scale
        , shy_guts :: logic_main_menu_letters_layout_position_state :: row_rect
        , so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_horizontal_spacing
        ) ;
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_letter_position 
        ( shy_guts :: logic_main_menu_letters_layout_position_state :: letter_position
        , shy_guts :: logic_main_menu_letters_layout_position_state :: letter_rect
        , so_called_common_logic_main_menu_letters_layout_consts :: menu_position_z
        ) ;
}

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_common_engine_render_aspect_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_aspect_state :: requested ) )
    {
        shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_aspect_state :: width = msg . width ;
        shy_guts :: engine_render_aspect_state :: height = msg . height ;
        shy_guts :: proceed_with_layout ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_common_init_message )
{
    shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_boundaries_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_boundaries_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_cols_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_cols_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_common_logic_main_menu_letters_boundaries_reply_message msg )
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

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_common_logic_main_menu_letters_cols_reply_message msg )
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

void _shy_common_logic_main_menu_letters_layout_position :: receive ( so_called_common_logic_main_menu_letters_layout_position_request_message msg )
{
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested_col = msg . col ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row = msg . row ;
    shy_guts :: proceed_with_layout ( ) ;
}

void _shy_common_logic_main_menu_letters_layout_position :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
