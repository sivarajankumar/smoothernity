class _shy_common_logic_image
{
public :
    static void receive ( so_called_common_engine_render_mesh_create_reply_message ) ;
    static void receive ( so_called_common_engine_render_texture_create_reply_message ) ;
    static void receive ( so_called_common_engine_render_texture_loader_ready_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_image_prepare_permit_message ) ;
    static void receive ( so_called_common_logic_image_render_request_message ) ;
    static void receive ( so_called_common_logic_image_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_image > :: module shy_common_logic_image_scheduled ;
