class _shy_common_logic_salutation_letters_animation
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_appear_transform_reply_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_disappear_transform_reply_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_layout_transform_reply_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_roll_in_transform_reply_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_roll_out_transform_reply_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_transform_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_animation 
    > :: module 
    shy_common_logic_salutation_letters_animation_scheduled ;
