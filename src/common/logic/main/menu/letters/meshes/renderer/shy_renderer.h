class _shy_common_logic_main_menu_letters_meshes_renderer
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_iterate_finished_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_iteration_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_render_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_renderer > :: module shy_common_logic_main_menu_letters_meshes_renderer_scheduled ;
