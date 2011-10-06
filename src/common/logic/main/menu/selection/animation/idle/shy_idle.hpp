namespace shy_guts
{
    namespace logic_main_menu_selection_animation_idle_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type row_is_selected ;
        static so_called_platform_math_num_whole_type selected_row_index ;
        static so_called_platform_vector_data_type position ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_letters_layout_row_rect_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_common_engine_rect_type row_rect ;
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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_row_rect ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: received_row_rect ( ) ;
    }
}

void shy_guts :: obtain_row_rect ( )
{
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row = shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: selected_row_index ;

    so_called_common_logic_main_menu_letters_layout_row_rect_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row ;
    so_called_common_logic_main_menu_letters_layout_row_rect_request_sender :: send ( msg ) ;
}

void shy_guts :: received_row_rect ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: row_is_selected ) )
        shy_guts :: compute_row_rect_mesh_transform ( ) ;
    else
        shy_guts :: compute_empty_mesh_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_main_menu_selection_animation_idle_transform_reply_message reply_msg ;
    reply_msg . position = shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: position ;
    reply_msg . scale_x = shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_x ;
    reply_msg . scale_y = shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_y ;
    so_called_common_logic_main_menu_selection_animation_idle_transform_reply_sender :: send ( reply_msg ) ;
}

void shy_guts :: compute_row_rect_mesh_transform ( )
{
    so_called_platform_math_num_fract_type zero ;
    so_called_platform_math_num_fract_type half ;
    so_called_platform_math_num_fract_type scale_x ;
    so_called_platform_math_num_fract_type scale_y ;
    so_called_platform_math_num_fract_type pos_x ;
    so_called_platform_math_num_fract_type pos_y ;
    so_called_platform_math_num_fract_type pos_z ;
    so_called_platform_math_num_fract_type width ;
    so_called_platform_math_num_fract_type height ;
    so_called_platform_math_num_fract_type mesh_size ;
    so_called_common_engine_rect_type row_rect ;
    so_called_platform_vector_data_type position ;
    
    row_rect = shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect ;
    mesh_size = so_called_common_logic_main_menu_selection_consts :: mesh_size ;
    zero = so_called_platform_math_consts :: fract_0 ;
    
    so_called_platform_math :: sub_fracts ( width , row_rect . right , row_rect . left ) ;
    so_called_platform_math :: sub_fracts ( height , row_rect . top , row_rect . bottom ) ;
    
    so_called_platform_math :: div_fracts ( scale_x , width , mesh_size ) ;
    so_called_platform_math :: div_fracts ( scale_y , height , mesh_size ) ;

    so_called_platform_math :: add_fracts ( pos_x , row_rect . right , row_rect . left ) ;
    so_called_platform_math :: add_fracts ( pos_y , row_rect . top , row_rect . bottom ) ;
    so_called_platform_math :: div_fract_by ( pos_x , so_called_platform_math_consts :: fract_2 ) ;
    so_called_platform_math :: div_fract_by ( pos_y , so_called_platform_math_consts :: fract_2 ) ;
    pos_z = so_called_common_logic_main_menu_selection_animation_consts :: idle_position_z ;
    
    so_called_platform_vector :: xyz ( position , pos_x , pos_y , pos_z ) ;
    
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: position = position ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_x = scale_x ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_y = scale_y ;
}

void shy_guts :: compute_empty_mesh_transform ( )
{
    so_called_platform_math_num_fract_type zero ;
    so_called_platform_vector_data_type position ;
    
    zero = so_called_platform_math_consts :: fract_0 ;
    
    so_called_platform_vector :: xyz ( position , zero , zero , zero ) ;
    
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: position = position ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_x = zero ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_y = zero ;
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: row_is_selected = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: selected_row_index = so_called_platform_math_consts :: whole_minus_1 ;
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_common_logic_main_menu_letters_layout_row_rect_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested_row , msg . row )
       )
    {
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_layout_row_rect_state :: row_rect = msg . row_rect ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_common_logic_main_menu_selection_animation_idle_row_selected_message msg )
{
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: row_is_selected = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: selected_row_index = msg . row ;
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_common_logic_main_menu_selection_animation_idle_transform_request_message )
{
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation_idle :: receive ( so_called_common_logic_main_menu_selection_animation_idle_void_selected_message )
{
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: row_is_selected = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_selection_animation_idle :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
