class _shy_common_logic_main_menu_animation_shake
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
    static void receive ( so_called_message_common_logic_main_menu_void_chosen ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_animation_shake > :: module shy_common_logic_main_menu_animation_shake_scheduled ;
