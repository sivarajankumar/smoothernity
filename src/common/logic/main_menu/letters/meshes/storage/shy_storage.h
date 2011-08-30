class _shy_common_logic_main_menu_letters_meshes_storage
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_count_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_iterate_start_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_mesh_has_been_created_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_mesh_id_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_mesh_row_col_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_storage > :: module shy_common_logic_main_menu_letters_meshes_storage_scheduled ;
