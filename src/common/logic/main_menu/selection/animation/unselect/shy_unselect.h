class _shy_common_logic_main_menu_selection_animation_unselect
{
public :
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_unselect_start ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_unselect_transform_request ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_unselect > :: module
    shy_common_logic_main_menu_selection_animation_unselect_scheduled ;