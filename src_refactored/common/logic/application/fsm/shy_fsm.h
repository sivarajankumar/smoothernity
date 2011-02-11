class _shy_common_logic_application_fsm
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_application_render ) ;
    static void receive ( so_called_message_common_logic_application_update ) ;
    static void receive ( so_called_message_common_logic_text_prepared ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_application_fsm > :: module shy_common_logic_application_fsm_scheduled ;
