class _shy_common_logic_salutation_timer_appear
{
public :
    static void receive ( so_called_message_common_logic_salutation_timer_appear_run ) ;
    static void receive ( so_called_message_common_logic_salutation_timer_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_timer_appear 
    > :: module
    shy_common_logic_salutation_timer_appear_scheduled ;
