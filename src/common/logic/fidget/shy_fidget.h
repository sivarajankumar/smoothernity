class _shy_common_logic_fidget
{
public :
    static void receive ( so_called_common_engine_render_aspect_reply_message ) ;
    static void receive ( so_called_common_engine_render_frame_loss_reply_message ) ;
    static void receive ( so_called_common_engine_render_mesh_create_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_fidget_prepare_permit_message ) ;
    static void receive ( so_called_common_logic_fidget_render_request_message ) ;
    static void receive ( so_called_common_logic_fidget_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_fidget > :: module shy_common_logic_fidget_scheduled ;
