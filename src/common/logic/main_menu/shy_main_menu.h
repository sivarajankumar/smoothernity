class _shy_common_logic_main_menu
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_main_menu_creation_permit ) ;
    static void receive ( so_called_message_common_logic_main_menu_launch_permit ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_animation_disappear_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_create_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_meshes_creation_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_meshes_destroy_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_row_chosen ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_mesh_create_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_mesh_destroy_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu > :: module shy_common_logic_main_menu_scheduled ;