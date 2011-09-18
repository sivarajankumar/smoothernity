class _shy_common_logic_salutation_letters_animation_appear
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_appear_rewind_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_appear_step_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_appear_transform_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_animation_appear 
    > :: module 
    shy_common_logic_salutation_letters_animation_appear_scheduled ;
