class _shy_common_logic_main_menu_letters_meshes_renderer
{
public :
    static void receive ( so_called_message_common_logic_main_menu_letters_meshes_iterate_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_meshes_iteration ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_meshes_render_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_renderer > :: module shy_common_logic_main_menu_letters_meshes_renderer_scheduled ;
