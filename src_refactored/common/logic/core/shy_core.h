class _shy_common_logic_core
{
public :
    static void receive ( so_called_message_common_engine_render_aspect_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_core_near_plane_distance_request ) ;
    static void receive ( so_called_message_common_render ) ;
    static void receive ( so_called_message_common_update ) ;
    static void receive ( so_called_message_common_video_mode_changed ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_core > :: module shy_common_logic_core_scheduled ;
