class _shy_common_logic_observer_animation
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_observer_animation_flight_transform_reply ) ;
    static void receive ( so_called_message_common_logic_observer_animation_transform_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_observer_animation > :: module shy_common_logic_observer_animation_scheduled ;
