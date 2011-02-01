class _shy_common_logic_fidget
{
public :
    static void receive ( so_called_message_common_engine_render_aspect_reply ) ;
    static void receive ( so_called_message_common_engine_render_frame_loss_reply ) ;
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_fidget_prepare_permit ) ;
    static void receive ( so_called_message_common_logic_fidget_render_request ) ;
    static void receive ( so_called_message_common_logic_fidget_update ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_fidget > :: module shy_common_logic_fidget_scheduled ;
