class _shy_common_logic_salutation_timer_disappear
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_timer_disappear_run_message ) ;
    static void receive ( so_called_common_logic_salutation_timer_disappear_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_timer_disappear 
    > :: module 
    shy_common_logic_salutation_timer_disappear_scheduled ;
