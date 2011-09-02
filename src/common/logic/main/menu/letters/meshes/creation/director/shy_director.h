class _shy_common_logic_main_menu_letters_meshes_creation_director
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_create_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_creation_finished_message ) ;
    static void receive ( so_called_common_logic_main_menu_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creation_director > :: module
    shy_common_logic_main_menu_letters_meshes_creation_director_scheduled ;
