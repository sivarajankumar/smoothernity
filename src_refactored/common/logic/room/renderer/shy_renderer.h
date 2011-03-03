class _shy_common_logic_room_renderer
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_room_mesh_render_reply ) ;
    static void receive ( so_called_message_common_logic_room_render_permit ) ;
    static void receive ( so_called_message_common_logic_room_render_request ) ;
    static void receive ( so_called_message_common_logic_room_texture_select_reply ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room_renderer > :: module shy_common_logic_room_renderer_scheduled ;
