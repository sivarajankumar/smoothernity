class _shy_common_logic_door_renderer
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_door_mesh_render_reply_message ) ;
    static void receive ( so_called_common_logic_door_render_request_message ) ;
    static void receive ( so_called_common_logic_door_texture_select_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_renderer > :: module shy_common_logic_door_renderer_scheduled ;
