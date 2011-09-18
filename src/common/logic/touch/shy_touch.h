class _shy_common_logic_touch
{
public :
    static void receive ( so_called_common_engine_render_mesh_create_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_touch_prepare_permit_message ) ;
    static void receive ( so_called_common_logic_touch_render_message ) ;
    static void receive ( so_called_common_logic_touch_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_touch > :: module shy_common_logic_touch_scheduled ;
