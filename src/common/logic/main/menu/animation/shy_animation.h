class _shy_common_logic_main_menu_animation
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_animation_shake_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_animation_transform_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_animation > :: module shy_common_logic_main_menu_animation_scheduled ;
