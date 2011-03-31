namespace shy_guts
{
    namespace logic_main_menu_letters_meshes_storage_consts
    {
        static so_called_type_platform_math_const_int_32 max_meshes 
            = so_called_common_logic_main_menu_consts :: max_rows 
            * so_called_common_logic_main_menu_consts :: max_cols
            ;
    }

    namespace mesh_state
    {
        static so_called_type_common_engine_render_mesh_id mesh ;
        static so_called_type_platform_math_num_whole row ;
        static so_called_type_platform_math_num_whole col ;
    }

    static so_called_type_platform_math_num_whole meshes_count ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_storage > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_init )
{
    shy_guts :: meshes_count = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_count_request )
{
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_iterate_start )
{
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_has_been_created )
{
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_id_request )
{
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_row_col_request )
{
}
