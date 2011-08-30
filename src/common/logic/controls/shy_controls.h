class _shy_common_logic_controls
{
public :
    static void receive ( so_called_common_logic_controls_state_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_controls > :: module shy_common_logic_controls_scheduled ;
