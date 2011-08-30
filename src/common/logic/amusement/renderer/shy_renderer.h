class _shy_common_logic_amusement_renderer
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_amusement_render_message ) ;
    static void receive ( so_called_common_logic_blanket_render_reply_message ) ;
    static void receive ( so_called_common_logic_door_render_reply_message ) ;
    static void receive ( so_called_common_logic_observer_animation_transform_reply_message ) ;
    static void receive ( so_called_common_logic_ortho_planes_reply_message ) ;
    static void receive ( so_called_common_logic_perspective_planes_reply_message ) ;
    static void receive ( so_called_common_logic_room_render_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_amusement_renderer > :: module shy_common_logic_amusement_renderer_scheduled ;
