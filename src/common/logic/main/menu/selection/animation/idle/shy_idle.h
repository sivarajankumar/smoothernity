class _shy_common_logic_main_menu_selection_animation_idle
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_layout_row_rect_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_idle_row_selected_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_idle_transform_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_idle_void_selected_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_idle > :: module shy_common_logic_main_menu_selection_animation_idle_scheduled ;
