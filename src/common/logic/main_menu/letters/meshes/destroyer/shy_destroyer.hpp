namespace shy_guts
{
    static so_called_type_platform_math_num_whole iteration_in_progress ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_destroyer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu_letters_meshes_destroyer :: receive ( so_called_message_common_init )
{
    shy_guts :: iteration_in_progress = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_letters_meshes_destroyer :: receive ( so_called_message_common_logic_main_menu_letters_meshes_destroy_request )
{
    shy_guts :: iteration_in_progress = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_letters_meshes_iterate_start_sender :: send ( so_called_message_common_logic_main_menu_letters_meshes_iterate_start ( ) ) ;
}

void _shy_common_logic_main_menu_letters_meshes_destroyer :: receive ( so_called_message_common_logic_main_menu_letters_meshes_iterate_finished )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: iteration_in_progress ) )
    {
        shy_guts :: iteration_in_progress = so_called_platform_math_consts :: whole_false ;
        so_called_common_logic_main_menu_letters_meshes_destroy_reply_sender :: send ( so_called_message_common_logic_main_menu_letters_meshes_destroy_reply ( ) ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_destroyer :: receive ( so_called_message_common_logic_main_menu_letters_meshes_iteration msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: iteration_in_progress ) )
    {
        so_called_message_common_engine_render_mesh_delete delete_msg ;
        delete_msg . mesh = msg . mesh ;
        so_called_common_engine_render_mesh_delete_sender :: send ( delete_msg ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_destroyer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

