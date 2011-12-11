class _shy_common_logic_door_texture
{
public :
    static void receive ( so_called_common_engine_rasterizer_finalize_reply_message ) ;
    static void receive ( so_called_common_engine_render_texture_create_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_door_texture_create_message ) ;
    static void receive ( so_called_common_logic_door_texture_select_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_texture > :: module shy_common_logic_door_texture_scheduled ;
