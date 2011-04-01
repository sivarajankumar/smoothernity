class _shy_common_logic_main_menu_selection_animation_appear
{
public :
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_appear_start ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_appear_transform_request ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_appear > :: module shy_common_logic_main_menu_selection_animation_appear_scheduled ;
