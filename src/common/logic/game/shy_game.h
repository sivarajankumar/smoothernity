class _shy_common_logic_game
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_camera_matrix_reply ) ;
    static void receive ( so_called_message_common_logic_camera_prepared ) ;
    static void receive ( so_called_message_common_logic_core_near_plane_distance_reply ) ;
    static void receive ( so_called_message_common_logic_core_use_ortho_projection_reply ) ;
    static void receive ( so_called_message_common_logic_core_use_perspective_projection_reply ) ;
    static void receive ( so_called_message_common_logic_entities_prepared ) ;
    static void receive ( so_called_message_common_logic_entities_render_reply ) ;
    static void receive ( so_called_message_common_logic_fidget_render_reply ) ;
    static void receive ( so_called_message_common_logic_game_launch_permit ) ;
    static void receive ( so_called_message_common_logic_game_render ) ;
    static void receive ( so_called_message_common_logic_game_update ) ;
    static void receive ( so_called_message_common_logic_image_prepared ) ;
    static void receive ( so_called_message_common_logic_image_render_reply ) ;
    static void receive ( so_called_message_common_logic_land_prepared ) ;
    static void receive ( so_called_message_common_logic_land_render_reply ) ;
    static void receive ( so_called_message_common_logic_sound_prepared ) ;
    static void receive ( so_called_message_common_logic_text_render_reply ) ;
    static void receive ( so_called_message_common_logic_touch_prepared ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_game > :: module shy_common_logic_game_scheduled ;