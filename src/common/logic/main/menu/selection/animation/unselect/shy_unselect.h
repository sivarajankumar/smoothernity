class _shy_common_logic_main_menu_selection_animation_unselect
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_unselect_start_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_unselect_transform_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_unselect > :: module
    shy_common_logic_main_menu_selection_animation_unselect_scheduled ;
