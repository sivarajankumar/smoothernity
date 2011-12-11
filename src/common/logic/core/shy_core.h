class _shy_common_logic_core
{
public :
    static void receive ( so_called_common_engine_render_aspect_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_core_near_plane_distance_request_message ) ;
    static void receive ( so_called_common_logic_core_use_ortho_projection_request_message ) ;
    static void receive ( so_called_common_logic_core_use_perspective_projection_request_message ) ;
    static void receive ( so_called_common_logic_fidget_prepared_message ) ;
    static void receive ( so_called_common_next_frame_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_core > :: module shy_common_logic_core_scheduled ;
