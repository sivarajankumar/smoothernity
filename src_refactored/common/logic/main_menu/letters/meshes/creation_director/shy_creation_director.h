class _shy_common_logic_main_menu_letters_meshes_creation_director
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_meshes_create ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_meshes_creation_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creation_director > :: module
    shy_common_logic_main_menu_letters_meshes_creation_director_scheduled ;
