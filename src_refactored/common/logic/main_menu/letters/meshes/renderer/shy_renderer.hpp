namespace shy_guts
{
    static so_called_type_platform_math_num_whole iteration_in_progress ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu_letters_meshes_renderer :: receive ( so_called_message_common_logic_main_menu_letters_meshes_iterate_finished )
{
}

void _shy_common_logic_main_menu_letters_meshes_renderer :: receive ( so_called_message_common_logic_main_menu_letters_meshes_iteration )
{
}

void _shy_common_logic_main_menu_letters_meshes_renderer :: receive ( so_called_message_common_logic_main_menu_letters_meshes_render_request )
{
    shy_guts :: iteration_in_progress = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_main_menu_letters_meshes_iterate_start :: send ( so_called_message_common_logic_main_menu_letters_meshes_iterate_start ( ) ) ;
}
