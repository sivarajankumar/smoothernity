class _shy_common_logic_camera
{
public :
    static void receive ( so_called_message_common_engine_render_aspect_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_camera_matrix_request ) ;
    static void receive ( so_called_message_common_logic_camera_prepare_permit ) ;
    static void receive ( so_called_message_common_logic_camera_update ) ;
    static void receive ( so_called_message_common_logic_core_near_plane_distance_reply ) ;
    static void receive ( so_called_message_common_logic_entities_height_reply ) ;
    static void receive ( so_called_message_common_logic_entities_mesh_grid_reply ) ;
    static void receive ( so_called_message_common_logic_entities_origin_reply ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_camera > :: module shy_common_logic_camera_scheduled ;
