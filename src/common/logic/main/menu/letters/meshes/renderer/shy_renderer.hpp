namespace shy_guts
{
    static so_called_platform_math_num_whole_type iteration_in_progress ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu_letters_meshes_renderer :: receive ( so_called_common_init_message )
{
    shy_guts :: iteration_in_progress = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_letters_meshes_renderer :: receive ( so_called_common_logic_main_menu_letters_meshes_iterate_finished_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: iteration_in_progress ) )
    {
        shy_guts :: iteration_in_progress = so_called_platform_math_consts :: whole_false ;
        so_called_common_logic_main_menu_letters_meshes_render_reply_sender :: send ( so_called_common_logic_main_menu_letters_meshes_render_reply_message ( ) ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_renderer :: receive ( so_called_common_logic_main_menu_letters_meshes_iteration_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: iteration_in_progress ) )
    {
        so_called_common_engine_render_mesh_render_message render_msg ;
        render_msg . mesh = msg . mesh ;
        so_called_common_engine_render_mesh_render_sender :: send ( render_msg ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_renderer :: receive ( so_called_common_logic_main_menu_letters_meshes_render_request_message )
{
    shy_guts :: iteration_in_progress = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_letters_meshes_iterate_start_sender :: send ( so_called_common_logic_main_menu_letters_meshes_iterate_start_message ( ) ) ;
}

void _shy_common_logic_main_menu_letters_meshes_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
