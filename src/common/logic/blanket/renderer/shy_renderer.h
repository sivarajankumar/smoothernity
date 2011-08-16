class _shy_common_logic_blanket_renderer
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_blanket_mesh_render_reply ) ;
    static void receive ( so_called_message_common_logic_blanket_render_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_renderer > :: module shy_common_logic_blanket_renderer_scheduled ;
