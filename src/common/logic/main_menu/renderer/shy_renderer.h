class _shy_common_logic_main_menu_renderer
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_fidget_render_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_animation_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_render_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_render_message ) ;
    static void receive ( so_called_common_logic_main_menu_render_permit_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_mesh_render_reply_message ) ;
    static void receive ( so_called_common_logic_ortho_planes_reply_message ) ;
    static void receive ( so_called_common_logic_text_use_text_texture_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_renderer > :: module shy_common_logic_main_menu_renderer_scheduled ;
