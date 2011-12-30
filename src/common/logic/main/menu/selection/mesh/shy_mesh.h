class _shy_common_logic_main_menu_selection_mesh
{
public :
    static void receive ( so_called_common_engine_render_mesh_create_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_mesh_create_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_mesh_destroy_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_mesh_place_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_mesh_render_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler 
    :: scheduled_context < _shy_common_logic_main_menu_selection_mesh > :: module 
    shy_common_logic_main_menu_selection_mesh_scheduled ;
