class _shy_common_logic_observer_animation_flight
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_observer_animation_flight_transform_request ) ;
    static void receive ( so_called_message_common_logic_observer_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_observer_animation_flight > :: module shy_common_logic_observer_animation_flight_scheduled ;