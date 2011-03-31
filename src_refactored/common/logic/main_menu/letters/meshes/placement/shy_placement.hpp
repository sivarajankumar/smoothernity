namespace shy_guts
{
    namespace logic_main_menu_letters_meshes_place_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole current_mesh_index ;
    }
    
    namespace logic_main_menu_letters_meshes_count_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole meshes ;
    }

    namespace logic_main_menu_letters_mesh_row_col_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_index ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole row ;
        static so_called_type_platform_math_num_whole col ;
    }

    namespace logic_main_menu_letters_mesh_id_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_index ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_common_engine_render_mesh_id mesh ;
    }

    namespace logic_main_menu_letters_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_matrix_data transform ;
    }

    static void proceed_with_placement ( ) ;
    static void obtain_meshes_count ( ) ;
    static void obtain_first_mesh_row_col ( ) ;
    static void obtain_current_mesh_row_col ( ) ;
    static void obtain_current_mesh_id ( ) ;
    static void obtain_animated_transform ( ) ;
    static void animated_transform_received ( ) ;
    static void place_current_mesh ( ) ;
    static void move_to_next_mesh ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_placement > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_placement ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_meshes_place_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_meshes_place_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_meshes_count ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_meshes_count_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_meshes_count_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_first_mesh_row_col ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_mesh_row_col_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_mesh_row_col_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_current_mesh_id ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_mesh_id_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_mesh_id_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_animated_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_animation_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: animated_transform_received ( ) ;
    }
}

void shy_guts :: obtain_meshes_count ( )
{
    shy_guts :: logic_main_menu_letters_meshes_count_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_main_menu_letters_meshes_count_request :: send ( so_called_message_common_logic_main_menu_letters_meshes_count_request ( ) ) ;
}

void shy_guts :: obtain_first_mesh_row_col ( )
{
    shy_guts :: logic_main_menu_letters_meshes_place_state :: current_mesh_index = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: obtain_current_mesh_row_col ( ) ;
}

void shy_guts :: obtain_current_mesh_row_col ( )
{
    shy_guts :: logic_main_menu_letters_mesh_row_col_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_mesh_row_col_state :: requested_index = shy_guts :: logic_main_menu_letters_meshes_place_state :: current_mesh_index ;

    so_called_message_common_logic_main_menu_letters_meshes_mesh_row_col_request msg ;
    msg . index = shy_guts :: logic_main_menu_letters_meshes_place_state :: current_mesh_index ;
    so_called_sender_common_logic_main_menu_letters_meshes_mesh_row_col_request :: send ( msg ) ;
}

void shy_guts :: obtain_current_mesh_id ( )
{
    shy_guts :: logic_main_menu_letters_mesh_id_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_mesh_id_state :: requested_index = shy_guts :: logic_main_menu_letters_meshes_place_state :: current_mesh_index ;

    so_called_message_common_logic_main_menu_letters_meshes_mesh_id_request msg ;
    msg . index = shy_guts :: logic_main_menu_letters_meshes_place_state :: current_mesh_index ;
    so_called_sender_common_logic_main_menu_letters_meshes_mesh_id_request :: send ( msg ) ;
}

void shy_guts :: obtain_animated_transform ( )
{
    shy_guts :: logic_main_menu_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letters_animation_transform_state :: requested_row = shy_guts :: logic_main_menu_letters_mesh_row_col_state :: row ;
    shy_guts :: logic_main_menu_letters_animation_transform_state :: requested_col = shy_guts :: logic_main_menu_letters_mesh_row_col_state :: col ;

    so_called_message_common_logic_main_menu_letters_animation_transform_request msg ;
    msg . row = shy_guts :: logic_main_menu_letters_mesh_row_col_state :: row ;
    msg . col = shy_guts :: logic_main_menu_letters_mesh_row_col_state :: col ;
    so_called_sender_common_logic_main_menu_letters_animation_transform_request :: send ( msg ) ;
}

void shy_guts :: animated_transform_received ( )
{
    shy_guts :: place_current_mesh ( ) ;
    shy_guts :: move_to_next_mesh ( ) ;
}

void shy_guts :: place_current_mesh ( )
{
    so_called_message_common_engine_render_mesh_set_transform msg ;
    msg . transform = shy_guts :: logic_main_menu_letters_animation_transform_state :: transform ;
    msg . mesh = shy_guts :: logic_main_menu_letters_mesh_id_state :: mesh ;
    so_called_sender_common_engine_render_mesh_set_transform :: send ( msg ) ;
}

void shy_guts :: move_to_next_mesh ( )
{
    so_called_platform_math :: inc_whole ( shy_guts :: logic_main_menu_letters_meshes_place_state :: current_mesh_index ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole 
        ( shy_guts :: logic_main_menu_letters_meshes_place_state :: current_mesh_index 
        , shy_guts :: logic_main_menu_letters_meshes_count_state :: meshes 
        ) 
    )
    {
        shy_guts :: obtain_current_mesh_row_col ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_placement :: receive ( so_called_message_common_logic_main_menu_letters_animation_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_animation_transform_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_transform_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_animation_transform_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_animation_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_animation_transform_state :: transform = msg . transform ;
        shy_guts :: proceed_with_placement ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_placement :: receive ( so_called_message_common_logic_main_menu_letters_meshes_count_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_meshes_count_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_meshes_count_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_meshes_count_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_meshes_count_state :: meshes = msg . meshes ;
        shy_guts :: proceed_with_placement ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_placement :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_id_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_mesh_id_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_mesh_id_state :: requested_index , msg . index )
       )
    {
        shy_guts :: logic_main_menu_letters_mesh_id_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_mesh_id_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_mesh_id_state :: mesh = msg . mesh ;
        shy_guts :: proceed_with_placement ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_placement :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_row_col_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_mesh_row_col_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_mesh_row_col_state :: requested_index , msg . index )
       )
    {
        shy_guts :: logic_main_menu_letters_mesh_row_col_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_mesh_row_col_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_mesh_row_col_state :: row = msg . row ;
        shy_guts :: logic_main_menu_letters_mesh_row_col_state :: col = msg . col ;
        shy_guts :: proceed_with_placement ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_placement :: receive ( so_called_message_common_logic_main_menu_letters_meshes_place )
{
    shy_guts :: logic_main_menu_letters_meshes_place_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_placement ( ) ;
}
