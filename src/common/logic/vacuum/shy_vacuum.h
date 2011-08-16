class _shy_common_logic_vacuum
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_vacuum_render ) ;
    static void receive ( so_called_message_common_logic_vacuum_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_vacuum > :: module shy_common_logic_vacuum_scheduled ;
