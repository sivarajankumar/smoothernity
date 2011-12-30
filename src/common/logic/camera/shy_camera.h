class _shy_common_logic_camera
{
public :
    static void receive ( so_called_common_engine_render_aspect_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_camera_matrix_request_message ) ;
    static void receive ( so_called_common_logic_camera_prepare_permit_message ) ;
    static void receive ( so_called_common_logic_camera_update_message ) ;
    static void receive ( so_called_common_logic_core_near_plane_distance_reply_message ) ;
    static void receive ( so_called_common_logic_entities_height_reply_message ) ;
    static void receive ( so_called_common_logic_entities_mesh_grid_reply_message ) ;
    static void receive ( so_called_common_logic_entities_origin_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_camera > :: module shy_common_logic_camera_scheduled ;
