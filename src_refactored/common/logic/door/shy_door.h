class _shy_common_logic_door
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_door_creation_permit ) ;
    static void receive ( so_called_message_common_logic_door_launch_permit ) ;
    static void receive ( so_called_message_common_logic_door_update ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door > :: module shy_common_logic_door_scheduled ;
