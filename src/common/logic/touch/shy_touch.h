class _shy_common_logic_touch
{
public :
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_touch_prepare_permit ) ;
    static void receive ( so_called_message_common_logic_touch_render ) ;
    static void receive ( so_called_message_common_logic_touch_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_touch > :: module shy_common_logic_touch_scheduled ;