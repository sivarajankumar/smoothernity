class _shy_common_logic_room_texture
{
public :
    static void receive ( so_called_message_common_engine_rasterizer_finalize_reply ) ;
    static void receive ( so_called_message_common_engine_render_texture_create_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_room_texture_create ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room_texture > :: module shy_common_logic_room_texture_scheduled ;
