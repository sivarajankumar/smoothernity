namespace shy_guts
{
    namespace logic_main_menu_letters_layout_row_rect_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        
        static so_called_platform_math_num_fract_type unscaled_menu_width ;
        static so_called_platform_math_num_fract_type unscaled_menu_height ;
        static so_called_platform_math_num_fract_type menu_scale ;

        static so_called_common_engine_rect_type menu_rect ;
        static so_called_common_engine_rect_type row_rect ;
    }
    
    namespace logic_main_menu_letters_boundaries_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_whole_type rows ;
        static so_called_platform_math_num_whole_type cols ;
    }

    namespace engine_render_aspect_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type width ;
        static so_called_platform_math_num_fract_type height ;
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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_boundaries ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_boundaries_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_boundaries_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_aspect_ratio ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_aspect_state :: replied ) )
    {
        shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: received_aspect_ratio ( ) ;
    }
}

void shy_guts :: obtain_boundaries ( )
{
    shy_guts :: logic_main_menu_letters_boundaries_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_letters_boundaries_request_sender :: send ( so_called_common_logic_main_menu_letters_boundaries_request_message ( ) ) ;
}

void shy_guts :: obtain_aspect_ratio ( )
{
    shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_render_aspect_request_sender :: send ( so_called_common_engine_render_aspect_request_message ( ) ) ;
}

void shy_guts :: received_aspect_ratio ( )
{
    shy_guts :: compute_row_rect ( ) ;
    shy_guts :: decorate_row_rect ( ) ;
    shy_guts :: reply_row_rect ( ) ;
}

void shy_guts :: compute_row_rect ( )
{
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_unscaled_menu_size 
        ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: unscaled_menu_width
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: unscaled_menu_height
        , shy_guts :: logic_main_menu_letters_boundaries_state :: cols
        , shy_guts :: logic_main_menu_letters_boundaries_state :: rows
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_horizontal_spacing
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_vertical_spacing
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_horizontal_border
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_vertical_border
        , so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size
        ) ;
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_menu_scale 
        ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: menu_scale
        , shy_guts :: engine_render_aspect_state :: width
        , shy_guts :: engine_render_aspect_state :: height
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: unscaled_menu_width
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: unscaled_menu_height
        ) ;
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_menu_rect 
        ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: menu_rect
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: menu_scale
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: unscaled_menu_width
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: unscaled_menu_height
        ) ;
    so_called_common_logic_main_menu_letters_layout_stateless :: compute_row_rect 
        ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row
        , shy_guts :: logic_main_menu_letters_boundaries_state :: cols
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: menu_scale
        , shy_guts :: logic_main_menu_letters_layout_row_rect_state :: menu_rect
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_vertical_border
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_horizontal_spacing
        , so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_vertical_spacing
        , so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size
        ) ;
}

void shy_guts :: decorate_row_rect ( )
{
    so_called_common_engine_rect_type row_rect ;
    so_called_platform_math_num_fract_type horizontal_border ;
    so_called_platform_math_num_fract_type letter_mesh_scale ;
    so_called_platform_math_num_fract_type menu_scale ;
    so_called_platform_math_num_fract_type scaled_horizontal_border ;
    so_called_platform_math_num_fract_type final_scale ;
    
    row_rect = shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect ;
    horizontal_border = so_called_common_logic_main_menu_letters_layout_consts :: letter_size_fract_horizontal_border ;
    letter_mesh_scale = so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size ;
    menu_scale = shy_guts :: logic_main_menu_letters_layout_row_rect_state :: menu_scale ;
    
    so_called_platform_math :: mul_fracts ( final_scale , menu_scale , letter_mesh_scale ) ;
    so_called_platform_math :: mul_fracts ( scaled_horizontal_border , horizontal_border , final_scale ) ;
    so_called_platform_math :: sub_from_fract ( row_rect . left , scaled_horizontal_border ) ;
    so_called_platform_math :: add_to_fract ( row_rect . right , scaled_horizontal_border ) ;
    
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect = row_rect ;
}

void shy_guts :: reply_row_rect ( )
{
    so_called_common_logic_main_menu_letters_layout_row_rect_reply_message reply_msg ;
    reply_msg . row = shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row ;
    reply_msg . row_rect = shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect ;
    so_called_common_logic_main_menu_letters_layout_row_rect_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_layout_row_rect :: receive ( so_called_common_engine_render_aspect_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_aspect_state :: requested ) )
    {
        shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_aspect_state :: width = msg . width ;
        shy_guts :: engine_render_aspect_state :: height = msg . height ;
        shy_guts :: proceed_with_row_rect ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_layout_row_rect :: receive ( so_called_common_init_message )
{
    shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_boundaries_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_boundaries_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_letters_layout_row_rect :: receive ( so_called_common_logic_main_menu_letters_boundaries_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_boundaries_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_boundaries_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_boundaries_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_boundaries_state :: rows = msg . rows ;
        shy_guts :: logic_main_menu_letters_boundaries_state :: cols = msg . cols ;
        shy_guts :: proceed_with_row_rect ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_layout_row_rect :: receive ( so_called_common_logic_main_menu_letters_layout_row_rect_request_message msg )
{
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row = msg . row ;
    shy_guts :: proceed_with_row_rect ( ) ;
}

void _shy_common_logic_main_menu_letters_layout_row_rect :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

