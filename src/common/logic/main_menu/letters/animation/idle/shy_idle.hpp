namespace shy_guts
{
    namespace logic_main_menu_letters_animation_idle_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type row ;
        static so_called_platform_math_num_whole_type col ;
        static so_called_platform_vector_data_type vertical_position_delta ;
        static so_called_platform_vector_data_type horizontal_position_delta ;
        static so_called_platform_vector_data_type position ;
        static so_called_platform_math_num_fract_type scale ;
    }
    
    namespace logic_main_menu_letters_layout_position_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_vector_data_type position ;
        static so_called_platform_math_num_fract_type scale ;
    }
    
    namespace logic_main_menu_update_state
    {
        static so_called_platform_math_num_whole_type launch_permitted ;
        static so_called_platform_math_num_fract_type time ;
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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_layout_position ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_position_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_layout_position_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: layout_position_received ( ) ;
    }
}

void shy_guts :: obtain_layout_position ( )
{
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested_col = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: col ;

    so_called_common_logic_main_menu_letters_layout_position_request_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: col ;
    so_called_common_logic_main_menu_letters_layout_position_request_sender :: send ( msg ) ;
}

void shy_guts :: layout_position_received ( )
{
    shy_guts :: compute_horizontal_position_delta ( ) ;
    shy_guts :: compute_vertical_position_delta ( ) ;
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_animated_transform ( ) ;
}

void shy_guts :: compute_horizontal_position_delta ( )
{
    so_called_platform_vector_data_type horizontal_position_delta ;
    so_called_platform_math_num_fract_type zero ;
    so_called_platform_math_num_fract_type row ;
    so_called_platform_math_num_fract_type phase_shift ;
    so_called_platform_math_num_fract_type phase ;
    so_called_platform_math_num_fract_type delta ;
    
    zero = so_called_platform_math_consts :: fract_0 ;
    so_called_platform_math :: make_fract_from_whole ( row , shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row ) ;
    so_called_platform_math :: mul_fracts ( phase_shift , row , so_called_common_logic_main_menu_letters_animation_consts :: idle_horizontal_shift_phase_per_row ) ;
    
    so_called_platform_math :: div_fracts 
        ( phase 
        , shy_guts :: logic_main_menu_update_state :: time 
        , so_called_common_logic_main_menu_letters_animation_consts :: idle_horizontal_shift_period_in_seconds 
        ) ;
    so_called_platform_math :: add_to_fract ( phase , phase_shift ) ;
    so_called_platform_math :: mul_fract_by ( phase , so_called_platform_math_consts :: fract_2pi ) ;
    
    so_called_platform_math :: sin ( delta , phase ) ;
    so_called_platform_math :: mul_fract_by ( delta , so_called_common_logic_main_menu_letters_animation_consts :: idle_horizontal_shift_amplitude ) ;
    so_called_platform_math :: mul_fract_by ( delta , shy_guts :: logic_main_menu_letters_layout_position_state :: scale ) ;
    so_called_platform_math :: mul_fract_by ( delta , so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size ) ;
    
    so_called_platform_vector :: xyz ( horizontal_position_delta , delta , zero , zero ) ;
    
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: horizontal_position_delta = horizontal_position_delta ;
}

void shy_guts :: compute_vertical_position_delta ( )
{
    so_called_platform_vector_data_type vertical_position_delta ;
    so_called_platform_math_num_fract_type zero ;
    so_called_platform_math_num_fract_type col ;
    so_called_platform_math_num_fract_type row ;
    so_called_platform_math_num_fract_type phase_shift_col ;
    so_called_platform_math_num_fract_type phase_shift_row ;
    so_called_platform_math_num_fract_type phase ;
    so_called_platform_math_num_fract_type delta ;
    
    zero = so_called_platform_math_consts :: fract_0 ;
    so_called_platform_math :: make_fract_from_whole ( col , shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: col ) ;
    so_called_platform_math :: make_fract_from_whole ( row , shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row ) ;
    
    so_called_platform_math :: mul_fracts ( phase_shift_col , col , so_called_common_logic_main_menu_letters_animation_consts :: idle_vertical_shift_phase_per_col ) ;
    so_called_platform_math :: mul_fracts ( phase_shift_row , row , so_called_common_logic_main_menu_letters_animation_consts :: idle_vertical_shift_phase_per_row ) ;
    
    so_called_platform_math :: div_fracts 
        ( phase 
        , shy_guts :: logic_main_menu_update_state :: time 
        , so_called_common_logic_main_menu_letters_animation_consts :: idle_vertical_shift_period_in_seconds 
        ) ;
    so_called_platform_math :: add_to_fract ( phase , phase_shift_col ) ;
    so_called_platform_math :: add_to_fract ( phase , phase_shift_row ) ;
    so_called_platform_math :: mul_fract_by ( phase , so_called_platform_math_consts :: fract_2pi ) ;
    
    so_called_platform_math :: sin ( delta , phase ) ;
    so_called_platform_math :: mul_fract_by ( delta , so_called_common_logic_main_menu_letters_animation_consts :: idle_vertical_shift_amplitude ) ;
    so_called_platform_math :: mul_fract_by ( delta , shy_guts :: logic_main_menu_letters_layout_position_state :: scale ) ;
    so_called_platform_math :: mul_fract_by ( delta , so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size ) ;
    
    so_called_platform_vector :: xyz ( vertical_position_delta , zero , delta , zero ) ;
    
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: vertical_position_delta = vertical_position_delta ;
}

void shy_guts :: compute_transform ( )
{
    so_called_platform_vector_data_type vertical_position_delta ;
    so_called_platform_vector_data_type horizontal_position_delta ;
    so_called_platform_vector_data_type layout_position ;
    so_called_platform_vector_data_type position ;
    so_called_platform_math_num_fract_type scale ;
    
    vertical_position_delta = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: vertical_position_delta ;
    horizontal_position_delta = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: horizontal_position_delta ;
    layout_position = shy_guts :: logic_main_menu_letters_layout_position_state :: position ;
    scale = shy_guts :: logic_main_menu_letters_layout_position_state :: scale ;
    
    so_called_platform_vector :: add ( position , vertical_position_delta , horizontal_position_delta ) ;
    so_called_platform_vector :: add_to ( position , layout_position ) ;
        
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: position = position ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: scale = scale ;
}

void shy_guts :: reply_animated_transform ( )
{
    so_called_common_logic_main_menu_letters_animation_idle_transform_reply_message msg ;
    msg . row = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: col ;
    msg . position = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: position ;
    msg . scale = shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: scale ;
    so_called_common_logic_main_menu_letters_animation_idle_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_layout_position_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_common_logic_main_menu_launch_permit_message )
{
    shy_guts :: logic_main_menu_update_state :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_common_logic_main_menu_letters_animation_idle_transform_request_message msg )
{
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: row = msg . row ;
    shy_guts :: logic_main_menu_letters_animation_idle_transform_state :: col = msg . col ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_common_logic_main_menu_letters_layout_position_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_layout_position_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_layout_position_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_layout_position_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_layout_position_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_layout_position_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_layout_position_state :: position = msg . position ;
        shy_guts :: logic_main_menu_letters_layout_position_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation_idle :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: launch_permitted ) )
    {
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: logic_main_menu_update_state :: time , time_step ) ;
    }
}

void _shy_common_logic_main_menu_letters_animation_idle :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

