namespace shy_guts
{
    static so_called_platform_math_num_whole_type creation_permitted ;
    static so_called_platform_math_num_whole_type launch_permitted ;
    static so_called_platform_math_num_whole_type created ;
    static so_called_platform_math_num_whole_type launched ;
    static so_called_platform_math_num_whole_type disappearing ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu :: receive ( so_called_common_init_message )
{
    shy_guts :: launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: creation_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: launched = so_called_platform_math_consts :: whole_false ;
    shy_guts :: created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: disappearing = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_creation_permit_message )
{
    shy_guts :: creation_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_launch_permit_message )
{
    shy_guts :: launch_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_letters_animation_disappear_finished_message )
{
    shy_guts :: disappearing = so_called_platform_math_consts :: whole_false ;
    so_called_common_logic_main_menu_letters_meshes_destroy_request_sender :: send ( so_called_common_logic_main_menu_letters_meshes_destroy_request_message ( ) ) ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_letters_create_finished_message )
{
    so_called_common_logic_main_menu_letters_meshes_create_sender :: send ( so_called_common_logic_main_menu_letters_meshes_create_message ( ) ) ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_letters_meshes_creation_finished_message )
{
    so_called_common_logic_main_menu_selection_mesh_create_sender :: send ( so_called_common_logic_main_menu_selection_mesh_create_message ( ) ) ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_letters_meshes_destroy_reply_message )
{
    shy_guts :: created = so_called_platform_math_consts :: whole_false ;
    so_called_common_logic_main_menu_selection_mesh_destroy_request_sender :: send ( so_called_common_logic_main_menu_selection_mesh_destroy_request_message ( ) ) ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_row_chosen_message )
{
    shy_guts :: launched = so_called_platform_math_consts :: whole_false ;
    shy_guts :: disappearing = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_letters_animation_disappear_start_sender :: send ( so_called_common_logic_main_menu_letters_animation_disappear_start_message ( ) ) ;
    so_called_common_logic_main_menu_selection_animation_disappear_start_sender :: send ( so_called_common_logic_main_menu_selection_animation_disappear_start_message ( ) ) ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_selection_mesh_create_finished_message )
{
    shy_guts :: created = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_render_permit_sender :: send ( so_called_common_logic_main_menu_render_permit_message ( ) ) ;
    so_called_common_logic_main_menu_created_sender :: send ( so_called_common_logic_main_menu_created_message ( ) ) ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_selection_mesh_destroy_reply_message )
{
    so_called_common_logic_main_menu_finished_sender :: send ( so_called_common_logic_main_menu_finished_message ( ) ) ;
}

void _shy_common_logic_main_menu :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: creation_permitted ) )
    {
        shy_guts :: creation_permitted = so_called_platform_math_consts :: whole_false ;
        so_called_common_logic_main_menu_letters_create_sender :: send ( so_called_common_logic_main_menu_letters_create_message ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: created ) 
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: launch_permitted )
       )
    {
        shy_guts :: launch_permitted = so_called_platform_math_consts :: whole_false ;
        shy_guts :: launched = so_called_platform_math_consts :: whole_true ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: created ) 
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: launched )
       )
    {
        so_called_common_logic_main_menu_letters_meshes_place_sender :: send ( so_called_common_logic_main_menu_letters_meshes_place_message ( ) ) ;
        so_called_common_logic_main_menu_selection_tracking_director_update_sender :: send ( so_called_common_logic_main_menu_selection_tracking_director_update_message ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: created )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: disappearing )
       )
    {
        so_called_common_logic_main_menu_letters_meshes_place_sender :: send ( so_called_common_logic_main_menu_letters_meshes_place_message ( ) ) ;
        so_called_common_logic_main_menu_selection_mesh_place_sender :: send ( so_called_common_logic_main_menu_selection_mesh_place_message ( ) ) ;
    }
}

void _shy_common_logic_main_menu :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
