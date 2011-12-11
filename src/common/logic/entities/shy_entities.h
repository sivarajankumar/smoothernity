class _shy_common_logic_entities
{
public :
    static void receive ( so_called_common_engine_render_mesh_create_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_entities_height_request_message ) ;
    static void receive ( so_called_common_logic_entities_mesh_grid_request_message ) ;
    static void receive ( so_called_common_logic_entities_origin_request_message ) ;
    static void receive ( so_called_common_logic_entities_prepare_permit_message ) ;
    static void receive ( so_called_common_logic_entities_render_request_message ) ;
    static void receive ( so_called_common_logic_entities_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_entities > :: module shy_common_logic_entities_scheduled ;
