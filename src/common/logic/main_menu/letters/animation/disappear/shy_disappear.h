class _shy_common_logic_main_menu_letters_animation_disappear
{
public :
    static void receive ( so_called_message_common_logic_main_menu_launch_permit ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_animation_disappear_start ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_animation_disappear_transform_request ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_disappear > :: module shy_common_logic_main_menu_letters_animation_disappear_scheduled ;