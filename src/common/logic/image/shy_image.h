class _shy_common_logic_image
{
public :
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
    static void receive ( so_called_message_common_engine_render_texture_create_reply ) ;
    static void receive ( so_called_message_common_engine_render_texture_loader_ready_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_image_prepare_permit ) ;
    static void receive ( so_called_message_common_logic_image_render_request ) ;
    static void receive ( so_called_message_common_logic_image_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_image > :: module shy_common_logic_image_scheduled ;