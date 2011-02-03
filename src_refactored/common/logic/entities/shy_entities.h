class _shy_common_logic_entities
{
public :
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_entities_height_request ) ;
    static void receive ( so_called_message_common_logic_entities_mesh_grid_request ) ;
    static void receive ( so_called_message_common_logic_entities_origin_request ) ;
    static void receive ( so_called_message_common_logic_entities_prepare_permit ) ;
    static void receive ( so_called_message_common_logic_entities_render_request ) ;
    static void receive ( so_called_message_common_logic_entities_update ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_entities > :: module shy_common_logic_entities_scheduled ;
