class _shy_common_logic_observer_animation_flight
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_observer_animation_flight_transform_request_message ) ;
    static void receive ( so_called_common_logic_observer_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_observer_animation_flight > :: module shy_common_logic_observer_animation_flight_scheduled ;
