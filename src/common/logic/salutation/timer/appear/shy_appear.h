class _shy_common_logic_salutation_timer_appear
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_timer_appear_run_message ) ;
    static void receive ( so_called_common_logic_salutation_timer_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_timer_appear 
    > :: module
    shy_common_logic_salutation_timer_appear_scheduled ;
